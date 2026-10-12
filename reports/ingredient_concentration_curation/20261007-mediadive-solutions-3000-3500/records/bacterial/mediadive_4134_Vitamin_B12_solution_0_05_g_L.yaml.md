# Solution Concentration Review: Vitamin B12 solution 0.05 g/L

- Record: data/normalized_yaml/bacterial/mediadive_4134_Vitamin_B12_solution_0_05_g_L.yaml
- ID: CultureMech:013170
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7674e7c2d5e5a26ac3f17a0017e81e96f8be45b1f00c5415945c8d5b441e704d`
- Proposed/result SHA256: `346ecedd035e71615b7947ab80bd8efa81fc0bbd79cdf4929e794d6cdb2ded80`
- Source: https://mediadive.dsmz.de/rest/solution/4134
- Source SHA256: e085f15e1df6af68027db596d79ce1b513183beb500ef2a0609342db4d2469b8
- Retrieved: 2026-10-07T09:40:49.131655+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Vitamin B12 | {"unit": "G_PER_L", "value": "0.05"} | {"unit": "G_PER_L", "value": "0.05"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4134 | {<br>                "recipe_order": 1,<br>                "compound": "Vitamin B12",<br>                "compound_id": 18,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "mg",<br>                "g_l": 0.05,<br>                "mmol_l": 0.0368895,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=18) | Provider explicitly reports g_l=0.05. Arithmetic check: 5 mg * 0.001 g/mg / (100 ml / 1000 ml per L) = 0.05 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/4134 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
