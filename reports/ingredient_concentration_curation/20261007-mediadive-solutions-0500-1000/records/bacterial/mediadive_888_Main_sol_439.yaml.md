# Solution Concentration Review: Main sol. 439

- Record: data/normalized_yaml/bacterial/mediadive_888_Main_sol_439.yaml
- ID: CultureMech:015247
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `356c53ed12b75b0f4c4c98f1ab10454564cc73ff46e75a6837f45724f525e965`
- Proposed/result SHA256: `356c53ed12b75b0f4c4c98f1ab10454564cc73ff46e75a6837f45724f525e965`
- Source: https://mediadive.dsmz.de/rest/solution/888
- Source SHA256: 65da10b5feb947dd6a00c517635123fdcf27a3d6726fc1a3eece509e17b0e15b
- Retrieved: 2026-10-07T08:47:30.926082+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Casman-Agar-Base | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/888 | {<br>                "recipe_order": 1,<br>                "compound": "Casman-Agar-Base",<br>                "compound_id": 2099,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Difco",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2099) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Sheep blood | {"unit": "G_PER_L", "value": "50"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/888 | unknown / not asserted | unknown / not asserted | Ambiguous source rows for this compound ID. | unchanged |
| `composition[2].concentration` | Sheep blood | {"unit": "G_PER_L", "value": "1.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/888 | unknown / not asserted | unknown / not asserted | Ambiguous source rows for this compound ID. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
