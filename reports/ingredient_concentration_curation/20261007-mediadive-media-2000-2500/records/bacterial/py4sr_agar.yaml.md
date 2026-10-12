# Medium Concentration Review: PY4SR AGAR

- Record: data/normalized_yaml/bacterial/py4sr_agar.yaml
- ID: CultureMech:002723
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9e875fb45514cc940273cf241643081ca1433e3451e084de6c188e8bbf185821`
- Proposed/result SHA256: `9e875fb45514cc940273cf241643081ca1433e3451e084de6c188e8bbf185821`
- Source: https://mediadive.dsmz.de/rest/medium/J364
- Source SHA256: dbaaf1262837be1bc2da58e928628ed0c4aa53faa63b0c66380cbbaf93782908
- Retrieved: 2026-10-07T14:05:33.366631+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Trypticase peptone | {"unit": "G_PER_L", "value": "9.96016"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J364 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "4.98008"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J364 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Glucose | {"unit": "G_PER_L", "value": "0.249004"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J364 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Cellobiose | {"unit": "G_PER_L", "value": "0.249004"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J364 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | Maltose | {"unit": "G_PER_L", "value": "0.249004"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J364 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | Starch | {"unit": "G_PER_L", "value": "0.249004"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J364 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | Sodium resazurin | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J364 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | Na2CO3 | {"unit": "G_PER_L", "value": "2.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J364 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[8].concentration` | L-Cysteine HCl x H2O | {"unit": "G_PER_L", "value": "0.298805"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J364 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[9].concentration` | Agar | {"unit": "G_PER_L", "value": "14.9402"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J364 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J364 | {<br>                        "step": "Use Medium No. 363 supplemented with 50 ml/L plant residue extract. To prepare the plant residue extract, autoclave rice straw in water (1:5) at 120C for 20 min, and use the supernatant after centrifugation."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
