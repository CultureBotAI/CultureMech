# Solution Concentration Review: Supplement 2

- Record: data/normalized_yaml/bacterial/mediadive_3081_Supplement_2.yaml
- ID: CultureMech:012306
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7b3e946ff9058e8229b48f3ff64c543928450c43d965c644de390016156f0903`
- Proposed/result SHA256: `7b3e946ff9058e8229b48f3ff64c543928450c43d965c644de390016156f0903`
- Source: https://mediadive.dsmz.de/rest/solution/3081
- Source SHA256: f2f8095ede979fb90b1e3b87b8c038998adb1b8d81bfe2f7dc7bf09528789456
- Retrieved: 2026-10-07T09:18:19.833753+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Ascorbic acid | {"unit": "G_PER_L", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3081 | {<br>                "recipe_order": 1,<br>                "compound": "Ascorbic acid",<br>                "compound_id": 112,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "%(w/v)",<br>                "g_l": 100,<br>                "mmol_l": 567.795,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=112) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3081 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
