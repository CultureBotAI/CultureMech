# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_786_Solution_E.yaml
- ID: CultureMech:015162
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2941c6ef7c07541688ae3bafe5665286fb094042610356ddd7e22898cb0c1f7c`
- Proposed/result SHA256: `2941c6ef7c07541688ae3bafe5665286fb094042610356ddd7e22898cb0c1f7c`
- Source: https://mediadive.dsmz.de/rest/solution/786
- Source SHA256: 6e21ee974b51b6a7f98ce4160b7a158f052efe8fe405704e9561fb6120b8cba5
- Retrieved: 2026-10-07T08:46:31.698153+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2S2O5 | {"unit": "G_PER_L", "value": "95"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/786 | {<br>                "recipe_order": 1,<br>                "compound": "Na2S2O5",<br>                "compound_id": 440,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "sodium pyrosulfite",<br>                "amount": 0.95,<br>                "unit": "g",<br>                "g_l": 95,<br>                "mmol_l": 499.711,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=440) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/786 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
