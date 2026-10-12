# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_77_Solution_C.yaml
- ID: CultureMech:015158
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c357f5b2cf85257bf8e8ccb4c91578749d549f4af64987163b8fe85204e308ee`
- Proposed/result SHA256: `27e9f676188f050caf913b1901f1cb74b3074011ea33ada1d63036bdc19ee79e`
- Source: https://mediadive.dsmz.de/rest/solution/77
- Source SHA256: d33cfc881c2c05a2e6b89e246cd20e5dbb1306ef128e0804759e83644a1a504e
- Retrieved: 2026-10-07T08:20:02.974275+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Fructose | {"unit": "G_PER_L", "value": "25"} | {"unit": "G_PER_L", "value": "25"} | evidence_only | https://mediadive.dsmz.de/rest/solution/77 | {<br>                "recipe_order": 1,<br>                "compound": "Fructose",<br>                "compound_id": 98,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 25,<br>                "mmol_l": 138.766,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=98) | Provider explicitly reports g_l=25. Arithmetic check: 5 g * 1 g/g / (200 ml / 1000 ml per L) = 25 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 200. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.2"} | correct | https://mediadive.dsmz.de/rest/solution/77 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 200,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 200 ml per prepared batch: 200 / 1000 = 0.2 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 200. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
