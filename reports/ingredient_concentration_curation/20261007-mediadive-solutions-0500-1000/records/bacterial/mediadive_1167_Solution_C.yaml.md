# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_1167_Solution_C.yaml
- ID: CultureMech:010662
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `91335e918a363a88d7cc953296f7f472753caff49f915d8478a0abf50fe92639`
- Proposed/result SHA256: `5bfc3b6d8637bcb55c059dc6846d4257825694357cf2d7821eb58ee0c9541da8`
- Source: https://mediadive.dsmz.de/rest/solution/1167
- Source SHA256: f26bfb526d7f01f60ac4a067ed8935b3995c3649d9a5247391766d3616b4b619
- Retrieved: 2026-10-07T08:49:41.676834+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | D-Glucose | {"unit": "G_PER_L", "value": "200"} | {"unit": "G_PER_L", "value": "200"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1167 | {<br>                "recipe_order": 1,<br>                "compound": "D-Glucose",<br>                "compound_id": 211,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "g",<br>                "g_l": 200,<br>                "mmol_l": 1110.12,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=211) | Provider explicitly reports g_l=200. Arithmetic check: 20 g * 1 g/g / (100 ml / 1000 ml per L) = 2.0E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/1167 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
