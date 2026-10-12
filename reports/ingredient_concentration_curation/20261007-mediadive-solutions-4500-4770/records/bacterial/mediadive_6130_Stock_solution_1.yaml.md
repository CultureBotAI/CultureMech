# Solution Concentration Review: Stock solution 1

- Record: data/normalized_yaml/bacterial/mediadive_6130_Stock_solution_1.yaml
- ID: CultureMech:014835
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `cf47a74707b696cd49e40822650754b9d013e2ad04658ffe52b730e048fd8671`
- Proposed/result SHA256: `6faa4f22d35d2b814fd45da4fa5901511256f4b0dad05c2a15ed054f59a783e8`
- Source: https://mediadive.dsmz.de/rest/solution/6130
- Source SHA256: 75ac437a0a2e0bf687ba0a8c6ace00c42da5286d146c8de5449a6b4a7dad4dde
- Retrieved: 2026-10-07T10:00:26.750571+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | EDTA | {"unit": "G_PER_L", "value": "50"} | {"unit": "G_PER_L", "value": "50"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6130 | {<br>                "recipe_order": 2,<br>                "compound": "EDTA",<br>                "compound_id": 271,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "g",<br>                "g_l": 50,<br>                "mmol_l": 171.092,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=271) | Provider explicitly reports g_l=50. Arithmetic check: 50 g * 1 g/g / (1000 ml / 1000 ml per L) = 50 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | KOH | {"unit": "G_PER_L", "value": "31"} | {"unit": "G_PER_L", "value": "31"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6130 | {<br>                "recipe_order": 3,<br>                "compound": "KOH",<br>                "compound_id": 126,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 31,<br>                "unit": "g",<br>                "g_l": 31,<br>                "mmol_l": 552.526,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=126) | Provider explicitly reports g_l=31. Arithmetic check: 31 g * 1 g/g / (1000 ml / 1000 ml per L) = 31 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
