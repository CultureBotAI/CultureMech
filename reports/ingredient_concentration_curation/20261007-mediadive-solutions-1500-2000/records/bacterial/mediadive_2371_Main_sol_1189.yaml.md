# Solution Concentration Review: Main sol. 1189

- Record: data/normalized_yaml/bacterial/mediadive_2371_Main_sol_1189.yaml
- ID: CultureMech:011749
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `663b586ac7653e9c1395827d244d97699c4962a9f99b563c3dd0c5ec73366694`
- Proposed/result SHA256: `663b586ac7653e9c1395827d244d97699c4962a9f99b563c3dd0c5ec73366694`
- Source: https://mediadive.dsmz.de/rest/solution/2371
- Source SHA256: 742fec84685eea5fa5ef514f06894b772888581133455b18da6ce3b3d7f19403
- Retrieved: 2026-10-07T09:11:53.425349+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2371 | {<br>                "recipe_order": 2,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Difco",<br>                "amount": 0.5,<br>                "unit": "g",<br>                "g_l": 0.5,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=16) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Salt base solution | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2371 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Salt base solution",<br>                "solution_id": 2372,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
