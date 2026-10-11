# Solution Concentration Review: CasAA mix 5x

- Record: data/normalized_yaml/bacterial/mediadive_5494_CasAA_mix_5x.yaml
- ID: CultureMech:014397
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0f99e13edc64b22e15bff55cd0da9c937f7c394e62dd76385c8bf8ff0f8bc501`
- Proposed/result SHA256: `0f99e13edc64b22e15bff55cd0da9c937f7c394e62dd76385c8bf8ff0f8bc501`
- Source: https://mediadive.dsmz.de/rest/solution/5494
- Source SHA256: f2f15fb5eec0c0626644d4ab4e6c98fc2ac6ffa78beca47589d9ecee7e5051d4
- Retrieved: 2026-10-07T09:55:34.823695+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Casamino acids | {"unit": "G_PER_L", "value": "50"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5494 | {<br>                "recipe_order": 1,<br>                "compound": "Casamino acids",<br>                "compound_id": 101,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "g/l",<br>                "g_l": 50,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=101) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | L-Cysteine | {"unit": "G_PER_L", "value": "2.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5494 | {<br>                "recipe_order": 2,<br>                "compound": "L-Cysteine",<br>                "compound_id": 671,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.5,<br>                "unit": "g/l",<br>                "g_l": 2.5,<br>                "mmol_l": 20.6339,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=671) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | L-Tryptophan | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5494 | {<br>                "recipe_order": 3,<br>                "compound": "L-Tryptophan",<br>                "compound_id": 449,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.5,<br>                "unit": "g/l",<br>                "g_l": 0.5,<br>                "mmol_l": 2.44834,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=449) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
