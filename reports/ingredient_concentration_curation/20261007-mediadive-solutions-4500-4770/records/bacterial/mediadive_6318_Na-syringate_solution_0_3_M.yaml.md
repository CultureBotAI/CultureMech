# Solution Concentration Review: Na-syringate solution (0.3 M)

- Record: data/normalized_yaml/bacterial/mediadive_6318_Na-syringate_solution_0_3_M.yaml
- ID: CultureMech:014983
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1561f8193e43e0c2bf302ac43c89266bfc909ac8bd9a3e78385399e6fb5749a9`
- Proposed/result SHA256: `1561f8193e43e0c2bf302ac43c89266bfc909ac8bd9a3e78385399e6fb5749a9`
- Source: https://mediadive.dsmz.de/rest/solution/6318
- Source SHA256: 78ee103c9285b0c3accab13d0685a1473e70a1212372d8eaf5e040baa20af9e0
- Retrieved: 2026-10-07T10:02:12.408290+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Syringic  acid | {"unit": "G_PER_L", "value": "60"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6318 | {<br>                "recipe_order": 1,<br>                "compound": "Syringic  acid",<br>                "compound_id": 2124,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "SIGMA S6881",<br>                "amount": 60,<br>                "unit": "g",<br>                "g_l": 60,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2124) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | NaOH | {"unit": "PERCENT_V_V", "value": "50"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6318 | {<br>                "recipe_order": 2,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "5 N",<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=256) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "950"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6318 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 950,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
