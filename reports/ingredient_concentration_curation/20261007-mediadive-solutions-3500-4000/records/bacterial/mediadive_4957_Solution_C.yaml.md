# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_4957_Solution_C.yaml
- ID: CultureMech:013880
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5e0acaa8d95a55c99bea3eb69fe13be9574ed621d051cfc5b58b43d3f7c72dcf`
- Proposed/result SHA256: `e5797d24520c9d24d5a49fe8ab9a4e40d0b543aaaedb840962763b55143422ee`
- Source: https://mediadive.dsmz.de/rest/solution/4957
- Source SHA256: 05174d914afcff88dca582ef22b4bfdc23bbdc03445d717234c24986262f80c8
- Retrieved: 2026-10-07T09:49:20.556171+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2S2O4 x 2 H2O | {"unit": "G_PER_L", "value": "125"} | {"unit": "G_PER_L", "value": "125"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4957 | {<br>                "recipe_order": 1,<br>                "compound": "Na2S2O4 x 2 H2O",<br>                "compound_id": 1946,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 125,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1946) | Provider explicitly reports g_l=125. Arithmetic check: 5 g * 1 g/g / (40 ml / 1000 ml per L) = 125 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 40. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.04"} | correct | https://mediadive.dsmz.de/rest/solution/4957 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 40,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 40 ml per prepared batch: 40 / 1000 = 0.04 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 40. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
