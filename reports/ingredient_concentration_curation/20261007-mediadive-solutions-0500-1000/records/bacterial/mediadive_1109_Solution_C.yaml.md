# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_1109_Solution_C.yaml
- ID: CultureMech:010612
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `432f77f40593fa773803177461923f833db8f2189e6b146bc358a8e01fa2e409`
- Proposed/result SHA256: `0847f19f43f6ce54b8f49fd9be619a496a5a3aad3a70fecc8b871dce09f29f0b`
- Source: https://mediadive.dsmz.de/rest/solution/1109
- Source SHA256: 8b9f5f45c5ac9bbd0a1a77d23c4d95e521fa12f064f3cc70e8f6abfe7986aff2
- Retrieved: 2026-10-07T08:49:04.795473+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Trisodium citrate x 2 H2O | {"unit": "G_PER_L", "value": "150"} | {"unit": "G_PER_L", "value": "150"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1109 | {<br>                "recipe_order": 1,<br>                "compound": "Trisodium citrate x 2 H2O",<br>                "compound_id": 1249,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3,<br>                "unit": "g",<br>                "g_l": 150,<br>                "mmol_l": 510.031,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1249) | Provider explicitly reports g_l=150. Arithmetic check: 3 g * 1 g/g / (20 ml / 1000 ml per L) = 1.5E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 20. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.02"} | correct | https://mediadive.dsmz.de/rest/solution/1109 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 20 ml per prepared batch: 20 / 1000 = 0.02 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 20. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
