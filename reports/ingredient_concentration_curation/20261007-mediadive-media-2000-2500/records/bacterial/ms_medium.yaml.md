# Medium Concentration Review: MS MEDIUM

- Record: data/normalized_yaml/bacterial/ms_medium.yaml
- ID: CultureMech:002626
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3dadec73e33b0f254381b0c6abd38f2dd73f9a437cfb445b9766c7013253d4a2`
- Proposed/result SHA256: `3dadec73e33b0f254381b0c6abd38f2dd73f9a437cfb445b9766c7013253d4a2`
- Source: https://mediadive.dsmz.de/rest/medium/J269
- Source SHA256: b4b6c7d6297f0b41b5a5ebdb564ea9a1629ba24ca694421d9add5e3fa0a86361
- Retrieved: 2026-10-07T14:04:15.538165+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J269 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | (NH4)2SO4 | {"unit": "G_PER_L", "value": "1.3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J269 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "0.28"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J269 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "0.25"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J269 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "0.07"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J269 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | FeCl3 x 6 H2O | {"unit": "G_PER_L", "value": "0.002"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J269 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | MnCl2 x 4 H2O | {"unit": "G_PER_L", "value": "0.0018"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J269 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | Na2B4O7 x 10 H2O | {"unit": "G_PER_L", "value": "0.0045"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J269 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[8].concentration` | ZnSO4 x 7 H2O | {"unit": "G_PER_L", "value": "0.00022"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J269 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[9].concentration` | CuCl2 x 2 H2O | {"unit": "G_PER_L", "value": "5e-05"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J269 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[10].concentration` | Na2MoO4 x 2 H2O | {"unit": "G_PER_L", "value": "3e-05"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J269 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[11].concentration` | VOSO4 x n H2O | {"unit": "G_PER_L", "value": "3e-05"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J269 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[12].concentration` | CoSO4 x 7 H2O | {"unit": "G_PER_L", "value": "1e-05"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J269 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J269 | {<br>                        "step": "Use Medium No. 165 with 1.0 g Na2S2O3 x 5H2O, and adjust pH to 7.0-7.5 with NaOH."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
