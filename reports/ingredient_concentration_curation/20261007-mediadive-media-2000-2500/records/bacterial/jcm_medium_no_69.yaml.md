# Medium Concentration Review: JCM MEDIUM No. 69

- Record: data/normalized_yaml/bacterial/jcm_medium_no_69.yaml
- ID: CultureMech:003045
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9562826ca29966e2bc5814ab761edc1c42cec9de8d168d1750087015a3fef644`
- Proposed/result SHA256: `9562826ca29966e2bc5814ab761edc1c42cec9de8d168d1750087015a3fef644`
- Source: https://mediadive.dsmz.de/rest/medium/J69
- Source SHA256: 3dfebbc3c45015374477b729d8a15b4cd67214bfe8317190b70b401a8104270b
- Retrieved: 2026-10-07T14:01:38.051636+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "50.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J69 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].concentration` | GYP-sodium acetate-mineral salts broth | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J69 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | gyp_sodium_acetate_mineral_salts_broth | {"id": "CultureMech:003035", "name": "gyp_sodium_acetate_mineral_salts_broth", "notes": "Supplements 1.0 L GYP-sodium acetate-mineral salts broth with 50.0 g/L NaCl.", "path": "data/normalized_yaml/bacterial/gyp_sodium_acetate_mineral_salts_broth.yaml", "relationship": "SALINITY_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | GYP-sodium acetate-mineral salts broth | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J69 | {<br>                        "recipe_order": 1,<br>                        "compound": "GYP-sodium acetate-mineral salts broth",<br>                        "compound_id": 1618,<br>                        "attribute": "see Medium No. 68",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J69 | {<br>                        "recipe_order": 2,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 50,<br>                        "unit": "g",<br>                        "g_l": 50,<br>                        "mmol_l": 855.578,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
