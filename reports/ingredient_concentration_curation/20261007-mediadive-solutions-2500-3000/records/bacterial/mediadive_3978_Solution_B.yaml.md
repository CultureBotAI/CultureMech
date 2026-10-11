# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_3978_Solution_B.yaml
- ID: CultureMech:013035
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7bb45f99cd6dea670cbb4c34e4526aa992d6498ef20ef6172c8fb0b96fb5c525`
- Proposed/result SHA256: `782f7207face5a00a35aa21057824f7f8d71d3ab323681fe2e22b0cf3bb623c7`
- Source: https://mediadive.dsmz.de/rest/solution/3978
- Source SHA256: 811e77b08a1affd443b96c2963237a69970cec3687ead6426e3223bb0cd0bca3
- Retrieved: 2026-10-07T09:27:06.373660+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sodium pyruvate | {"unit": "G_PER_L", "value": "22"} | {"unit": "G_PER_L", "value": "22"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3978 | {<br>                "recipe_order": 1,<br>                "compound": "Sodium pyruvate",<br>                "compound_id": 438,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.2,<br>                "unit": "g",<br>                "g_l": 22,<br>                "mmol_l": 199.927,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=438) | Provider explicitly reports g_l=22. Arithmetic check: 2.2 g * 1 g/g / (100 ml / 1000 ml per L) = 22 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3978 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
