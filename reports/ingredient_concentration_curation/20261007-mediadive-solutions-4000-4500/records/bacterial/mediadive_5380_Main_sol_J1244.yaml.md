# Solution Concentration Review: Main sol. J1244

- Record: data/normalized_yaml/bacterial/mediadive_5380_Main_sol_J1244.yaml
- ID: CultureMech:014290
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a860eeb3b6fba5415169051b2f8120b670fa51094f42e92e3044ebe38fe99867`
- Proposed/result SHA256: `a860eeb3b6fba5415169051b2f8120b670fa51094f42e92e3044ebe38fe99867`
- Source: https://mediadive.dsmz.de/rest/solution/5380
- Source SHA256: aa14652a16252294831b966ebd11da8ce4a72738d430956297a5559b4141f914
- Retrieved: 2026-10-07T09:54:15.906798+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Marine broth 2216 | {"unit": "G_PER_L", "value": "37.0297"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5380 | {<br>                "recipe_order": 1,<br>                "compound": "Marine broth 2216",<br>                "compound_id": 1607,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 37.4,<br>                "unit": "g",<br>                "g_l": 37.0297,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1607) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "990.09900990099"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5380 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `composition[2].concentration` | Sodium pyruvate | {"unit": "PERCENT_V_V", "value": "9.900990099009901"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5380 | {<br>                "recipe_order": 3,<br>                "compound": "Sodium pyruvate",<br>                "compound_id": 438,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "1.0 M",<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=438) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
