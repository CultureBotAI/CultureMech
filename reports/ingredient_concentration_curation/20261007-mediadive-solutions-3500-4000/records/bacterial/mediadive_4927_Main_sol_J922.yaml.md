# Solution Concentration Review: Main sol. J922

- Record: data/normalized_yaml/bacterial/mediadive_4927_Main_sol_J922.yaml
- ID: CultureMech:013854
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ae543b18fda7df2c61bd566b37c48472d586a8e4e0a460d20bd886232c2e4162`
- Proposed/result SHA256: `ea46736bce82cc3e37ee98791ceb2b817738c239fe79104f9829c0e597400da5`
- Source: https://mediadive.dsmz.de/rest/solution/4927
- Source SHA256: 3f734df7f647a7e1e96d91e24a2b0678f7219a4c94f3dac73061c6b3fe295798
- Retrieved: 2026-10-07T09:49:01.604699+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Marine agar 2216 | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4927 | {<br>                "recipe_order": 1,<br>                "compound": "Marine agar 2216",<br>                "compound_id": 1628,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "see Medium No. 118",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1628) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | NaCl | {"unit": "G_PER_L", "value": "10"} | {"unit": "G_PER_L", "value": "10"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4927 | {<br>                "recipe_order": 2,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "g",<br>                "g_l": 10,<br>                "mmol_l": 171.116,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=43) | Provider explicitly reports g_l=10. Arithmetic check: 10 g * 1 g/g / (1000 ml / 1000 ml per L) = 10 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
