# Solution Concentration Review: Cycloheximid solution

- Record: data/normalized_yaml/bacterial/mediadive_5953_Cycloheximid_solution.yaml
- ID: CultureMech:014707
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `57a48396e910b9b4b9d0a939c2011eee8ea01bb3769ba541a4c40555ed7d57a2`
- Proposed/result SHA256: `36bfabda9c7b77dd1ffec4a119c58ed7904a9269c4ca9e3ece41eaf739f260db`
- Source: https://mediadive.dsmz.de/rest/solution/5953
- Source SHA256: 2887c444637756e49b9073054d172a20e0c2b1c6a77cc8516c0bdd166852d6ca
- Retrieved: 2026-10-07T09:59:01.406831+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Cycloheximid | {"unit": "G_PER_L", "value": "1"} | {"unit": "G_PER_L", "value": "1"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5953 | {<br>                "recipe_order": 2,<br>                "compound": "Cycloheximid",<br>                "compound_id": 1286,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "mg",<br>                "g_l": 1,<br>                "mmol_l": 3.55433,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1286) | Provider explicitly reports g_l=1. Arithmetic check: 10 mg * 0.001 g/mg / (10 ml / 1000 ml per L) = 1.0 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Demineralized water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5953 | {<br>                "recipe_order": 3,<br>                "compound": "Demineralized water",<br>                "compound_id": 1448,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1448) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
