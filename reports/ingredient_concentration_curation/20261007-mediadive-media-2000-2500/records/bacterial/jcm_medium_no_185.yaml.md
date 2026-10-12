# Medium Concentration Review: JCM MEDIUM No. 185

- Record: data/normalized_yaml/bacterial/jcm_medium_no_185.yaml
- ID: CultureMech:002546
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e1250000a862086d7687837e7a6326ef6d25903410fc0ccfce6e47a4a677f6a5`
- Proposed/result SHA256: `e1250000a862086d7687837e7a6326ef6d25903410fc0ccfce6e47a4a677f6a5`
- Source: https://mediadive.dsmz.de/rest/medium/J185
- Source SHA256: 06d0d772ea5f663c7027f66b853273b2f1efe5928697074522777c1b0a45b84c
- Retrieved: 2026-10-07T14:03:07.806023+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J185 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Sulfur | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J185 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | (NH4)2SO4 | {"unit": "G_PER_L", "value": "1.3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J185 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "0.28"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J185 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "0.25"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J185 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "0.07"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J185 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | FeCl3 x 6 H2O | {"unit": "G_PER_L", "value": "0.002"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J185 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | MnCl2 x 4 H2O | {"unit": "G_PER_L", "value": "0.0018"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J185 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[8].concentration` | Na2B4O7 x 10 H2O | {"unit": "G_PER_L", "value": "0.0045"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J185 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[9].concentration` | ZnSO4 x 7 H2O | {"unit": "G_PER_L", "value": "0.00022"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J185 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[10].concentration` | CuCl2 x 2 H2O | {"unit": "G_PER_L", "value": "5e-05"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J185 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[11].concentration` | Na2MoO4 x 2 H2O | {"unit": "G_PER_L", "value": "3e-05"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J185 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[12].concentration` | VOSO4 x n H2O | {"unit": "G_PER_L", "value": "3e-05"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J185 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[13].concentration` | CoSO4 x 7 H2O | {"unit": "G_PER_L", "value": "1e-05"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J185 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `variant_children[0]` | acidianus_infernus_medium_a | {"id": "CultureMech:002534", "name": "acidianus_infernus_medium_a", "notes": "Same ingredient and concentration signature; review as possible duplicate source record.", "path": "data/normalized_yaml/bacterial/acidianus_infernus_medium_a.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J185 | {<br>                        "step": "Use Medium No. 174 with 0.02 g/L (final) yeast extract."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
