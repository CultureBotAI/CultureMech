# Solution Concentration Review: Main sol. 1514

- Record: data/normalized_yaml/bacterial/mediadive_3133_Main_sol_1514.yaml
- ID: CultureMech:012347
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6d8877efb442953ffb4d290444976ff37b635583979d85b19b25f9fa73c90069`
- Proposed/result SHA256: `6d8877efb442953ffb4d290444976ff37b635583979d85b19b25f9fa73c90069`
- Source: https://mediadive.dsmz.de/rest/solution/3133
- Source SHA256: ac5c24d95507f74bc12a920a2de63aae9f89ca3397da72a80d8f2127b55e46dc
- Retrieved: 2026-10-07T09:18:47.100317+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Grace's Insect Medium | {"unit": "PERCENT_V_V", "value": "900"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3133 | {<br>                "recipe_order": 1,<br>                "compound": "Grace's Insect Medium",<br>                "compound_id": 1382,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Sigma Aldrich, G8142",<br>                "amount": 900,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1382) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Fetal bovine serum | {"unit": "PERCENT_V_V", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3133 | {<br>                "recipe_order": 2,<br>                "compound": "Fetal bovine serum",<br>                "compound_id": 954,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "heat-inactivated, 56\u00b0C, 30 min",<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=954) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
