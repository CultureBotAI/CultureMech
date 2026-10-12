# Solution Concentration Review: Mail sol. C100

- Record: data/normalized_yaml/bacterial/mediadive_6238_Mail_sol_C100.yaml
- ID: CultureMech:014929
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `779bd1184d0fd6f052789223d26d25285306e3da96bc27cfd5f90c87926c55e3`
- Proposed/result SHA256: `59bccd86efc5458ddc9856693ea4cd9909e1609e79cdd035a6ab215ac7b176ed`
- Source: https://mediadive.dsmz.de/rest/solution/6238
- Source SHA256: 34a7a50839b13fefe63daee2d2dfac28daf428b43bde341d36082fadccbb37ac
- Retrieved: 2026-10-07T10:01:35.543430+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Soil | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6238 | {<br>                "recipe_order": 2,<br>                "compound": "Soil",<br>                "compound_id": 2350,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "air-dried, sieved, garden loam",<br>                "amount": null,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2350) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | (NH4)MgPO4 | {"unit": "G_PER_L", "value": "0.01"} | {"unit": "G_PER_L", "value": "0.01"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6238 | {<br>                "recipe_order": 3,<br>                "compound": "(NH4)MgPO4",<br>                "compound_id": 2365,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.01,<br>                "unit": "g",<br>                "g_l": 0.01,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2365) | Provider explicitly reports g_l=0.01. Arithmetic check: 0.01 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.01 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
