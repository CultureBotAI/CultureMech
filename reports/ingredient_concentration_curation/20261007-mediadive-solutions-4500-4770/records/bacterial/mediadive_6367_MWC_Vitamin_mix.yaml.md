# Solution Concentration Review: MWC Vitamin mix**

- Record: data/normalized_yaml/bacterial/mediadive_6367_MWC_Vitamin_mix.yaml
- ID: CultureMech:014998
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `70c1e258c1324852b0875f26c5954a3f55b18185e04196ad3d028cb528c373fb`
- Proposed/result SHA256: `70c1e258c1324852b0875f26c5954a3f55b18185e04196ad3d028cb528c373fb`
- Source: https://mediadive.dsmz.de/rest/solution/6367
- Source SHA256: 572ffcf8744e1d3280f558546cd96914e0fe6bd5084c25e93b782cd76c004614
- Retrieved: 2026-10-07T10:02:20.989260+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Thiamine HCl | {"unit": "G_PER_L", "value": "0.1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6367 | {<br>                "recipe_order": 1,<br>                "compound": "Thiamine HCl",<br>                "compound_id": 1207,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "10 g/l stock solution",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": 0.1,<br>                "mmol_l": 0.296472,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1207) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Biotin | {"unit": "PERCENT_V_V", "value": "1.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6367 | {<br>                "recipe_order": 2,<br>                "compound": "Biotin",<br>                "compound_id": 46,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.5 g/l stock solution",<br>                "amount": 0.1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=46) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Vitamin B12 | {"unit": "PERCENT_V_V", "value": "2.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6367 | {<br>                "recipe_order": 3,<br>                "compound": "Vitamin B12",<br>                "compound_id": 18,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.2 g/l stock solution",<br>                "amount": 0.25,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=18) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
