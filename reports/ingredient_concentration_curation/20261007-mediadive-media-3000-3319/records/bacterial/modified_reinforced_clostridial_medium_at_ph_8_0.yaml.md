# Medium Concentration Review: MODIFIED REINFORCED CLOSTRIDIAL MEDIUM AT pH 8.0

- Record: data/normalized_yaml/bacterial/modified_reinforced_clostridial_medium_at_ph_8_0.yaml
- ID: CultureMech:002442
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1909e067249bdc4e278ddf3262d966bd97464ce2e11fb0d9d4fbbd3319750b90`
- Proposed/result SHA256: `1909e067249bdc4e278ddf3262d966bd97464ce2e11fb0d9d4fbbd3319750b90`
- Source: https://mediadive.dsmz.de/rest/medium/J1276
- Source SHA256: d982bec9722aed62156ffbdc14dbd400afaedd7bfeb221cd8a71b94706b156ac
- Retrieved: 2026-10-07T15:21:47.562053+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1276 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Tryptone | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1276 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Beef extract | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1276 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Glucose | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1276 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | L-Cysteine HCl x H2O | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1276 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | NaCl | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1276 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | Sodium acetate | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1276 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | Starch | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1276 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `parent_media` | modified_reinforced_clostridial_medium | {"id": "CultureMech:002386", "name": "modified_reinforced_clostridial_medium", "path": "data/normalized_yaml/bacterial/modified_reinforced_clostridial_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1276 | {<br>                        "step": "Use Medium No. 1217 adjusted pH to 8.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
