# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_2075_Solution_B.yaml
- ID: CultureMech:011475
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a92e3b8ed3585826ae955bcd1b66ab9f8af9bc2121f10d5fb4111d0bd2cc8a21`
- Proposed/result SHA256: `8f95d06cb5870db258e4fc5e647aac0f51e7672a24e5c215325d575bc8e12ac2`
- Source: https://mediadive.dsmz.de/rest/solution/2075
- Source SHA256: 7d59a348cc6924b6c39871096f6965ff6865d529838beca2db83821ee300a1d0
- Retrieved: 2026-10-07T09:08:41.828645+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaH2PO4 x 2 H2O | {"unit": "G_PER_L", "value": "2.8"} | {"unit": "G_PER_L", "value": "2.8"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2075 | {<br>                "recipe_order": 1,<br>                "compound": "NaH2PO4 x 2 H2O",<br>                "compound_id": 678,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.28,<br>                "unit": "g",<br>                "g_l": 2.8,<br>                "mmol_l": 23.3378,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=678) | Provider explicitly reports g_l=2.8. Arithmetic check: 0.28 g * 1 g/g / (100 ml / 1000 ml per L) = 2.8 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/2075 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
