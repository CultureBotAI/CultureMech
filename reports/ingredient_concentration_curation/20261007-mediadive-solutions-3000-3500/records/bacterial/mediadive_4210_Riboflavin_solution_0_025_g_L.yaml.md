# Solution Concentration Review: Riboflavin solution 0.025 g/L

- Record: data/normalized_yaml/bacterial/mediadive_4210_Riboflavin_solution_0_025_g_L.yaml
- ID: CultureMech:013236
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0771071234435c148ea765c033367aeb69beb5cc260dc07a79129ef098159746`
- Proposed/result SHA256: `152f62f84c6efd133bb8d5eb53bc11feb19eb421fd770ecc524df91008091a5d`
- Source: https://mediadive.dsmz.de/rest/solution/4210
- Source SHA256: 9a388ac41fa9c1bcb2dceda6ab653dfe4500ae6804ac8ed4f6ca782df1c12612
- Retrieved: 2026-10-07T09:41:36.202880+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Riboflavin | {"unit": "G_PER_L", "value": "0.025"} | {"unit": "G_PER_L", "value": "0.025"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4210 | {<br>                "recipe_order": 1,<br>                "compound": "Riboflavin",<br>                "compound_id": 136,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.5,<br>                "unit": "mg",<br>                "g_l": 0.025,<br>                "mmol_l": 0.0664187,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=136) | Provider explicitly reports g_l=0.025. Arithmetic check: 2.5 mg * 0.001 g/mg / (100 ml / 1000 ml per L) = 0.025 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/4210 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
