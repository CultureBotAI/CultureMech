# Solution Concentration Review: Main sol. 609

- Record: data/normalized_yaml/bacterial/mediadive_1308_Main_sol_609.yaml
- ID: CultureMech:010798
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1669b49c3252a84538c41fb325559cbff7cfedfe09b60cbd1c0749781c80c8ae`
- Proposed/result SHA256: `1669b49c3252a84538c41fb325559cbff7cfedfe09b60cbd1c0749781c80c8ae`
- Source: https://mediadive.dsmz.de/rest/solution/1308
- Source SHA256: 662e2544350f7993362d747c1bb40978654af70ea99070144d6a44cf0161c2fa
- Retrieved: 2026-10-07T08:51:19.836403+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Oatmeal | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1308 | {<br>                "recipe_order": 1,<br>                "compound": "Oatmeal",<br>                "compound_id": 471,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Quaker White Oats",<br>                "amount": 20,<br>                "unit": "g",<br>                "g_l": 20,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=471) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Agar | {"unit": "G_PER_L", "value": "18"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1308 | {<br>                "recipe_order": 2,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Difco",<br>                "amount": 18,<br>                "unit": "g",<br>                "g_l": 18,<br>                "mmol_l": 53.5189,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=3) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1308 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[3]` | Trace salt solution | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1308 | {<br>                "recipe_order": 4,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Trace salt solution",<br>                "solution_id": 1209,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
