# Solution Concentration Review: Solution G

- Record: data/normalized_yaml/bacterial/mediadive_2207_Solution_G.yaml
- ID: CultureMech:011598
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `fc6ad6fdf94996c29fe05b96c70ee8e3bb4a4e92ece192b77719c61f7d46d5de`
- Proposed/result SHA256: `6dcaab547da989058e92bfaddeea3a444214dd0af6e63e205ba771eba23304fb`
- Source: https://mediadive.dsmz.de/rest/solution/2207
- Source SHA256: e0e7f3a513d7145a67c3233d9f81fe6b391c3dab26bce2f6ddf524d73e1a62da
- Retrieved: 2026-10-07T09:10:08.298907+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2S x 9 H2O | {"unit": "G_PER_L", "value": "0.96"} | {"unit": "G_PER_L", "value": "0.96"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2207 | {<br>                "recipe_order": 1,<br>                "compound": "Na2S x 9 H2O",<br>                "compound_id": 54,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 9.6,<br>                "unit": "mg",<br>                "g_l": 0.96,<br>                "mmol_l": 3.99697,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=54) | Provider explicitly reports g_l=0.96. Arithmetic check: 9.6 mg * 0.001 g/mg / (10 ml / 1000 ml per L) = 0.96 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/2207 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
