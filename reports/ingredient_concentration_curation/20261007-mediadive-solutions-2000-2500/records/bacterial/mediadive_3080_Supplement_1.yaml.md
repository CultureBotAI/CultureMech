# Solution Concentration Review: Supplement 1

- Record: data/normalized_yaml/bacterial/mediadive_3080_Supplement_1.yaml
- ID: CultureMech:012305
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `aec028bb6062926b1b8c8069e604ceec4501099a2b81190015544528dff6de7e`
- Proposed/result SHA256: `aec028bb6062926b1b8c8069e604ceec4501099a2b81190015544528dff6de7e`
- Source: https://mediadive.dsmz.de/rest/solution/3080
- Source SHA256: 83b4cb9b7cb5c1b591393182e452f959b030b52b712fe2bf2f701ba36cc1fc6b
- Retrieved: 2026-10-07T09:18:19.049092+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Fe SO4 x 7 H2O | {"unit": "G_PER_L", "value": "2.78015"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3080 | {<br>                "recipe_order": 1,<br>                "compound": "Fe SO4 x 7 H2O",<br>                "compound_id": 1418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "mM",<br>                "g_l": 2.78015,<br>                "mmol_l": 10,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | HCl | {"unit": "G_PER_L", "value": "0.3646"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3080 | {<br>                "recipe_order": 2,<br>                "compound": "HCl",<br>                "compound_id": 68,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "mM",<br>                "g_l": 0.3646,<br>                "mmol_l": 10,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=68) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
