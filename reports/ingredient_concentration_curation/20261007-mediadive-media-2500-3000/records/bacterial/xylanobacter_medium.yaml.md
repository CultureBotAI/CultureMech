# Medium Concentration Review: XYLANOBACTER MEDIUM

- Record: data/normalized_yaml/bacterial/xylanobacter_medium.yaml
- ID: CultureMech:002873
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `32c0ae1552fff242e5a37fc8ee61a2bd740964a8e1349e3d15c3c7115f1ef63e`
- Proposed/result SHA256: `32c0ae1552fff242e5a37fc8ee61a2bd740964a8e1349e3d15c3c7115f1ef63e`
- Source: https://mediadive.dsmz.de/rest/medium/J522
- Source SHA256: 6726c209b0e05d69d33d1011ad24c9e791eb1bb169051308e84ad69ab526dd4e
- Retrieved: 2026-10-07T14:35:59.398085+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `solutions[0].concentration` | PY4S Agar | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J522 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | py4s_agar | {"id": "CultureMech:002722", "name": "py4s_agar", "notes": "Adjusts PY4S Agar from JCM Medium 363 to pH 6.0.", "path": "data/normalized_yaml/bacterial/py4s_agar.yaml", "relationship": "PH_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J522 | {<br>                        "step": "Prepare PY4S agar (see Medium No. 363) and adjust pH to 6.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
