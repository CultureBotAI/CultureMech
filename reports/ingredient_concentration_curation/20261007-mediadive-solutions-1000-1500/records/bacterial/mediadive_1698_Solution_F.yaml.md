# Solution Concentration Review: Solution F

- Record: data/normalized_yaml/bacterial/mediadive_1698_Solution_F.yaml
- ID: CultureMech:011151
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `dc2ee1a1296ad0e386326afabbdfc6703796cb8a9ac9389f91120460aaddb930`
- Proposed/result SHA256: `8419c74570dfc95546c391cb98a104550d6a92f57739dc88a650307bfa8f3899`
- Source: https://mediadive.dsmz.de/rest/solution/1698
- Source SHA256: 343eafcc3a057da917632cacc2030a184bd496452ba388c5196730561ae5ca47
- Retrieved: 2026-10-07T08:55:36.765227+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2-fumarate | {"unit": "G_PER_L", "value": "160"} | {"unit": "G_PER_L", "value": "160"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1698 | {<br>                "recipe_order": 1,<br>                "compound": "Na2-fumarate",<br>                "compound_id": 276,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 6.4,<br>                "unit": "g",<br>                "g_l": 160,<br>                "mmol_l": 999.775,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=276) | Provider explicitly reports g_l=160. Arithmetic check: 6.4 g * 1 g/g / (40 ml / 1000 ml per L) = 1.6E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 40. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.04"} | correct | https://mediadive.dsmz.de/rest/solution/1698 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 40,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 40 ml per prepared batch: 40 / 1000 = 0.04 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 40. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
