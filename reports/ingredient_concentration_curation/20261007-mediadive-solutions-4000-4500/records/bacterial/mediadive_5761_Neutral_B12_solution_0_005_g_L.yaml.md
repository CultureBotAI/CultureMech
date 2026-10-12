# Solution Concentration Review: Neutral B12 solution 0.005 g/L

- Record: data/normalized_yaml/bacterial/mediadive_5761_Neutral_B12_solution_0_005_g_L.yaml
- ID: CultureMech:014617
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f0d6c75cf197fc92cafaad197d814f1f481aaa9a2bcca9113a75c52b9b6c9cd7`
- Proposed/result SHA256: `7303c278269c6d78cc98283acdb4bec24efe80190d81430a0a3c2701eeab126f`
- Source: https://mediadive.dsmz.de/rest/solution/5761
- Source SHA256: 95ddd7e889c07690057502f303d45885bc4188c6e42a400ad12628b0e96617e7
- Retrieved: 2026-10-07T09:58:07.255221+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | B12 | {"unit": "G_PER_L", "value": "0.005"} | {"unit": "G_PER_L", "value": "0.005"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5761 | {<br>                "recipe_order": 1,<br>                "compound": "B12",<br>                "compound_id": 1238,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.5,<br>                "unit": "mg",<br>                "g_l": 0.005,<br>                "mmol_l": 0.00368895,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1238) | Provider explicitly reports g_l=0.005. Arithmetic check: 0.5 mg * 0.001 g/mg / (100 ml / 1000 ml per L) = 0.005 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/5761 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
