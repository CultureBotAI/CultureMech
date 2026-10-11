# Solution Concentration Review: Milk Medium

- Record: data/normalized_yaml/bacterial/mediadive_841_Milk_Medium.yaml
- ID: CultureMech:015207
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5f841265c6ef85a36adcc28d857068f179098453a7f6adff5a7b53bdd73255f9`
- Proposed/result SHA256: `5f841265c6ef85a36adcc28d857068f179098453a7f6adff5a7b53bdd73255f9`
- Source: https://mediadive.dsmz.de/rest/solution/841
- Source SHA256: f5b6d1f7743bc1c93c72e9c7c3c265a59ddde7f325d7a34f921087a33a7f4f5b
- Retrieved: 2026-10-07T08:47:02.511933+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Milk | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/841 | {<br>                "recipe_order": 1,<br>                "compound": "Milk",<br>                "compound_id": 467,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "fresh",<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=467) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Sodium resazurin | {"unit": "G_PER_L", "value": "0.0001"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/841 | {<br>                "recipe_order": 2,<br>                "compound": "Sodium resazurin",<br>                "compound_id": 1852,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.1% w/v",<br>                "amount": 0.1,<br>                "unit": "ml",<br>                "g_l": 0.0001,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1852) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
