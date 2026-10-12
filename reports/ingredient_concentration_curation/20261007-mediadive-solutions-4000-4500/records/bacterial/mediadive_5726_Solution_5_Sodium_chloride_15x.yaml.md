# Solution Concentration Review: Solution 5 Sodium chloride (15x)

- Record: data/normalized_yaml/bacterial/mediadive_5726_Solution_5_Sodium_chloride_15x.yaml
- ID: CultureMech:014588
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `dda212645143afe5304a55d616a925b4417d8cbca82411658be05afa2cf823f4`
- Proposed/result SHA256: `b80469b1fa6fce84c645bb9246fd130e2f1d2004e5c95e1759464c869676b266`
- Source: https://mediadive.dsmz.de/rest/solution/5726
- Source SHA256: 89e917f0d99f04666ce7f4b6aa391ad6984f4f49eddabc8fa3579c29905e7bb5
- Retrieved: 2026-10-07T09:57:46.892716+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "300"} | {"unit": "G_PER_L", "value": "300"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5726 | {<br>                "recipe_order": 1,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 300,<br>                "unit": "g",<br>                "g_l": 300,<br>                "mmol_l": 5133.47,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=43) | Provider explicitly reports g_l=300. Arithmetic check: 300 g * 1 g/g / (1000 ml / 1000 ml per L) = 300 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5726 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
