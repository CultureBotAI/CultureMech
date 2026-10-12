# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_448_Solution_C.yaml
- ID: CultureMech:013466
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1ebdd384faefdc97428828f61a9d7805d3f10c1d8f0d8152b190dc14e132ac02`
- Proposed/result SHA256: `d81fa0fe7baf2687699b8a5f39173208285b4a59e8b89fda390a6c930dc5d153`
- Source: https://mediadive.dsmz.de/rest/solution/448
- Source SHA256: c07f4a2742babdc27c50d6acb4991e3b5b9218891b947e8a7a771f2bd6db65d5
- Retrieved: 2026-10-07T08:23:34.865583+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na-butyrate | {"unit": "G_PER_L", "value": "170"} | {"unit": "G_PER_L", "value": "170"} | evidence_only | https://mediadive.dsmz.de/rest/solution/448 | {<br>                "recipe_order": 1,<br>                "compound": "Na-butyrate",<br>                "compound_id": 232,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.7,<br>                "unit": "g",<br>                "g_l": 170,<br>                "mmol_l": 1544.23,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=232) | Provider explicitly reports g_l=170. Arithmetic check: 1.7 g * 1 g/g / (10 ml / 1000 ml per L) = 1.7E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/448 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |

## Medium212 Source-Specific Follow-Up

The source-specific ingredient review is complete for this checkpoint: the guarded repair is applied locally. The [current follow-up](../../../20261009-synthrophomonas-family/applied-records/S448.md) contains every old/new claim, exact supporting snippet, source uncertainty and actual validation result. This earlier report remains historical context.
