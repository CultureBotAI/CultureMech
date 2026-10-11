# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_1172_Solution_B.yaml
- ID: CultureMech:010668
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `481236f5f27d4965169cc930afacbab17d3e750809565fdcd611bca0729c99cf`
- Proposed/result SHA256: `9bb2609b07a6aa5c3f0a19a6c47ba61d389962b558b544815bda660465cf64b8`
- Source: https://mediadive.dsmz.de/rest/solution/1172
- Source SHA256: 2660bfb17adeda648b7111186977f0c287e82cae35043031e3f28bf2bf148d98
- Retrieved: 2026-10-07T08:49:45.585116+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Naphthalene sulfonic acid | {"unit": "G_PER_L", "value": "2.3"} | {"unit": "G_PER_L", "value": "2.3"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1172 | {<br>                "recipe_order": 1,<br>                "compound": "Naphthalene sulfonic acid",<br>                "compound_id": 542,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.3,<br>                "unit": "g",<br>                "g_l": 2.3,<br>                "mmol_l": 11.0455,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=542) | Provider explicitly reports g_l=2.3. Arithmetic check: 2.3 g * 1 g/g / (1000 ml / 1000 ml per L) = 2.3 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1172 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
