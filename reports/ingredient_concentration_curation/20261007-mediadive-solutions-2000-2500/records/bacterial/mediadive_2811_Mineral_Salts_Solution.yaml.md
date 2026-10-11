# Solution Concentration Review: Mineral Salts Solution

- Record: data/normalized_yaml/bacterial/mediadive_2811_Mineral_Salts_Solution.yaml
- ID: CultureMech:012096
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `77ed5b95f4703afa7ac25025baca57fdfad28e62346284d99cd68f21371e4cd8`
- Proposed/result SHA256: `77ed5b95f4703afa7ac25025baca57fdfad28e62346284d99cd68f21371e4cd8`
- Source: https://mediadive.dsmz.de/rest/solution/2811
- Source SHA256: 77946f507c44ec4ba93f6ac57a1f54c48d214942fe96a541b36d8274a8291847
- Retrieved: 2026-10-07T09:15:53.442556+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | HEPES | {"unit": "G_PER_L", "value": "4.766"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2811 | {<br>                "recipe_order": 1,<br>                "compound": "HEPES",<br>                "compound_id": 371,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "20mM",<br>                "amount": 2.383,<br>                "unit": "g",<br>                "g_l": 4.766,<br>                "mmol_l": 20,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=371) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2811 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 500,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
