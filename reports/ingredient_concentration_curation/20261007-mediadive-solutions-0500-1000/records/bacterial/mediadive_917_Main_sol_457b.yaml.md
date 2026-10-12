# Solution Concentration Review: Main sol. 457b

- Record: data/normalized_yaml/bacterial/mediadive_917_Main_sol_457b.yaml
- ID: CultureMech:015270
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `34135c558f6243e2712f9ae043c0c9faaf27f46106794bdbe67f58de56bba5c3`
- Proposed/result SHA256: `34135c558f6243e2712f9ae043c0c9faaf27f46106794bdbe67f58de56bba5c3`
- Source: https://mediadive.dsmz.de/rest/solution/917
- Source SHA256: 66822880fb87582a1b70815dd7648ec161062f8f977d99d39d333b7551671b53
- Retrieved: 2026-10-07T08:47:46.729167+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Tween 80 | {"unit": "G_PER_L", "value": "0.2"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/917 | {<br>                "recipe_order": 2,<br>                "compound": "Tween 80",<br>                "compound_id": 22,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 200,<br>                "unit": "mg/l",<br>                "g_l": 0.2,<br>                "mmol_l": 0.152807,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=22) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 457 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/917 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 457",<br>                "solution_id": 913,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
