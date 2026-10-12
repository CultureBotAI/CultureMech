# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_1086_Solution_D.yaml
- ID: CultureMech:010598
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `50c6f225aee4ef1a0cb4b078f4c1277c008079cda38a8c6a06b7b39d50870399`
- Proposed/result SHA256: `5c29f9db3f65c4c2086763dcca0c27bd0f2860cae8ff534af099477abee0400b`
- Source: https://mediadive.dsmz.de/rest/solution/1086
- Source SHA256: d37b8a2fb1d5c65ec035ca5d69a8dc20f20507b994c6e216cfaec4338c5bbde5
- Retrieved: 2026-10-07T08:48:55.338841+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2SO3 | {"unit": "G_PER_L", "value": "60"} | {"unit": "G_PER_L", "value": "60"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1086 | {<br>                "recipe_order": 1,<br>                "compound": "Na2SO3",<br>                "compound_id": 109,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.6,<br>                "unit": "g",<br>                "g_l": 60,<br>                "mmol_l": 476.002,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=109) | Provider explicitly reports g_l=60. Arithmetic check: 0.6 g * 1 g/g / (10 ml / 1000 ml per L) = 6E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/1086 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
