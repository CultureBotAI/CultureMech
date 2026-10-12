# Solution Concentration Review: FeCl2 solution

Historical review, retained unchanged below apart from this follow-up notice.
The [current claim table](../../../20261008-fecl2-stock/record.md) supersedes
the old HCl decision and provides the resulting field locations and validation.

- Record: data/normalized_yaml/bacterial/mediadive_3846_FeCl2_solution.yaml
- ID: CultureMech:012919
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6219b9c95d62dd0eb32312430840b2a99b718db8bc11e5597a0be9492b7e71b8`
- Proposed/result SHA256: `79ad5df8a66ee42ca19a7150dfdb0a4539fec3b7cc71b7b767ba3889d20d762c`
- Source: https://mediadive.dsmz.de/rest/solution/3846
- Source SHA256: 3b17c2e79a0ef85051dc8c41ff95bb0361a83b12179a510184b61ef9edbb96f0
- Retrieved: 2026-10-07T09:25:43.288435+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | HCl | {"unit": "G_PER_L", "value": "2.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3846 | {<br>                "recipe_order": 1,<br>                "compound": "HCl",<br>                "compound_id": 68,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "7.7 M, 25%",<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": 2.5,<br>                "mmol_l": 68.5683,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=68) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | FeCl2 x 4 H2O | {"unit": "G_PER_L", "value": "1.5"} | {"unit": "G_PER_L", "value": "1.5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3846 | {<br>                "recipe_order": 2,<br>                "compound": "FeCl2 x 4 H2O",<br>                "compound_id": 260,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.5,<br>                "unit": "g",<br>                "g_l": 1.5,<br>                "mmol_l": 7.54482,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=260) | Provider explicitly reports g_l=1.5. Arithmetic check: 1.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "990"} | {"unit": "L", "value": "0.99"} | correct | https://mediadive.dsmz.de/rest/solution/3846 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 990,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Source water addition is 990 ml per prepared batch: 990 / 1000 = 0.99 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |

## Later Source-Backed Follow-Up

The [2026-10-08 FeCl2 stock review](../../../20261008-fecl2-stock/record.md)
supersedes this report's unresolved HCl row and records every current amount
slot. It separates reagent strength from batch dose and preserves the FeCl2 and
water quantities with their prior qualifications. The original review above is
retained as a historical snapshot; current source/result hashes and terminal
validation results are in the linked follow-up.
