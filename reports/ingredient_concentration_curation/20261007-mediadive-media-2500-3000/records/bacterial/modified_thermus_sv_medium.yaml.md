# Medium Concentration Review: MODIFIED THERMUS SV MEDIUM

- Record: data/normalized_yaml/bacterial/modified_thermus_sv_medium.yaml
- ID: CultureMech:002971
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `4c371d8556a978d1ace5086d60964f41eba07357107b4d84c5398665445fa354`
- Proposed/result SHA256: `4c371d8556a978d1ace5086d60964f41eba07357107b4d84c5398665445fa354`
- Source: https://mediadive.dsmz.de/rest/medium/J625
- Source SHA256: 38483bc669943680a00eba516d4d5578b1400c05d3acfb3b0cce5e47dc68c03a
- Retrieved: 2026-10-07T14:37:22.319878+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Peptone | {"unit": "G_PER_L", "value": "2.9703"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J625 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.990099"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J625 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Sodium glutamate monohydrate | {"unit": "G_PER_L", "value": "0.990099"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J625 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | NaCl | {"unit": "G_PER_L", "value": "29.7814314"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J625 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | Nitrilotriacetic acid | {"unit": "G_PER_L", "value": "0.980392"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J625 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | CaSO4 x 2 H2O | {"unit": "G_PER_L", "value": "0.588235"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J625 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "0.980392"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J625 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | KNO3 | {"unit": "G_PER_L", "value": "1.0098"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J625 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[8].concentration` | NaNO3 | {"unit": "G_PER_L", "value": "6.7549"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J625 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[9].concentration` | Na2HPO4 | {"unit": "G_PER_L", "value": "1.08824"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J625 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[10].concentration` | FeCl3 x 6 H2O | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J625 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J625 | {<br>                        "step": "Use Medium No. 624 supplemented with 3.0 g/L L-proline. Trace vitamins (see Medium No. 197, 10 ml/L) can be substituted for L-proline."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
