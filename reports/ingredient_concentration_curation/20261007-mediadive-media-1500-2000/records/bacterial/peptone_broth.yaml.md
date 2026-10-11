# Medium Concentration Review: PEPTONE BROTH

- Record: data/normalized_yaml/bacterial/peptone_broth.yaml
- ID: CultureMech:000938
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a68b3d141a042bbfdcfc109df6d5e66e575a23a8fe1a62d61dc8338698db8dd1`
- Proposed/result SHA256: `a68b3d141a042bbfdcfc109df6d5e66e575a23a8fe1a62d61dc8338698db8dd1`
- Source: https://mediadive.dsmz.de/rest/medium/1471
- Source SHA256: 85aceae66d07a4b9dffe8c8e42881ff120a7a4d75fd655bee14e780a46a42ffc
- Retrieved: 2026-10-07T13:42:19.085597+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Peptone | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1471 | {<br>                        "recipe_order": 1,<br>                        "compound": "Peptone",<br>                        "compound_id": 1,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[1].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1471 | {<br>                        "recipe_order": 2,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1471 | {<br>                        "step": "Put a 3 inch strip of Whatman no. 1 filter paper into each test tube with the above solution to cover approximately 2/3 the length of the paper."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
