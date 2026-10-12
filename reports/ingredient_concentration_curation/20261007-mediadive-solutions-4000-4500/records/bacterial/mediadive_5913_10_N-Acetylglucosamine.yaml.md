# Solution Concentration Review: 10% N-Acetylglucosamine

- Record: data/normalized_yaml/bacterial/mediadive_5913_10_N-Acetylglucosamine.yaml
- ID: CultureMech:014696
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b34d66266dd010eff6f4e9cf501e6a9b859d72fecfd45b0c4b14a9d4a80f8356`
- Proposed/result SHA256: `0d4dbe26ac5c07956a0dd199c2e32cab42df7431174501dbf09850d2adbd1595`
- Source: https://mediadive.dsmz.de/rest/solution/5913
- Source SHA256: ad8cf379eac5856c04f47af52462cb7cca24a364bf4e9aa0471a941bb73aee51
- Retrieved: 2026-10-07T09:58:55.934821+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | N-Acetylglucosamine | {"unit": "G_PER_L", "value": "100"} | {"unit": "G_PER_L", "value": "100"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5913 | {<br>                "recipe_order": 2,<br>                "compound": "N-Acetylglucosamine",<br>                "compound_id": 462,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "g",<br>                "g_l": 100,<br>                "mmol_l": 452.059,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=462) | Provider explicitly reports g_l=100. Arithmetic check: 10 g * 1 g/g / (100 ml / 1000 ml per L) = 1.0E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
