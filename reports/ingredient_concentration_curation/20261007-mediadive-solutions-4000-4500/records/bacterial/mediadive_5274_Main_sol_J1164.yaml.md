# Solution Concentration Review: Main sol. J1164

- Record: data/normalized_yaml/bacterial/mediadive_5274_Main_sol_J1164.yaml
- ID: CultureMech:014186
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `086e6a3da28ad76df6ca9934619af526fe6617b22512da5dc97720e7d1de8077`
- Proposed/result SHA256: `086e6a3da28ad76df6ca9934619af526fe6617b22512da5dc97720e7d1de8077`
- Source: https://mediadive.dsmz.de/rest/solution/5274
- Source SHA256: 0326dc6a789d782f5ad956b6d67ac3bce2cf9e82c688e2e235a92d82745831d7
- Retrieved: 2026-10-07T09:53:01.560498+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Marine agar 2216 | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5274 | {<br>                "recipe_order": 1,<br>                "compound": "Marine agar 2216",<br>                "compound_id": 1628,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "see Medium No. 118",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1628) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Starch | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5274 | {<br>                "recipe_order": 2,<br>                "compound": "Starch",<br>                "compound_id": 199,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "soluble",<br>                "amount": 10,<br>                "unit": "g",<br>                "g_l": 10,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=199) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
