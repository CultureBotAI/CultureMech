# Solution Concentration Review: Main sol. 138

- Record: data/normalized_yaml/bacterial/mediadive_237_Main_sol_138.yaml
- ID: CultureMech:011758
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c50caa9420cfacfa3363effd0220000a41ad6d99064f2a1d6b00814e75145f12`
- Proposed/result SHA256: `587f58a2f6a454b786e3630831c52675d31b6954fa00a93ea8266f0921cb9c11`
- Source: https://mediadive.dsmz.de/rest/solution/237
- Source SHA256: 39898235ce4e19aaff292cf72471dd7a3e2a53450d51c11ac49c81edb8914e7c
- Retrieved: 2026-10-07T08:21:39.312108+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "5"} | {"unit": "G_PER_L", "value": "5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/237 | {<br>                "recipe_order": 1,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 5,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=16) | Provider explicitly reports g_l=5. Arithmetic check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Hexachlorocyclo-hexane | {"unit": "G_PER_L", "value": "0.1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/237 | {<br>                "recipe_order": 2,<br>                "compound": "Hexachlorocyclo-hexane",<br>                "compound_id": 245,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Lindane",<br>                "amount": 0.1,<br>                "unit": "g",<br>                "g_l": 0.1,<br>                "mmol_l": 0.343846,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=245) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/237 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
