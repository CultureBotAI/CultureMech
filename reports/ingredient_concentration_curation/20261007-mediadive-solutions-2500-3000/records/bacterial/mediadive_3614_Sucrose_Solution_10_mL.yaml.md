# Solution Concentration Review: Sucrose Solution (10 mL)

- Record: data/normalized_yaml/bacterial/mediadive_3614_Sucrose_Solution_10_mL.yaml
- ID: CultureMech:012697
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ea3fda847d7dc15a3933122e46d813e486f54874658e9fa4d054df395914a90f`
- Proposed/result SHA256: `4685f4e119390350d59cf8720a558362e83c6e0d6b7593962a533be407fa3b00`
- Source: https://mediadive.dsmz.de/rest/solution/3614
- Source SHA256: ba280bafeb3491d81bc35c28a576b173acfe369127ad9a9404c04305341dab78
- Retrieved: 2026-10-07T09:22:59.819631+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sucrose | {"unit": "G_PER_L", "value": "2000"} | {"unit": "G_PER_L", "value": "2000"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3614 | {<br>                "recipe_order": 1,<br>                "compound": "Sucrose",<br>                "compound_id": 108,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "g",<br>                "g_l": 2000,<br>                "mmol_l": 5842.83,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=108) | Provider explicitly reports g_l=2000. Arithmetic check: 20 g * 1 g/g / (10 ml / 1000 ml per L) = 2.0E+3 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
