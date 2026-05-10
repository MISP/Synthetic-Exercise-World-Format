# Synthetic Exercise World - Self-contained fictional world dataset for cyber exercises and standards documents.

## Why the Synthetic Exercise World Format Matters

The Synthetic Exercise World Format provides a neutral and reusable reference environment for cyber threat intelligence exercises, drills, training scenarios, and documentation. By using fictional countries, organizations, sectors, infrastructures, and threat actors, participants can discuss realistic CTI concepts without implicitly referring to real geopolitical situations, real victims, or real adversaries. This helps trainers, analysts, vendors, public institutions, and standardization bodies focus on the structure, quality, and interoperability of the information rather than on politically sensitive interpretations.

Neutrality is especially important when creating reference material for CTI formats, taxonomies, sharing models, or operational procedures. Real-world examples can unintentionally introduce bias, diplomatic sensitivity, legal concerns, or disagreement between participating countries and organizations. A synthetic world avoids these issues by offering realistic but non-attributable entities that can be safely used in examples, schemas, test cases, playbooks, and exercises. This makes the reference document easier to adopt across different jurisdictions and communities.

A shared synthetic environment also improves consistency. Instead of each exercise or standard document inventing its own partial examples, the same fictional countries, companies, sectors, and threat actors can be reused across multiple tools and formats. This makes it easier to compare implementations, validate parsers, test data models, and demonstrate interoperability between CTI platforms. The format can become a common neutral vocabulary for examples, much like test datasets are used in software engineering.

The Synthetic Exercise World Format also supports realistic scenario design without exposing sensitive national, sectoral, or organizational information. Exercise planners can model cross-border incidents, supply-chain compromises, sector-specific threats, vulnerability disclosure workflows, and intelligence-sharing procedures while avoiding references to real critical infrastructure or real governmental relationships. This lowers the barrier for participation and allows organizations with different confidentiality requirements to collaborate in the same scenario.

Including the Synthetic Exercise World Format in reference documentation helps ensure that CTI standards and tools can be widely deployed. It provides a safe, politically neutral, and technically meaningful foundation for examples, demonstrations, conformance testing, and training. By separating the technical purpose of CTI sharing from real-world sensitivities, the format encourages broader adoption, clearer communication, and more inclusive participation across countries, sectors, and communities.

# Synthetic Exercise World Format — Data Model

![Synthetic Exercise World Format diagram](https://hdoc.csirt-tooling.org/uploads/4c5f388f-4965-4a79-b8cf-507361747c1a.png)

## What the JSON provides

The dataset is a single JSON object with document-level fields such as `name`, `type`, `uuid`, `version`, `description`, and a reusable `values[]` list. Each item in `values[]` has a common record shape: `value`, `uuid`, `description`, and `meta`.

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

## MISP Galaxy 

- [Self-contained fictional world dataset for cyber exercises and standards documents](https://github.com/MISP/misp-galaxy/blob/main/clusters/exercise-world.json) in MISP Galaxy JSON format.

# Geography of the Synthetic Exercise World

![Synthetic Exercise World - Planet Nacre](https://hdoc.csirt-tooling.org/uploads/34c1f8f7-4ee9-431b-ab5a-ae72247a952c.png)

[SVG](https://hdoc.csirt-tooling.org/uploads/e5e4e1af-188d-4748-ac51-40ed98b32721.svg)


## Synthetic Exercise World Map — Planet Nacre

This field guide accompanies the revised fictional atlas map. The map is designed for neutral cyber-exercise planning and keeps the original synthetic country, company, and threat-actor relationships while making the visual layout easier to read.

![Synthetic Exercise World — Planet Nacre clear-label map](synthetic_exercise_world_clear_map.png)



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


