# Solution Concentration Review: Mail sol. C58

- Record: data/normalized_yaml/bacterial/mediadive_6049_Mail_sol_C58.yaml
- ID: CultureMech:014774
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `8c46d88861e62b5a1a0c62e97b18157bea2eae5dc048d077a4364ff17e46856c`
- Proposed/result SHA256: `8c46d88861e62b5a1a0c62e97b18157bea2eae5dc048d077a4364ff17e46856c`
- Source: https://mediadive.dsmz.de/rest/solution/6049
- Source SHA256: 4ae3154ed6dc455ca4079eaf93985789448e980e9486ad706f4c96010f3e51da
- Retrieved: 2026-10-07T09:59:46.734505+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Mineral water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6049 | {<br>                "recipe_order": 2,<br>                "compound": "Mineral water",<br>                "compound_id": 2359,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2359) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
