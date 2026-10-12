# Solution Concentration Review: Solution F

- Record: data/normalized_yaml/bacterial/mediadive_677_Solution_F.yaml
- ID: CultureMech:015084
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `187746c5093b211ed4eed446832aa0af9e6a7b6f6ea830a7479a7cc66cd5fcb0`
- Proposed/result SHA256: `3cc8f290e80e45b215ec2e9c584a6e97ab4a868ece0779952f26deb999834d47`
- Source: https://mediadive.dsmz.de/rest/solution/677
- Source SHA256: 277f6a78c9f469d2bc800d7eea24cf680747504c0297e0ab2cc3313e81b67e46
- Retrieved: 2026-10-07T08:45:39.063497+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | L-Cysteine HCl x H2O | {"unit": "G_PER_L", "value": "30"} | {"unit": "G_PER_L", "value": "30"} | evidence_only | https://mediadive.dsmz.de/rest/solution/677 | {<br>                "recipe_order": 1,<br>                "compound": "L-Cysteine HCl x H2O",<br>                "compound_id": 770,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.3,<br>                "unit": "g",<br>                "g_l": 30,<br>                "mmol_l": 170.808,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=770) | Provider explicitly reports g_l=30. Arithmetic check: 0.3 g * 1 g/g / (10 ml / 1000 ml per L) = 3E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/677 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
