# Solution Concentration Review: Stock Solution B (10 ml)

- Record: data/normalized_yaml/bacterial/mediadive_5741_Stock_Solution_B_10_ml.yaml
- ID: CultureMech:014596
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `4ffa66b184e91278ed9fbc55badb9779c6746f8b5eeb04f37f204237e2a48c68`
- Proposed/result SHA256: `e3383cc55bcb08a145645fa90256646b5fb5c31880465b6c44c2b5ab5acdb28c`
- Source: https://mediadive.dsmz.de/rest/solution/5741
- Source SHA256: 1e8797e44e6310dabf4ae11b83d1b34efb0d3897620436f6daca6e7ccca96e4e
- Retrieved: 2026-10-07T09:57:52.389785+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2 MoO4 x 2 H2O | {"unit": "G_PER_L", "value": "2"} | {"unit": "G_PER_L", "value": "2"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5741 | {<br>                "recipe_order": 1,<br>                "compound": "Na2 MoO4 x 2 H2O",<br>                "compound_id": 1503,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.02,<br>                "unit": "g",<br>                "g_l": 2,<br>                "mmol_l": 8.26617,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1503) | Provider explicitly reports g_l=2. Arithmetic check: 0.02 g * 1 g/g / (10 ml / 1000 ml per L) = 2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
