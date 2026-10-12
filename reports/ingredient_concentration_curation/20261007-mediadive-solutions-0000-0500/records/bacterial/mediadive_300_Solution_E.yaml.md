# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_300_Solution_E.yaml
- ID: CultureMech:012240
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d62fe5054a31bb9a65f9a248b3a3e0f043855af3b4c054620976a2648cdda6cb`
- Proposed/result SHA256: `65298dcfbd553fe63f21bbe87466733b6b9e022f8914fe9d7d6bc9559327cdcf`
- Source: https://mediadive.dsmz.de/rest/solution/300
- Source SHA256: d9ce3661fb5a7613679a2d0f7b194224df5f9c21148064771469ca07b561b72b
- Retrieved: 2026-10-07T08:22:20.699327+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | DL-Dithiothreitol | {"unit": "G_PER_L", "value": "15"} | {"unit": "G_PER_L", "value": "15"} | evidence_only | https://mediadive.dsmz.de/rest/solution/300 | {<br>                "recipe_order": 1,<br>                "compound": "DL-Dithiothreitol",<br>                "compound_id": 151,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.15,<br>                "unit": "g",<br>                "g_l": 15,<br>                "mmol_l": 97.2132,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=151) | Provider explicitly reports g_l=15. Arithmetic check: 0.15 g * 1 g/g / (10 ml / 1000 ml per L) = 15 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/300 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
