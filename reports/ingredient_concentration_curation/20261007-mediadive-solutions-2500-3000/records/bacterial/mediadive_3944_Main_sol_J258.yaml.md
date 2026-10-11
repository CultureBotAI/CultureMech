# Solution Concentration Review: Main sol. J258

- Record: data/normalized_yaml/bacterial/mediadive_3944_Main_sol_J258.yaml
- ID: CultureMech:013006
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `460e4f9c5773e7a1b7817ec868c7ee3f9e54b913dc2eff06db8d0464da61df69`
- Proposed/result SHA256: `460e4f9c5773e7a1b7817ec868c7ee3f9e54b913dc2eff06db8d0464da61df69`
- Source: https://mediadive.dsmz.de/rest/solution/3944
- Source SHA256: cb9de844c09d2cd9b429ab7606eb4071f887063cc51a256efb597b29995f819d
- Retrieved: 2026-10-07T09:26:45.099398+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Malt extract agar | {"unit": "G_PER_L", "value": "50"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3944 | {<br>                "recipe_order": 1,<br>                "compound": "Malt extract agar",<br>                "compound_id": 1712,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Oxoid",<br>                "amount": 50,<br>                "unit": "g",<br>                "g_l": 50,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1712) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3944 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
