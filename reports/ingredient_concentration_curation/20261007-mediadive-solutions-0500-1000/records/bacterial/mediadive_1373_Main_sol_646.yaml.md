# Solution Concentration Review: Main sol. 646

- Record: data/normalized_yaml/bacterial/mediadive_1373_Main_sol_646.yaml
- ID: CultureMech:010857
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f0dca2b08bd28289669009600d14f1966cdef4f29994718c869ba7e4c87f2b61`
- Proposed/result SHA256: `f0dca2b08bd28289669009600d14f1966cdef4f29994718c869ba7e4c87f2b61`
- Source: https://mediadive.dsmz.de/rest/solution/1373
- Source SHA256: 2fb8d263a45d73372886168ebf583e87450c23b8f42df7ebcd1c0541b8333705
- Retrieved: 2026-10-07T08:52:04.321959+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Blood Agar Base | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1373 | {<br>                "recipe_order": 2,<br>                "compound": "Blood Agar Base",<br>                "compound_id": 2130,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Difco 0045",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2130) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Rabbit blood | {"unit": "G_PER_L", "value": "50"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1373 | {<br>                "recipe_order": 3,<br>                "compound": "Rabbit blood",<br>                "compound_id": 1927,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "sterile, defibrinated",<br>                "amount": 5,<br>                "unit": "%",<br>                "g_l": 50,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1927) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
