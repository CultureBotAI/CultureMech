# Solution Concentration Review: Main sol. 465e

- Record: data/normalized_yaml/bacterial/mediadive_952_Main_sol_465e.yaml
- ID: CultureMech:015290
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5cb1c2039d6a6a5c0c064f3a3bb2f5632dbf61307ad31584f36403f4b208eedf`
- Proposed/result SHA256: `5cb1c2039d6a6a5c0c064f3a3bb2f5632dbf61307ad31584f36403f4b208eedf`
- Source: https://mediadive.dsmz.de/rest/solution/952
- Source SHA256: 07ac45507eb5ad86d74e269b8a5a5022229705180da9f66c7bc8c483eb08d93c
- Retrieved: 2026-10-07T08:48:00.141284+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | 2-Sulfobenzoic acid | {"unit": "PERCENT_V_V", "value": "50"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/952 | {<br>                "recipe_order": 3,<br>                "compound": "2-Sulfobenzoic acid",<br>                "compound_id": 2116,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "20 mg/ml",<br>                "amount": 50,<br>                "unit": "ml/l",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=2116) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 465 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/952 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 465",<br>                "solution_id": 945,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[1]` | Vitamin solution | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/952 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Vitamin solution",<br>                "solution_id": 934,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
