# Solution Concentration Review: Stock solution 4

- Record: data/normalized_yaml/bacterial/mediadive_6146_Stock_solution_4.yaml
- ID: CultureMech:014848
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `309f23ebcc1cf7812ab224d727f60d7ec3185503d9038756790f779a53f1e3fe`
- Proposed/result SHA256: `8459a34c92bf9f64789a26bbb57b284dc8e13d3d44097e079415f99ae0880d76`
- Source: https://mediadive.dsmz.de/rest/solution/6146
- Source SHA256: c21081dbdbc6a19e93cfe5d4535cfbcabbb130b46363f7126a50d448066cb4b8
- Retrieved: 2026-10-07T10:00:36.960940+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2SiO3 x 9 H2O | {"unit": "G_PER_L", "value": "57"} | {"unit": "G_PER_L", "value": "57"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6146 | {<br>                "recipe_order": 2,<br>                "compound": "Na2SiO3 x 9 H2O",<br>                "compound_id": 903,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 11.4,<br>                "unit": "g",<br>                "g_l": 57,<br>                "mmol_l": 200.562,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=903) | Provider explicitly reports g_l=57. Arithmetic check: 11.4 g * 1 g/g / (200 ml / 1000 ml per L) = 57 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 200. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
