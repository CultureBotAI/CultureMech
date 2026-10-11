# Solution Concentration Review: Galactose stock solution (filter-sterilized)

- Record: data/normalized_yaml/bacterial/mediadive_4297_Galactose_stock_solution_filter-sterilized.yaml
- ID: CultureMech:013305
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `462be76ea47a564ea837daf2fc0a8bf1fc369258a226c3c0c0b7232502b788bf`
- Proposed/result SHA256: `0d9d6d9bcf314dc15662e317bc8982896cf535e7496e72e899d785d0f42ec1bd`
- Source: https://mediadive.dsmz.de/rest/solution/4297
- Source SHA256: 8068f3dfd431aa9780ac14732d7ae7a8f921579a666c9ccd1a3fa3df7c78b2a0
- Retrieved: 2026-10-07T09:42:27.214042+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Galactose | {"unit": "G_PER_L", "value": "90.1"} | {"unit": "G_PER_L", "value": "90.1"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4297 | {<br>                "recipe_order": 1,<br>                "compound": "Galactose",<br>                "compound_id": 321,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.901,<br>                "unit": "g",<br>                "g_l": 90.1,<br>                "mmol_l": 500.111,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=321) | Provider explicitly reports g_l=90.1. Arithmetic check: 0.901 g * 1 g/g / (10 ml / 1000 ml per L) = 90.1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/4297 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
