# Solution Concentration Review: Main sol. J1011

- Record: data/normalized_yaml/bacterial/mediadive_5052_Main_sol_J1011.yaml
- ID: CultureMech:013969
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9c34525181d1374646f5b1b82bd8ed2da61b143aeaffa9980d88e112bebab87d`
- Proposed/result SHA256: `9c34525181d1374646f5b1b82bd8ed2da61b143aeaffa9980d88e112bebab87d`
- Source: https://mediadive.dsmz.de/rest/solution/5052
- Source SHA256: df87556e59502a6c05d6d3d920c820057a6865c570cb69cd71c4b29cb1f483ee
- Retrieved: 2026-10-07T09:50:24.361979+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "700"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5052 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 700,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `composition[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5052 | {<br>                "recipe_order": 3,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 5,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=16) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | SW-25 solution | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5052 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "SW-25 solution",<br>                "solution_id": 5053,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 300,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
