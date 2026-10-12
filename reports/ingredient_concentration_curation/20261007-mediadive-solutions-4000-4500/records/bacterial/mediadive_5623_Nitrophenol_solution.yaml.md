# Solution Concentration Review: Nitrophenol solution

- Record: data/normalized_yaml/bacterial/mediadive_5623_Nitrophenol_solution.yaml
- ID: CultureMech:014498
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6e184dbc6475cdec631677163336712e17a33c167a804431c0f1d9adb6a92645`
- Proposed/result SHA256: `c68ef5b01a92c9bacddc0bb643f297acfbbe22881f64e84c23859658829c8f3a`
- Source: https://mediadive.dsmz.de/rest/solution/5623
- Source SHA256: e5b60a2817268902f6f7498205c1764efdbaad7132ab12f005faac702516316e
- Retrieved: 2026-10-07T09:56:42.928809+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | 2-Nitrophenol | {"unit": "G_PER_L", "value": "0.5"} | {"unit": "G_PER_L", "value": "0.5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5623 | {<br>                "recipe_order": 1,<br>                "compound": "2-Nitrophenol",<br>                "compound_id": 2109,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.5,<br>                "unit": "g",<br>                "g_l": 0.5,<br>                "mmol_l": 3.59428,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2109) | Provider explicitly reports g_l=0.5. Arithmetic check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Phosphate buffer | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5623 | {<br>                "recipe_order": 2,<br>                "compound": "Phosphate buffer",<br>                "compound_id": 625,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "50 mM, pH 7.5",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": 50,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=625) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
