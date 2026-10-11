# Solution Concentration Review: alpha-ketoglutamate solution (20mM)

- Record: data/normalized_yaml/bacterial/mediadive_6373_alpha-ketoglutamate_solution_20mM.yaml
- ID: CultureMech:015004
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5f07f2e94e52f32470a4bdbcd099ad50abb2c879a13a994e134b0fcd4a89da7a`
- Proposed/result SHA256: `5f07f2e94e52f32470a4bdbcd099ad50abb2c879a13a994e134b0fcd4a89da7a`
- Source: https://mediadive.dsmz.de/rest/solution/6373
- Source SHA256: ef942ab552f3904b3143772b3f24ece58e52613b7ac22688b04110c80d4f4f65
- Retrieved: 2026-10-07T10:02:24.893500+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | alpha-ketoglutamate | {"unit": "MILLIMOLAR", "value": "20"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6373 | {<br>                "recipe_order": 2,<br>                "compound": "alpha-ketoglutamate",<br>                "compound_id": 2384,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "mM",<br>                "g_l": null,<br>                "mmol_l": 20,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2384) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Double distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6373 | {<br>                "recipe_order": 3,<br>                "compound": "Double distilled water",<br>                "compound_id": 1021,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1021) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
