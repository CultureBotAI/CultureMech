# Solution Concentration Review: Solution H

- Record: data/normalized_yaml/bacterial/mediadive_670_Solution_H.yaml
- ID: CultureMech:015079
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `97af1ed5b9594a3e1a53b3f52fe0b63f3158d990f985997492989454d375c059`
- Proposed/result SHA256: `c45e88137c4fbb7b34b9a45a8a2dea098c509dfd225920ce94597034b00ff6f1`
- Source: https://mediadive.dsmz.de/rest/solution/670
- Source SHA256: 407e2e58f2e4547e3868638e48c10e6c643b986402a4ae548a755f082a751239
- Retrieved: 2026-10-07T08:25:47.259326+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2S x 9 H2O | {"unit": "G_PER_L", "value": "25"} | {"unit": "G_PER_L", "value": "25"} | evidence_only | https://mediadive.dsmz.de/rest/solution/670 | {<br>                "recipe_order": 1,<br>                "compound": "Na2S x 9 H2O",<br>                "compound_id": 54,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "mg",<br>                "g_l": 25,<br>                "mmol_l": 104.088,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=54) | Provider explicitly reports g_l=25. Arithmetic check: 50 mg * 0.001 g/mg / (2 ml / 1000 ml per L) = 25 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 2. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "850.0"} | {"unit": "L", "value": "0.0017"} | correct | https://mediadive.dsmz.de/rest/solution/670 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.7,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1.7 ml per prepared batch: 1.7 / 1000 = 0.0017 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 2. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
