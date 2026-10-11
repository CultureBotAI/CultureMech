# Medium Concentration Review: wMalt Yeast Extract Medium (wMY)

- Record: data/normalized_yaml/fungal/wmalt_yeast_extract_medium_wmy.yaml
- ID: CultureMech:010440
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `bc7b6d8539d1d7f327de5858c0e9b2ca6700ec584ff585f8ccbf6261646c1c7c`
- Proposed/result SHA256: `bc7b6d8539d1d7f327de5858c0e9b2ca6700ec584ff585f8ccbf6261646c1c7c`
- Source: https://mediadive.dsmz.de/rest/medium/C109
- Source SHA256: bb68051ef4e34195761c606ae87657353c3e87c9cfe11369b1814105210bbcaa
- Retrieved: 2026-10-07T14:00:51.072425+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "0.75"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/C109 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.002"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/C109 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[2].concentration` | Malt extract | {"unit": "G_PER_L", "value": "0.002"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/C109 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[3].concentration` | Distilled water | {"unit": "L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/C109 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/C109 | {<br>                        "step": "This medium recipe is coming very soon!"<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
