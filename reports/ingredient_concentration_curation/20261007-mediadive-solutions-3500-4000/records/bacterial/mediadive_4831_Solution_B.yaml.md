# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_4831_Solution_B.yaml
- ID: CultureMech:013771
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c0ca991bb30c31f63746c1526f486a9c3989f810e37d7263ce737b576136069a`
- Proposed/result SHA256: `769a9bac5f989889577ebc54afac380597f94cc75e29d61aa846a43e79785542`
- Source: https://mediadive.dsmz.de/rest/solution/4831
- Source SHA256: 1a4d20edd74df32d49fd44207bd3e37f47f138625736a480ade8a0c26251ff2d
- Retrieved: 2026-10-07T09:48:00.845994+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "2.7"} | {"unit": "G_PER_L", "value": "2.7"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4831 | {<br>                "recipe_order": 1,<br>                "compound": "K2HPO4",<br>                "compound_id": 10,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.7,<br>                "unit": "g",<br>                "g_l": 2.7,<br>                "mmol_l": 15.5016,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=10) | Provider explicitly reports g_l=2.7. Arithmetic check: 2.7 g * 1 g/g / (1000 ml / 1000 ml per L) = 2.7 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4831 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
