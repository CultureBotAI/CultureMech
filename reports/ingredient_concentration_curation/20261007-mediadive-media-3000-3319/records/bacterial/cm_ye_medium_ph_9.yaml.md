# Medium Concentration Review: CM+YE MEDIUM (pH 9)

- Record: data/normalized_yaml/bacterial/cm_ye_medium_ph_9.yaml
- ID: CultureMech:002400
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a9e49ea2b8870cc080713db6b1434518d63c6e2fd687be85ff22267edaf6d7de`
- Proposed/result SHA256: `a9e49ea2b8870cc080713db6b1434518d63c6e2fd687be85ff22267edaf6d7de`
- Source: https://mediadive.dsmz.de/rest/medium/J1233
- Source SHA256: 4cd830bf39c570c7903e998dcf0229b3137c27edab731bf27307fc3eff85072e
- Retrieved: 2026-10-07T15:21:12.423702+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Casamino acids | {"unit": "G_PER_L", "value": "7.49251"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1233 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "9.99001"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1233 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "19.98"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1233 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Trisodium citrate x 2 H2O | {"unit": "G_PER_L", "value": "2.997"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1233 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | KCl | {"unit": "G_PER_L", "value": "1.998"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1233 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | NaCl | {"unit": "G_PER_L", "value": "199.8"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1233 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | Agar | {"unit": "G_PER_L", "value": "14.985"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1233 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "49.8"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1233 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1233 | {<br>                        "step": "Prepare CM+YE medium (see Medium No. 59). After autoclaving, adjust pH to 9.0 with sterilized 10% Na2CO3 solution."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
