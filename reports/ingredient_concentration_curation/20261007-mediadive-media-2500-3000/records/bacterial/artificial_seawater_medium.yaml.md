# Medium Concentration Review: ARTIFICIAL SEAWATER MEDIUM

- Record: data/normalized_yaml/bacterial/artificial_seawater_medium.yaml
- ID: CultureMech:003321
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6129d4bc2d3fedde878aa9caaf7269ef2aaa54c8e3c74c6c7825d82c09ba431b`
- Proposed/result SHA256: `6129d4bc2d3fedde878aa9caaf7269ef2aaa54c8e3c74c6c7825d82c09ba431b`
- Source: https://mediadive.dsmz.de/rest/medium/J972
- Source SHA256: b745490884b6dbe8bb75833bb0467e49cbf4fddfb5e2dd12f528bef1d4759fec
- Retrieved: 2026-10-07T14:42:02.981259+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "24"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J972 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | KCl | {"unit": "G_PER_L", "value": "0.7"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J972 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | MgCl2 x 6 H2O | {"unit": "G_PER_L", "value": "7"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J972 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J972 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | Peptone | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J972 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `variant_children[0]` | low_strength_artificial_seawater_medium | {"id": "CultureMech:003047", "name": "low_strength_artificial_seawater_medium", "notes": "Same ingredient and concentration signature; review as possible duplicate source record.", "path": "data/normalized_yaml/bacterial/low_strength_artificial_seawater_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J972 | {<br>                        "step": "Use Medium No. 701 with 3.0 g/L (final) yeast extract and 2.5 g/L (final) peptone."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
| `source.data.solutions[0].steps[1]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J972 | {<br>                        "step": "Adjust pH to 7.5."<br>                    } | $.data.solutions[0].steps[1] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
