# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_3602_Solution_B.yaml
- ID: CultureMech:012689
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1ef8ca222c948fc985fe09029aebc975cd94ae0f070cb0a015b2a3cf080fddc6`
- Proposed/result SHA256: `5ad65ae7c419a57330d8209fe08fc339a34ebfa331e65371c7bc87cde4465631`
- Source: https://mediadive.dsmz.de/rest/solution/3602
- Source SHA256: 966c31b2722a290499aaa57c694a23c26e26d90d3e63e15f2b98b2e949ffbd58
- Retrieved: 2026-10-07T09:22:54.345069+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "5.44"} | {"unit": "G_PER_L", "value": "5.44"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3602 | {<br>                "recipe_order": 1,<br>                "compound": "KH2PO4",<br>                "compound_id": 11,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5.44,<br>                "unit": "g",<br>                "g_l": 5.44,<br>                "mmol_l": 39.975,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=11) | Provider explicitly reports g_l=5.44. Arithmetic check: 5.44 g * 1 g/g / (1000 ml / 1000 ml per L) = 5.44 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Na2HPO4 | {"unit": "G_PER_L", "value": "5.69"} | {"unit": "G_PER_L", "value": "5.69"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3602 | {<br>                "recipe_order": 2,<br>                "compound": "Na2HPO4",<br>                "compound_id": 233,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5.69,<br>                "unit": "g",<br>                "g_l": 5.69,<br>                "mmol_l": 40.082,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=233) | Provider explicitly reports g_l=5.69. Arithmetic check: 5.69 g * 1 g/g / (1000 ml / 1000 ml per L) = 5.69 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
