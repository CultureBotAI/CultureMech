# Solution Concentration Review: BBM + V Vitamine Mix

- Record: data/normalized_yaml/bacterial/mediadive_6406_BBM_V_Vitamine_Mix.yaml
- ID: CultureMech:015020
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `aac8a02a39d2b814d9070bb1d7d8b65398becb93f8a28f9476ea0e36a3e9d368`
- Proposed/result SHA256: `aac8a02a39d2b814d9070bb1d7d8b65398becb93f8a28f9476ea0e36a3e9d368`
- Source: https://mediadive.dsmz.de/rest/solution/6406
- Source SHA256: 4b6e7f773ec41461b07bddf8bb09cada334faee131181076d00920d37b62038b
- Retrieved: 2026-10-07T10:02:35.038864+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Thiamine | {"unit": "PERCENT_V_V", "value": "333.33333333333337"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6406 | {<br>                "recipe_order": 2,<br>                "compound": "Thiamine",<br>                "compound_id": 666,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "10 g/l stock solution",<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=666) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Biotine | {"unit": "PERCENT_V_V", "value": "333.33333333333337"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6406 | {<br>                "recipe_order": 3,<br>                "compound": "Biotine",<br>                "compound_id": 899,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "2.5 g/l stock solution",<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=899) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Vitamine B12 | {"unit": "PERCENT_V_V", "value": "25.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6406 | {<br>                "recipe_order": 4,<br>                "compound": "Vitamine B12",<br>                "compound_id": 900,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.02 g/l stock solution",<br>                "amount": 0.75,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=900) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
