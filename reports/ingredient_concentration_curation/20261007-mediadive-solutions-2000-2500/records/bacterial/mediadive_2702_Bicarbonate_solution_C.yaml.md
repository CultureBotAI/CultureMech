# Solution Concentration Review: Bicarbonate solution (C)

- Record: data/normalized_yaml/bacterial/mediadive_2702_Bicarbonate_solution_C.yaml
- ID: CultureMech:012019
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a1e65c788dfca024b4a9fb764e41b1707fb8c42f7bafdea82da6ca84d3c8901d`
- Proposed/result SHA256: `b7c20dbf7d9bf7eabf1a536286ef59075cbe2efef8548e7d11ba03e9a8273904`
- Source: https://mediadive.dsmz.de/rest/solution/2702
- Source SHA256: c6294c46ee7f18baf96191f6219f1e0bc433b99dcc345db51a7e3fcf26544119
- Retrieved: 2026-10-07T09:15:01.057732+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaHCO3 | {"unit": "G_PER_L", "value": "83.3333"} | {"unit": "G_PER_L", "value": "83.3333"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2702 | {<br>                "recipe_order": 1,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.5,<br>                "unit": "g",<br>                "g_l": 83.3333,<br>                "mmol_l": 991.981,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=55) | Provider explicitly reports g_l=83.3333. Arithmetic check: 2.5 g * 1 g/g / (30 ml / 1000 ml per L) = 83.33333333333333333333333333 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 30. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0000000000001"} | {"unit": "L", "value": "0.03"} | correct | https://mediadive.dsmz.de/rest/solution/2702 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 30,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 30 ml per prepared batch: 30 / 1000 = 0.03 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 30. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
