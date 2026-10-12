# Solution Concentration Review: Main sol. 480d

- Record: data/normalized_yaml/bacterial/mediadive_982_Main_sol_480d.yaml
- ID: CultureMech:015317
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1f471dd0cc0bcb55b0c58a7e05b334fc996e9c200d155870b32ac21c059e5747`
- Proposed/result SHA256: `1f471dd0cc0bcb55b0c58a7e05b334fc996e9c200d155870b32ac21c059e5747`
- Source: https://mediadive.dsmz.de/rest/solution/982
- Source SHA256: c776ae7552733325e3ad81b759f2fa93de806a8229b1e542b424dd6264cba381
- Retrieved: 2026-10-07T08:48:19.149965+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Casitone | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/982 | {<br>                "recipe_order": 2,<br>                "compound": "Casitone",<br>                "compound_id": 84,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3,<br>                "unit": "g/l",<br>                "g_l": 3,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=84) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 480 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/982 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 480",<br>                "solution_id": 978,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
