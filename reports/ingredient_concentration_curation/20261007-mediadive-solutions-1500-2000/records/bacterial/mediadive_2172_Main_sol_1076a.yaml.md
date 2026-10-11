# Solution Concentration Review: Main sol. 1076a

- Record: data/normalized_yaml/bacterial/mediadive_2172_Main_sol_1076a.yaml
- ID: CultureMech:011567
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f51817e8d63fde5191316ba4b203bcc1a2f07f1257d83b44e4bc1037e3d549d6`
- Proposed/result SHA256: `f51817e8d63fde5191316ba4b203bcc1a2f07f1257d83b44e4bc1037e3d549d6`
- Source: https://mediadive.dsmz.de/rest/solution/2172
- Source SHA256: 9556d9d2ed61e35afa25dab7f9b784d2f78832832d557b88f7e84f37c4d4ef81
- Retrieved: 2026-10-07T09:09:47.188161+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Glucose | {"unit": "G_PER_L", "value": "0.52"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2172 | {<br>                "recipe_order": 2,<br>                "compound": "Glucose",<br>                "compound_id": 5,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "10 %",<br>                "amount": 5.2,<br>                "unit": "ml",<br>                "g_l": 0.52,<br>                "mmol_l": 2.88632,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=5) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 1076 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2172 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 1076",<br>                "solution_id": 2171,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 517,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
