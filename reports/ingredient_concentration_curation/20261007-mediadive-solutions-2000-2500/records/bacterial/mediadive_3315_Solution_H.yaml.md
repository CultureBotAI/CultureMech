# Solution Concentration Review: Solution H

- Record: data/normalized_yaml/bacterial/mediadive_3315_Solution_H.yaml
- ID: CultureMech:012477
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b777b8fa11ab2bca145ac4cab0f53781d300f22783a045968365dc39cff6ee3a`
- Proposed/result SHA256: `fbea62ca7a3599188f4ab39103dd26566daf5afb2d76ee23515178254c8cdc05`
- Source: https://mediadive.dsmz.de/rest/solution/3315
- Source SHA256: bd3161b9fde8a045a5304dae957dfd5ffabfb28b17efe8b9f9bdf30b6abde5cf
- Retrieved: 2026-10-07T09:20:20.233730+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "4"} | {"unit": "G_PER_L", "value": "4"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3315 | {<br>                "recipe_order": 1,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.02,<br>                "unit": "g",<br>                "g_l": 4,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=16) | Provider explicitly reports g_l=4. Arithmetic check: 0.02 g * 1 g/g / (5 ml / 1000 ml per L) = 4 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 5. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.005"} | correct | https://mediadive.dsmz.de/rest/solution/3315 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 5 ml per prepared batch: 5 / 1000 = 0.005 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 5. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
