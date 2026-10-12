# Medium Concentration Review: Bs 107 MEDIUM

- Record: data/normalized_yaml/bacterial/bs_107_medium.yaml
- ID: CultureMech:003213
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5f5e644fc73bf2b609dea6a77e39b37cbf0a73a794b1f9b58cf17a8cebd35a6e`
- Proposed/result SHA256: `5f5e644fc73bf2b609dea6a77e39b37cbf0a73a794b1f9b58cf17a8cebd35a6e`
- Source: https://mediadive.dsmz.de/rest/medium/J867
- Source SHA256: d80680e72ab34281171dea9b5b0396b74577e446bff914d0ac6819ebceaa36d5
- Retrieved: 2026-10-07T14:40:37.367330+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `solutions[0].concentration` | Bs 107 Medium | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J867 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | bs_107_medium | {"id": "CultureMech:010323", "name": "bs_107_medium", "notes": "The stale JCM J867 import represents the same Bs 107 formulation preserved by TOGO M904.", "path": "data/normalized_yaml/bacterial/TOGO_M904_Bs_107_Medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J867 | {<br>                        "step": "Use Medium No. 866, replacing yeast extract with 3.0 &mu;g/L Na2SeO3 x 5H2O."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
