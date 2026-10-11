# Medium Concentration Review: MINERAL MEDIUM FOR THIOMONAS ISLANDICUM

- Record: data/normalized_yaml/bacterial/mineral_medium_for_thiomonas_islandicum.yaml
- ID: CultureMech:003117
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `abe487b8fcad87d12e7a4cf2385aa5d4997f0b2ef50d44b5269ed429e032661a`
- Proposed/result SHA256: `abe487b8fcad87d12e7a4cf2385aa5d4997f0b2ef50d44b5269ed429e032661a`
- Source: https://mediadive.dsmz.de/rest/medium/J775
- Source SHA256: 8ed7b8ce85802e41aa1ce54dd34a4dc5cf36cc6c25b27d80a807fa7c21d245ff
- Retrieved: 2026-10-07T14:39:22.461780+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "2.28856"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J775 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Na2HPO4 x 6 H2O | {"unit": "G_PER_L", "value": "2.88557"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J775 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | NH4Cl | {"unit": "G_PER_L", "value": "0.995025"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J775 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | NaHCO3 | {"unit": "G_PER_L", "value": "0.497512"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J775 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "0.0995025"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J775 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "100"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J775 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | Fe(NH4)citrate | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J775 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | ZnSO4 x 7 H2O | {"unit": "G_PER_L", "value": "0.1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J775 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[8].concentration` | MnCl2 x 4 H2O | {"unit": "G_PER_L", "value": "0.03"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J775 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[9].concentration` | H3BO3 | {"unit": "G_PER_L", "value": "0.3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J775 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[10].concentration` | CoCl2 x 6 H2O | {"unit": "G_PER_L", "value": "0.2"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J775 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[11].concentration` | CuCl2 x 2 H2O | {"unit": "G_PER_L", "value": "0.01"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J775 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[12].concentration` | NiCl2 x 6 H2O | {"unit": "G_PER_L", "value": "0.02"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J775 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[13].concentration` | Na2MoO4 x 2 H2O | {"unit": "G_PER_L", "value": "0.03"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J775 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `variant_children[0]` | mineral_medium_for_hydrogenophilus_islandicum | {"id": "CultureMech:003116", "name": "mineral_medium_for_hydrogenophilus_islandicum", "notes": "Same ingredient and concentration signature; review as possible duplicate source record.", "path": "data/normalized_yaml/bacterial/mineral_medium_for_hydrogenophilus_islandicum.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J775 | {<br>                        "step": "Use Medium No. 774 and adjust pH to 4.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
