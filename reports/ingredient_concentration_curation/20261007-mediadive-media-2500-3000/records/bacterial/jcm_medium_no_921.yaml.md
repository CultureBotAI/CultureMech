# Medium Concentration Review: JCM MEDIUM No. 921

- Record: data/normalized_yaml/bacterial/jcm_medium_no_921.yaml
- ID: CultureMech:003269
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e3a52b112fd499214af8f22d20b0a9dd68e99ae29cefe0468be1260cfdd1b092`
- Proposed/result SHA256: `e3a52b112fd499214af8f22d20b0a9dd68e99ae29cefe0468be1260cfdd1b092`
- Source: https://mediadive.dsmz.de/rest/medium/J921
- Source SHA256: 2848e2330dd83e8a5ec67b5889ad47c85da6de7ec14facde01796d8327ba0b76
- Retrieved: 2026-10-07T14:41:21.022951+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Marine broth 2216 | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J921 | {<br>                        "recipe_order": 1,<br>                        "compound": "Marine broth 2216",<br>                        "compound_id": 1607,<br>                        "attribute": "BD-Difco",<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[1].concentration` | Starch | {"unit": "G_PER_L", "value": "2"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J921 | {<br>                        "recipe_order": 2,<br>                        "compound": "Starch",<br>                        "compound_id": 199,<br>                        "attribute": "soluble",<br>                        "amount": 2,<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[2].concentration` | NaCl | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J921 | {<br>                        "recipe_order": 3,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Missing numeric input | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J921 | {<br>                        "step": "Adjust pH to 7.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
