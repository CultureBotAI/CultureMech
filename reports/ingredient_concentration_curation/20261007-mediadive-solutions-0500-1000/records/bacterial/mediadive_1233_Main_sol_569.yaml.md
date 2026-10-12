# Solution Concentration Review: Main sol. 569

- Record: data/normalized_yaml/bacterial/mediadive_1233_Main_sol_569.yaml
- ID: CultureMech:010727
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `8313a8dddbc9fb0967ed386ea415ba37dba3dbe6728a8794b99b37c83c04ad08`
- Proposed/result SHA256: `8313a8dddbc9fb0967ed386ea415ba37dba3dbe6728a8794b99b37c83c04ad08`
- Source: https://mediadive.dsmz.de/rest/solution/1233
- Source SHA256: 4d26846c1c4477a9ee08b4036feecc795f6fb9041e80243944799f746da63991
- Retrieved: 2026-10-07T08:50:28.279759+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Methanol | {"unit": "G_PER_L", "value": "7.92"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1233 | {<br>                "recipe_order": 2,<br>                "compound": "Methanol",<br>                "compound_id": 226,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": 7.92,<br>                "mmol_l": 247.176,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=226) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 125 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1233 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 125",<br>                "solution_id": 223,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
