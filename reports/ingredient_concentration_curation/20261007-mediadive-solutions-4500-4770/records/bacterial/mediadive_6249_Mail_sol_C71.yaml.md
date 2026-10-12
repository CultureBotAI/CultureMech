# Solution Concentration Review: Mail sol. C71

- Record: data/normalized_yaml/bacterial/mediadive_6249_Mail_sol_C71.yaml
- ID: CultureMech:014941
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `38986fe7d6bb65c273e53c2e79518a56e1f5f5fb0ad457d2ad3307728d9ed0c0`
- Proposed/result SHA256: `38986fe7d6bb65c273e53c2e79518a56e1f5f5fb0ad457d2ad3307728d9ed0c0`
- Source: https://mediadive.dsmz.de/rest/solution/6249
- Source SHA256: aec8b7b4e323b0187aaeff7901773b3e5b13cfd52cd66983f1ef845d425125a5
- Retrieved: 2026-10-07T10:01:44.138236+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Natural sea water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6249 | {<br>                "recipe_order": 2,<br>                "compound": "Natural sea water",<br>                "compound_id": 2152,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "filtered",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2152) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
