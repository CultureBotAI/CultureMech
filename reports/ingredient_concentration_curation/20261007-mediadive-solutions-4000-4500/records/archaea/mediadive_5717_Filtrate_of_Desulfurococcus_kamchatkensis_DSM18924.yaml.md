# Solution Concentration Review: Filtrate of Desulfurococcus kamchatkensis (DSM18924)

- Record: data/normalized_yaml/archaea/mediadive_5717_Filtrate_of_Desulfurococcus_kamchatkensis_DSM18924.yaml
- ID: CultureMech:014579
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `386d04440dc3914d8b850cafe7fb7c00c3b355622045946879116333d0d8ba04`
- Proposed/result SHA256: `386d04440dc3914d8b850cafe7fb7c00c3b355622045946879116333d0d8ba04`
- Source: https://mediadive.dsmz.de/rest/solution/5717
- Source SHA256: 1b9bcd40a2e5ed43954c58a55f80ac01a6d337c2c0a0646c69235b9ef32bac27
- Retrieved: 2026-10-07T09:57:40.676088+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Glucose | {"unit": "G_PER_L", "value": "2"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5717 | {<br>                "recipe_order": 2,<br>                "compound": "Glucose",<br>                "compound_id": 5,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "g/l",<br>                "g_l": 2,<br>                "mmol_l": 11.1012,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=5) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.6"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5717 | {<br>                "recipe_order": 3,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.6,<br>                "unit": "g/l",<br>                "g_l": 0.6,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=16) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Liquid medium | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5717 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Liquid medium",<br>                "solution_id": 5720,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
