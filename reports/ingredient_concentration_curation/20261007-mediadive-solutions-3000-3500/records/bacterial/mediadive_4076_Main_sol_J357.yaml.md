# Solution Concentration Review: Main sol. J357

- Record: data/normalized_yaml/bacterial/mediadive_4076_Main_sol_J357.yaml
- ID: CultureMech:013127
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `8096921939e55690a4d781563245781950d8c76ba7ae3c6261ab2e3dcb034bd4`
- Proposed/result SHA256: `4a2a100d635424768fec27cdf360ca70d2dc8d2a5fd6da15a5428be14693cc7a`
- Source: https://mediadive.dsmz.de/rest/solution/4076
- Source SHA256: 2aefa905fa6405aeb4d0df806f3ef53a6fdf03589c9754d1a88b428c3b726877
- Retrieved: 2026-10-07T09:40:18.762613+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "31"} | {"unit": "G_PER_L", "value": "31"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4076 | {<br>                "recipe_order": 2,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 31,<br>                "unit": "g",<br>                "g_l": 31,<br>                "mmol_l": 530.459,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=43) | Provider explicitly reports g_l=31. Arithmetic check: 31 g * 1 g/g / (1000 ml / 1000 ml per L) = 31 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. J118 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4076 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. J118",<br>                "solution_id": 3756,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
