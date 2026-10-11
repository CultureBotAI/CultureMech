# Medium Concentration Review: VY/2 AGAR

- Record: data/normalized_yaml/bacterial/JCM_J436_VY_2_AGAR.yaml
- ID: CultureMech:002787
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7d777fd30846843d41f9206a1c230edc757edd87bb28940ca5fbb53b5b38bcb8`
- Proposed/result SHA256: `7d777fd30846843d41f9206a1c230edc757edd87bb28940ca5fbb53b5b38bcb8`
- Source: https://mediadive.dsmz.de/rest/medium/J436
- Source SHA256: 30d7aceb0f87d02fcdb432da57c7c3b499bdb9b9c7f6dddba6d88cd63f83f6b7
- Retrieved: 2026-10-07T14:06:35.573446+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Vitamin B12 | {"unit": "G_PER_L", "value": "0.0005"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J436 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J436 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Sea water | {"unit": "G_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J436 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J436 | {<br>                        "step": "Use Medium No. 341 with 1.36 g/L (final) CaCl2 x 2H2O, and with distilled water instead of the artificial seawater. Adjust pH to 7.2."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
| `source.data.solutions[0].steps[1]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J436 | {<br>                        "step": "Comment: For strain JCM 12614, place pieces of sterile filter paper (e.g., 1 cm x 1 cm) onto the surface of the plate. Inoculate onto the filter paper."<br>                    } | $.data.solutions[0].steps[1] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
