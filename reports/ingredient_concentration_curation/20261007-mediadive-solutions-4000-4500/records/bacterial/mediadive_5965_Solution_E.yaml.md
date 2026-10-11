# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_5965_Solution_E.yaml
- ID: CultureMech:014717
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e7de5d73d62cfb427df9cb13f3f585a3801409bcf58e6e455ebc72e706631030`
- Proposed/result SHA256: `33593c5ee602b0a42038c3164f8115159243e011c7d8490efaddad7cf94a91b2`
- Source: https://mediadive.dsmz.de/rest/solution/5965
- Source SHA256: 9c932c8abbcccc255e92155c4890e324f13c6f84bb0222ac5d931dae8578a996
- Retrieved: 2026-10-07T09:59:08.462911+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sodium perchlorate | {"unit": "G_PER_L", "value": "122"} | {"unit": "G_PER_L", "value": "122"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5965 | {<br>                "recipe_order": 2,<br>                "compound": "Sodium perchlorate",<br>                "compound_id": 2064,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.22,<br>                "unit": "g",<br>                "g_l": 122,<br>                "mmol_l": 996.406,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2064) | Provider explicitly reports g_l=122. Arithmetic check: 1.22 g * 1 g/g / (10 ml / 1000 ml per L) = 122 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/5965 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
