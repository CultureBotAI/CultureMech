# Solution Concentration Review: Starch solution 5%(w/v)

- Record: data/normalized_yaml/bacterial/mediadive_4431_Starch_solution_5_w_v.yaml
- ID: CultureMech:013414
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `955acb2039123fce87414d945c44a7b8df24df886feae4aad3f23560d74bc36b`
- Proposed/result SHA256: `955acb2039123fce87414d945c44a7b8df24df886feae4aad3f23560d74bc36b`
- Source: https://mediadive.dsmz.de/rest/solution/4431
- Source SHA256: 680dc471e07cb1ed6af6c871c9562fd0976f8dd7e988a2cb5485ea11f1e0f206
- Retrieved: 2026-10-07T09:43:40.722060+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Starch | {"unit": "G_PER_L", "value": "50"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4431 | {<br>                "recipe_order": 1,<br>                "compound": "Starch",<br>                "compound_id": 199,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "soluble",<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 50,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=199) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4431 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
