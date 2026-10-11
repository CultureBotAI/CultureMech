# Solution Concentration Review: Solution F

- Record: data/normalized_yaml/bacterial/mediadive_649_Solution_F.yaml
- ID: CultureMech:015051
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1ea1fdcae4bf1ea5bdb075d57fb88e1629a68731a6ce304b171385ead181bc26`
- Proposed/result SHA256: `64ce9cb1fe53ee69eb6309d459f015db41f775d7a0cb4c8cf114fb375eab0a3b`
- Source: https://mediadive.dsmz.de/rest/solution/649
- Source SHA256: eed7fe28a5aff682491acfcfcea3691e563003f63285c7a3a39c369b3cc9dbbf
- Retrieved: 2026-10-07T08:25:35.474201+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2S x 9 H2O | {"unit": "G_PER_L", "value": "78"} | {"unit": "G_PER_L", "value": "78"} | evidence_only | https://mediadive.dsmz.de/rest/solution/649 | {<br>                "recipe_order": 1,<br>                "compound": "Na2S x 9 H2O",<br>                "compound_id": 54,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 78,<br>                "unit": "mg",<br>                "g_l": 78,<br>                "mmol_l": 324.754,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=54) | Provider explicitly reports g_l=78. Arithmetic check: 78 mg * 0.001 g/mg / (1 ml / 1000 ml per L) = 78 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.001"} | correct | https://mediadive.dsmz.de/rest/solution/649 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1 ml per prepared batch: 1 / 1000 = 0.001 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
