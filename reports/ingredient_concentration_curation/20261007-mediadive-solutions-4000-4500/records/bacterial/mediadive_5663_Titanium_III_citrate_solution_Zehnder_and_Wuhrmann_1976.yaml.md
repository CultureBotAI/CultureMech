# Solution Concentration Review: Titanium (III) citrate solution (Zehnder and Wuhrmann 1976)

- Record: data/normalized_yaml/bacterial/mediadive_5663_Titanium_III_citrate_solution_Zehnder_and_Wuhrmann_1976.yaml
- ID: CultureMech:014529
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `762e364ce5081fb3072c2557dff1b21e3b182b7615afb8c14943ab9c81e2fa14`
- Proposed/result SHA256: `762e364ce5081fb3072c2557dff1b21e3b182b7615afb8c14943ab9c81e2fa14`
- Source: https://mediadive.dsmz.de/rest/solution/5663
- Source SHA256: a9058c9940056c7faec1e130fa4080c12013216a5e4e4749f1ed6c8f8892020c
- Retrieved: 2026-10-07T09:57:04.807220+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Titanium(III) chloride | {"unit": "G_PER_L", "value": "0.75"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5663 | {<br>                "recipe_order": 1,<br>                "compound": "Titanium(III) chloride",<br>                "compound_id": 805,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "",<br>                "attribute": "Merck 808307, 15% solution",<br>                "amount": 5,<br>                "unit": "ml",<br>                "g_l": 0.75,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=805) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Sodium citrate | {"unit": "G_PER_L", "value": "2.5807"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5663 | {<br>                "recipe_order": 2,<br>                "compound": "Sodium citrate",<br>                "compound_id": 792,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "",<br>                "attribute": "0.2M",<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": 2.5807,<br>                "mmol_l": 10,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=792) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
