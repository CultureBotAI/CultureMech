# Solution Concentration Review: Main sol. 605a

- Record: data/normalized_yaml/bacterial/mediadive_1301_Main_sol_605a.yaml
- ID: CultureMech:010792
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `acc02cafbe4e526445a6e411a583999c2f0307e52d10bb2ffa3e4957ab6ed91a`
- Proposed/result SHA256: `acc02cafbe4e526445a6e411a583999c2f0307e52d10bb2ffa3e4957ab6ed91a`
- Source: https://mediadive.dsmz.de/rest/solution/1301
- Source SHA256: 56e0a7f82fed56abc8e7224d3d4c90d4e10a7e77a18eccd49414f3a35cd6645d
- Retrieved: 2026-10-07T08:51:15.086030+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "0.45"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1301 | {<br>                "recipe_order": 2,<br>                "compound": "KH2PO4",<br>                "compound_id": 11,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.45,<br>                "unit": "g/l",<br>                "g_l": 0.45,<br>                "mmol_l": 3.30676,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=11) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Na2HPO4 x 12 H2O | {"unit": "G_PER_L", "value": "2.39"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1301 | {<br>                "recipe_order": 3,<br>                "compound": "Na2HPO4 x 12 H2O",<br>                "compound_id": 95,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.39,<br>                "unit": "g/l",<br>                "g_l": 2.39,<br>                "mmol_l": 16.8358,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=95) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 605 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1301 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 605",<br>                "solution_id": 1300,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
