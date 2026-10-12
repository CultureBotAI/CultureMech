# Solution Concentration Review: KH2PO4 solution (2.93 nM)

- Record: data/normalized_yaml/bacterial/mediadive_6372_KH2PO4_solution_2_93_nM.yaml
- ID: CultureMech:015003
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `bba62b52c25c52ab955d1e1990054b1b4db55fded086fd97b8f390abdbcbc2b6`
- Proposed/result SHA256: `45dc9efc3fa72233a65467f77feab02c6aa522d1d1d21f7e1272cc1a79fcd33a`
- Source: https://mediadive.dsmz.de/rest/solution/6372
- Source SHA256: e2c9a1e1553ae91aaf2a179ce783f83c5d7fec8eb7956273f690a67215af9e4c
- Retrieved: 2026-10-07T10:02:24.107208+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "0.4"} | {"unit": "G_PER_L", "value": "0.4"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6372 | {<br>                "recipe_order": 2,<br>                "compound": "KH2PO4",<br>                "compound_id": 11,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.4,<br>                "unit": "g",<br>                "g_l": 0.4,<br>                "mmol_l": 2.93934,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=11) | Provider explicitly reports g_l=0.4. Arithmetic check: 0.4 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.4 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Double distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6372 | {<br>                "recipe_order": 3,<br>                "compound": "Double distilled water",<br>                "compound_id": 1021,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1021) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
