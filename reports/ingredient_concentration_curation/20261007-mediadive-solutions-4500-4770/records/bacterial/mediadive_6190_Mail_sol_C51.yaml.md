# Solution Concentration Review: Mail sol. C51

- Record: data/normalized_yaml/bacterial/mediadive_6190_Mail_sol_C51.yaml
- ID: CultureMech:014889
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f3a9649fcdd45f27190918b2d3bbac0e0a594c8e1603b0d5d0d2e389d9e02a40`
- Proposed/result SHA256: `f3a9649fcdd45f27190918b2d3bbac0e0a594c8e1603b0d5d0d2e389d9e02a40`
- Source: https://mediadive.dsmz.de/rest/solution/6190
- Source SHA256: 091500870292eb589601d955ef3cf8958eb29d1b3311dd154f7e57252c77b53f
- Retrieved: 2026-10-07T10:01:06.277857+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaHCO3 | {"unit": "PERCENT_V_V", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6190 | {<br>                "recipe_order": 2,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.4 g/100 ml stock solution",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=55) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Deionized water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6190 | {<br>                "recipe_order": 4,<br>                "compound": "Deionized water",<br>                "compound_id": 418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Stock solution 1 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6190 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Stock solution 1",<br>                "solution_id": 6191,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[2]` | Stock solution 2 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6190 | {<br>                "recipe_order": 3,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Stock solution 2",<br>                "solution_id": 6192,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
