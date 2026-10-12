# Solution Concentration Review: Main sol. J1015

- Record: data/normalized_yaml/bacterial/mediadive_5060_Main_sol_J1015.yaml
- ID: CultureMech:013977
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a68fb46df22db7d9f3a8d9971274089fae6278bc6e8cbbf6ebb9c8ab32cac244`
- Proposed/result SHA256: `e94272a58415faa545819bbd1d51587a86104dd58d03592d75cac7cc8ff09ac0`
- Source: https://mediadive.dsmz.de/rest/solution/5060
- Source SHA256: 3e73a7f2b2ce292c692bf11ee7655a8aaa2e965c38fee20571a4b991c4606e8a
- Retrieved: 2026-10-07T09:50:30.616615+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Marine agar 2216 | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5060 | {<br>                "recipe_order": 1,<br>                "compound": "Marine agar 2216",<br>                "compound_id": 1628,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "see Medium No. 118",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1628) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | NaCl | {"unit": "G_PER_L", "value": "80"} | {"unit": "G_PER_L", "value": "80"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5060 | {<br>                "recipe_order": 2,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 80,<br>                "unit": "g",<br>                "g_l": 80,<br>                "mmol_l": 1368.93,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=43) | Provider explicitly reports g_l=80. Arithmetic check: 80 g * 1 g/g / (1000 ml / 1000 ml per L) = 80 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
