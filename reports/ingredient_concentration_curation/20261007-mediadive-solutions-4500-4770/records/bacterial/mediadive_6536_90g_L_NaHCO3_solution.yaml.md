# Solution Concentration Review: 90g/L NaHCO3 solution

- Record: data/normalized_yaml/bacterial/mediadive_6536_90g_L_NaHCO3_solution.yaml
- ID: CultureMech:015058
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `25f0fd40377fad9897e4b189e1e1c8aa779b9f648e2caa9000871b1373f59527`
- Proposed/result SHA256: `25f0fd40377fad9897e4b189e1e1c8aa779b9f648e2caa9000871b1373f59527`
- Source: https://mediadive.dsmz.de/rest/solution/6536
- Source SHA256: 5ae5d5e132ec324ec5ddf6df4cc6af9e6dc221e32db8a5a47f67f2673f6e37ef
- Retrieved: 2026-10-07T10:02:57.008223+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaHCO3 | {"unit": "G_PER_L", "value": "90"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6536 | {<br>                "recipe_order": 2,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 90,<br>                "unit": "g",<br>                "g_l": 90,<br>                "mmol_l": 1071.34,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=55) | Missing numeric input | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
