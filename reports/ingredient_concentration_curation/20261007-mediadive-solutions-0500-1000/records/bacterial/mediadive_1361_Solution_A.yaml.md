# Solution Concentration Review: Solution A

- Record: data/normalized_yaml/bacterial/mediadive_1361_Solution_A.yaml
- ID: CultureMech:010844
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d1f3a96db56d2cf55b961ea5b85fb5366d2502dab8a97ca73174246585aa4117`
- Proposed/result SHA256: `77057361695b78d4217f7d6bc6bb173563ec738d6da6b8acd085373cdaaa4569`
- Source: https://mediadive.dsmz.de/rest/solution/1361
- Source SHA256: 0e4e1bb6f4a190eeab97dfa803c64d2b804095fc5509590210d4568250b28938
- Retrieved: 2026-10-07T08:51:54.562061+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Benzothiazole | {"unit": "G_PER_L", "value": "0.333333"} | {"unit": "G_PER_L", "value": "0.333333"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1361 | {<br>                "recipe_order": 1,<br>                "compound": "Benzothiazole",<br>                "compound_id": 2128,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 30,<br>                "unit": "mg",<br>                "g_l": 0.333333,<br>                "mmol_l": 2.46567,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2128) | Provider explicitly reports g_l=0.333333. Arithmetic check: 30 mg * 0.001 g/mg / (90 ml / 1000 ml per L) = 0.3333333333333333333333333333 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 90. | applied |
| `composition[1].concentration` | NaOH | {"unit": "G_PER_L", "value": "9"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1361 | {<br>                "recipe_order": 2,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "10 %",<br>                "amount": 90,<br>                "unit": "ml",<br>                "g_l": 9,<br>                "mmol_l": 225.017,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=256) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
