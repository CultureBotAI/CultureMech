# Medium Concentration Review: OAT FLAKE MEDIUM

- Record: data/normalized_yaml/bacterial/oat_flake_medium.yaml
- ID: CultureMech:001281
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `fcc6ebd4768113ea76dab09bad3c5d82d0d6f7e6dfb8e693c5ec940900326453`
- Proposed/result SHA256: `fcc6ebd4768113ea76dab09bad3c5d82d0d6f7e6dfb8e693c5ec940900326453`
- Source: https://mediadive.dsmz.de/rest/medium/189
- Source SHA256: 5f9a3c04ab01c39d3a249d81a5327ee074141354070941060433704b179cd74e
- Retrieved: 2026-10-07T10:43:25.566116+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Oat flakes | {"unit": "G_PER_L", "value": "30.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/189 | {<br>                        "recipe_order": 1,<br>                        "compound": "Oat flakes",<br>                        "compound_id": 292,<br>                        "amount": 30,<br>                        "unit": "g",<br>                        "g_l": 30,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[1].concentration` | Agar | {"unit": "G_PER_L", "value": "15.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/189 | {<br>                        "recipe_order": 2,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/189 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `variant_children[0]` | oat_flake_medium | {"id": "CultureMech:004213", "name": "oat_flake_medium", "notes": "KOMODO record is an exact source duplicate of DSMZ Medium 189; local physical state, ingredient, and concentration signatures match.", "path": "data/normalized_yaml/bacterial/KOMODO_189_OAT_FLAKE_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/189 | {<br>                        "step": "Boil oat flakes in water for 10 min; fill up to 1 l and add agar. Autoclave 20 min at 121\u00b0C. Shake before pouring. pH 6.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
