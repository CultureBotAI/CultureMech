# Solution Concentration Review: Mail sol. C75

- Record: data/normalized_yaml/bacterial/mediadive_6066_Mail_sol_C75.yaml
- ID: CultureMech:014784
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `fadb599660c88f30e228bfd77dc482288ccc251125aba8f4b243099ae9b68030`
- Proposed/result SHA256: `fadb599660c88f30e228bfd77dc482288ccc251125aba8f4b243099ae9b68030`
- Source: https://mediadive.dsmz.de/rest/solution/6066
- Source SHA256: f4ba4a4a90c3c0961cd8180f157dcb6a979e0c7dd37e90b8c673f5efe06be4a6
- Retrieved: 2026-10-07T09:59:52.948873+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Complan | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6066 | {<br>                "recipe_order": 3,<br>                "compound": "Complan",<br>                "compound_id": 2363,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Heinz, UB4 8AL",<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2363) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | SES (Soil Extract with Added Salts) | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6066 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "SES (Soil Extract with Added Salts)",<br>                "solution_id": 6219,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
