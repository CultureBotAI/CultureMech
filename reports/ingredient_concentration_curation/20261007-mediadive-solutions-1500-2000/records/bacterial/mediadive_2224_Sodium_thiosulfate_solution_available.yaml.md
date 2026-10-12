# Solution Concentration Review: Sodium thiosulfate solution (available)

- Record: data/normalized_yaml/bacterial/mediadive_2224_Sodium_thiosulfate_solution_available.yaml
- ID: CultureMech:011615
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `800f48fdb5a0d72ddf927d95897f94025a875fc710ff49da4bf9a8a32b91e23b`
- Proposed/result SHA256: `800f48fdb5a0d72ddf927d95897f94025a875fc710ff49da4bf9a8a32b91e23b`
- Source: https://mediadive.dsmz.de/rest/solution/2224
- Source SHA256: 9bab5352241686fc0659ccb84ee0ce57a1a1fb47068c2dfb3108d1e63ecb011f
- Retrieved: 2026-10-07T09:10:20.059448+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2S2O3 | {"unit": "G_PER_L", "value": "500"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2224 | {<br>                "recipe_order": 1,<br>                "compound": "Na2S2O3",<br>                "compound_id": 552,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "%",<br>                "g_l": 500,<br>                "mmol_l": 1166.82,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=552) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
