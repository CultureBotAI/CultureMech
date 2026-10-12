# Solution Concentration Review: Solution A

- Record: data/normalized_yaml/bacterial/mediadive_3297_Solution_A.yaml
- ID: CultureMech:012464
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `97742712d4467070653f2a5dea00a46e55423bc626281f97c7902940e5330f8c`
- Proposed/result SHA256: `97742712d4467070653f2a5dea00a46e55423bc626281f97c7902940e5330f8c`
- Source: https://mediadive.dsmz.de/rest/solution/3297
- Source SHA256: 14224a628ad26449a23b16916fc8129aeebd19640374858a1e40b23d66e98310
- Retrieved: 2026-10-07T09:20:10.858170+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2CO3 | {"unit": "G_PER_L", "value": "95"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/3297 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `composition[1].concentration` | NaHCO3 | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/3297 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `composition[2].concentration` | NaCl | {"unit": "G_PER_L", "value": "5.33333"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/3297 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `composition[3].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/3297 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `composition[4].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/3297 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/3297 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `source.recipe[4]` | KCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3297 | {<br>                "recipe_order": 5,<br>                "compound": "KCl",<br>                "compound_id": 61,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.25,<br>                "unit": "g",<br>                "g_l": 0.333333,<br>                "mmol_l": 4.47127,<br>                "optional": 0<br>            } | $.data.recipe[4] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
