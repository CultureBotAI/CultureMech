# Medium Concentration Review: GAUZE'S SYNTHETIC MEDIUM NO. 1 (pH 5.3)

- Record: data/normalized_yaml/bacterial/gauzes_synthetic_medium_no_1_ph_5_3.yaml
- ID: CultureMech:003296
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f393b02244af482c3f2d5a448443327ce62b8c4f2b7040b5100f964fc39d6403`
- Proposed/result SHA256: `f393b02244af482c3f2d5a448443327ce62b8c4f2b7040b5100f964fc39d6403`
- Source: https://mediadive.dsmz.de/rest/medium/J949
- Source SHA256: 288eb5ea960315c2002ae7bc0bd83d1705d06592eb8edc74df5a32d5fcd189b4
- Retrieved: 2026-10-07T14:41:44.471045+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Starch | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J949 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | KNO3 | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J949 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | NaCl | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J949 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J949 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J949 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "0.01"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J949 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J949 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J949 | {<br>                        "step": "Prepare Gauze's synthetic medium No. 1 (see Medium No. 81) and adjust pH to 5.3."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
