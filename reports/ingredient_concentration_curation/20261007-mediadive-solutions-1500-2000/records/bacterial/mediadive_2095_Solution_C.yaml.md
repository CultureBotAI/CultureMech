# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_2095_Solution_C.yaml
- ID: CultureMech:011494
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d3e6a428a91d805364a6d19a46639c6b1ba26e79e5675d1ea97e3d0a257e2e4b`
- Proposed/result SHA256: `4102838823bbf4efa86c3b85b61d7b8c92d84f886c81a2bf7a1561c61d622045`
- Source: https://mediadive.dsmz.de/rest/solution/2095
- Source SHA256: 8f8a06ae6d976d46eef9f12ef17f5faa90f855475f49546f57d0c7ae8db8e0ce
- Retrieved: 2026-10-07T09:08:55.110486+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeCl3 x 6 H2O | {"unit": "G_PER_L", "value": "6.66"} | {"unit": "G_PER_L", "value": "6.66"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2095 | {<br>                "recipe_order": 1,<br>                "compound": "FeCl3 x 6 H2O",<br>                "compound_id": 82,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 666,<br>                "unit": "mg",<br>                "g_l": 6.66,<br>                "mmol_l": 24.6397,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=82) | Provider explicitly reports g_l=6.66. Arithmetic check: 666 mg * 0.001 g/mg / (100 ml / 1000 ml per L) = 6.66 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/2095 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
