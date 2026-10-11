# Solution Concentration Review: Pentachlorophenol solution

- Record: data/normalized_yaml/bacterial/mediadive_5631_Pentachlorophenol_solution.yaml
- ID: CultureMech:014502
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9f2258ff2fc42f56a996b37516af0b38db33911369b59a1a05fcece7307f291a`
- Proposed/result SHA256: `9f2258ff2fc42f56a996b37516af0b38db33911369b59a1a05fcece7307f291a`
- Source: https://mediadive.dsmz.de/rest/solution/5631
- Source SHA256: 91224ec92682c8e8786322083820284903a1fc2eedb373d2dfbdba236af4b3b5
- Retrieved: 2026-10-07T09:56:45.302275+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Pentachlorophenol | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5631 | {<br>                "recipe_order": 2,<br>                "compound": "Pentachlorophenol",<br>                "compound_id": 2115,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2115) | Missing numeric input | unchanged |
| `composition[1].concentration` | NaOH | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5631 | {<br>                "recipe_order": 3,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.01 M",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=256) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
