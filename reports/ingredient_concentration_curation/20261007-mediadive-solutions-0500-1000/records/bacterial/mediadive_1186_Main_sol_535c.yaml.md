# Solution Concentration Review: Main sol. 535c

- Record: data/normalized_yaml/bacterial/mediadive_1186_Main_sol_535c.yaml
- ID: CultureMech:010680
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `59a112eded66c08aec84f4955fd805bcb00a10a514dc9a566e35c892d45ee85c`
- Proposed/result SHA256: `59a112eded66c08aec84f4955fd805bcb00a10a514dc9a566e35c892d45ee85c`
- Source: https://mediadive.dsmz.de/rest/solution/1186
- Source SHA256: 40807fee411c222fa9a00c8d87e67e29a685c44782fe1028381db8d13e91d4d3
- Retrieved: 2026-10-07T08:49:54.923479+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Tween 80 | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1186 | {<br>                "recipe_order": 2,<br>                "compound": "Tween 80",<br>                "compound_id": 22,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "%",<br>                "g_l": 10,<br>                "mmol_l": 7.64035,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=22) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 535 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1186 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 535",<br>                "solution_id": 1181,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
