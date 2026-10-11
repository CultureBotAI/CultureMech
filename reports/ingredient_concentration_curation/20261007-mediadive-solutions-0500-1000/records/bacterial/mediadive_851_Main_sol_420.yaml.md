# Solution Concentration Review: Main sol. 420

- Record: data/normalized_yaml/bacterial/mediadive_851_Main_sol_420.yaml
- ID: CultureMech:015213
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `667ec3a0238dc584627dbef9e2c535c0b3adedd6135fda9ec4946797ec10e5ff`
- Proposed/result SHA256: `667ec3a0238dc584627dbef9e2c535c0b3adedd6135fda9ec4946797ec10e5ff`
- Source: https://mediadive.dsmz.de/rest/solution/851
- Source SHA256: 9d53f7c92e26bc3f6324e75bc60b4becc1dbe16e3534308c135a19da5aa8f44f
- Retrieved: 2026-10-07T08:47:06.497380+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Blood agar No 2 | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/851 | {<br>                "recipe_order": 1,<br>                "compound": "Blood agar No 2",<br>                "compound_id": 2111,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2111) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Horse blood | {"unit": "PERCENT_V_V", "value": "40"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/851 | {<br>                "recipe_order": 2,<br>                "compound": "Horse blood",<br>                "compound_id": 724,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 40,<br>                "unit": "ml/l",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=724) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
