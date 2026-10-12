# Solution Concentration Review: HEPES solution

- Record: data/normalized_yaml/bacterial/mediadive_5044_HEPES_solution.yaml
- ID: CultureMech:013962
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b4f47ab1dc9c1bd73a09645df72ab7a997d98d97195b10aa5ab29b867bf654eb`
- Proposed/result SHA256: `b4f47ab1dc9c1bd73a09645df72ab7a997d98d97195b10aa5ab29b867bf654eb`
- Source: https://mediadive.dsmz.de/rest/solution/5044
- Source SHA256: 9cf5d9087c3f729f48f2b75db7c5a8ee56c8f65fb74ea7b8785f968e36be6a3e
- Retrieved: 2026-10-07T09:50:19.655826+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaOH | {"unit": "G_PER_L", "value": "12"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5044 | {<br>                "recipe_order": 1,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 12,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=256) | Missing numeric input | unchanged |
| `composition[1].concentration` | HEPES | {"unit": "G_PER_L", "value": "119.2"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5044 | {<br>                "recipe_order": 2,<br>                "compound": "HEPES",<br>                "compound_id": 371,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "free acid",<br>                "amount": 119.2,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=371) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
