# Solution Concentration Review: Vitamin K1 solution

- Record: data/normalized_yaml/bacterial/mediadive_125_Vitamin_K1_solution.yaml
- ID: CultureMech:010752
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a3c26a2fc67843af1a5b8bab920fb7d1f65d4666b48faac747946664e511e134`
- Proposed/result SHA256: `a3c26a2fc67843af1a5b8bab920fb7d1f65d4666b48faac747946664e511e134`
- Source: https://mediadive.dsmz.de/rest/solution/125
- Source SHA256: 605a4f24c7c95bb650c17abfb1878d5e3c1fd0944c60093f96678c402a93156d
- Retrieved: 2026-10-07T08:20:33.584794+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Vitamin K1 | {"unit": "PERCENT_V_V", "value": "5.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/125 | {<br>                "recipe_order": 1,<br>                "compound": "Vitamin K1",<br>                "compound_id": 150,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=150) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Ethanol | {"unit": "G_PER_L", "value": "950"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/125 | {<br>                "recipe_order": 2,<br>                "compound": "Ethanol",<br>                "compound_id": 201,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "95 %",<br>                "amount": 20,<br>                "unit": "ml",<br>                "g_l": 950,<br>                "mmol_l": 20620.8,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=201) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |

## Medium212 Source-Specific Follow-Up

The source-specific ingredient review is complete for this checkpoint: the guarded repair is applied locally. The [current follow-up](../../../20261009-synthrophomonas-family/applied-records/S125.md) contains every old/new claim, exact supporting snippet, source uncertainty and actual validation result. This earlier report remains historical context.
