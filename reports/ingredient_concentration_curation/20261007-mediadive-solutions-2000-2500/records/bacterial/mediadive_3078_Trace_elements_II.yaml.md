# Solution Concentration Review: Trace elements II

- Record: data/normalized_yaml/bacterial/mediadive_3078_Trace_elements_II.yaml
- ID: CultureMech:012302
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a391ecfdb5272573b68320d42b57eef3f6e161a3e289e30ab94063d74520981b`
- Proposed/result SHA256: `2238616a4aa1a35801f604301e1959c8e0ea1d2f8d87decd0cce3192e922f551`
- Source: https://mediadive.dsmz.de/rest/solution/3078
- Source SHA256: 70a14172076dd3b22066c3f95bef654127bdb2bfe9d2d282187aa945d3c4a9d6
- Retrieved: 2026-10-07T09:18:17.492951+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2SeO3 | {"unit": "G_PER_L", "value": "1.73"} | {"unit": "G_PER_L", "value": "1.73"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3078 | {<br>                "recipe_order": 1,<br>                "compound": "Na2SeO3",<br>                "compound_id": 699,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 173,<br>                "unit": "mg",<br>                "g_l": 1.73,<br>                "mmol_l": 10.0036,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=699) | Provider explicitly reports g_l=1.73. Arithmetic check: 173 mg * 0.001 g/mg / (100 ml / 1000 ml per L) = 1.73 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | HCl | {"unit": "G_PER_L", "value": "0.03646"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3078 | {<br>                "recipe_order": 2,<br>                "compound": "HCl",<br>                "compound_id": 68,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "10mM",<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": 0.03646,<br>                "mmol_l": 1,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=68) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
