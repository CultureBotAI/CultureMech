# Solution Concentration Review: Solution 5

- Record: data/normalized_yaml/bacterial/mediadive_5183_Solution_5.yaml
- ID: CultureMech:014093
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `26c26dfaa7da40aeb2ced2d0ea0e0cfe76aec7cccbe0661ed17b1674e163f29a`
- Proposed/result SHA256: `b8b04c9d3b883dc4f3a2ed9f821d62b8ed4216c23662f356ec2c1033dfe1e4b5`
- Source: https://mediadive.dsmz.de/rest/solution/5183
- Source SHA256: 5ae97e67d143abdd5c14fa8d3b79c5e3727319480c5d4a4b77bf38d58ec4a330
- Retrieved: 2026-10-07T09:51:54.411277+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Bacto peptone | {"unit": "G_PER_L", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5183 | {<br>                "recipe_order": 1,<br>                "compound": "Bacto peptone",<br>                "compound_id": 19,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 10,<br>                "unit": "g",<br>                "g_l": 100,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=19) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/5183 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
