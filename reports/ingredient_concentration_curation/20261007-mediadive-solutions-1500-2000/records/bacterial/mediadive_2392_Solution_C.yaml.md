# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_2392_Solution_C.yaml
- ID: CultureMech:011771
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `af2db7d3f815a70d11e85c33b8ecb3311737a23430337a2ea543387664ab0fd5`
- Proposed/result SHA256: `de2bb610045fef1b0aeeed4bc6e4aa0b9d1b9d5c28f76652c1c9d4a3bfa1f85f`
- Source: https://mediadive.dsmz.de/rest/solution/2392
- Source SHA256: 86c0ce6b3e55e55d3f902eda06d6f274d040b4de0e91f379c222cf95c8cdfd59
- Retrieved: 2026-10-07T09:12:09.191783+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | DL-Dithiothreitol | {"unit": "G_PER_L", "value": "7.7"} | {"unit": "G_PER_L", "value": "7.7"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2392 | {<br>                "recipe_order": 1,<br>                "compound": "DL-Dithiothreitol",<br>                "compound_id": 151,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 385,<br>                "unit": "mg",<br>                "g_l": 7.7,<br>                "mmol_l": 49.9028,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=151) | Provider explicitly reports g_l=7.7. Arithmetic check: 385 mg * 0.001 g/mg / (50 ml / 1000 ml per L) = 7.7 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.05"} | correct | https://mediadive.dsmz.de/rest/solution/2392 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 50 ml per prepared batch: 50 / 1000 = 0.05 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
