# Solution Concentration Review: Solution I

- Record: data/normalized_yaml/bacterial/mediadive_461_Solution_I.yaml
- ID: CultureMech:013580
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `999ac1927e7c8348ff0841ab56fa3234e3e57ccd5fa71ced241fb0048de8b2d5`
- Proposed/result SHA256: `462473d812aecefa18b221faff094568ac39fcb4ef0debe10314c72ff47d3b0f`
- Source: https://mediadive.dsmz.de/rest/solution/461
- Source SHA256: 2f948988af8f4b1a0eb4c7e5ea95cd54f647818ff1762178c8a44725fce34442
- Retrieved: 2026-10-07T08:23:41.945571+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | DL-Dithiothreitol | {"unit": "G_PER_L", "value": "40"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/461 | {<br>                "recipe_order": 1,<br>                "compound": "DL-Dithiothreitol",<br>                "compound_id": 151,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "DTT",<br>                "amount": 0.4,<br>                "unit": "g",<br>                "g_l": 40,<br>                "mmol_l": 259.235,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=151) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/461 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |

## Medium212 Source-Specific Follow-Up

The source-specific ingredient review is complete for this checkpoint: the guarded repair is applied locally. The [current follow-up](../../../20261009-synthrophomonas-family/applied-records/S461.md) contains every old/new claim, exact supporting snippet, source uncertainty and actual validation result. This earlier report remains historical context.
