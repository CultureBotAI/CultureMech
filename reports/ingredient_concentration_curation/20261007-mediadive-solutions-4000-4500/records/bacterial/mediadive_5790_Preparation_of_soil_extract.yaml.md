# Solution Concentration Review: Preparation of soil extract

- Record: data/normalized_yaml/bacterial/mediadive_5790_Preparation_of_soil_extract.yaml
- ID: CultureMech:014637
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `aec410de10201f0e1b06387a598c100440c91a766e0c78e8f401a7116ba6251d`
- Proposed/result SHA256: `aec410de10201f0e1b06387a598c100440c91a766e0c78e8f401a7116ba6251d`
- Source: https://mediadive.dsmz.de/rest/solution/5790
- Source SHA256: 07e5732aa2429d7498881a9b79eb4c75e41586d78af3256ea91e70d6dcb6cf95
- Retrieved: 2026-10-07T09:58:20.582042+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Garden soil | {"unit": "PERCENT_V_V", "value": "428.57142857142856"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5790 | {<br>                "recipe_order": 1,<br>                "compound": "Garden soil",<br>                "compound_id": 2159,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 300,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2159) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
