# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_647_Solution_D.yaml
- ID: CultureMech:015049
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `63c4283fa5df377aac8ad0215dee315429b70fc5509de79d924e841da1457aeb`
- Proposed/result SHA256: `2e09301fd92fdc160568128d3cfecc5b03ddce7ec92ea2e535109e5758d04759`
- Source: https://mediadive.dsmz.de/rest/solution/647
- Source SHA256: 89abc5388218db1acd3c3a53c13d0b770d2ce6ee7afab53d23bc5d6377c6767f
- Retrieved: 2026-10-07T08:25:33.886530+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Lactose | {"unit": "G_PER_L", "value": "200"} | {"unit": "G_PER_L", "value": "200"} | evidence_only | https://mediadive.dsmz.de/rest/solution/647 | {<br>                "recipe_order": 1,<br>                "compound": "Lactose",<br>                "compound_id": 394,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 200,<br>                "mmol_l": 584.283,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=394) | Provider explicitly reports g_l=200. Arithmetic check: 5 g * 1 g/g / (25 ml / 1000 ml per L) = 2E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 25. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.025"} | correct | https://mediadive.dsmz.de/rest/solution/647 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 25,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 25 ml per prepared batch: 25 / 1000 = 0.025 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 25. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
