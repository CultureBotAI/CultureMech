# Medium Concentration Review: MODIFIED SAP2 MEDIUM

- Record: data/normalized_yaml/bacterial/modified_sap2_medium.yaml
- ID: CultureMech:003259
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `325f2059c8ff1c17d18954e4e7d42d5cf47e6c7e0e4eb5b52a99656addd42ce6`
- Proposed/result SHA256: `325f2059c8ff1c17d18954e4e7d42d5cf47e6c7e0e4eb5b52a99656addd42ce6`
- Source: https://mediadive.dsmz.de/rest/medium/J910
- Source SHA256: 72ed3d9b13d1875cc5a82b4b22f89bbd7ad7c218d99fb7c2a5eb35bbfe28f50f
- Retrieved: 2026-10-07T14:41:11.907199+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Tryptone | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J910 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J910 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J910 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | NaCl | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J910 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | KCl | {"unit": "G_PER_L", "value": "0.35"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J910 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | MgCl2 x 6 H2O | {"unit": "G_PER_L", "value": "5.4"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J910 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "2.7"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J910 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J910 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J910 | {<br>                        "step": "Use Medium No. 651 with 1.0 x artificial seawater (instead of the 0.5 x artificial seawater). For preparation of liquid medium, omit agar."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
