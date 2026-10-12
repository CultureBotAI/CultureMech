# Solution Concentration Review: Sterile 1% "Marmite" solution

- Record: data/normalized_yaml/bacterial/mediadive_6168_Sterile_1_Marmite_solution.yaml
- ID: CultureMech:014870
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0c802be59cee263b5c0b286e8229b93f61b87ee1ab66d4999a80aa287d53cc2d`
- Proposed/result SHA256: `8e1f69aa6f314962b818e9e242f5f7e9f2c44bfc4f1c388c70bc09af12498707`
- Source: https://mediadive.dsmz.de/rest/solution/6168
- Source SHA256: 9927ef61610d5e79d7b9cd8d363957ab12348fc7c2720a95d1da9748d573314b
- Retrieved: 2026-10-07T10:00:52.974573+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Marmite | {"unit": "G_PER_L", "value": "10"} | {"unit": "G_PER_L", "value": "10"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6168 | {<br>                "recipe_order": 2,<br>                "compound": "Marmite",<br>                "compound_id": 2353,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 10,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2353) | Provider explicitly reports g_l=10. Arithmetic check: 1 g * 1 g/g / (100 ml / 1000 ml per L) = 1E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
