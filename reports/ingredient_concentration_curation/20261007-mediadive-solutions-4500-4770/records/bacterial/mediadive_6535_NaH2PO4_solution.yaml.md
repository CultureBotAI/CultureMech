# Solution Concentration Review: NaH2PO4 solution

- Record: data/normalized_yaml/bacterial/mediadive_6535_NaH2PO4_solution.yaml
- ID: CultureMech:015057
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `cce9dc30e37d7d7372437f21f9018665ca269c50c9ddcb250b7b23c4b4aab6f7`
- Proposed/result SHA256: `cce9dc30e37d7d7372437f21f9018665ca269c50c9ddcb250b7b23c4b4aab6f7`
- Source: https://mediadive.dsmz.de/rest/solution/6535
- Source SHA256: d08ba16cf562afc180568e1af9880715650a88bae1126d43016734d8e6a57a3e
- Retrieved: 2026-10-07T10:02:56.230883+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaH2PO4 | {"unit": "G_PER_L", "value": "80"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6535 | {<br>                "recipe_order": 2,<br>                "compound": "NaH2PO4",<br>                "compound_id": 229,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "",<br>                "amount": 80,<br>                "unit": "g",<br>                "g_l": 80,<br>                "mmol_l": 666.794,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=229) | Missing numeric input | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
