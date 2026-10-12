# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_1408_Solution_D.yaml
- ID: CultureMech:010891
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `aa1cb567f1077de21272b8b6e7f7ae567c56f8d2a61262269f0b44c2511f91e7`
- Proposed/result SHA256: `56d54547af5b3f9f838ea2b36dbf7a400fccc77968d2503de9ad4ca96b6d0778`
- Source: https://mediadive.dsmz.de/rest/solution/1408
- Source SHA256: 1b621b194a652659483ea2e0d6f850e7f417af545ab1b528468e1ed4377a7e31
- Retrieved: 2026-10-07T08:52:29.557711+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2S x 9 H2O | {"unit": "G_PER_L", "value": "40"} | {"unit": "G_PER_L", "value": "40"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1408 | {<br>                "recipe_order": 1,<br>                "compound": "Na2S x 9 H2O",<br>                "compound_id": 54,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.2,<br>                "unit": "g",<br>                "g_l": 40,<br>                "mmol_l": 166.54,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=54) | Provider explicitly reports g_l=40. Arithmetic check: 0.2 g * 1 g/g / (5 ml / 1000 ml per L) = 4E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 5. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.005"} | correct | https://mediadive.dsmz.de/rest/solution/1408 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 5 ml per prepared batch: 5 / 1000 = 0.005 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 5. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
