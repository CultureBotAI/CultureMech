# Solution Concentration Review: Main sol. 79

- Record: data/normalized_yaml/bacterial/mediadive_135_Main_sol_79.yaml
- ID: CultureMech:010843
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1de3a9bfa16e94cea449f5e3c50f64afb89842401ac7999bcda24baa5ccb5716`
- Proposed/result SHA256: `c323ab05989abcee9b72bf2e3ce041d070a7b99208bde34b5311ec62881fbdda`
- Source: https://mediadive.dsmz.de/rest/solution/135
- Source SHA256: b15283fa20fc65d99132f06d73fe03fcac08d9f8fdb5e2ef0f890a8865513e40
- Retrieved: 2026-10-07T08:20:36.777937+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Tryptone | {"unit": "G_PER_L", "value": "10"} | {"unit": "G_PER_L", "value": "10"} | evidence_only | https://mediadive.dsmz.de/rest/solution/135 | {<br>                "recipe_order": 1,<br>                "compound": "Tryptone",<br>                "compound_id": 71,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "g",<br>                "g_l": 10,<br>                "mmol_l": 140.687,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=71) | Provider explicitly reports g_l=10. Arithmetic check: 10 g * 1 g/g / (1000 ml / 1000 ml per L) = 10 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[1]` | Synthetic sea water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/135 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Synthetic sea water",<br>                "solution_id": 5554,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
