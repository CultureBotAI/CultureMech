# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_1573_Solution_E.yaml
- ID: CultureMech:011032
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1458d7dddd121f6b7ebec0952dc809be702cf6974ed15a37d98e3b0c1a2c07b0`
- Proposed/result SHA256: `a2e4c7e5af1c630da98950866609d9f7215df74dc46b2757bf23bc1054350651`
- Source: https://mediadive.dsmz.de/rest/solution/1573
- Source SHA256: f5ffae48bd3684232235e5f9194a2ea75c9d6b25e051735ecdc46ce32959bd75
- Retrieved: 2026-10-07T08:54:09.690981+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Dithiothreitol | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1573 | {<br>                "recipe_order": 1,<br>                "compound": "Dithiothreitol",<br>                "compound_id": 574,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "DTT",<br>                "amount": 150,<br>                "unit": "mg",<br>                "g_l": 15,<br>                "mmol_l": 97.2132,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=574) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/1573 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
