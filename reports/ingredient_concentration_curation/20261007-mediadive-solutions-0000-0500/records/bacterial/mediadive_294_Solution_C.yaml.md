# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_294_Solution_C.yaml
- ID: CultureMech:012199
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3db103a597460973772a68635116d41f8c8c2df5902e0beb93c4a02f3494e4f9`
- Proposed/result SHA256: `3db103a597460973772a68635116d41f8c8c2df5902e0beb93c4a02f3494e4f9`
- Source: https://mediadive.dsmz.de/rest/solution/294
- Source SHA256: 1b228cd0c38803f008d476b81e9aca198e7d3ff9f1e2dfd2f6e0172326f1d566
- Retrieved: 2026-10-07T08:22:17.565692+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "1.39689"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/294 | {<br>                "recipe_order": 1,<br>                "compound": "K2HPO4",<br>                "compound_id": 10,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.5 M",<br>                "amount": 16.04,<br>                "unit": "ml",<br>                "g_l": 1.39689,<br>                "mmol_l": 8.02,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=10) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "0.269448"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/294 | {<br>                "recipe_order": 2,<br>                "compound": "KH2PO4",<br>                "compound_id": 11,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.5 M",<br>                "amount": 3.96,<br>                "unit": "ml",<br>                "g_l": 0.269448,<br>                "mmol_l": 1.98,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=11) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
