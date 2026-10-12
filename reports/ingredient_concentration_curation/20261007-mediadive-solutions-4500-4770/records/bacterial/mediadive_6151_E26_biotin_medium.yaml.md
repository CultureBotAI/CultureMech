# Solution Concentration Review: E26 + biotin medium

- Record: data/normalized_yaml/bacterial/mediadive_6151_E26_biotin_medium.yaml
- ID: CultureMech:014852
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7859dbd4d399c33cfd98824e4d31003008239cd9db2bc8d7992909354a61d2ce`
- Proposed/result SHA256: `7859dbd4d399c33cfd98824e4d31003008239cd9db2bc8d7992909354a61d2ce`
- Source: https://mediadive.dsmz.de/rest/solution/6151
- Source SHA256: 66db5a4e679967545cfbd82496d3713bcd27b1c6652d0f4c5e765bc1386f6b00
- Retrieved: 2026-10-07T10:00:39.637704+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Natural sea water | {"unit": "PERCENT_V_V", "value": "500"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6151 | {<br>                "recipe_order": 3,<br>                "compound": "Natural sea water",<br>                "compound_id": 2152,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "filtered and autoclaved",<br>                "amount": 500,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2152) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Part 1 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6151 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Part 1",<br>                "solution_id": 6153,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 500,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
