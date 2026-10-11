# Solution Concentration Review: Bicarbonate solution (C)

- Record: data/normalized_yaml/bacterial/mediadive_5592_Bicarbonate_solution_C.yaml
- ID: CultureMech:014469
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7f73126aff5cc355258cd53385edab6b05a5fc75974a1bbf9cb777f3bfc084c6`
- Proposed/result SHA256: `d5ec344474b8f8263b3b72fee6175ff0ef46db08af199964c0f3d5a0c24b4e41`
- Source: https://mediadive.dsmz.de/rest/solution/5592
- Source SHA256: fa40d1749bb10f7649f7ba0ff7965b812bac5e346fbe2e369d45c51fe72e6d21
- Retrieved: 2026-10-07T09:56:23.401165+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaHCO3 | {"unit": "G_PER_L", "value": "70"} | {"unit": "G_PER_L", "value": "70"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5592 | {<br>                "recipe_order": 1,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 14,<br>                "unit": "g",<br>                "g_l": 70,<br>                "mmol_l": 833.264,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=55) | Provider explicitly reports g_l=70. Arithmetic check: 14 g * 1 g/g / (200 ml / 1000 ml per L) = 7E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 200. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.2"} | correct | https://mediadive.dsmz.de/rest/solution/5592 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 200,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 200 ml per prepared batch: 200 / 1000 = 0.2 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 200. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
