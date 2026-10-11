# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_420_Solution_E.yaml
- ID: CultureMech:013235
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1a316aec685f89440ea33418b29de4a97528a3c1419240ddb56f9c7c67d3d74d`
- Proposed/result SHA256: `2e96a4f52d5eedc335c2c54ac2a8f46191e2615226fa5defa1dd5a9e547b4d12`
- Source: https://mediadive.dsmz.de/rest/solution/420
- Source SHA256: 7d7c5f1dba005a5eb458cee53a8f37a1edf12529a3b26175b3b578781207e982
- Retrieved: 2026-10-07T08:23:17.163473+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Disodium succinate | {"unit": "G_PER_L", "value": "100"} | {"unit": "G_PER_L", "value": "100"} | evidence_only | https://mediadive.dsmz.de/rest/solution/420 | {<br>                "recipe_order": 1,<br>                "compound": "Disodium succinate",<br>                "compound_id": 1189,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.1,<br>                "unit": "g",<br>                "g_l": 100,<br>                "mmol_l": 617.094,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1189) | Provider explicitly reports g_l=100. Arithmetic check: 0.1 g * 1 g/g / (1 ml / 1000 ml per L) = 1E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.001"} | correct | https://mediadive.dsmz.de/rest/solution/420 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1 ml per prepared batch: 1 / 1000 = 0.001 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
