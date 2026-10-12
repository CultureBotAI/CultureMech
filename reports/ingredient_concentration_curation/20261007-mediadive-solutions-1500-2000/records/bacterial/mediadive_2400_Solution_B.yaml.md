# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_2400_Solution_B.yaml
- ID: CultureMech:011778
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c86f9a69ca9604ab78d19be4acaeb4d3cdd7335ee2627b3dc6f5fbb5d73f2e7c`
- Proposed/result SHA256: `272465dc6834cf820f38a735f1bd39288cc783ac4f4ff86c67dd4b64e617163e`
- Source: https://mediadive.dsmz.de/rest/solution/2400
- Source SHA256: 3a135ed92cb2222eb197fd2b083507844711bfcaea9f17d714c54407dfaba9b3
- Retrieved: 2026-10-07T09:12:13.862052+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "200"} | {"unit": "G_PER_L", "value": "200"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2400 | {<br>                "recipe_order": 1,<br>                "compound": "FeSO4 x 7 H2O",<br>                "compound_id": 12,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "g",<br>                "g_l": 200,<br>                "mmol_l": 719.386,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=12) | Provider explicitly reports g_l=200. Arithmetic check: 20 g * 1 g/g / (100 ml / 1000 ml per L) = 2.0E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
