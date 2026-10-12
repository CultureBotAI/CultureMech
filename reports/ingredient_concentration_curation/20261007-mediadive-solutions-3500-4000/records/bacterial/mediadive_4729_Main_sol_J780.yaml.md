# Solution Concentration Review: Main sol. J780

- Record: data/normalized_yaml/bacterial/mediadive_4729_Main_sol_J780.yaml
- ID: CultureMech:013678
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3a03f9a61e0a91dc651bc1b919b6c82efdf3e4688b95102ed1f4ab684b5f9440`
- Proposed/result SHA256: `3a03f9a61e0a91dc651bc1b919b6c82efdf3e4688b95102ed1f4ab684b5f9440`
- Source: https://mediadive.dsmz.de/rest/solution/4729
- Source SHA256: 35519c89a152a94270157f809ae03845fd49d36147aca9454b3c67ec3ee3ad3a
- Retrieved: 2026-10-07T09:46:53.550590+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NH4Cl | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4729 | {<br>                "recipe_order": 1,<br>                "compound": "NH4Cl",<br>                "compound_id": 42,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=42) | Missing numeric input | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
