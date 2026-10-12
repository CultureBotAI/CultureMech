# Solution Concentration Review: B-solution

- Record: data/normalized_yaml/bacterial/mediadive_5069_B-solution.yaml
- ID: CultureMech:013984
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c5f4d429bf620bda8f48e29bb71cd6bc79372fc26c1d2c19ab3de76257fd9dba`
- Proposed/result SHA256: `c5f4d429bf620bda8f48e29bb71cd6bc79372fc26c1d2c19ab3de76257fd9dba`
- Source: https://mediadive.dsmz.de/rest/solution/5069
- Source SHA256: 760feb962687ba77d9d2f383a86a5d51b6d1a23bd2f9c8d6498084b59718fcf4
- Retrieved: 2026-10-07T09:50:36.098342+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2HPO4 x 12 H2O | {"unit": "G_PER_L", "value": "55.51"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5069 | {<br>                "recipe_order": 1,<br>                "compound": "Na2HPO4 x 12 H2O",<br>                "compound_id": 95,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 55.51,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=95) | Missing numeric input | unchanged |
| `composition[1].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "12.93"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5069 | {<br>                "recipe_order": 2,<br>                "compound": "KH2PO4",<br>                "compound_id": 11,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 12.93,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=11) | Missing numeric input | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
