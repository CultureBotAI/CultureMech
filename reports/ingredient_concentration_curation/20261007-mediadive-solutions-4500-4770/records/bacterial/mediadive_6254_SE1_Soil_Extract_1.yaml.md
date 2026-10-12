# Solution Concentration Review: SE1 (Soil Extract 1)

- Record: data/normalized_yaml/bacterial/mediadive_6254_SE1_Soil_Extract_1.yaml
- ID: CultureMech:014947
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ee4c8f60448922e4b834b2429e9311ef2cdeb09778fe498b4b99570b464c62fd`
- Proposed/result SHA256: `ee4c8f60448922e4b834b2429e9311ef2cdeb09778fe498b4b99570b464c62fd`
- Source: https://mediadive.dsmz.de/rest/solution/6254
- Source SHA256: 5e8bc6603818cc2f1c192b716f2c30a1cfdd6e5123f4ce2daf3a25d89d9284ae
- Retrieved: 2026-10-07T10:01:48.066108+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Soil | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6254 | {<br>                "recipe_order": 2,<br>                "compound": "Soil",<br>                "compound_id": 2350,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "air-dried",<br>                "amount": null,<br>                "unit": null,<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2350) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6254 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": null,<br>                "unit": null,<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Missing numeric input | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
