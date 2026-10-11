# Solution Concentration Review: Main sol. 245

- Record: data/normalized_yaml/bacterial/mediadive_506_Main_sol_245.yaml
- ID: CultureMech:013985
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `12ee83291eddc25a6320ead42386e68087da0b2f934834375fa6620b7c09b06e`
- Proposed/result SHA256: `12ee83291eddc25a6320ead42386e68087da0b2f934834375fa6620b7c09b06e`
- Source: https://mediadive.dsmz.de/rest/solution/506
- Source SHA256: fe716444c5d605c930b447bc4bb5884a9bad738e6eec947942c3aee6e271ee73
- Retrieved: 2026-10-07T08:24:03.288079+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Defibrinated sheep blood | {"unit": "PERCENT_W_V", "value": "5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/506 | {<br>                "recipe_order": 2,<br>                "compound": "Defibrinated sheep blood",<br>                "compound_id": 1717,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "%",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1717) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 220 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/506 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 220",<br>                "solution_id": 477,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
