# Medium Concentration Review: GAM BROTH WITH SODIUM PYRUVATE

- Record: data/normalized_yaml/bacterial/gam_broth_with_sodium_pyruvate.yaml
- ID: CultureMech:002478
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `94801ee5865f465f3b20ea5f0455ef6254717664d29ed0bf3cf9bf786079a4bd`
- Proposed/result SHA256: `94801ee5865f465f3b20ea5f0455ef6254717664d29ed0bf3cf9bf786079a4bd`
- Source: https://mediadive.dsmz.de/rest/medium/J1314
- Source SHA256: 2345df9c03c4d72624496566e9df42b07692f7b05f38a53cd903b030b18c152d
- Retrieved: 2026-10-07T15:22:19.208036+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | GAM broth (Nissui) | {"unit": "G_PER_L", "value": "59.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1314 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): GAM broth, GAM broth (Nissui) | unchanged |
| `ingredients[1].concentration` | Sodium pyruvate | {"unit": "G_PER_L", "value": "10.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1314 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): GAM broth, GAM broth (Nissui) | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1314 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): GAM broth, GAM broth (Nissui) | unchanged |
| `source.data.solutions[0].recipe[0]` | GAM broth | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1314 | {<br>                        "recipe_order": 1,<br>                        "compound": "GAM broth",<br>                        "compound_id": 1620,<br>                        "attribute": "Nissui",<br>                        "amount": 59,<br>                        "unit": "g",<br>                        "g_l": 59,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Sodium pyruvate | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1314 | {<br>                        "recipe_order": 2,<br>                        "compound": "Sodium pyruvate",<br>                        "compound_id": 438,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "mmol_l": 90.876,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1314 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1314 | {<br>                        "step": "Adjust pH to 7.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
