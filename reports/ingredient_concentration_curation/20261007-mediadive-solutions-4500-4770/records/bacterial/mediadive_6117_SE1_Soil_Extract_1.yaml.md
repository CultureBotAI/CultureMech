# Solution Concentration Review: SE1 (Soil Extract 1)

- Record: data/normalized_yaml/bacterial/mediadive_6117_SE1_Soil_Extract_1.yaml
- ID: CultureMech:014820
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `51a36af7def22485ed9da4c0a972dd87e907a9e158ff2f75529ea91950bcd813`
- Proposed/result SHA256: `51a36af7def22485ed9da4c0a972dd87e907a9e158ff2f75529ea91950bcd813`
- Source: https://mediadive.dsmz.de/rest/solution/6117
- Source SHA256: 57c97545cae1d74098f76cc3a80fbec93ff157e5bae9454747eccdad1f73598d
- Retrieved: 2026-10-07T10:00:16.601265+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Soil extract | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6117 | {<br>                "recipe_order": 2,<br>                "compound": "Soil extract",<br>                "compound_id": 180,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "air-dried",<br>                "amount": null,<br>                "unit": null,<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=180) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6117 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": null,<br>                "unit": null,<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Missing numeric input | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
