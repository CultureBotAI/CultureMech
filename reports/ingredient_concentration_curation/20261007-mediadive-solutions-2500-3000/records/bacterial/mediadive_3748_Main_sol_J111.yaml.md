# Solution Concentration Review: Main sol. J111

- Record: data/normalized_yaml/bacterial/mediadive_3748_Main_sol_J111.yaml
- ID: CultureMech:012826
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3e006a8e36e7783d1b0357b2734b13b666d0e8782b5fcb2d303c2fda0d758971`
- Proposed/result SHA256: `3e006a8e36e7783d1b0357b2734b13b666d0e8782b5fcb2d303c2fda0d758971`
- Source: https://mediadive.dsmz.de/rest/solution/3748
- Source SHA256: 27d5a2f5b00e73f35fae56f0b24c4e49a735abc717e111c81c08c0f42a6bdacf
- Retrieved: 2026-10-07T09:24:33.920208+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | MRS medium | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3748 | {<br>                "recipe_order": 1,<br>                "compound": "MRS medium",<br>                "compound_id": 1626,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "see Medium No. 1",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1626) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
