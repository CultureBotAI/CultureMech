# Solution Concentration Review: Solution 4

- Record: data/normalized_yaml/bacterial/mediadive_5181_Solution_4.yaml
- ID: CultureMech:014091
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `bbe6a3cb6080adf77c490f87cb1ce48494553c0dec7bdf32531c024c05d2e45a`
- Proposed/result SHA256: `9062e96a77d866b7589571b6fb5c9857d1e09c6e18822f49f3b96fc1289de39e`
- Source: https://mediadive.dsmz.de/rest/solution/5181
- Source SHA256: 9274f0575a9aa5d9a572fe1b60c6d54b91e85138afc30f5ecc20c08bbdb98845
- Retrieved: 2026-10-07T09:51:52.858250+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | 2-Oxoglutarate | {"unit": "G_PER_L", "value": "14.6"} | {"unit": "G_PER_L", "value": "14.6"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5181 | {<br>                "recipe_order": 1,<br>                "compound": "2-Oxoglutarate",<br>                "compound_id": 1992,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 14.6,<br>                "unit": "g",<br>                "g_l": 14.6,<br>                "mmol_l": 101.331,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1992) | Provider explicitly reports g_l=14.6. Arithmetic check: 14.6 g * 1 g/g / (1000 ml / 1000 ml per L) = 14.6 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5181 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
