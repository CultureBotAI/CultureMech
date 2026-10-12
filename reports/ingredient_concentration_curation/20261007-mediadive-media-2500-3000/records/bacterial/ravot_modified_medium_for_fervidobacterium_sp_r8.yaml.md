# Medium Concentration Review: RAVOT MODIFIED MEDIUM FOR FERVIDOBACTERIUM SP. R8

- Record: data/normalized_yaml/bacterial/ravot_modified_medium_for_fervidobacterium_sp_r8.yaml
- ID: CultureMech:003070
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6508d9bb1909659d15325ce3dbef83a00d2c52aea4ffb671b4c84cfd3bf3148e`
- Proposed/result SHA256: `6508d9bb1909659d15325ce3dbef83a00d2c52aea4ffb671b4c84cfd3bf3148e`
- Source: https://mediadive.dsmz.de/rest/medium/J726
- Source SHA256: 7d884d99eadae19516566af0e03f4c7d1a1249b56fab1c9df6d4f6a6168723c7
- Retrieved: 2026-10-07T14:38:43.013174+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | NH4Cl | {"unit": "G_PER_L", "value": "0.981354"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J726 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | MgCl2 x 6 H2O | {"unit": "G_PER_L", "value": "0.196271"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J726 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "0.0981354"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J726 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | KCl | {"unit": "G_PER_L", "value": "0.0981354"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J726 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | Sodium acetate x 3 H2O | {"unit": "G_PER_L", "value": "0.814524"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J726 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "4.90677"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J726 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | Trypticase peptone | {"unit": "G_PER_L", "value": "4.90677"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J726 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | PIPES | {"unit": "G_PER_L", "value": "3.38567"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J726 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[8].concentration` | Sulfur | {"unit": "G_PER_L", "value": "4.90677"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J726 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[9].concentration` | Resazurin | {"unit": "G_PER_L", "value": "0.000981354"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J726 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[10].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "4.3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J726 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[11].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "4.3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J726 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[12].concentration` | Na2S x 9 H2O | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J726 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `parent_media` | ravot_modified_medium_for_thermosipho_sp_g60 | {"id": "CultureMech:003071", "name": "ravot_modified_medium_for_thermosipho_sp_g60", "path": "data/normalized_yaml/bacterial/ravot_modified_medium_for_thermosipho_sp_g60.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J726 | {<br>                        "step": "Use Medium No. 725 with 5.0 g/L NaCl. Adjust pH to 6.3."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
