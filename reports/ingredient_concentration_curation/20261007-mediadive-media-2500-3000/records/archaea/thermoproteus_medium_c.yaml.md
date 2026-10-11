# Medium Concentration Review: THERMOPROTEUS MEDIUM (C)

- Record: data/normalized_yaml/archaea/thermoproteus_medium_c.yaml
- ID: CultureMech:002977
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `8adcfc9d09091d20f7e7de6cd4c49fd8f5e4589a3b325b8feb87de79126a7acc`
- Proposed/result SHA256: `8adcfc9d09091d20f7e7de6cd4c49fd8f5e4589a3b325b8feb87de79126a7acc`
- Source: https://mediadive.dsmz.de/rest/medium/J630
- Source SHA256: 4fbc3f36a6745a684385a47738657d0fe07e6f76eefd0785cd8ff914be70e219
- Retrieved: 2026-10-07T14:37:26.313745+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `solutions[0].concentration` | Vulcanisaeta Medium | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J630 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J630 | {<br>                        "step": "Prepare Medium No. 297 and adjust pH to 7.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
