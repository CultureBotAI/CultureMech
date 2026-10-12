# Solution Concentration Review: MnCl2 solution 0.36 g/L

- Record: data/normalized_yaml/bacterial/mediadive_2022_MnCl2_solution_0_36_g_L.yaml
- ID: CultureMech:011425
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `aa1c6751a524591ede62be04792139f876f587da90e4904973a4a9e60e328978`
- Proposed/result SHA256: `a99f53daf295f346bb63ff038aaa28e22ba6e1db2159ace9e58489efaaf74d7b`
- Source: https://mediadive.dsmz.de/rest/solution/2022
- Source SHA256: c347fecfc991855a5204facad5f5377733dc08707473238d479e8e4021b4afcd
- Retrieved: 2026-10-07T09:08:03.444016+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | MnCl2 x 4 H2O | {"unit": "G_PER_L", "value": "0.36"} | {"unit": "G_PER_L", "value": "0.36"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2022 | {<br>                "recipe_order": 1,<br>                "compound": "MnCl2 x 4 H2O",<br>                "compound_id": 36,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.36,<br>                "unit": "g",<br>                "g_l": 0.36,<br>                "mmol_l": 1.81905,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=36) | Provider explicitly reports g_l=0.36. Arithmetic check: 0.36 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.36 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/2022 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
