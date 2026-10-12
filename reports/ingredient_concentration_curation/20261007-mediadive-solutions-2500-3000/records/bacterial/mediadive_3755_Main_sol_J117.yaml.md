# Solution Concentration Review: Main sol. J117

- Record: data/normalized_yaml/bacterial/mediadive_3755_Main_sol_J117.yaml
- ID: CultureMech:012832
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `78703c7db4a57f2afa30a61d03ae9510179cbcbdbe7323a71b3a5c64a01a22fe`
- Proposed/result SHA256: `78703c7db4a57f2afa30a61d03ae9510179cbcbdbe7323a71b3a5c64a01a22fe`
- Source: https://mediadive.dsmz.de/rest/solution/3755
- Source SHA256: 038ce71261ce74d2c4bdb1119ceb78d73d84a0b0d0b731374120304a5393e382
- Retrieved: 2026-10-07T09:24:39.258257+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | R agar | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3755 | {<br>                "recipe_order": 1,<br>                "compound": "R agar",<br>                "compound_id": 1619,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "see Medium No. 26",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1619) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Catalase | {"unit": "G_PER_L", "value": "0.06"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3755 | {<br>                "recipe_order": 2,<br>                "compound": "Catalase",<br>                "compound_id": 270,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Sigma C-10",<br>                "amount": 60,<br>                "unit": "mg",<br>                "g_l": 0.06,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=270) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
