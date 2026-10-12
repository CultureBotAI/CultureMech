# Solution Concentration Review: Solution A

- Record: data/normalized_yaml/bacterial/mediadive_1639_Solution_A.yaml
- ID: CultureMech:011096
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f745f041f3c480cfdea58200188888d08860fdf6c75c87aead89fbb61326ea80`
- Proposed/result SHA256: `f745f041f3c480cfdea58200188888d08860fdf6c75c87aead89fbb61326ea80`
- Source: https://mediadive.dsmz.de/rest/solution/1639
- Source SHA256: db80f11555fa25dfc71aff92d4dfd80611491cb084fb4173585140ac859b8633
- Retrieved: 2026-10-07T08:54:57.168404+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "6"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1639 | {<br>                "recipe_order": 1,<br>                "compound": "K2HPO4",<br>                "compound_id": 10,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 6,<br>                "unit": "g/l",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=10) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
