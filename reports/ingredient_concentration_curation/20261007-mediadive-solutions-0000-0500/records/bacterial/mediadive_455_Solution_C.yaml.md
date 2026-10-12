# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_455_Solution_C.yaml
- ID: CultureMech:013527
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b8be31fd8eae8ede71833bd07ba708b57447bfbc73748a42d3ad2d05c8240de5`
- Proposed/result SHA256: `08796bb2c7d1b02d1a06dea81164fb394d2f02d106ff6229c790163e0c8da8d8`
- Source: https://mediadive.dsmz.de/rest/solution/455
- Source SHA256: 0c7482109a6c818d868df73e97df037951df3f152de424dec59ce21f9e85c2b7
- Retrieved: 2026-10-07T08:23:38.799987+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Starch | {"unit": "G_PER_L", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/455 | {<br>                "recipe_order": 1,<br>                "compound": "Starch",<br>                "compound_id": 199,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "soluble",<br>                "amount": 0.4,<br>                "unit": "g",<br>                "g_l": 100,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=199) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.004"} | correct | https://mediadive.dsmz.de/rest/solution/455 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 4,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 4 ml per prepared batch: 4 / 1000 = 0.004 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 4. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |

## Medium212 Source-Specific Follow-Up

The source-specific ingredient review is complete for this checkpoint: the guarded repair is applied locally. The [current follow-up](../../../20261009-synthrophomonas-family/applied-records/S455.md) contains every old/new claim, exact supporting snippet, source uncertainty and actual validation result. This earlier report remains historical context.
