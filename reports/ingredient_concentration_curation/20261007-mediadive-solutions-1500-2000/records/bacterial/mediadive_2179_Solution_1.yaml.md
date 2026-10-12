# Solution Concentration Review: Solution 1

- Record: data/normalized_yaml/bacterial/mediadive_2179_Solution_1.yaml
- ID: CultureMech:011569
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b79c4808041cec34a349b0af8a3a0ee3e14c52903deb90d21af78603d5562202`
- Proposed/result SHA256: `0987384b3b1a616d7d3c4cce1e27384925a2fef9b5cbfc6e35481f2e56d6c0f5`
- Source: https://mediadive.dsmz.de/rest/solution/2179
- Source SHA256: 2fcdfb601d03df0466b2df6d788cf8486a615218c73baf69ca15d45cb80340de
- Retrieved: 2026-10-07T09:09:48.753929+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | PPLO broth | {"unit": "G_PER_L", "value": "21"} | {"unit": "G_PER_L", "value": "21"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2179 | {<br>                "recipe_order": 1,<br>                "compound": "PPLO broth",<br>                "compound_id": 953,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.68,<br>                "unit": "g",<br>                "g_l": 21,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=953) | Provider explicitly reports g_l=21. Arithmetic check: 1.68 g * 1 g/g / (80 ml / 1000 ml per L) = 21 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 80. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2179 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 80,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
