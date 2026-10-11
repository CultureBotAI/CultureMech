# Medium Concentration Review: DILUTED ASM MEDIUM

- Record: data/normalized_yaml/bacterial/diluted_asm_medium.yaml
- ID: CultureMech:003160
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c610f9bc44d69ca1ba4803fece2b6291d2b906f3ef7bc401d9562ef8cb8f8c46`
- Proposed/result SHA256: `c610f9bc44d69ca1ba4803fece2b6291d2b906f3ef7bc401d9562ef8cb8f8c46`
- Source: https://mediadive.dsmz.de/rest/medium/J816
- Source SHA256: 911394a306e631cab8571a8115a3432ac110e8ab5691b567956697a8876e7437
- Retrieved: 2026-10-07T14:39:55.397884+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `solutions[0].concentration` | Acidic Diluted ASM Medium | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J816 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | acidic_diluted_asm_medium | {"id": "CultureMech:003159", "name": "acidic_diluted_asm_medium", "notes": "Adjusts Acidic Diluted ASM Medium from JCM Medium 815 to pH 6.7.", "path": "data/normalized_yaml/bacterial/acidic_diluted_asm_medium.yaml", "relationship": "PH_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J816 | {<br>                        "step": "Prepare Medium No. 815 and adjust pH to 6.7."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
