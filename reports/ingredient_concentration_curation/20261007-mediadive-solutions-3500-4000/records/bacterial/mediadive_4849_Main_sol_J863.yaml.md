# Solution Concentration Review: Main sol. J863

- Record: data/normalized_yaml/bacterial/mediadive_4849_Main_sol_J863.yaml
- ID: CultureMech:013782
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a49b5b64416a422fb0b7bb2d2abd0c72d243d18e23125cd6835286ce6edc0cc9`
- Proposed/result SHA256: `78414b2eb68ba062e77f5f6ec5a1aeef7dd1a64a9081df9c8be66024a4156e56`
- Source: https://mediadive.dsmz.de/rest/solution/4849
- Source SHA256: 5563a2daa64bbcf298de85d0a39cfce3864daa3f66a5097ed41c1ae73415dd71
- Retrieved: 2026-10-07T09:48:08.803073+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Inorganic salts-starch agar | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4849 | {<br>                "recipe_order": 1,<br>                "compound": "Inorganic salts-starch agar",<br>                "compound_id": 1692,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "ISP-4) (see Medium No. 58",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1692) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | NaCl | {"unit": "G_PER_L", "value": "150"} | {"unit": "G_PER_L", "value": "150"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4849 | {<br>                "recipe_order": 2,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 150,<br>                "unit": "g",<br>                "g_l": 150,<br>                "mmol_l": 2566.74,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=43) | Provider explicitly reports g_l=150. Arithmetic check: 150 g * 1 g/g / (1000 ml / 1000 ml per L) = 150 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
