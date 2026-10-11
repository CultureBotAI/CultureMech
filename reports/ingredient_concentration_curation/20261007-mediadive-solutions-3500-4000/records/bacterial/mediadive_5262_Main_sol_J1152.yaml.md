# Solution Concentration Review: Main sol. J1152

- Record: data/normalized_yaml/bacterial/mediadive_5262_Main_sol_J1152.yaml
- ID: CultureMech:014173
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a88ff2af7c0d7d4b99b49b21fbcc7c0f841aebd5d7369ca8aa84663001c31388`
- Proposed/result SHA256: `e915d489791056e52f7f9b589e31c26887433c8853e1f35befb6df134312f0b7`
- Source: https://mediadive.dsmz.de/rest/solution/5262
- Source SHA256: 2ed0aa3824a1435b0de62c654cfe081e2606cdcfe6e576028544b4b0674241ad
- Retrieved: 2026-10-07T09:52:52.118500+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Yeast extract-malt extract agar | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5262 | {<br>                "recipe_order": 1,<br>                "compound": "Yeast extract-malt extract agar",<br>                "compound_id": 1682,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "ISP-2) (see Medium No. 43",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1682) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | NaCl | {"unit": "G_PER_L", "value": "20"} | {"unit": "G_PER_L", "value": "20"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5262 | {<br>                "recipe_order": 2,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "g",<br>                "g_l": 20,<br>                "mmol_l": 342.231,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=43) | Provider explicitly reports g_l=20. Arithmetic check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) = 20 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
