# Solution Concentration Review: Main sol. 465f

- Record: data/normalized_yaml/bacterial/mediadive_953_Main_sol_465f.yaml
- ID: CultureMech:015291
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `bf6a8a0e5e987950c325ca06d5f41fd8494dab6171c2c0bd64512d009006bc5f`
- Proposed/result SHA256: `bf6a8a0e5e987950c325ca06d5f41fd8494dab6171c2c0bd64512d009006bc5f`
- Source: https://mediadive.dsmz.de/rest/solution/953
- Source SHA256: ad6a769f18e7d05ff5e5edad637a043649555a473498ecc497ce4897d6e469fa
- Retrieved: 2026-10-07T08:48:00.917693+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | 3-Aminophenol | {"unit": "PERCENT_V_V", "value": "10"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/953 | {<br>                "recipe_order": 2,<br>                "compound": "3-Aminophenol",<br>                "compound_id": 2117,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "10 g/l",<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2117) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 465 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/953 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 465",<br>                "solution_id": 945,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
