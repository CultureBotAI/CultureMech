# Solution Concentration Review: Cerium(III)chloride: (0.03M)

- Record: data/normalized_yaml/bacterial/mediadive_5739_Cerium_III_chloride_0_03M.yaml
- ID: CultureMech:014593
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `61472a06bb95942e5eb902a356fca4caf28f245cf49b6eb7b21e0705fe80254b`
- Proposed/result SHA256: `ea7730fa60c4d4a592d4fabdedf6e43a1b54455d173f57cc221bb8fbe6c82575`
- Source: https://mediadive.dsmz.de/rest/solution/5739
- Source SHA256: 3b6426548d25d4cd1ad64524a48305c97cf96d5d19adfd7202fa7d585d6f5912
- Retrieved: 2026-10-07T09:57:50.824354+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | CeCl3 x 7 H2O | {"unit": "G_PER_L", "value": "11.2"} | {"unit": "G_PER_L", "value": "11.2"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5739 | {<br>                "recipe_order": 1,<br>                "compound": "CeCl3 x 7 H2O",<br>                "compound_id": 1444,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 11.2,<br>                "unit": "g",<br>                "g_l": 11.2,<br>                "mmol_l": 45.4409,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1444) | Provider explicitly reports g_l=11.2. Arithmetic check: 11.2 g * 1 g/g / (1000 ml / 1000 ml per L) = 11.2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5739 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
