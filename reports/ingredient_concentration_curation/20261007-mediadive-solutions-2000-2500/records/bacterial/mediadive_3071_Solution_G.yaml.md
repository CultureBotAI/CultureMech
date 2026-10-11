# Solution Concentration Review: Solution G

- Record: data/normalized_yaml/bacterial/mediadive_3071_Solution_G.yaml
- ID: CultureMech:012295
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `914c5899faef1ae518707a98b568c3d8920b0d3edaa606dad77b7b75cb9409c7`
- Proposed/result SHA256: `914c5899faef1ae518707a98b568c3d8920b0d3edaa606dad77b7b75cb9409c7`
- Source: https://mediadive.dsmz.de/rest/solution/3071
- Source SHA256: cbababa6b27b27bf24b5bbac46ec3531d3a882589211835cc73a9c578a1379d6
- Retrieved: 2026-10-07T09:18:12.028665+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Asialofetuin | {"unit": "G_PER_L", "value": "100.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3071 | {<br>                "recipe_order": 1,<br>                "compound": "Asialofetuin",<br>                "compound_id": 2150,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "mg/ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2150) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
