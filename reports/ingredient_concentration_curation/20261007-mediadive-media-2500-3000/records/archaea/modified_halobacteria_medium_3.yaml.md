# Medium Concentration Review: MODIFIED HALOBACTERIA MEDIUM-3

- Record: data/normalized_yaml/archaea/modified_halobacteria_medium_3.yaml
- ID: CultureMech:002192
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `660e8744b99ec71e3b9c29a4f760e5102f6eada4fe346a922d27a6609ce61007`
- Proposed/result SHA256: `660e8744b99ec71e3b9c29a4f760e5102f6eada4fe346a922d27a6609ce61007`
- Source: https://mediadive.dsmz.de/rest/medium/J1008
- Source SHA256: c5ea5f0069023ab5fed00b7d07bc037d0953c415396ced6b8e985488b80d4bf9
- Retrieved: 2026-10-07T14:42:33.438059+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Casamino acids | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1008 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1008 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Na glutamate | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1008 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Trisodium citrate | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1008 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1008 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | KCl | {"unit": "G_PER_L", "value": "2"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1008 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | NaCl | {"unit": "G_PER_L", "value": "200"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1008 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | FeCl2 x 4 H2O | {"unit": "MG_PER_L", "value": "36"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1008 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[8].concentration` | MnCl2 x 4 H2O | {"unit": "MG_PER_L", "value": "0.36"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1008 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `parent_media` | halobacteria_medium | {"id": "CultureMech:002527", "name": "halobacteria_medium", "path": "data/normalized_yaml/bacterial/JCM_J168_HALOBACTERIA_MEDIUM.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1008 | {<br>                        "step": "Use Medium No. 168 supplemented with 270.0 g/L NaCl (final) and 15.0 g/L MgSO4 x 7H2O. Adjust pH to 7.5."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Halobacteria Variant Concentration Follow-Up

The [applied source-specific follow-up](../../../20261009-halobacteria-variants/applied-records/J1008.md) records all reviewed quantities, exact source snippets, preserved parent ingredients, preparation boundaries and actual checks. This earlier report remains historical context.
