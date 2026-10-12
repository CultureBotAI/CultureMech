# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_761_Solution_E.yaml
- ID: CultureMech:015146
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2aebc3064499cfb957db45c6e91b4c056e629c0fb060e742b80c805e865499a8`
- Proposed/result SHA256: `393515ea9be5d3538c58f2c0233c2be71ed1090aac654f95f7f1cbf65c9fd545`
- Source: https://mediadive.dsmz.de/rest/solution/761
- Source SHA256: 5c4dea2ab76497fd71f83bc0e8826b9eb3e242da52d78e7dd20559929875368f
- Retrieved: 2026-10-07T08:46:20.747211+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2S x 9 H2O | {"unit": "G_PER_L", "value": "30.7692"} | {"unit": "G_PER_L", "value": "30.7692"} | evidence_only | https://mediadive.dsmz.de/rest/solution/761 | {<br>                "recipe_order": 1,<br>                "compound": "Na2S x 9 H2O",<br>                "compound_id": 54,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.4,<br>                "unit": "g",<br>                "g_l": 30.7692,<br>                "mmol_l": 128.108,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=54) | Provider explicitly reports g_l=30.7692. Arithmetic check: 0.4 g * 1 g/g / (13 ml / 1000 ml per L) = 30.76923076923076923076923077 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 13. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.013"} | correct | https://mediadive.dsmz.de/rest/solution/761 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 13,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 13 ml per prepared batch: 13 / 1000 = 0.013 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 13. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
