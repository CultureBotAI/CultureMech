# Solution Concentration Review: Trace element solution

- Record: data/normalized_yaml/bacterial/mediadive_4452_Trace_element_solution.yaml
- ID: CultureMech:013433
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a3447b5e0672455618bd8cee1506321f4a533ddef0837b1a57aecdcccf8cb1f0`
- Proposed/result SHA256: `bf7d34d35d15a1c474d8ac4bb1dda18c3cb238eb7b61cf8874474933078d5e6a`
- Source: https://mediadive.dsmz.de/rest/solution/4452
- Source SHA256: 3e562b127df820e3a4499fd6902eede2e0e95cac6abade8e31e0c8c570752713
- Retrieved: 2026-10-07T09:43:53.940998+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | AlCl3 x 6 H2O | {"unit": "G_PER_L", "value": "0.01"} | {"unit": "G_PER_L", "value": "0.01"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4452 | {<br>                "recipe_order": 2,<br>                "compound": "AlCl3 x 6 H2O",<br>                "compound_id": 677,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "mg",<br>                "g_l": 0.01,<br>                "mmol_l": 0.0414197,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=677) | Provider explicitly reports g_l=0.01. Arithmetic check: 10 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.010 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Trace element solution | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4452 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Trace element solution",<br>                "solution_id": 3847,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
