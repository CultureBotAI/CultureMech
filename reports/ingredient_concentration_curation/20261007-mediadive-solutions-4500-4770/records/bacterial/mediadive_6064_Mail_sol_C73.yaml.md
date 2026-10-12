# Solution Concentration Review: Mail sol. C73

- Record: data/normalized_yaml/bacterial/mediadive_6064_Mail_sol_C73.yaml
- ID: CultureMech:014782
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c2f2cb597e20667164405fa2afab24c0117700f3fa7f44e7cb05658ae1051acb`
- Proposed/result SHA256: `c2f2cb597e20667164405fa2afab24c0117700f3fa7f44e7cb05658ae1051acb`
- Source: https://mediadive.dsmz.de/rest/solution/6064
- Source SHA256: b885fa932ef2a78eb60423b135c69cd6345be4f010d840fcdee42c57f54b5bdc
- Retrieved: 2026-10-07T09:59:51.378742+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Deionized water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6064 | {<br>                "recipe_order": 4,<br>                "compound": "Deionized water",<br>                "compound_id": 418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Stock solution 1 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6064 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Stock solution 1",<br>                "solution_id": 6216,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[1]` | Stock solution 2 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6064 | {<br>                "recipe_order": 3,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Stock solution 2",<br>                "solution_id": 6217,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
