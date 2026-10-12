# Solution Concentration Review: 20mM (NH4)2HPO4

- Record: data/normalized_yaml/bacterial/mediadive_2508_20mM_NH4_2HPO4.yaml
- ID: CultureMech:011870
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `dde12f55dda2960868b864bf49717eca6f46f2a13778a3b0212d1d2f23f30110`
- Proposed/result SHA256: `0cd7f48a95f26a80f04e0dde0f77668ca56ba770ca630c0c607dc9f2bb752088`
- Source: https://mediadive.dsmz.de/rest/solution/2508
- Source SHA256: afaf731d4404db4ace5879cd72edd09d84a6ef67e912ae8ca8fe528efbb39cbf
- Retrieved: 2026-10-07T09:13:17.294924+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | H2O | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2508 | {<br>                "recipe_order": 1,<br>                "compound": "H2O",<br>                "compound_id": 56,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=56) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | (NH4)2HPO4 | {"unit": "G_PER_L", "value": "2.6"} | {"unit": "G_PER_L", "value": "2.6"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2508 | {<br>                "recipe_order": 2,<br>                "compound": "(NH4)2HPO4",<br>                "compound_id": 257,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.26,<br>                "unit": "g",<br>                "g_l": 2.6,<br>                "mmol_l": 19.688,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=257) | Provider explicitly reports g_l=2.6. Arithmetic check: 0.26 g * 1 g/g / (100 ml / 1000 ml per L) = 2.6 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
