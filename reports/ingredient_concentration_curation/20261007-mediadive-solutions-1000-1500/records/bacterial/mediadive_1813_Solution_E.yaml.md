# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_1813_Solution_E.yaml
- ID: CultureMech:011240
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1326c74321b3ad71e8824ff5dec7460c83d4f871641e2f6afebdfcb9198e1803`
- Proposed/result SHA256: `fa7699f2391b6bd9d8218497de1118539143cb570819d794d166b73386bea4e6`
- Source: https://mediadive.dsmz.de/rest/solution/1813
- Source SHA256: 778fbcb417363750c2ca35266bc51d0df120d514c5e232e21026a5f4a5a123a2
- Retrieved: 2026-10-07T08:56:38.012300+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na-DL-lactate | {"unit": "G_PER_L", "value": "250"} | {"unit": "G_PER_L", "value": "250"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1813 | {<br>                "recipe_order": 1,<br>                "compound": "Na-DL-lactate",<br>                "compound_id": 111,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.5,<br>                "unit": "g",<br>                "g_l": 250,<br>                "mmol_l": 2230.95,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=111) | Provider explicitly reports g_l=250. Arithmetic check: 2.5 g * 1 g/g / (10 ml / 1000 ml per L) = 2.5E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/1813 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
