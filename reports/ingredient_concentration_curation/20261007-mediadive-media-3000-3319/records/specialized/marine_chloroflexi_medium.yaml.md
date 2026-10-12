# Medium Concentration Review: MARINE CHLOROFLEXI MEDIUM

- Record: data/normalized_yaml/specialized/marine_chloroflexi_medium.yaml
- ID: CultureMech:015391
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1f0d9d7b8876b5b6a8297eb84c85d79e13f24dcec3c0e03c4519d1e59c826937`
- Proposed/result SHA256: `1f0d9d7b8876b5b6a8297eb84c85d79e13f24dcec3c0e03c4519d1e59c826937`
- Source: https://mediadive.dsmz.de/rest/medium/J1188
- Source SHA256: fc96f738ac1889d8a2ad1e0ccf0a700cb148b3c88997c5c66fb32bfb4da87e2e
- Retrieved: 2026-10-07T15:20:35.122473+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "0.1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1188 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | MgCl2·6H2O | {"unit": "G_PER_L", "value": "4.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1188 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | CaCl2·2H2O | {"unit": "G_PER_L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1188 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | NH4Cl | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1188 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | NaCl | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1188 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1188 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | Peptone | {"unit": "G_PER_L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1188 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | Trace vitamins solution (see Medium No.284) | {"unit": "ML_PER_L", "value": "2.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1188 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[8].concentration` | Trace mineral solution (see Medium No.852) | {"unit": "ML_PER_L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1188 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[9].concentration` | Se/W solution (Medium No.852) | {"unit": "ML_PER_L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1188 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[10].concentration` | 1 M Sodium pyruvate* | {"unit": "ML_PER_L", "value": "10.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1188 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[11].concentration` | 8% NaHCO3solution* | {"unit": "ML_PER_L", "value": "25.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1188 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[12].concentration` | 5% L-Cysteine·HCl·H2O solution | {"unit": "ML_PER_L", "value": "6.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1188 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[13].concentration` | 5% Na2S·9H2O solution | {"unit": "ML_PER_L", "value": "6.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1188 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1188 | {<br>                        "step": "Use Medium No. 1187 supplemented with 10 mM sodium pyruvate (final, filter-sterilized)."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
