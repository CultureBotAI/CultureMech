# Solution Concentration Review: Sulfide stock solution (autoclaved)

- Record: data/normalized_yaml/bacterial/mediadive_4296_Sulfide_stock_solution_autoclaved.yaml
- ID: CultureMech:013304
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6635e6453ebef7a57dffb1c72472c0e5ed02f491a5cb886638b3402c8d5bd631`
- Proposed/result SHA256: `ea16c984efd8fd85c6bded004451f57b7fd32edd02bb53087b99e83330c6041c`
- Source: https://mediadive.dsmz.de/rest/solution/4296
- Source SHA256: 72594a82fcbf1d42b6b78490ce4c63e18f75d0b9802af1be6e5c75b9348f29ae
- Retrieved: 2026-10-07T09:42:26.434613+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2S x 9 H2O | {"unit": "G_PER_L", "value": "40"} | {"unit": "G_PER_L", "value": "40"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4296 | {<br>                "recipe_order": 1,<br>                "compound": "Na2S x 9 H2O",<br>                "compound_id": 54,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.4,<br>                "unit": "g",<br>                "g_l": 40,<br>                "mmol_l": 166.54,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=54) | Provider explicitly reports g_l=40. Arithmetic check: 0.4 g * 1 g/g / (10 ml / 1000 ml per L) = 4E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/4296 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
