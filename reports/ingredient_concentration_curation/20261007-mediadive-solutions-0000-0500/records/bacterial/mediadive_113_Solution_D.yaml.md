# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_113_Solution_D.yaml
- ID: CultureMech:010637
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `46546d6cdef2869be7157c36e7d065b38bcee6d1321d4083be912f794e8f4ba1`
- Proposed/result SHA256: `8ffe7d11af1d7eab7d6ab2a8b7ecafabedacc7571794965d42a7b2398d3c58e0`
- Source: https://mediadive.dsmz.de/rest/solution/113
- Source SHA256: 221ad36f2d1f1a5fa5470eaecae404a3d84055b4c2b8440eed113c2e72df4300
- Retrieved: 2026-10-07T08:20:25.715414+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2S2O3 x 5 H2O | {"unit": "G_PER_L", "value": "100"} | {"unit": "G_PER_L", "value": "100"} | evidence_only | https://mediadive.dsmz.de/rest/solution/113 | {<br>                "recipe_order": 1,<br>                "compound": "Na2S2O3 x 5 H2O",<br>                "compound_id": 65,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 100,<br>                "mmol_l": 402.924,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=65) | Provider explicitly reports g_l=100. Arithmetic check: 5 g * 1 g/g / (50 ml / 1000 ml per L) = 1E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.05"} | correct | https://mediadive.dsmz.de/rest/solution/113 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 50 ml per prepared batch: 50 / 1000 = 0.05 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
