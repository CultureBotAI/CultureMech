# Solution Concentration Review: Main sol. J126

- Record: data/normalized_yaml/bacterial/mediadive_3766_Main_sol_J126.yaml
- ID: CultureMech:012843
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5277799ec89d36bb09a31e0f177d25e1da69d768719a640abc513cf1351ff342`
- Proposed/result SHA256: `5277799ec89d36bb09a31e0f177d25e1da69d768719a640abc513cf1351ff342`
- Source: https://mediadive.dsmz.de/rest/solution/3766
- Source SHA256: da6b3342f50864683c35b2af96d76cc4f686a4a950143656d28a267e8e986b36
- Retrieved: 2026-10-07T09:24:47.058591+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Methanol-utilizing bacteria medium B | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3766 | {<br>                "recipe_order": 1,<br>                "compound": "Methanol-utilizing bacteria medium B",<br>                "compound_id": 1633,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "see Medium No. 79",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1633) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
