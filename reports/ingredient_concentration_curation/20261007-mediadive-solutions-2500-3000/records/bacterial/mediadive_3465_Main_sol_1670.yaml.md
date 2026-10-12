# Solution Concentration Review: Main sol. 1670

- Record: data/normalized_yaml/bacterial/mediadive_3465_Main_sol_1670.yaml
- ID: CultureMech:012590
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `07e8012a527e2db8490eb8b1de649ef79020a7b595e8f1a3518d487f3a671e66`
- Proposed/result SHA256: `07e8012a527e2db8490eb8b1de649ef79020a7b595e8f1a3518d487f3a671e66`
- Source: https://mediadive.dsmz.de/rest/solution/3465
- Source SHA256: c743c5b01fd5c6d49d4f0e5ff41f95b2626224f3a87a830378e259de2ba21a36
- Retrieved: 2026-10-07T09:21:44.188567+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | L-15 (Leibovitz) medium | {"unit": "ML_PER_L", "value": "693.069307"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/3465 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `composition[1].concentration` | Tryptose phosphate broth | {"unit": "ML_PER_L", "value": "99.009901"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/3465 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `composition[2].concentration` | Foetal calf serum | {"unit": "ML_PER_L", "value": "198.019802"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/3465 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `solutions[0].concentration` | 200 mM L-glutamine stock | {"unit": "ML_PER_L", "value": "9.90099"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/3465 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `solutions[0].composition[0].concentration` | L-Glutamine | {"unit": "MILLIMOLAR", "value": "200.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/3465 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `source.recipe[3]` | L-Glutamine | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3465 | {<br>                "recipe_order": 4,<br>                "compound": "L-Glutamine",<br>                "compound_id": 134,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "200 mM",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": 0.029228,<br>                "mmol_l": 0.2,<br>                "optional": 0<br>            } | $.data.recipe[3] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
