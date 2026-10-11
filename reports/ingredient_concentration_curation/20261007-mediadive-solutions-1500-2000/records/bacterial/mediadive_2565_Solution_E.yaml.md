# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_2565_Solution_E.yaml
- ID: CultureMech:011906
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5198e8006cc297bf9da38e96244a2fa37acc83caf475e8bba264801b97424204`
- Proposed/result SHA256: `a34732210539a375a9dda480264ed97f67cc6f1e5d2f8a202653451f59ecbc64`
- Source: https://mediadive.dsmz.de/rest/solution/2565
- Source SHA256: efa5021b522527472ae1535b54a2b9cc07df3f26c3a85a2fc7dc25b8b0cec80b
- Retrieved: 2026-10-07T09:13:41.524968+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | 2-Mercaptoethanesulfonate | {"unit": "G_PER_L", "value": "7"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2565 | {<br>                "recipe_order": 1,<br>                "compound": "2-Mercaptoethanesulfonate",<br>                "compound_id": 227,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "coenzyme M",<br>                "amount": 0.07,<br>                "unit": "g",<br>                "g_l": 7,<br>                "mmol_l": 49.2264,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=227) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/2565 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
