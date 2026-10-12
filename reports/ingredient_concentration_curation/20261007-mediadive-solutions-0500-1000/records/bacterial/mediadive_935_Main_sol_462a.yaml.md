# Solution Concentration Review: Main sol. 462a

- Record: data/normalized_yaml/bacterial/mediadive_935_Main_sol_462a.yaml
- ID: CultureMech:015281
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `4ac86b1fc76b0abf8b9d29980efee5e55afb7d6460085b5dfa6120e7cc0bf87e`
- Proposed/result SHA256: `4ac86b1fc76b0abf8b9d29980efee5e55afb7d6460085b5dfa6120e7cc0bf87e`
- Source: https://mediadive.dsmz.de/rest/solution/935
- Source SHA256: bbd769298f04eadc49d840569d8590b569288a92d0f9f7e26485df168645640b
- Retrieved: 2026-10-07T08:47:53.867919+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Fluoranthene | {"unit": "G_PER_L", "value": "2"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/935 | {<br>                "recipe_order": 2,<br>                "compound": "Fluoranthene",<br>                "compound_id": 2113,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "dissolved in acetone",<br>                "amount": 0,<br>                "unit": "",<br>                "g_l": 2,<br>                "mmol_l": 9.88875,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2113) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 462 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/935 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 462",<br>                "solution_id": 931,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
