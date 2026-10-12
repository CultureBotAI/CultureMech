# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_1705_Solution_C.yaml
- ID: CultureMech:011158
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2ed22e8452e32dec2b09063c9c691dcfedb9e9fd332ddb3fe9b7a231129f5143`
- Proposed/result SHA256: `3cb816896e61667134c59481fa372d0696e25a3097c84b9e09569d62d047a304`
- Source: https://mediadive.dsmz.de/rest/solution/1705
- Source SHA256: 7abb431788581d64f57a9f2311fa1c41bba1368ef6f0c1b5124893f617f25375
- Retrieved: 2026-10-07T08:55:41.472107+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2-fumarate | {"unit": "G_PER_L", "value": "128"} | {"unit": "G_PER_L", "value": "128"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1705 | {<br>                "recipe_order": 1,<br>                "compound": "Na2-fumarate",<br>                "compound_id": 276,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3.2,<br>                "unit": "g",<br>                "g_l": 128,<br>                "mmol_l": 799.82,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=276) | Provider explicitly reports g_l=128. Arithmetic check: 3.2 g * 1 g/g / (25 ml / 1000 ml per L) = 128 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 25. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.025"} | correct | https://mediadive.dsmz.de/rest/solution/1705 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 25,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 25 ml per prepared batch: 25 / 1000 = 0.025 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 25. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
