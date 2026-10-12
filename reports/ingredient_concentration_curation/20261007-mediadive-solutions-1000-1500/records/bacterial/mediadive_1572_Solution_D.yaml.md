# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_1572_Solution_D.yaml
- ID: CultureMech:011031
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `140909aab680bd486c7fb97d8935ad67747c88f740f5c47c201bceb37f8fe61f`
- Proposed/result SHA256: `836a503fadb5151e6237f475d3035a0105b3181f38278f80051446ab4a62ff50`
- Source: https://mediadive.dsmz.de/rest/solution/1572
- Source SHA256: be2c958ee3630b4fe778937cbc510f6dc44c7ead8f6c25c3bdd7f7a2f579656f
- Retrieved: 2026-10-07T08:54:08.884185+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "10"} | {"unit": "G_PER_L", "value": "10"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1572 | {<br>                "recipe_order": 1,<br>                "compound": "FeSO4 x 7 H2O",<br>                "compound_id": 12,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "mg",<br>                "g_l": 10,<br>                "mmol_l": 35.9693,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=12) | Provider explicitly reports g_l=10. Arithmetic check: 50 mg * 0.001 g/mg / (5 ml / 1000 ml per L) = 10 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 5. | applied |
| `composition[1].concentration` | H2SO4 | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1572 | {<br>                "recipe_order": 2,<br>                "compound": "H2SO4",<br>                "compound_id": 122,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.1 N",<br>                "amount": 5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=122) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
