# Solution Concentration Review: Solution F

- Record: data/normalized_yaml/bacterial/mediadive_1708_Solution_F.yaml
- ID: CultureMech:011160
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c88fbaca15b3768d433bb6205e98246144239f125ecdd214d50cd6f89f6a08e2`
- Proposed/result SHA256: `c148a11a9d88ff445f88020feba9b7f281c849868df704e5ced4ce080327bea8`
- Source: https://mediadive.dsmz.de/rest/solution/1708
- Source SHA256: a1bb06ef0e839fdefa0f90b4bbf509955c60fee0ec01a178c9db336c80b2c0ec
- Retrieved: 2026-10-07T08:55:43.041622+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2S x 9 H2O | {"unit": "G_PER_L", "value": "25"} | {"unit": "G_PER_L", "value": "25"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1708 | {<br>                "recipe_order": 1,<br>                "compound": "Na2S x 9 H2O",<br>                "compound_id": 54,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.25,<br>                "unit": "g",<br>                "g_l": 25,<br>                "mmol_l": 104.088,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=54) | Provider explicitly reports g_l=25. Arithmetic check: 0.25 g * 1 g/g / (10 ml / 1000 ml per L) = 25 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/1708 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
