# Solution Concentration Review: FeNa-EDTA

- Record: data/normalized_yaml/bacterial/mediadive_5695_FeNa-EDTA.yaml
- ID: CultureMech:014559
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e08838130942888b12a9e928f32f01c80bfda861a88cf894e2574fffdda15b94`
- Proposed/result SHA256: `f05c296661a775a39c72a885b3eb96afb8f2cd5c294903542cc13e2ba6d6dfc7`
- Source: https://mediadive.dsmz.de/rest/solution/5695
- Source SHA256: 4f6a0c72309fb2f2e9149eaf542240f98e5f934eccdbe1583a7ea029ff871a6a
- Retrieved: 2026-10-07T09:57:26.628399+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeNa-EDTA | {"unit": "G_PER_L", "value": "4.5"} | {"unit": "G_PER_L", "value": "4.5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5695 | {<br>                "recipe_order": 1,<br>                "compound": "FeNa-EDTA",<br>                "compound_id": 1230,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 4.5,<br>                "unit": "g",<br>                "g_l": 4.5,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1230) | Provider explicitly reports g_l=4.5. Arithmetic check: 4.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 4.5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5695 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
