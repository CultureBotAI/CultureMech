# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_456_Solution_D.yaml
- ID: CultureMech:013537
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `14da886f4b9544753f9162bd983861c3ac5eb4a282430674c65696f3f2b8c9e3`
- Proposed/result SHA256: `99c828de9bf60a8ef8a1f04846bd9b50a7e4f1a165ffe335c604b0a925156afc`
- Source: https://mediadive.dsmz.de/rest/solution/456
- Source SHA256: 35cc340439e8d3524567476882b7fb0594cb9e188ed45472508c819b5e80e4d7
- Retrieved: 2026-10-07T08:23:39.584513+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | D-Glucose | {"unit": "G_PER_L", "value": "200"} | {"unit": "G_PER_L", "value": "200"} | evidence_only | https://mediadive.dsmz.de/rest/solution/456 | {<br>                "recipe_order": 1,<br>                "compound": "D-Glucose",<br>                "compound_id": 211,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.8,<br>                "unit": "g",<br>                "g_l": 200,<br>                "mmol_l": 1110.12,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=211) | Provider explicitly reports g_l=200. Arithmetic check: 0.8 g * 1 g/g / (4 ml / 1000 ml per L) = 2E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 4. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.004"} | correct | https://mediadive.dsmz.de/rest/solution/456 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 4,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 4 ml per prepared batch: 4 / 1000 = 0.004 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 4. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |

## Medium212 Source-Specific Follow-Up

The source-specific ingredient review is complete for this checkpoint: the guarded repair is applied locally. The [current follow-up](../../../20261009-synthrophomonas-family/applied-records/S456.md) contains every old/new claim, exact supporting snippet, source uncertainty and actual validation result. This earlier report remains historical context.
