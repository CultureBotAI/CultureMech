# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_6292_Solution_E.yaml
- ID: CultureMech:014972
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `24c565c1bacab28ad921fb727fe016ff4caa1926518c06f03f241c96a8f2dfe6`
- Proposed/result SHA256: `bd20fda2e22c4865a4ce697dc42c493d554164e95f4e9de75373f45998991842`
- Source: https://mediadive.dsmz.de/rest/solution/6292
- Source SHA256: a0f8be6f126c978eaf7f3a2ac084b7f9690f82575f2171e5e6f7a91b04909961
- Retrieved: 2026-10-07T10:02:05.413160+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na-acetate | {"unit": "G_PER_L", "value": "80"} | {"unit": "G_PER_L", "value": "80"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6292 | {<br>                "recipe_order": 2,<br>                "compound": "Na-acetate",<br>                "compound_id": 23,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.16,<br>                "unit": "g",<br>                "g_l": 80,<br>                "mmol_l": 975.208,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=23) | Provider explicitly reports g_l=80. Arithmetic check: 0.16 g * 1 g/g / (2 ml / 1000 ml per L) = 8E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 2. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.002"} | correct | https://mediadive.dsmz.de/rest/solution/6292 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 2 ml per prepared batch: 2 / 1000 = 0.002 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 2. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
