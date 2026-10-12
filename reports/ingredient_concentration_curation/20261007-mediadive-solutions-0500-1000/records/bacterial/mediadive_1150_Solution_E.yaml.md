# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_1150_Solution_E.yaml
- ID: CultureMech:010645
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ce15f2bd5029dfa9869d1d847289e2e15da811744d49b6e969148fdb3ee4282d`
- Proposed/result SHA256: `ce15f2bd5029dfa9869d1d847289e2e15da811744d49b6e969148fdb3ee4282d`
- Source: https://mediadive.dsmz.de/rest/solution/1150
- Source SHA256: a676c4bc178af495ad0c4a8501c8c69fdaa7bdfd78e3ff2833ef463ad7e1068f
- Retrieved: 2026-10-07T08:49:27.600430+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Vitamin B12 | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1150 | {<br>                "recipe_order": 1,<br>                "compound": "Vitamin B12",<br>                "compound_id": 18,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "50 \u00b5g/ml",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=18) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
