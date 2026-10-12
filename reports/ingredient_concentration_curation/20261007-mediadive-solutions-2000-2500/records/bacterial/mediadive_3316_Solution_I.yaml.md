# Solution Concentration Review: Solution I

- Record: data/normalized_yaml/bacterial/mediadive_3316_Solution_I.yaml
- ID: CultureMech:012478
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2a06295f7d0371859384af2d3cecf22e3cc1b821fb92c6151661b3deef9be822`
- Proposed/result SHA256: `36f02f0909d3d971285852e5093fe587ca04fba070111b99764334b2a21fa796`
- Source: https://mediadive.dsmz.de/rest/solution/3316
- Source SHA256: fa81097b9585e0e9b7890f83357cb082c3cb25a2e601da2aadc2676cb7b3f328
- Retrieved: 2026-10-07T09:20:21.013049+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | 2-Mercaptoethanesulfonic acid | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3316 | {<br>                "recipe_order": 1,<br>                "compound": "2-Mercaptoethanesulfonic acid",<br>                "compound_id": 506,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "coenzyme M",<br>                "amount": 0.15,<br>                "unit": "g",<br>                "g_l": 15,<br>                "mmol_l": 105.485,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=506) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/3316 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
