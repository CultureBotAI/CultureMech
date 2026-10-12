# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_2549_Solution_D.yaml
- ID: CultureMech:011891
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3fc29d8233110a3e3d7e9e84b63e3b527223dfe9f0f3d0567719b12031ccf098`
- Proposed/result SHA256: `026516b8843a4b853399073a8208fe05a0f2d99ea2da485911042a08ffa71884`
- Source: https://mediadive.dsmz.de/rest/solution/2549
- Source SHA256: 41e4294185ec05bd1606c3061dd53d5c20cc815442d8d2e24c0d46ad993ae788
- Retrieved: 2026-10-07T09:13:31.397710+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaNO3 | {"unit": "G_PER_L", "value": "34"} | {"unit": "G_PER_L", "value": "34"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2549 | {<br>                "recipe_order": 1,<br>                "compound": "NaNO3",<br>                "compound_id": 187,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3.4,<br>                "unit": "g",<br>                "g_l": 34,<br>                "mmol_l": 400.024,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=187) | Provider explicitly reports g_l=34. Arithmetic check: 3.4 g * 1 g/g / (100 ml / 1000 ml per L) = 34 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/2549 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
