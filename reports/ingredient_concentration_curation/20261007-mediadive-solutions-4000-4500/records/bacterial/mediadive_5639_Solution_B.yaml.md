# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_5639_Solution_B.yaml
- ID: CultureMech:014507
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1adf1ba091c943b147f1bd1f56f482cbdfc9342fa861a51ddb4d8b584a2a6607`
- Proposed/result SHA256: `af3a70959677b38401299e47154b33a72834e036b92a90010c73f85d48a23378`
- Source: https://mediadive.dsmz.de/rest/solution/5639
- Source SHA256: fea271a0f4f74aacda9922f1992096ee66943a1aab39bc9de3ee1b042997cc46
- Retrieved: 2026-10-07T09:56:49.216312+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2S2O3 x 5 H2O | {"unit": "G_PER_L", "value": "66.6667"} | {"unit": "G_PER_L", "value": "66.6667"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5639 | {<br>                "recipe_order": 1,<br>                "compound": "Na2S2O3 x 5 H2O",<br>                "compound_id": 65,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "g",<br>                "g_l": 66.6667,<br>                "mmol_l": 268.616,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=65) | Provider explicitly reports g_l=66.6667. Arithmetic check: 2 g * 1 g/g / (30 ml / 1000 ml per L) = 66.66666666666666666666666667 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 30. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0000000000001"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5639 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 30,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
