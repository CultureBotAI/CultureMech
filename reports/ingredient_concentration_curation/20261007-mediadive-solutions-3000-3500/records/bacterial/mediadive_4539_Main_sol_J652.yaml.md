# Solution Concentration Review: Main sol. J652

- Record: data/normalized_yaml/bacterial/mediadive_4539_Main_sol_J652.yaml
- ID: CultureMech:013505
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d753474cd65f800991971f3a5a7b0440c476b62d12661e593b9d59f8c70a67b4`
- Proposed/result SHA256: `d753474cd65f800991971f3a5a7b0440c476b62d12661e593b9d59f8c70a67b4`
- Source: https://mediadive.dsmz.de/rest/solution/4539
- Source SHA256: 2e33b66b10c9f569ae57b2697150070924f066b7371131fdd034f9f981baa72d
- Retrieved: 2026-10-07T09:44:47.773458+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Trypticase soy agar | {"unit": "G_PER_L", "value": "40"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4539 | {<br>                "recipe_order": 1,<br>                "compound": "Trypticase soy agar",<br>                "compound_id": 1617,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-BBL",<br>                "amount": 40,<br>                "unit": "g",<br>                "g_l": 40,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1617) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[1]` | 0.5 x Artificial seawater | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4539 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "0.5 x Artificial seawater",<br>                "solution_id": 4538,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
