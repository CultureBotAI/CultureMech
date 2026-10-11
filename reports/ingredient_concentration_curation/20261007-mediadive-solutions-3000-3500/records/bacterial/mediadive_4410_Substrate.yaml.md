# Solution Concentration Review: Substrate

- Record: data/normalized_yaml/bacterial/mediadive_4410_Substrate.yaml
- ID: CultureMech:013398
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e7be87468451c197c7a279788c1bec9e3321670253c75bc162ded9b7f6128a6b`
- Proposed/result SHA256: `e7be87468451c197c7a279788c1bec9e3321670253c75bc162ded9b7f6128a6b`
- Source: https://mediadive.dsmz.de/rest/solution/4410
- Source SHA256: 385fabd200ad8b1874266d66e249fd200ea66fc02632e57ea614cbfd2b4f4e3b
- Retrieved: 2026-10-07T09:43:29.726377+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sodium palmitate | {"unit": "G_PER_L", "value": "2.8"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4410 | {<br>                "recipe_order": 1,<br>                "compound": "Sodium palmitate",<br>                "compound_id": 1813,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.8,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1813) | Missing numeric input | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
