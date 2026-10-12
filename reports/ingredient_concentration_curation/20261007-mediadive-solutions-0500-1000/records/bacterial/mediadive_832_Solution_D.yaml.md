# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_832_Solution_D.yaml
- ID: CultureMech:015198
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `cf33b5c36bbcb8ddd837d8b21a8173aa9bae5e55f3a97a45cd169a4153118779`
- Proposed/result SHA256: `51c7d0e054745748d729ef68792adcaec908533046a25682442a87af2d8c6b00`
- Source: https://mediadive.dsmz.de/rest/solution/832
- Source SHA256: 936d74d6581810024d89c1ae71cca45725d0c4683fb428e605487fb1ee80bb31
- Retrieved: 2026-10-07T08:46:56.139587+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na-stearate | {"unit": "G_PER_L", "value": "30.5"} | {"unit": "G_PER_L", "value": "30.5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/832 | {<br>                "recipe_order": 1,<br>                "compound": "Na-stearate",<br>                "compound_id": 298,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.61,<br>                "unit": "g",<br>                "g_l": 30.5,<br>                "mmol_l": 99.5236,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=298) | Provider explicitly reports g_l=30.5. Arithmetic check: 0.61 g * 1 g/g / (20 ml / 1000 ml per L) = 30.5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 20. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/832 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
