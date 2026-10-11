# Solution Concentration Review: Main sol. 209

- Record: data/normalized_yaml/bacterial/mediadive_441_Main_sol_209.yaml
- ID: CultureMech:013404
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5ecd54f1172c568908b4fbd6ad867141e424df730985862ab177c4001ec11ae2`
- Proposed/result SHA256: `5ecd54f1172c568908b4fbd6ad867141e424df730985862ab177c4001ec11ae2`
- Source: https://mediadive.dsmz.de/rest/solution/441
- Source SHA256: e3d34c4fe30c1cf5f7c7453f1f3817095d6d490b9a0c2cb6c8577c8bccce55d2
- Retrieved: 2026-10-07T08:23:29.949066+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Arginine | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/441 | {<br>                "recipe_order": 2,<br>                "compound": "Arginine",<br>                "compound_id": 326,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.5,<br>                "unit": "%(w/v)",<br>                "g_l": 5,<br>                "mmol_l": 28.7026,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=326) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 78 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/441 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 78",<br>                "solution_id": 123,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
