# Solution Concentration Review: Stock Solution C (10 ml)

- Record: data/normalized_yaml/bacterial/mediadive_5742_Stock_Solution_C_10_ml.yaml
- ID: CultureMech:014597
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0e2b12e9e1f6123599098ce378643f532ee95bd5ff2429051ebd7a1841f982f6`
- Proposed/result SHA256: `f8a312bc9daee36a268e76edeb18c596f5ba8a5a3197ede37664fea3cf5c5c10`
- Source: https://mediadive.dsmz.de/rest/solution/5742
- Source SHA256: 91d91f96d2e9ebaff106f0d303ec2931d6cdb97b511e3646f9cca6e381b461d2
- Retrieved: 2026-10-07T09:57:53.163965+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2SeO3 | {"unit": "G_PER_L", "value": "2"} | {"unit": "G_PER_L", "value": "2"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5742 | {<br>                "recipe_order": 1,<br>                "compound": "Na2SeO3",<br>                "compound_id": 699,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.02,<br>                "unit": "g",<br>                "g_l": 2,<br>                "mmol_l": 11.5648,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=699) | Provider explicitly reports g_l=2. Arithmetic check: 0.02 g * 1 g/g / (10 ml / 1000 ml per L) = 2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
