# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_4513_Solution_C.yaml
- ID: CultureMech:013484
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f61ead330141874116c9ad1ae5aae94fb40b9bc9075767959b03ce1f3663bfbd`
- Proposed/result SHA256: `f61ead330141874116c9ad1ae5aae94fb40b9bc9075767959b03ce1f3663bfbd`
- Source: https://mediadive.dsmz.de/rest/solution/4513
- Source SHA256: bc1187b97cc6018eaaad0d793b2e0e8a9e609adf096d34b89bbd9e820e984ea2
- Retrieved: 2026-10-07T09:44:31.426462+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Methanol | {"unit": "PERCENT_V_V", "value": "79.54545454545455"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4513 | {<br>                "recipe_order": 1,<br>                "compound": "Methanol",<br>                "compound_id": 226,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "50%",<br>                "amount": 3.5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=226) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | NaHCO3 | {"unit": "PERCENT_V_V", "value": "681.8181818181818"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4513 | {<br>                "recipe_order": 3,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "8%",<br>                "amount": 30,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=55) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[1]` | Trace vitamins | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4513 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Trace vitamins",<br>                "solution_id": 3861,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
