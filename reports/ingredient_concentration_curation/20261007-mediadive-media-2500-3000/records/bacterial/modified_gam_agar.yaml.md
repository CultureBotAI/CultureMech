# Medium Concentration Review: MODIFIED GAM AGAR

- Record: data/normalized_yaml/bacterial/modified_gam_agar.yaml
- ID: CultureMech:003001
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `94fc34d2cfc860f413b89658c99daf97676848c45de08559771f30876a26ccbc`
- Proposed/result SHA256: `94fc34d2cfc860f413b89658c99daf97676848c45de08559771f30876a26ccbc`
- Source: https://mediadive.dsmz.de/rest/medium/J655
- Source SHA256: 00b89b3bc03d3d6c9731c0a710c34021dc00c2bb1196fff30e4a9e1302391256
- Retrieved: 2026-10-07T14:37:46.657855+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | GAM agar, modified (Nissui) | {"unit": "G_PER_L", "value": "56.7"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J655 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J655 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | GAM agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J655 | {<br>                        "recipe_order": 1,<br>                        "compound": "GAM agar",<br>                        "compound_id": 1843,<br>                        "condition": " modified",<br>                        "attribute": "Nissui",<br>                        "amount": 56.7,<br>                        "unit": "g",<br>                        "g_l": 56.7,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J655 | {<br>                        "recipe_order": 2,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
