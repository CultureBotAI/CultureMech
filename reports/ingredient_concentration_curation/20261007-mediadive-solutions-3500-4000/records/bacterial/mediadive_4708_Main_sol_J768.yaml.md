# Solution Concentration Review: Main sol. J768

- Record: data/normalized_yaml/bacterial/mediadive_4708_Main_sol_J768.yaml
- ID: CultureMech:013660
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `df181e7a5899ef2e47e32073c8925ecccbe623a06df1601e3c4a7988ee0652d9`
- Proposed/result SHA256: `ef81a574c1d86d5f14a5660c3a6a481f2272c18d661f12ed94fed03159bc1538`
- Source: https://mediadive.dsmz.de/rest/solution/4708
- Source SHA256: e2d04bb7d8caa68555ef46eddff69b57c90751542377d829fa501ab6de9dd9f8
- Retrieved: 2026-10-07T09:46:40.981004+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Marine agar 2216 | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4708 | {<br>                "recipe_order": 1,<br>                "compound": "Marine agar 2216",<br>                "compound_id": 1628,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "see Medium No. 118",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1628) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Tween 20 | {"unit": "G_PER_L", "value": "10"} | {"unit": "G_PER_L", "value": "10"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4708 | {<br>                "recipe_order": 2,<br>                "compound": "Tween 20",<br>                "compound_id": 1891,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "g",<br>                "g_l": 10,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1891) | Provider explicitly reports g_l=10. Arithmetic check: 10 g * 1 g/g / (1000 ml / 1000 ml per L) = 10 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
