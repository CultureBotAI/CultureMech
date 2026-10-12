# Solution Concentration Review: Main sol. 672

- Record: data/normalized_yaml/bacterial/mediadive_1421_Main_sol_672.yaml
- ID: CultureMech:010898
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `00c07f9aac62912f9b0f9c3683249fd531636c8611faeaae75a17725510202f9`
- Proposed/result SHA256: `00c07f9aac62912f9b0f9c3683249fd531636c8611faeaae75a17725510202f9`
- Source: https://mediadive.dsmz.de/rest/solution/1421
- Source SHA256: c38a5879de733147bec0a23e0d90c15b485e5db3cce49f7ffcebd5d1de8b3e33
- Retrieved: 2026-10-07T08:52:33.480022+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Difco 0001 | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1421 | {<br>                "recipe_order": 1,<br>                "compound": "Difco 0001",<br>                "compound_id": 2132,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2132) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
