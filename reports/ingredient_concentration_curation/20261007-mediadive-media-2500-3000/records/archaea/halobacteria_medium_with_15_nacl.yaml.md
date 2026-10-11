# Medium Concentration Review: HALOBACTERIA MEDIUM WITH 15% NaCl

- Record: data/normalized_yaml/archaea/halobacteria_medium_with_15_nacl.yaml
- ID: CultureMech:003262
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0fbd06e56a648ecf87d1e553f92f707f73560ed32a5b71010596aafc421edbe2`
- Proposed/result SHA256: `0fbd06e56a648ecf87d1e553f92f707f73560ed32a5b71010596aafc421edbe2`
- Source: https://mediadive.dsmz.de/rest/medium/J914
- Source SHA256: d7563277a2e41e6b60fc5cf04eda1279af24445f38ca3b5ff88cf78f88c525bc
- Retrieved: 2026-10-07T14:41:15.280990+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Casamino acids | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J914 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J914 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Na glutamate | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J914 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Trisodium citrate | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J914 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J914 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | KCl | {"unit": "G_PER_L", "value": "2"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J914 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | NaCl | {"unit": "G_PER_L", "value": "200"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J914 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | FeCl2 x 4 H2O | {"unit": "MG_PER_L", "value": "36"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J914 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[8].concentration` | MnCl2 x 4 H2O | {"unit": "MG_PER_L", "value": "0.36"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J914 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J914 | {<br>                        "step": "Use Medium No. 168 with 150.0 g/L (final) NaCl. Omit agar for preparation of liquid medium."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Halobacteria Variant Concentration Follow-Up

The [applied source-specific follow-up](../../../20261009-halobacteria-variants/applied-records/J914.md) records all reviewed quantities, exact source snippets, preserved parent ingredients, preparation boundaries and actual checks. This earlier report remains historical context.
