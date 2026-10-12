# Medium Concentration Review: DISTILLED WATER

- Record: data/normalized_yaml/bacterial/distilled_water.yaml
- ID: CultureMech:003010
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `770c8da1b0561f579a1614c3cb3594850faf978ff2b3551a832608f95d12d20e`
- Proposed/result SHA256: `770c8da1b0561f579a1614c3cb3594850faf978ff2b3551a832608f95d12d20e`
- Source: https://mediadive.dsmz.de/rest/medium/J664
- Source SHA256: af0edc297ffe86c5fa26b5ef939b4acdbff7b3b38b703d6421cf8d94d72ce920
- Retrieved: 2026-10-07T14:37:53.099040+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | water | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J664 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J664 | {<br>                        "step": "Autoclaved distilled water."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
