# Solution Concentration Review: Main sol. 993c

- Record: data/normalized_yaml/bacterial/mediadive_2027_Main_sol_993c.yaml
- ID: CultureMech:011430
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6ffaaca44009bd516ccf052bd3a805e9cc84a18a9d32b49225d7987ef849dbd5`
- Proposed/result SHA256: `6ffaaca44009bd516ccf052bd3a805e9cc84a18a9d32b49225d7987ef849dbd5`
- Source: https://mediadive.dsmz.de/rest/solution/2027
- Source SHA256: 2304f69a345caf5420cc10c7fa65a0d8d3f85a5fc76452f4c28c2623e749ed24
- Retrieved: 2026-10-07T09:08:07.340240+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2027 | {<br>                "recipe_order": 2,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "%",<br>                "g_l": 100,<br>                "mmol_l": 1711.16,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=43) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 993 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2027 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 993",<br>                "solution_id": 2024,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
