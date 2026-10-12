# Solution Concentration Review: Folic acid solution

- Record: data/normalized_yaml/bacterial/mediadive_5545_Folic_acid_solution.yaml
- ID: CultureMech:014423
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2163165129d52084147937999ef3ec90ecb5335f223b6f335c5bcab0c68fb4e2`
- Proposed/result SHA256: `2163165129d52084147937999ef3ec90ecb5335f223b6f335c5bcab0c68fb4e2`
- Source: https://mediadive.dsmz.de/rest/solution/5545
- Source SHA256: 4bc44c5619692a18294ee2304d3178ce29893ee5a692b03d17859ca7a5408190
- Retrieved: 2026-10-07T09:55:50.428966+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Folic acid | {"unit": "G_PER_L", "value": "0.0013986"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/5545 | {<br>                "recipe_order": 1,<br>                "compound": "Folic acid",<br>                "compound_id": 138,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "mg",<br>                "g_l": 0.0013986,<br>                "mmol_l": 0.00316856,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=138) | Source g_l disagrees with amount/unit/volume | unchanged |
| `composition[1].concentration` | NaHCO3 | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5545 | {<br>                "recipe_order": 2,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "10 mM",<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=55) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
