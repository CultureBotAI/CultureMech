# Medium Concentration Review: MARINE MEDIUM WITH THIOSULFATE

- Record: data/normalized_yaml/specialized/marine_medium_with_thiosulfate.yaml
- ID: CultureMech:015402
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3c35b457c2b349d3bf65898b53b873a1aa70b185c68f31364894a5b6bfde3a39`
- Proposed/result SHA256: `3c35b457c2b349d3bf65898b53b873a1aa70b185c68f31364894a5b6bfde3a39`
- Source: https://mediadive.dsmz.de/rest/medium/J376
- Source SHA256: d48a4c60e45d39a75b7d25e03bcf03fa0f611d2cf372f5a0f83db9171c6e5272
- Retrieved: 2026-10-07T14:05:43.563806+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Distilled water | {"unit": "L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J376 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | NaCl | {"unit": "G_PER_L", "value": "30"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J376 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | CaCl2・2H2O | {"unit": "G_PER_L", "value": "0.15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J376 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "0.2"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J376 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | NH4Cl | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J376 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | MgCl2・6H2O | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J376 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | Na2S・9H2O | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J376 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | KCl | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J376 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[8].concentration` | NaNO3 | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J376 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[9].concentration` | MES | {"unit": "G_PER_L", "value": "1.95"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J376 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[10].concentration` | sodium thiosulfate | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J376 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[11].concentration` | Carbon dioxide gas | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J376 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[12].concentration` | N2 | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J376 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[13].concentration` | Hydrogen gas | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J376 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J376 | {<br>                        "step": "Use Medium No. 375, replacing sulfur with 5.0 g/L sodium thiosulfate."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
