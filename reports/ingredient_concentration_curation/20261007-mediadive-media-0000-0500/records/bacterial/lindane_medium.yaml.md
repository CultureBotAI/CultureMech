# Medium Concentration Review: LINDANE MEDIUM

- Record: data/normalized_yaml/bacterial/lindane_medium.yaml
- ID: CultureMech:000850
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `214edc620273f3638982dfe171874ccc3825332af8dee8b062fe59467f41a85f`
- Proposed/result SHA256: `214edc620273f3638982dfe171874ccc3825332af8dee8b062fe59467f41a85f`
- Source: https://mediadive.dsmz.de/rest/medium/138
- Source SHA256: 9d997bf0b8d7f427d7abfda9fe21d1acbbc96a8e39719c7405de71dc6790906f
- Retrieved: 2026-10-07T10:42:45.376977+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/138 | {<br>                        "recipe_order": 1,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[1].concentration` | Hexachlorocyclo-hexane | {"unit": "G_PER_L", "value": "0.1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/138 | {<br>                        "recipe_order": 2,<br>                        "compound": "Hexachlorocyclo-hexane",<br>                        "compound_id": 245,<br>                        "attribute": "Lindane",<br>                        "amount": 0.1,<br>                        "unit": "g",<br>                        "g_l": 0.1,<br>                        "mmol_l": 0.343846,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/138 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `variant_children[0]` | lindane_medium | {"id": "CultureMech:004112", "name": "lindane_medium", "notes": "KOMODO record is an exact source duplicate of DSMZ Medium 138; local ingredient and concentration signatures match.", "path": "data/normalized_yaml/bacterial/KOMODO_138_LINDANE_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/138 | {<br>                        "step": "Adjust pH to 7.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
