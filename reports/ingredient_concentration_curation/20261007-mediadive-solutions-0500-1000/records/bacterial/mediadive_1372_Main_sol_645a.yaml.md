# Solution Concentration Review: Main sol. 645a

- Record: data/normalized_yaml/bacterial/mediadive_1372_Main_sol_645a.yaml
- ID: CultureMech:010856
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b46358dc869fb0c7cf9d37746ca4b3d0f8905fad16cb50b4a2c104e358798958`
- Proposed/result SHA256: `b46358dc869fb0c7cf9d37746ca4b3d0f8905fad16cb50b4a2c104e358798958`
- Source: https://mediadive.dsmz.de/rest/solution/1372
- Source SHA256: a1a4d4002eee9daf24585fc39f8d283d331aa093cf9b426afc4c3065cfb2f02f
- Retrieved: 2026-10-07T08:52:03.523459+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Middlebrook 7H10 agar | {"unit": "PERCENT_V_V", "value": "900"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1372 | {<br>                "recipe_order": 1,<br>                "compound": "Middlebrook 7H10 agar",<br>                "compound_id": 1748,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Difco 0627",<br>                "amount": 900,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1748) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | OADC Enrichment | {"unit": "PERCENT_V_V", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1372 | {<br>                "recipe_order": 2,<br>                "compound": "OADC Enrichment",<br>                "compound_id": 2129,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Difco 0722",<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2129) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Haemin | {"unit": "MICROMOLAR", "value": "60"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1372 | {<br>                "recipe_order": 3,<br>                "compound": "Haemin",<br>                "compound_id": 149,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "solubilized with 1N NaOH",<br>                "amount": 60,<br>                "unit": "\u03bcM",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=149) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
