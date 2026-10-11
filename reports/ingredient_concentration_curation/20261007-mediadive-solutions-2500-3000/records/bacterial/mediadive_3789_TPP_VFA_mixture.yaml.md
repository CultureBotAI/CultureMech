# Solution Concentration Review: TPP/VFA mixture

- Record: data/normalized_yaml/bacterial/mediadive_3789_TPP_VFA_mixture.yaml
- ID: CultureMech:012867
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2db79920eee55eccebdcbb4225ddb8c28907ebd6cc4b9485d3f4af775ce99eef`
- Proposed/result SHA256: `2db79920eee55eccebdcbb4225ddb8c28907ebd6cc4b9485d3f4af775ce99eef`
- Source: https://mediadive.dsmz.de/rest/solution/3789
- Source SHA256: 7a70f2f501554ba3bd5caf761257c4572b34510d7a6defd183a6ef9c5f142132
- Retrieved: 2026-10-07T09:25:05.007052+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Thiamine pyrophosphate | {"unit": "PERCENT_V_V", "value": "136.36363636363637"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3789 | {<br>                "recipe_order": 1,<br>                "compound": "Thiamine pyrophosphate",<br>                "compound_id": 778,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.2%",<br>                "amount": 1.5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=778) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "763.6363636363636"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3789 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 8.4,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[1]` | VFA solution | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3789 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "VFA solution",<br>                "solution_id": 3790,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
