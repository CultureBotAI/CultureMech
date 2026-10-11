# Solution Concentration Review: Main sol. 547

- Record: data/normalized_yaml/bacterial/mediadive_1206_Main_sol_547.yaml
- ID: CultureMech:010701
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `41768eb2792d1a6501b571bcc40e71100773b751454fec6188c362c099ebb22c`
- Proposed/result SHA256: `a84267823b82fb6040afae3e571ffcc12f611c06e5e93e2d0eedc02a732af63d`
- Source: https://mediadive.dsmz.de/rest/solution/1206
- Source SHA256: 651a3594fd12a990a05eb860c27a166688f144ff41704aa51bf5d0a484a45bd0
- Retrieved: 2026-10-07T08:50:09.269911+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Agar | {"unit": "G_PER_L", "value": "19.98"} | {"unit": "G_PER_L", "value": "19.98"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1206 | {<br>                "recipe_order": 3,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "g",<br>                "g_l": 19.98,<br>                "mmol_l": 59.406,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=3) | Provider explicitly reports g_l=19.98. Arithmetic check: 20 g * 1 g/g / (1001 ml / 1000 ml per L) = 19.98001998001998001998001998 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1001. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Solution I | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1206 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Solution I",<br>                "solution_id": 1207,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 500,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[1]` | Solution II | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1206 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Solution II",<br>                "solution_id": 1208,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 501,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
