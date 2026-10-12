# Solution Concentration Review: HEPES buffer solution

- Record: data/normalized_yaml/bacterial/mediadive_3383_HEPES_buffer_solution.yaml
- ID: CultureMech:012529
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e1d3c3e673c70f11ed4d8393b41bcaefea62d0f832d938519337628d7951a751`
- Proposed/result SHA256: `e1d3c3e673c70f11ed4d8393b41bcaefea62d0f832d938519337628d7951a751`
- Source: https://mediadive.dsmz.de/rest/solution/3383
- Source SHA256: f88ebab2e11dc43e321a88d6d12959b66f318293585192350454683fb22ccaf9
- Retrieved: 2026-10-07T09:21:01.114818+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaOH | {"unit": "G_PER_L", "value": "24"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3383 | {<br>                "recipe_order": 1,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "pellets",<br>                "amount": 24,<br>                "unit": "g",<br>                "g_l": 24,<br>                "mmol_l": 600.045,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=256) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | HEPES | {"unit": "G_PER_L", "value": "238.4"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3383 | {<br>                "recipe_order": 2,<br>                "compound": "HEPES",<br>                "compound_id": 371,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "free acid",<br>                "amount": 238.4,<br>                "unit": "g",<br>                "g_l": 238.4,<br>                "mmol_l": 1000.42,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=371) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3383 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
