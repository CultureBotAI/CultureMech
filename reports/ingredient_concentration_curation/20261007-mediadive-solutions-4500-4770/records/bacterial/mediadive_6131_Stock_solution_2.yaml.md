# Solution Concentration Review: Stock solution 2

- Record: data/normalized_yaml/bacterial/mediadive_6131_Stock_solution_2.yaml
- ID: CultureMech:014836
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `bc671114dfbb66c54aaf67e465c703baf7643db92b33de82774e6fe794ccc07d`
- Proposed/result SHA256: `4735a4c530707f0b10881aca462f303e726ebcb766082daf5c6579f346d1ceed`
- Source: https://mediadive.dsmz.de/rest/solution/6131
- Source SHA256: 61bafb6be30d64df1df1b673e450c4f247560c0c5721201a0bf0d5e09a769fe2
- Retrieved: 2026-10-07T10:00:27.529150+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "4.98"} | {"unit": "G_PER_L", "value": "4.98"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6131 | {<br>                "recipe_order": 2,<br>                "compound": "FeSO4 x 7 H2O",<br>                "compound_id": 12,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 4.98,<br>                "unit": "g",<br>                "g_l": 4.98,<br>                "mmol_l": 17.9127,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=12) | Provider explicitly reports g_l=4.98. Arithmetic check: 4.98 g * 1 g/g / (1000 ml / 1000 ml per L) = 4.98 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | H2SO4 | {"unit": "PERCENT_V_V", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6131 | {<br>                "recipe_order": 3,<br>                "compound": "H2SO4",<br>                "compound_id": 122,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "concentrated",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=122) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
