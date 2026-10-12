# Solution Concentration Review: Main sol. J292

- Record: data/normalized_yaml/bacterial/mediadive_3990_Main_sol_J292.yaml
- ID: CultureMech:013047
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `bfa452edab3506fcf86756f42e73cbf40f275790f4ad5b3f99ad9418e0016d9c`
- Proposed/result SHA256: `bfa452edab3506fcf86756f42e73cbf40f275790f4ad5b3f99ad9418e0016d9c`
- Source: https://mediadive.dsmz.de/rest/solution/3990
- Source SHA256: 6981356cddbf5d10fb348e627de57578720d9831a17a055e907d62cdf21039ec
- Retrieved: 2026-10-07T09:27:13.408280+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Lactobacilli MRS broth | {"unit": "G_PER_L", "value": "55"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3990 | {<br>                "recipe_order": 1,<br>                "compound": "Lactobacilli MRS broth",<br>                "compound_id": 1711,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 55,<br>                "unit": "g",<br>                "g_l": 55,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1711) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3990 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
