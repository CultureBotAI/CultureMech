# Solution Concentration Review: Lipoic acid solution

- Record: data/normalized_yaml/bacterial/mediadive_5550_Lipoic_acid_solution.yaml
- ID: CultureMech:014429
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `77b8e85dcba09b6b3e0d0147086429af869ad44cb45a1e19413e05f4e51087f7`
- Proposed/result SHA256: `77b8e85dcba09b6b3e0d0147086429af869ad44cb45a1e19413e05f4e51087f7`
- Source: https://mediadive.dsmz.de/rest/solution/5550
- Source SHA256: 538bd48c6a5677c9c6f29ccc9613a813e61eb5cea816f30750eb2480069e0fe6
- Retrieved: 2026-10-07T09:55:54.326327+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Lipoic acid | {"unit": "G_PER_L", "value": "0.00559441"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/5550 | {<br>                "recipe_order": 1,<br>                "compound": "Lipoic acid",<br>                "compound_id": 368,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "mg",<br>                "g_l": 0.00559441,<br>                "mmol_l": 0.0271178,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=368) | Source g_l disagrees with amount/unit/volume | unchanged |
| `composition[1].concentration` | NaOH | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5550 | {<br>                "recipe_order": 2,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "1 mM",<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=256) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
