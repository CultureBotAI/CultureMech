# Solution Concentration Review: Sodiumpyruvate (1 M)

- Record: data/normalized_yaml/bacterial/mediadive_6284_Sodiumpyruvate_1_M.yaml
- ID: CultureMech:014965
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1bc7b7cc1569423cc6bfcb700775240ef802f6f7548e9ad54940ec21e4218514`
- Proposed/result SHA256: `007b339d72f4b801bef4fc738a3eb997405facdbc853f580a35cd4bfed7c90a7`
- Source: https://mediadive.dsmz.de/rest/solution/6284
- Source SHA256: 799850bcbc7a06c308e8b2df50fa18dca038237a11e0c00dee880f978ba71231
- Retrieved: 2026-10-07T10:02:00.726925+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sodium pyruvate | {"unit": "G_PER_L", "value": "110"} | {"unit": "G_PER_L", "value": "110"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6284 | {<br>                "recipe_order": 2,<br>                "compound": "Sodium pyruvate",<br>                "compound_id": 438,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5.5,<br>                "unit": "g",<br>                "g_l": 110,<br>                "mmol_l": 999.636,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=438) | Provider explicitly reports g_l=110. Arithmetic check: 5.5 g * 1 g/g / (50 ml / 1000 ml per L) = 1.1E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Double distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6284 | {<br>                "recipe_order": 3,<br>                "compound": "Double distilled water",<br>                "compound_id": 1021,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1021) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
