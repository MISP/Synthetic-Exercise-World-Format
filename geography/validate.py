#!/usr/bin/env python3
"""Check the Nacre GeoJSON, Galaxy metadata, and standalone atlas data."""

import argparse
import json
import math
from pathlib import Path
from uuid import UUID


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA_START = '<script id="atlas-data" type="application/json">\n'
DATA_END = "\n</script>"
NON_GEOGRAPHIC = {
    "aircraft-type", "facility-company", "fictional-ethnicity", "fictional-religion",
    "military-aircraft-type", "navigation-coverage-snapshot", "navigation-interference-exercise",
    "satellite-link", "satellite-navigation-service", "satellite-service",
}
COUNTRY_REFERENCES = {
    "country-flag": "represents",
    "petroleum-country-profile": "profiles-country",
}


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def targets(record, role):
    return [item["dest-uuid"] for item in record.get("related", []) if item["type"] == role]


def valid_position(position):
    assert len(position) == 2, position
    longitude, latitude = position
    assert math.isfinite(longitude) and math.isfinite(latitude), position
    assert -180 <= longitude <= 180 and -90 <= latitude <= 90, position


def inside_ring(point, ring):
    x, y = point
    crossings = sum(
        (a[1] > y) != (b[1] > y) and x < (b[0] - a[0]) * (y - a[1]) / (b[1] - a[1]) + a[0]
        for a, b in zip(ring, ring[1:])
    )
    return crossings % 2 == 1


def inside_polygon(point, polygon):
    return inside_ring(point, polygon[0]) and not any(inside_ring(point, hole) for hole in polygon[1:])


def polygons(geometry):
    return [geometry["coordinates"]] if geometry["type"] == "Polygon" else geometry["coordinates"]


def contains(geometry, point):
    return any(inside_polygon(point, polygon) for polygon in polygons(geometry))


def validate_geometry(geometry):
    kind = geometry["type"]
    coordinates = geometry["coordinates"]
    if kind == "Point":
        valid_position(coordinates)
    elif kind in {"LineString", "MultiPoint"}:
        assert len(coordinates) >= 2, geometry
        for point in coordinates:
            valid_position(point)
        if kind == "LineString":
            assert all(a != b for a, b in zip(coordinates, coordinates[1:])), geometry
    else:
        assert kind in {"Polygon", "MultiPolygon"}, kind
        for polygon in polygons(geometry):
            assert polygon, geometry
            for index, ring in enumerate(polygon):
                assert len(ring) >= 4 and ring[0] == ring[-1], geometry
                for point in ring:
                    valid_position(point)
                area = sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(ring, ring[1:]))
                assert (area > 0 if index == 0 else area < 0), geometry


