# Medium Concentration Review: 2SNA

- Record: data/normalized_yaml/bacterial/2sna.yaml
- ID: CultureMech:000411
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `bd6a9550f0465707c760a34b088d6c6fd646e09cefd36a9f1993d6f844de2300`
- Proposed/result SHA256: `bd6a9550f0465707c760a34b088d6c6fd646e09cefd36a9f1993d6f844de2300`
- Source: https://mediadive.dsmz.de/rest/medium/C96
- Source SHA256: e6a203711863aab90440f391d4d8c173fc284255948dcd44ffe5ff41272fcb9b
- Retrieved: 2026-10-07T13:48:11.771892+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Nutrient agar (Oxoid CM3) | {"unit": "G_PER_L", "value": "28.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/C96 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[1].concentration` | NaCl | {"unit": "G_PER_L", "value": "35.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/C96 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[2].concentration` | Filtered natural seawater | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/C96 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/C96 | {<br>                        "step": "This medium recipe is coming very soon!"<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
