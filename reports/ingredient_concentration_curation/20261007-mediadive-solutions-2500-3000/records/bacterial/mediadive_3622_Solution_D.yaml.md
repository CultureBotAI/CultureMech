# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_3622_Solution_D.yaml
- ID: CultureMech:012702
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `efd63473554f3d65b0517b3a890a16a5dc26aa10e9d3801c5f7bd912b92d54bd`
- Proposed/result SHA256: `efd63473554f3d65b0517b3a890a16a5dc26aa10e9d3801c5f7bd912b92d54bd`
- Source: https://mediadive.dsmz.de/rest/solution/3622
- Source SHA256: 62e286d683a0889390658dd8a98430e09ecc13145e404493aa9218957290f7e5
- Retrieved: 2026-10-07T09:23:03.759363+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Resazurin | {"unit": "G_PER_L", "value": "0.005"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3622 | {<br>                "recipe_order": 1,<br>                "compound": "Resazurin",<br>                "compound_id": 25,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0,1%",<br>                "amount": 0.5,<br>                "unit": "ml",<br>                "g_l": 0.005,<br>                "mmol_l": 0.021816,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=25) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3622 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 450,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
