# Solution Concentration Review: Solution 7 (100 mM KNO3)

- Record: data/normalized_yaml/bacterial/mediadive_5753_Solution_7_100_mM_KNO3.yaml
- ID: CultureMech:014609
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9cbb2e89a63b009ec21fc82a98589b4dac31e3e1588ea2b7df630427863e8a13`
- Proposed/result SHA256: `5218202d1137083b2a5ca2d70cc6e766e8d6a337485b49b408993d9c29e5ff9d`
- Source: https://mediadive.dsmz.de/rest/solution/5753
- Source SHA256: 9b10af561a1584cf8d76a4df9b1eb06654a3c9fc56435933e16ee9fe5254ffdf
- Retrieved: 2026-10-07T09:58:01.773788+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | KNO3 | {"unit": "G_PER_L", "value": "10.1"} | {"unit": "G_PER_L", "value": "10.1"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5753 | {<br>                "recipe_order": 1,<br>                "compound": "KNO3",<br>                "compound_id": 191,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10.1,<br>                "unit": "g",<br>                "g_l": 10.1,<br>                "mmol_l": 99.8981,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=191) | Provider explicitly reports g_l=10.1. Arithmetic check: 10.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 10.1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5753 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
