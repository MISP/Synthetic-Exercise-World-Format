# Synthetic Exercise World - Self-contained fictional world dataset for cyber exercises and standards documents.

[Browse the world extensions and their maps](#world-extensions).

## Why the Synthetic Exercise World Format Matters

The Synthetic Exercise World Format provides a neutral and reusable reference environment for cyber threat intelligence exercises, drills, training scenarios, and documentation. By using fictional countries, organizations, sectors, infrastructures, and threat actors, participants can discuss realistic CTI concepts without implicitly referring to real geopolitical situations, real victims, or real adversaries. This helps trainers, analysts, vendors, public institutions, and standardization bodies focus on the structure, quality, and interoperability of the information rather than on politically sensitive interpretations.

Neutrality is especially important when creating reference material for CTI formats, taxonomies, sharing models, or operational procedures. Real-world examples can unintentionally introduce bias, diplomatic sensitivity, legal concerns, or disagreement between participating countries and organizations. A synthetic world avoids these issues by offering realistic but non-attributable entities that can be safely used in examples, schemas, test cases, playbooks, and exercises. This makes the reference document easier to adopt across different jurisdictions and communities.

A shared synthetic environment also improves consistency. Instead of each exercise or standard document inventing its own partial examples, the same fictional countries, companies, sectors, and threat actors can be reused across multiple tools and formats. This makes it easier to compare implementations, validate parsers, test data models, and demonstrate interoperability between CTI platforms. The format can become a common neutral vocabulary for examples, much like test datasets are used in software engineering.

The Synthetic Exercise World Format also supports realistic scenario design without exposing sensitive national, sectoral, or organizational information. Exercise planners can model cross-border incidents, supply-chain compromises, sector-specific threats, vulnerability disclosure workflows, and intelligence-sharing procedures while avoiding references to real critical infrastructure or real governmental relationships. This lowers the barrier for participation and allows organizations with different confidentiality requirements to collaborate in the same scenario.

Including the Synthetic Exercise World Format in reference documentation helps ensure that CTI standards and tools can be widely deployed. It provides a safe, politically neutral, and technically meaningful foundation for examples, demonstrations, conformance testing, and training. By separating the technical purpose of CTI sharing from real-world sensitivities, the format encourages broader adoption, clearer communication, and more inclusive participation across countries, sectors, and communities.

# Synthetic Exercise World Format — Data Model

![Synthetic Exercise World Format diagram](https://raw.githubusercontent.com/MISP/Synthetic-Exercise-World-Format/refs/heads/main/images/synthetic_exercise_world_format_diagram.png)

![Synthetic Exercise World map - official map](https://raw.githubusercontent.com/MISP/Synthetic-Exercise-World-Format/refs/heads/main/images/planet_nacre_official_map.png)

## What the JSON provides

The dataset is a [single JSON object](https://github.com/MISP/misp-galaxy/blob/main/clusters/exercise-world.json) with document-level fields such as `name`, `type`, `uuid`, `version`, `description`, and a reusable `values[]` list. Each item in `values[]` has a common record shape: `value`, `uuid`, `description`, and `meta`.

## Entity families

| Entity family | Count | Main metadata fields | How it is used |
|---|---:|---|---|
| Country | 10 | `entity-type`, `planet`, `capital`, `geography`, `exercise-use` | Provides fictional geopolitical context for neutral exercises and examples. |
| Company | 30 | `entity-type`, `planet`, `headquarters`, `sector`, `exercise-use` | Provides fictional organizations, victims, suppliers, operators, or reporting entities. |
| Threat actor | 20 | `entity-type`, `planet`, `origin`, `primary-motivation`, `sophistication`, `exercise-use` | Provides non-real actors for neutral attribution and CTI training scenarios. |

## Metadata relationships

```text
company.meta.headquarters == country.value
threat-actor.meta.origin  == country.value
all meta.planet values     == "Nacre"
```

This means a tool can group companies and threat actors by fictional country without relying on real-world geopolitical references.

## Country availability summary

| Country | Capital | Geography | Sector represented | Companies | Threat actors |
|---|---|---|---|---:|---:|
| Asterin Union | Asterin Prime | Northern supercontinent | Energy | 3 | 2 |
| Velkar Republic | Velkar Prime | Inland industrial basin | Finance | 3 | 2 |
| Orinthia | Orinthia Prime | Archipelago of research hubs | Healthcare | 3 | 2 |
| Caelum Protectorate | Caelum Prime | High-altitude plateau state | Telecommunications | 3 | 2 |
| Neruva Federation | Neruva Prime | Delta megacities and ports | Aerospace | 3 | 2 |
| Thyros Commonwealth | Thyros Prime | Resource-rich steppe | Logistics | 3 | 2 |
| Ilyndor | Ilyndor Prime | Neutral trade corridor | Manufacturing | 3 | 2 |
| Brinax Collective | Brinax Prime | Energy-grid cooperative state | Maritime | 3 | 2 |
| Soreth Dominion | Soreth Prime | Polar logistics nation | Food | 3 | 2 |
| Quenari League | Quenari Prime | Equatorial agri-tech alliance | Media | 3 | 2 |

## Synthetic Exercise World Format JSON

The JSON format follows the standard MISP galaxy structure, making it directly compatible with tools and platforms that already support [MISP galaxy](https://misp-galaxy.org/) definitions. This allows the Synthetic Exercise World data to be loaded, shared, and reused without requiring a custom parser or dedicated data model. As a result, countries, companies, and threat actors from the synthetic dataset can be integrated into existing MISP-compatible workflows for exercises, documentation, testing, and training.

- [Self-contained fictional world dataset for cyber exercises and standards documents](https://github.com/MISP/misp-galaxy/blob/main/clusters/exercise-world.json) in MISP Galaxy JSON format.

# Geography of the Synthetic Exercise World

The shared Nacre coordinate grid registers country boundaries, capitals, and extension sites, routes, and coverage. Explore the interactive atlas or download the GeoJSON through the [geographic atlas guide](geography/README.md).

## Synthetic Exercise World Map — Planet Nacre

This field guide accompanies the revised fictional atlas map. The map is designed for neutral cyber-exercise planning and keeps the original synthetic country, company, and threat-actor relationships while making the visual layout easier to read.

![Synthetic Exercise World - Planet Nacre](https://raw.githubusercontent.com/MISP/Synthetic-Exercise-World-Format/refs/heads/main/images/synthetic_exercise_world_clear_map.png)

[SVG](https://raw.githubusercontent.com/MISP/Synthetic-Exercise-World-Format/refs/heads/main/images/synthetic_exercise_world_clear_map.svg)

Match a flag to its country using the [flag atlas and visual index](extensions/country-flags/README.md).

![Synthetic Exercise World - MAP without labels](https://raw.githubusercontent.com/MISP/Synthetic-Exercise-World-Format/refs/heads/main/images/planet_nacre.png)
### Country index

| # | Country | Capital | Geography | Sector |
|---:|---|---|---|---|
| 1 | Asterin Union | Asterin Prime | Northern supercontinent | Energy |
| 2 | Soreth Dominion | Soreth Prime | Polar logistics nation | Food |
| 3 | Caelum Protectorate | Caelum Prime | High-altitude plateau state | Telecommunications |
| 4 | Orinthia | Orinthia Prime | Archipelago of research hubs | Healthcare |
| 5 | Velkar Republic | Velkar Prime | Inland industrial basin | Finance |
| 6 | Thyros Commonwealth | Thyros Prime | Resource-rich steppe | Logistics |
| 7 | Ilyndor | Ilyndor Prime | Neutral trade corridor | Manufacturing |
| 8 | Neruva Federation | Neruva Prime | Delta megacities and ports | Aerospace |
| 9 | Brinax Collective | Brinax Prime | Energy-grid cooperative state | Maritime |
| 10 | Quenari League | Quenari Prime | Equatorial agri-tech alliance | Media |

### Country notes and entities

#### Asterin Union

- **Capital:** Asterin Prime
- **Geography:** Northern supercontinent
- **Primary sector represented by companies:** Energy
- **Companies:** NovaCore Systems, NovaMatrix Systems, NovaNimbus Systems
- **Synthetic threat actors:** TA-700 Obsidian Jackal, TA-710 Obsidian Jackal
- **Map role:** North-western continental anchor. Energy infrastructure is represented by continental routes toward Brinax and the inland basin.

#### Soreth Dominion

- **Capital:** Soreth Prime
- **Geography:** Polar logistics nation
- **Primary sector represented by companies:** Food
- **Companies:** DeltaHarbor Networks, DeltaNimbus Networks, DeltaBeacon Networks
- **Synthetic threat actors:** TA-708 Sable Hydra, TA-718 Sable Hydra
- **Map role:** Polar and sub-polar logistics state. Dashed northern sea routes connect it to Asterin, Caelum, and Orinthia.

#### Caelum Protectorate

- **Capital:** Caelum Prime
- **Geography:** High-altitude plateau state
- **Primary sector represented by companies:** Telecommunications
- **Companies:** BlueBridge Networks, BluePulse Networks, BlueForge Networks
- **Synthetic threat actors:** TA-703 Violet Hydra, TA-713 Violet Hydra
- **Map role:** High central plateau and telecommunications relay state. Mountain symbols and river sources show why it matters for routing and connectivity.

#### Orinthia

- **Capital:** Orinthia Prime
- **Geography:** Archipelago of research hubs
- **Primary sector represented by companies:** Healthcare
- **Companies:** IronCore Dynamics, IronPulse Dynamics, IronForge Dynamics
- **Synthetic threat actors:** TA-702 Crimson Rook, TA-712 Crimson Rook
- **Map role:** North-eastern archipelago of research hubs. Islands are linked by research routes and undersea cables to the continent.

#### Velkar Republic

- **Capital:** Velkar Prime
- **Geography:** Inland industrial basin
- **Primary sector represented by companies:** Finance
- **Companies:** HelixCore Group, HelixMatrix Group, HelixForge Group
- **Synthetic threat actors:** TA-701 Silver Mantis, TA-711 Silver Mantis
- **Map role:** Inland industrial/finance basin between Asterin, Caelum, Thyros, and the Ilyndor corridor.

#### Thyros Commonwealth

- **Capital:** Thyros Prime
- **Geography:** Resource-rich steppe
- **Primary sector represented by companies:** Logistics
- **Companies:** VertexBridge Systems, VertexFoundry Systems, VertexLattice Systems
- **Synthetic threat actors:** TA-705 Cobalt Jackal, TA-715 Cobalt Jackal
- **Map role:** Eastern resource-rich steppe. Resource marks and open space support logistics and supply-chain narratives.

#### Ilyndor

- **Capital:** Ilyndor Prime
- **Geography:** Neutral trade corridor
- **Primary sector represented by companies:** Manufacturing
- **Companies:** CinderHarbor Group, CinderFoundry Group, CinderLattice Group
- **Synthetic threat actors:** TA-706 Onyx Mantis, TA-716 Onyx Mantis
- **Map role:** Narrow neutral trade corridor joining west, basin, steppe, south, ports, and grid infrastructure.

#### Neruva Federation

- **Capital:** Neruva Prime
- **Geography:** Delta megacities and ports
- **Primary sector represented by companies:** Aerospace
- **Companies:** SkyBridge Labs, SkyPulse Labs, SkyLattice Labs
- **Synthetic threat actors:** TA-704 Amber Drift, TA-714 Amber Drift
- **Map role:** South-eastern river delta with megacity and port concentration, suitable for aerospace, port, and crisis-communication scenarios.

#### Brinax Collective

- **Capital:** Brinax Prime
- **Geography:** Energy-grid cooperative state
- **Primary sector represented by companies:** Maritime
- **Companies:** AuroraHarbor Dynamics, AuroraFoundry Dynamics, AuroraBeacon Dynamics
- **Synthetic threat actors:** TA-707 Ivory Rook, TA-717 Ivory Rook
- **Map role:** South-eastern coastal/grid cooperative linking maritime infrastructure with the southern power grid.

#### Quenari League

- **Capital:** Quenari Prime
- **Geography:** Equatorial agri-tech alliance
- **Primary sector represented by companies:** Media
- **Companies:** QuantumMatrix Labs, QuantumNimbus Labs, QuantumBeacon Labs
- **Synthetic threat actors:** TA-709 Copper Drift, TA-719 Copper Drift
- **Map role:** Equatorial and sub-equatorial agri-tech belt, shown with field grids and floodplain routes.

### Adjacency and planning interpretation

| Country | Neighboring or nearby exercise regions | Planning rationale |
|---|---|---|
| Asterin Union | Soreth Dominion, Caelum Protectorate, Velkar Republic, Ilyndor | Energy, northern continental access, basin dependencies. |
| Soreth Dominion | Asterin Union, Caelum Protectorate, Orinthia sea routes | Polar logistics, cold-chain routing, maritime/satellite exercise narratives. |
| Caelum Protectorate | Asterin Union, Soreth Dominion, Velkar Republic, Thyros Commonwealth, Orinthia sea links | High-altitude telecom relays, river sources, route chokepoints. |
| Orinthia | Caelum Protectorate, Thyros Commonwealth, Soreth sea routes | Research hubs, healthcare dependencies, undersea cable resilience. |
| Velkar Republic | Asterin Union, Caelum Protectorate, Thyros Commonwealth, Ilyndor | Finance/industrial dependencies within a basin bordered by strategic neighbors. |
| Thyros Commonwealth | Caelum Protectorate, Velkar Republic, Ilyndor, Neruva Federation, Orinthia sea lanes | Resource logistics and overland transit between plateau, basin, and delta. |
| Ilyndor | Asterin Union, Velkar Republic, Thyros Commonwealth, Quenari League, Brinax Collective, Neruva Federation | Neutral corridor for road, rail, manufacturing, diplomatic escalation, and incident notification. |
| Neruva Federation | Thyros Commonwealth, Ilyndor, Brinax Collective, Quenari League, southern sea lanes | Delta ports and dense megacities create concentrated impact and recovery planning. |
| Brinax Collective | Ilyndor, Quenari League, Neruva Federation | Energy-grid and maritime interdependency scenarios. |
| Quenari League | Ilyndor, Brinax Collective, Neruva Federation | Agri-tech, media, floodplain logistics, and public communication narratives. |

### Scenario ideas

- **Cross-border infrastructure cascade:** Start with Asterin energy disruption, route it through Ilyndor and Brinax, then create follow-on impact in Neruva ports and Quenari agri-tech/media narratives.
- **Telecom/routing exercise:** Use Caelum as the high-altitude relay state, with Orinthia undersea links and Velkar/Thyros terrestrial routing as alternate paths.
- **Supply-chain drill:** Chain Soreth polar logistics, Thyros steppe logistics, Ilyndor corridor manufacturing, and Neruva delta ports.
- **Public communication and influence:** Pair Neruva delta megacity pressure with Quenari media companies and Orinthia healthcare/research stakeholders.
- **Neutral corridor stress test:** Treat Ilyndor as a diplomatic and technical choke point for data-sharing, emergency peering, cross-border incident notification, and temporary traffic rerouting.

## Veyra — the world beneath Nacre

Veyra is an inhabited network of caverns beneath Nacre, with crossings in Ilyndor, Brinax Collective, and on Kestrel Island in Orinthia. Its settlements share a council that allocates water and maintains the light galleries. Lantern Basin is the largest settlement and the main market for goods arriving from the surface.

[![Oblique cutaway of Nacre and Veyra showing the Ilyndor, Brinax, and Kestrel Island crossings and their routes to Threshold Station and Lantern Basin](images/nacre_veyra_cutaway.svg)](images/nacre_veyra_cutaway.svg)

Each crossing's depth is measured from its local surface. Horizontal distances and cavern sizes are schematic.

| Landmark | Depth | Role |
|---|---:|---|
| Ilyndor Gate | Surface to 1.2 km | Jointly operated transfer lift and Veyra's main route for general cargo. |
| Brinax Coastal Lift | Surface to 1.6 km | Heavy-freight lift at a Brinax Collective port. A freight gallery leads to Lantern Basin. |
| Kestrel Island Shaft | Surface to 1.2 km | Restricted crossing for research teams and medical transfers, with a passage to Threshold Station. Kestrel Island is the only Orinthian island with access to Veyra. |
| Threshold Station | 1.2 km | Ilyndor landing, cargo inspection point, and shared communications relay at the end of the Kestrel research passage. |
| Lantern Basin | 1.6 km | Main Veyran settlement and freight market. A haulway connects it to Threshold Station, and the Brinax freight gallery serves its receiving terraces. |
| Glasswater Reservoir | 2.1 km | Freshwater reserve feeding Lantern Basin's lower terraces. |

Ilyndor sends food, medicines, and replacement equipment down the gate lift. Veyra sends optical glass and specialist repair crews up to the corridor. The Ilyndor and Veyran councils must both approve a closure of Ilyndor Gate, and Threshold Station relays manifests and emergency messages in either direction. Brinax moves bulk supplies and grid equipment, while Kestrel handles research and medical transfers.

An Ilyndor Gate outage gives exercise participants a choice about what to reroute through Brinax, which medical transfers qualify for Kestrel, and which supplies to allocate from Veyra's reserves. When the gate reopens, participants can reconcile the manifests recorded at each crossing.

# Integrating the dataset

Projects consuming the Synthetic Exercise World should:

- pin the exact `MISP/misp-galaxy` revision of both
  [`clusters/exercise-world.json`](https://github.com/MISP/misp-galaxy/blob/main/clusters/exercise-world.json)
  and [`galaxies/exercise-world.json`](https://github.com/MISP/misp-galaxy/blob/main/galaxies/exercise-world.json),
  rather than relying only on the numeric dataset version;
- use entity UUIDs as stable references and treat `value` as display text;
- load the galaxy before importing events carrying `misp-galaxy:exercise-world` tags;
- validate the generic MISP Galaxy JSON schemas plus the documented country/company/actor
  relationships; and
- preserve CC-BY-4.0 attribution and record whether local changes were made.

Veyra has its own MISP [galaxy definition](galaxies/exercise-world-veyra.json) and
[cluster collection](clusters/exercise-world-veyra.json). Import both alongside
the surface dataset and use the `exercise-world-veyra` galaxy type for Veyran
entities. The three crossing clusters link by UUID to their surface countries
and their destinations within Veyra. The Kestrel Island Shaft cluster uses
`meta.surface-site` to identify the specific island within Orinthia. The surface
references were verified against [MISP Galaxy revision `779b780`](https://github.com/MISP/misp-galaxy/blob/779b780a13f67288d9b1a031b064fb140cdacaae/clusters/exercise-world.json).

## World extensions

Select a preview to open its full-size SVG. Each extension guide includes a tabletop case and links to its MISP Galaxy definition and cluster collection. Extensions reference the base world's entities by UUID.

| Map or diagram | Extension guide and coverage |
|---|---|
| <a href="extensions/country-flags/country-flags-map.svg"><img src="extensions/country-flags/country-flags-map.svg" alt="Map and visual index of Nacre’s ten country flags" width="240"></a> | **[Country flags](extensions/country-flags/README.md)**<br>Original flags for all ten countries, with a visual index of countries and capitals. |
| <a href="extensions/communities/communities-matrix.svg"><img src="extensions/communities/communities-matrix.svg" alt="Matrix of illustrative community associations across Nacre" width="240"></a> | **[Fictional communities](extensions/communities/README.md)**<br>Invented ethnic identities and religions with illustrative associations across all ten countries. |
| <a href="extensions/telecom/telecom-map.svg"><img src="extensions/telecom/telecom-map.svg" alt="Telecommunications operators and fiber routes across Nacre" width="240"></a> | **[Telecommunications](extensions/telecom/README.md)**<br>Fixed and radio access operators, shared and restricted fiber links, and a two-link outage exercise. |
| <a href="extensions/satellite-communications/satellite-communications-map.svg"><img src="extensions/satellite-communications/satellite-communications-map.svg" alt="GEO, MEO, and LEO satellite communications footprints" width="240"></a> | **[Satellite communications](extensions/satellite-communications/README.md)**<br>GEO VSAT, MEO backhaul, and a low-latency LEO mesh with coverage footprints and links to terrestrial telecom. |
| <a href="extensions/satellite-navigation/satellite-navigation-map.svg"><img src="extensions/satellite-navigation/satellite-navigation-map.svg" alt="Waymark satellite navigation visibility footprints over Nacre" width="240"></a> | **[Satellite navigation](extensions/satellite-navigation/README.md)**<br>Fictional positioning, navigation, and timing broadcasts, visibility footprints, and a defensive exercise on suspected jamming. |
| <a href="extensions/electricity/electricity-map.svg"><img src="extensions/electricity/electricity-map.svg" alt="Nacre power plants, transmission lines, and distribution hubs" width="240"></a> | **[Electricity](extensions/electricity/README.md)**<br>Renewable, nuclear, and fossil generation, cross-border transmission, local distribution, and an island supply shortfall exercise. |
| <a href="extensions/oil-refining/oil-refining-map.svg"><img src="extensions/oil-refining/oil-refining-map.svg" alt="Oil production sites, pipelines, and refineries across Nacre" width="240"></a> | **[Oil production and refining](extensions/oil-refining/README.md)**<br>Country capabilities, offshore and onshore crude supply, pipelines, refineries, and fuel links to the electricity grid. |
| <a href="extensions/water-supply/water-supply-map.svg"><img src="extensions/water-supply/water-supply-map.svg" alt="Water sources, treatment plants, and transfer routes across Nacre" width="240"></a> | **[Water supply](extensions/water-supply/README.md)**<br>Water sources, treatment plants, local distribution districts, and treated-water transfers across part of Nacre. |
| <a href="extensions/civil-humanitarian/civil-humanitarian-map.svg"><img src="extensions/civil-humanitarian/civil-humanitarian-map.svg" alt="Hospitals, schools, shelters, and relief facilities across Nacre" width="240"></a> | **[Civil and humanitarian services](extensions/civil-humanitarian/README.md)**<br>Hospitals, schools, shelters, and relief facilities with links to water, electricity, telecom, and transport. |
| <a href="extensions/datacenters/datacenters-map.svg"><img src="extensions/datacenters/datacenters-map.svg" alt="Nacre data centers and their fiber and power connections" width="240"></a> | **[Data centers](extensions/datacenters/README.md)**<br>Facility ownership and operation, carrier circuits, shared fiber entrances, and electricity grid connections. |
| <a href="extensions/transport/transport-map.svg"><img src="extensions/transport/transport-map.svg" alt="Road, rail, ferry, and cargo routes across Nacre" width="240"></a> | **[Transport and logistics](extensions/transport/README.md)**<br>Truck and coach roads, freight and passenger rail, cargo boats, ferries, and rerouting after a berth closure. |
| <a href="extensions/aviation/aviation-map.svg"><img src="extensions/aviation/aviation-map.svg" alt="Civil airports, air traffic control, and flight routes across Nacre" width="240"></a> | **[Civil aviation](extensions/aviation/README.md)**<br>Aircraft, airports, air traffic control, scheduled passenger and cargo routes, and an airport diversion exercise. |
| <a href="extensions/military-aviation/military-aviation-map.svg"><img src="extensions/military-aviation/military-aviation-map.svg" alt="Military airfields, radar, and aviation fuel links across Nacre" width="240"></a> | **[Military aviation](extensions/military-aviation/README.md)**<br>Military transport aircraft, airfields, radar reporting, aviation kerosene pipelines, and relief logistics coordinated with civil aviation. |
| <a href="extensions/army/army-map.svg"><img src="extensions/army/army-map.svg" alt="Nacre army liaison locations by country" width="240"></a> | **[Army](extensions/army/README.md)**<br>Land services and territorial reserves, with links to freight terminals and civil relief. |
| <a href="extensions/navy/navy-map.svg"><img src="extensions/navy/navy-map.svg" alt="Nacre navy liaison locations by country" width="240"></a> | **[Navy](extensions/navy/README.md)**<br>Naval services, port liaison, and maritime relief handoffs across four coastal and island countries. |
| <a href="extensions/air-force/air-force-map.svg"><img src="extensions/air-force/air-force-map.svg" alt="Nacre air force liaison locations by country" width="240"></a> | **[Air force](extensions/air-force/README.md)**<br>Air services and an army air wing, linked to the existing civil and military aviation records. |
| <a href="extensions/space-force/space-force-map.svg"><img src="extensions/space-force/space-force-map.svg" alt="Nacre space force liaison locations by country" width="240"></a> | **[Space force](extensions/space-force/README.md)**<br>Three models for space-service liaison, with links to Waymark timing and navigation monitors. |
| <a href="extensions/marines/marines-map.svg"><img src="extensions/marines/marines-map.svg" alt="Nacre marines liaison locations by country" width="240"></a> | **[Marines](extensions/marines/README.md)**<br>Marine contingents within three navies, with ship-to-shore relief and civil handoff links. |
| <a href="extensions/coast-guard/coast-guard-map.svg"><img src="extensions/coast-guard/coast-guard-map.svg" alt="Nacre coast guard liaison locations by country" width="240"></a> | **[Coast guard](extensions/coast-guard/README.md)**<br>Military and civilian coast guard models, with rescue, safety, and port reception links. |

## Community integrations

- [Range42](https://github.com/range42), an open-source cyber range platform, is integrating
  the dataset as a neutral narrative layer for its MISP lab, scenario manifests, reporting
  workflows, and future exercise-management tooling. The work is tracked in
  [range42/project_management#106](https://github.com/range42/project_management/issues/106),
  with implementation in
  [range42/range42-catalog#211](https://github.com/range42/range42-catalog/pull/211) and
  [range42/range42-playbooks#151](https://github.com/range42/range42-playbooks/pull/151).
  Status: integration in progress.

## PDF documentation

The GitHub Actions workflow builds a single PDF from this README, the geographic atlas guide, and every extension guide. Open a completed run and download the `synthetic-exercise-world-pdf` artifact. [Build documentation PDF](https://github.com/MISP/Synthetic-Exercise-World-Format/actions/workflows/documentation-pdf.yml)

To build locally, install Python 3.9 or later and Quarto 1.9.38, then run this command from the repository root.

```sh
python3 scripts/build_pdf.py
```

The PDF is written to `_book/synthetic-exercise-world.pdf`. The build downloads the pinned MISP Book Typst layout, logo, and fonts, and uses the maps in the current checkout. The layout is credited to the MISP Book contributors under CC BY-SA 4.0, with the cover and running text adapted for Synthetic Exercise World. The fonts use the SIL Open Font License 1.1. [MISP Book PDF template](https://github.com/MISP/misp-book/tree/b675fdc9e3926490bd104a3280e2344c10269b8f/assets/pdf)

# Contributing

Contributions can be made through the public GitHub repository by opening issues for proposed changes or submitting pull requests with new synthetic entities, metadata improvements, maps, diagrams, or documentation updates.

Repository: [https://github.com/MISP/Synthetic-Exercise-World-Format](https://github.com/MISP/Synthetic-Exercise-World-Format)

# License

Synthetic Exercise World is licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

You may share and adapt the material for any purpose, including commercial use, provided that you give appropriate credit, link to the license, and indicate whether changes were made.

Suggested attribution:

> Synthetic Exercise World — licensed under CC BY 4.0.

License text: <https://creativecommons.org/licenses/by/4.0/>

All countries, companies, sectors, and threat actors described in this project are fictional and intended for neutral CTI exercises, documentation, testing, and training.
