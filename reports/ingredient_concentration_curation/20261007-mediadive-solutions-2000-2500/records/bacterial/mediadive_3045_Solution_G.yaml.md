# Solution Concentration Review: Solution G

- Record: data/normalized_yaml/bacterial/mediadive_3045_Solution_G.yaml
- ID: CultureMech:012272
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `86c386fc92a155974a54608b49d3ed8c3c258b8ab51d162f378ccaa788e15311`
- Proposed/result SHA256: `d51995e976856385de891fa76e9ec106c2eacbad7a5235edd504b0d9c17cd4b7`
- Source: https://mediadive.dsmz.de/rest/solution/3045
- Source SHA256: 164213fc15e44bf28c64fd6d979b33e192649366446534789dc8aa5688c741ec
- Retrieved: 2026-10-07T09:17:56.367598+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na-formate | {"unit": "G_PER_L", "value": "340"} | {"unit": "G_PER_L", "value": "340"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3045 | {<br>                "recipe_order": 1,<br>                "compound": "Na-formate",<br>                "compound_id": 144,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3.4,<br>                "unit": "g",<br>                "g_l": 340,<br>                "mmol_l": 4999.47,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=144) | Provider explicitly reports g_l=340. Arithmetic check: 3.4 g * 1 g/g / (10 ml / 1000 ml per L) = 3.4E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/3045 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
