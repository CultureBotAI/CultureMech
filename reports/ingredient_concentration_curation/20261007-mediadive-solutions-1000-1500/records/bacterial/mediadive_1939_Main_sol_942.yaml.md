# Solution Concentration Review: Main sol. 942

- Record: data/normalized_yaml/bacterial/mediadive_1939_Main_sol_942.yaml
- ID: CultureMech:011348
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `908616708a795694dcfdf3e1827bbc335ed47aaa42cf1472ef15717718d2db1e`
- Proposed/result SHA256: `908616708a795694dcfdf3e1827bbc335ed47aaa42cf1472ef15717718d2db1e`
- Source: https://mediadive.dsmz.de/rest/solution/1939
- Source SHA256: 96c6ef93200c26a8b2af888d1ae4d2a693a39c6a47c7d48d670dd7d1eba11521
- Retrieved: 2026-10-07T08:57:57.203285+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/1939 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `composition[1].concentration` | Agar | {"unit": "G_PER_L", "value": "15.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/1939 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/1939 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `source.recipe[0]` | CaCl2 x 2 H2O | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1939 | {<br>                "recipe_order": 1,<br>                "compound": "CaCl2 x 2 H2O",<br>                "compound_id": 7,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": 6.80203,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[1]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1939 | {<br>                "recipe_order": 2,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 15,<br>                "unit": "g",<br>                "g_l": 15,<br>                "mmol_l": 44.5991,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1939 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
