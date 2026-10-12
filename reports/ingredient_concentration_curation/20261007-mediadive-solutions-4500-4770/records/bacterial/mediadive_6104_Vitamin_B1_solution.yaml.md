# Solution Concentration Review: Vitamin B1 solution

- Record: data/normalized_yaml/bacterial/mediadive_6104_Vitamin_B1_solution.yaml
- ID: CultureMech:014806
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `67dc3a2cceb7922d7b6839b7bd6b88d706f56c505aa74e80d76ccc41ad02a647`
- Proposed/result SHA256: `67dc3a2cceb7922d7b6839b7bd6b88d706f56c505aa74e80d76ccc41ad02a647`
- Source: https://mediadive.dsmz.de/rest/solution/6104
- Source SHA256: 2484c0de3dd8312b345c8da0f938f0309136b694dd1e6e08f31fc81bd0291b9d
- Retrieved: 2026-10-07T10:00:06.433549+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Thiamine hydrochloride | {"unit": "G_PER_L", "value": "1.2"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6104 | {<br>                "recipe_order": 2,<br>                "compound": "Thiamine hydrochloride",<br>                "compound_id": 1147,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Vitamin B1",<br>                "amount": 0.12,<br>                "unit": "g",<br>                "g_l": 1.2,<br>                "mmol_l": 3.55766,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1147) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
