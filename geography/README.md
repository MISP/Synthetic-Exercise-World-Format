# Nacre geographic atlas

The atlas registers country boundaries, capitals, and extension features to the latitude and longitude grid printed on the clear Nacre map. The [GeoJSON](nacre.geojson) covers 309 features across 19 layers. Open the [standalone atlas](atlas.html) in a browser to filter layers, search for a site or route, and inspect its coordinates or endpoints. Browsers that require HTTP can load the atlas through `python3 -m http.server --directory geography` from the repository root.

## Coordinate reference

`nacre-atlas-v1` is a fictional latitude and longitude grid on Nacre. GeoJSON positions use `[longitude, latitude]` in decimal degrees, with east and north positive. Veyra depths are separate properties in kilometres below the local surface. The coordinate convention is familiar to GIS tools. The basemap and positions belong to Nacre.

The clear SVG atlas is the reference artwork. Its zero meridian and equator are at SVG coordinates `x = 455.351786` and `y = 351.565714`. One degree is `3.587142857` SVG units along either axis. The painted planet map and Veyra cutaway are illustrations with their own framing. [Clear atlas](../images/synthetic_exercise_world_clear_map.svg)

## What the geometries represent

| Feature | Representation |
|---|---|
| Countries and capitals | Country boundaries trace the clear atlas and use the original MISP country UUIDs. Capital locations come from the atlas star markers. Orinthia has seven polygon parts. |
| Ground facilities | A point places each site on the shared grid. Existing markers were registered to the grid, with placements adjusted where needed to fit the named country. Water sources and plants have representative locations near their districts. |
| Utility districts and hubs | A point identifies each district's representative anchor. |
| Force liaison points | Each point uses an existing host facility or capital. The service model identifies whether the organization is independent, a component, a reserve, or a civilian authority. |
| Transport and utility routes | LineStrings follow the schematic corridors and terminate at registered endpoints. Data center circuits and feeds show logical handoffs, with the underlying assets identified by UUID. |
| Veyra | Surface coordinates register the three crossings and underground landmarks. Depths remain separate. The Veyra access entry shows the known surface entrances. |
| Satellite footprints | Polygons register the illustrated coverage windows or snapshot. They describe surface visibility. |
| Country flags and petroleum profiles | These records reuse their country's geometry. Community examples, aircraft types, organizations, and logical satellite links retain their existing relationships. |

## Using the Galaxy metadata

Use `meta.geographic-feature-id[0]` to join an extension record to the GeoJSON `Feature.id`. IDs are normally the original record UUID. Country flags and petroleum profiles point to the referenced country UUID instead. Point records also include `meta.latitude` and `meta.longitude` as separate single-value arrays. These fields use `meta.coordinate-reference = ["nacre-atlas-v1"]`.

The local base layer gives upstream country records their geometry through the existing UUIDs. Country and capital names were checked against the pinned cluster. [MISP Galaxy revision `779b780`](https://github.com/MISP/misp-galaxy/blob/779b780a13f67288d9b1a031b064fb140cdacaae/clusters/exercise-world.json)

## Updating the atlas

Edit the GeoJSON and any affected Galaxy metadata together. Run these commands from the repository root to check the geometry, UUIDs, endpoints, and metadata, then refresh the standalone browser copy.

```sh
python3 geography/validate.py --write-atlas
python3 geography/validate.py
```

The atlas uses the CC BY 4.0 Nacre artwork and extension diagrams. [License](../LICENSE)
