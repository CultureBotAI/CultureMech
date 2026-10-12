# Solution Concentration Review: Main sol. 1081a

- Record: data/normalized_yaml/bacterial/mediadive_2190_Main_sol_1081a.yaml
- ID: CultureMech:011581
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d8d977c11782d731d52c2ac2b6ffc01beba5dfcb20fb310e42c5be69dfd683ec`
- Proposed/result SHA256: `dbf314dfe6e4de27b406fa715066d5a9814df6bda3dd1649966e458892ade205`
- Source: https://mediadive.dsmz.de/rest/solution/2190
- Source SHA256: 1b6e88846a0de165327f3e9c242b68e9c72d7c89279c0ce3dcf91cddf00ce7aa
- Retrieved: 2026-10-07T09:09:56.535179+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "100"} | {"unit": "G_PER_L", "value": "100"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2190 | {<br>                "recipe_order": 2,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "g",<br>                "g_l": 100,<br>                "mmol_l": 1711.16,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=43) | Provider explicitly reports g_l=100. Arithmetic check: 100 g * 1 g/g / (1000 ml / 1000 ml per L) = 100 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 1081 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2190 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 1081",<br>                "solution_id": 2189,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