def check_atlas(data, write_atlas):
    atlas = HERE / "atlas.html"
    source = atlas.read_text(encoding="utf-8")
    before, marker, rest = source.partition(DATA_START)
    embedded, end, after = rest.partition(DATA_END)
    assert marker and end, "Atlas data block is missing"
    if write_atlas:
        packed = (HERE / "nacre.geojson").read_text(encoding="utf-8").strip().replace("<", r"\u003c")
        atlas.write_text(before + marker + packed + end + after, encoding="utf-8")
    else:
        assert json.loads(embedded) == data, "Run geography/validate.py --write-atlas"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-cluster", type=Path, help="Optional pinned upstream exercise-world.json for country UUID checks")
    parser.add_argument("--write-atlas", action="store_true", help="Refresh the standalone atlas from nacre.geojson after validation")
    args = parser.parse_args()

    data = load(HERE / "nacre.geojson")
    reference = data["coordinate_reference"]
    assert data["type"] == "FeatureCollection"
    assert reference["body"] == "Nacre" and reference["axis_order"] == ["longitude", "latitude"]
    features = {}
    countries = {}
    for feature in data["features"]:
        ident = feature["id"]
        assert feature["type"] == "Feature" and str(UUID(ident)) == ident
        assert ident not in features, ident
        validate_geometry(feature["geometry"])
        features[ident] = feature
        props = feature["properties"]
        assert props["layer"] in data["layers"], props
        if props["kind"] == "country":
            assert props["name"] not in countries and props["layer"] == "world", props
            countries[props["name"]] = feature

    if args.base_cluster:
        upstream = {entry["value"]: entry for entry in load(args.base_cluster)["values"]
                    if entry["meta"]["entity-type"] == ["country"]}
        assert countries.keys() == upstream.keys()
        for name, feature in countries.items():
            assert feature["id"] == upstream[name]["uuid"]
            assert feature["properties"]["capital"] == upstream[name]["meta"]["capital"][0]

    records = {}
    cluster_paths = sorted([*(ROOT / "clusters").glob("*.json"), *(ROOT / "extensions").glob("*/clusters/*.json")])
    for path in cluster_paths:
        cluster = load(path)
        definition = load(path.parent.with_name("galaxies") / path.name)
        assert definition["type"] == cluster["type"] and definition["version"] == cluster["version"], path
        for entry in cluster["values"]:
            assert entry["uuid"] not in records, entry
            records[entry["uuid"]] = entry
            meta = entry["meta"]
            entity, = meta["entity-type"]
            if entity in NON_GEOGRAPHIC:
                assert "geographic-feature-id" not in meta, entry
                continue
            feature_id, = meta["geographic-feature-id"]
            assert meta["coordinate-reference"] == [reference["id"]], entry
            if entity in COUNTRY_REFERENCES:
                assert targets(entry, COUNTRY_REFERENCES[entity]) == [feature_id]
                assert features[feature_id]["properties"]["kind"] == "country"
            else:
                assert feature_id == entry["uuid"], entry
                assert features[feature_id]["properties"]["layer"] == cluster["type"].removeprefix("exercise-world-"), entry
            geometry = features[feature_id]["geometry"]
            if geometry["type"] == "Point":
                assert geometry["coordinates"] == [float(meta["longitude"][0]), float(meta["latitude"][0])], entry
                depth = features[feature_id]["properties"].get("depth_km")
                if depth is not None:
                    assert float(meta["depth-km"][0]) == depth, entry
            else:
                assert "longitude" not in meta and "latitude" not in meta, entry

    capitals = {}
    for ident, feature in features.items():
        geometry = feature["geometry"]
        props = feature["properties"]
        coordinates = geometry["coordinates"]
        country = props.get("country")
        if geometry["type"] == "Point" and country:
            if props.get("setting") in {"offshore", "shoreline-intake"}:
                assert not any(contains(item["geometry"], coordinates) for item in countries.values()), props
            else:
                assert contains(countries[country]["geometry"], coordinates), props
        if props["kind"] == "capital":
            assert country not in capitals, props
            assert props["name"] == countries[country]["properties"]["capital"], props
            assert props["country_id"] == countries[country]["id"], props
            capitals[country] = feature
        if props.get("host_id"):
            assert coordinates == features[props["host_id"]]["geometry"]["coordinates"], props
        if props["kind"] == "force-liaison":
            record = records[ident]
            meta = record["meta"]
            host = features[props["host_id"]]["properties"]
            assert host["country"] == country == meta["country"], props
            assert props["country_id"] == countries[country]["id"], props
            assert targets(record, "located-in") == [props["country_id"]], record
            assert meta["entity-type"] == ["force-organization"], record
            assert meta["force-type"] == [props["layer"]], record
            assert meta["service-model"] == [props["service_model"]], record
            assert meta["liaison-site"] == [host["name"]], record
            host_targets = [] if host["kind"] == "capital" else [props["host_id"]]
            assert targets(record, "has-liaison-at") == host_targets, record
            assert all(link["dest-uuid"] in records or link["dest-uuid"] == props["country_id"]
                       for link in record["related"]), record
        if geometry["type"] == "LineString":
            start, end = props["endpoint_ids"]
            assert props["direction"] in {"one-way", "bidirectional"}, props
            assert coordinates[0] == features[start]["geometry"]["coordinates"], props
            assert coordinates[-1] == features[end]["geometry"]["coordinates"], props
        if geometry["type"] == "MultiPoint":
            assert coordinates == [features[key]["geometry"]["coordinates"] for key in props["access_ids"]], props
        if props["kind"] == "coverage-footprint":
            record = records[ident]
            relation = "visible-at" if props["layer"] == "satellite-navigation" else "covers-site"
            for site_id in targets(record, relation):
                assert contains(geometry, features[site_id]["geometry"]["coordinates"]), (props, site_id)
        if props["layer"] != "world" and ident not in records:
            assert props["layer"] == "veyra" and props["placement"] == "cutaway-surface-projection", props
    assert capitals.keys() == countries.keys()
    check_atlas(data, args.write_atlas)
    print(f"Validated {len(features)} geographic features across {len(data['layers'])} layers.")


if __name__ == "__main__":
    main()
