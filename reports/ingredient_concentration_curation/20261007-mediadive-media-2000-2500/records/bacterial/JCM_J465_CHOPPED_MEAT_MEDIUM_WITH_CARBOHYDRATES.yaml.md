# Medium Concentration Review: CHOPPED MEAT MEDIUM WITH CARBOHYDRATES

- Record: data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
- ID: CultureMech:002813
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ffb0ccecbe5b7d1e43b42901c2bede7b7ea2d89da65032070af88959eddf2869`
- Proposed/result SHA256: `ffb0ccecbe5b7d1e43b42901c2bede7b7ea2d89da65032070af88959eddf2869`
- Source: https://mediadive.dsmz.de/rest/medium/J465
- Source SHA256: 45907a66dd2144472795e8298857a58b403ad64e7bba850b3cec0633fbcbc172
- Retrieved: 2026-10-07T14:06:58.117953+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Ground beef | {"unit": "G_PER_L", "value": "487.805"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J465 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | NaOH | {"unit": "G_PER_L", "value": "25"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J465 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Casitone | {"unit": "G_PER_L", "value": "29.2683"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J465 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "4.87805"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J465 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "4.87805"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J465 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | Resazurin | {"unit": "G_PER_L", "value": "0.00097561"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J465 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J465 | {<br>                        "step": "Use Medium No. 461 with 0.4% glucose, 0.1% cellobiose, 0.1% maltose and 0.1% soluble starch."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
