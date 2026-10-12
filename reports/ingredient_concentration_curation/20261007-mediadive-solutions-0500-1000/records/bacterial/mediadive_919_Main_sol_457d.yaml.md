# Solution Concentration Review: Main sol. 457d

- Record: data/normalized_yaml/bacterial/mediadive_919_Main_sol_457d.yaml
- ID: CultureMech:015271
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0cce8ef8658f041a55294bfff34ed9e39de2ce61eee163fcdac0a8f93d5c1448`
- Proposed/result SHA256: `0cce8ef8658f041a55294bfff34ed9e39de2ce61eee163fcdac0a8f93d5c1448`
- Source: https://mediadive.dsmz.de/rest/solution/919
- Source SHA256: 290c8d17ed0c57113be26b7200837fb1d787678774142c4d520c6368289c3e41
- Retrieved: 2026-10-07T08:47:47.516409+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Biphenyl | {"unit": "G_PER_L", "value": "0.25"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/919 | {<br>                "recipe_order": 2,<br>                "compound": "Biphenyl",<br>                "compound_id": 2105,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "10 g/l in ethanol",<br>                "amount": 0.25,<br>                "unit": "g/l",<br>                "g_l": 0.25,<br>                "mmol_l": 1.62117,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2105) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 457 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/919 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 457",<br>                "solution_id": 913,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
