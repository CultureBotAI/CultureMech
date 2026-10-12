# Solution Concentration Review: Solution D ("red mix")

- Record: data/normalized_yaml/bacterial/mediadive_2393_Solution_D_red_mix.yaml
- ID: CultureMech:011772
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2e55c470760958117d276f9444ab439af33c009eb89c507e5fb55c2f50af337c`
- Proposed/result SHA256: `3100964560f817f7644bc44f6aac649c5ea8704bd1e206fe60ed83b3cd604495`
- Source: https://mediadive.dsmz.de/rest/solution/2393
- Source SHA256: 7cbf2b2b201b0275dbfcea1f6274a11b87688b0982c126727a2a68c7c7459571
- Retrieved: 2026-10-07T09:12:09.970521+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | L-Cysteine | {"unit": "G_PER_L", "value": "0.75"} | {"unit": "G_PER_L", "value": "0.75"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2393 | {<br>                "recipe_order": 1,<br>                "compound": "L-Cysteine",<br>                "compound_id": 671,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 37.5,<br>                "unit": "mg",<br>                "g_l": 0.75,<br>                "mmol_l": 6.19016,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=671) | Provider explicitly reports g_l=0.75. Arithmetic check: 37.5 mg * 0.001 g/mg / (50 ml / 1000 ml per L) = 0.75 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Na2S x H2O | {"unit": "G_PER_L", "value": "0.8"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2393 | {<br>                "recipe_order": 2,<br>                "compound": "Na2S x H2O",<br>                "compound_id": 1075,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "dissolved separately in water",<br>                "amount": 40,<br>                "unit": "mg",<br>                "g_l": 0.8,<br>                "mmol_l": 10.2505,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1075) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.05"} | correct | https://mediadive.dsmz.de/rest/solution/2393 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Source water addition is 50 ml per prepared batch: 50 / 1000 = 0.05 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
