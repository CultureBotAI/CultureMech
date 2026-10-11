# Solution Concentration Review: Main sol. 1619

- Record: data/normalized_yaml/bacterial/mediadive_3366_Main_sol_1619.yaml
- ID: CultureMech:012514
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `168dbd4d6a1c6ceddafe10e29cdd1bb5e5422a2c073c8ff7a5d16088016e5cae`
- Proposed/result SHA256: `8269ec718b1999561ac7de8b2b94f9482b29548c133d27d2cfdcdda3d144bb8a`
- Source: https://mediadive.dsmz.de/rest/solution/3366
- Source SHA256: db6a3511a922a8b5c277f64191d2dc932ea009ff3a12d807c225a2ad673bb0bd
- Retrieved: 2026-10-07T09:20:49.300081+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | ISP 7 Medium | {"unit": "G_PER_L", "value": "23.74"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3366 | {<br>                "recipe_order": 1,<br>                "compound": "ISP 7 Medium",<br>                "compound_id": 1467,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Himedia",<br>                "amount": 23.74,<br>                "unit": "g",<br>                "g_l": 23.74,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1467) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Glycerol | {"unit": "PERCENT_V_V", "value": "15"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3366 | {<br>                "recipe_order": 2,<br>                "compound": "Glycerol",<br>                "compound_id": 72,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 15,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=72) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/3366 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
