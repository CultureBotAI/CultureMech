# Solution Concentration Review: Solution II

- Record: data/normalized_yaml/bacterial/mediadive_3857_Solution_II.yaml
- ID: CultureMech:012930
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `03c11afa07cc6b5d5783b6184537fb423147974aace5ed59f69c7dff8d1c7ea9`
- Proposed/result SHA256: `03c11afa07cc6b5d5783b6184537fb423147974aace5ed59f69c7dff8d1c7ea9`
- Source: https://mediadive.dsmz.de/rest/solution/3857
- Source SHA256: 02a1e019e2ad6d626589e3bfe7fdb0e01f45094f3bd01bdb2b091d240cf58b7a
- Retrieved: 2026-10-07T09:25:51.077860+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Potassium phosphate buffer | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3857 | {<br>                "recipe_order": 1,<br>                "compound": "Potassium phosphate buffer",<br>                "compound_id": 275,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "pH 7.8, 20 mM",<br>                "amount": 500,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=275) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
