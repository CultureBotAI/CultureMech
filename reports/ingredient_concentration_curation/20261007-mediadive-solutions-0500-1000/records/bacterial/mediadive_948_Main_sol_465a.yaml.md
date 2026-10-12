# Solution Concentration Review: Main sol. 465a

- Record: data/normalized_yaml/bacterial/mediadive_948_Main_sol_465a.yaml
- ID: CultureMech:015288
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `63cc37f6175af836e05c2812afbc319bb965e234d7499aadaefde6c4f99a1e19`
- Proposed/result SHA256: `63cc37f6175af836e05c2812afbc319bb965e234d7499aadaefde6c4f99a1e19`
- Source: https://mediadive.dsmz.de/rest/solution/948
- Source SHA256: cbc1929e40911408782a501517ff29fa4d163dfa35c67540211826da52b453e7
- Retrieved: 2026-10-07T08:47:58.575684+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | [1,1′-Biphenyl]-2-ol | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/948 | {<br>                "recipe_order": 2,<br>                "compound": "[1,1\u2032-Biphenyl]-2-ol",<br>                "compound_id": 2114,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "dissolved in 50 g/l ethanol",<br>                "amount": 0.5,<br>                "unit": "g/l",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2114) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 465 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/948 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 465",<br>                "solution_id": 945,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
