# Medium Concentration Review: CLOSTRIDIUM BOVIS MEDIUM

- Record: data/normalized_yaml/bacterial/clostridium_bovis_medium.yaml
- ID: CultureMech:002982
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `41f318d0606c77b3e13e6a0ed39dc087911d9cfbdcc7e667be967bdd0d9b20eb`
- Proposed/result SHA256: `41f318d0606c77b3e13e6a0ed39dc087911d9cfbdcc7e667be967bdd0d9b20eb`
- Source: https://mediadive.dsmz.de/rest/medium/J635
- Source SHA256: 909f04b16f1a3cbc45cf6be2df8f5e6ac1273038e882d9fb69a4a97dc5bdf1a0
- Retrieved: 2026-10-07T14:37:30.341604+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Distilled water | {"unit": "L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J635 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | MgSO4・7H2O | {"unit": "G_PER_L", "value": "0.1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J635 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | yeast extract | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J635 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | NaCl | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J635 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | CaCl2・2H2O | {"unit": "G_PER_L", "value": "0.1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J635 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J635 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J635 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | Resazurin | {"unit": "MG_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J635 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[8].concentration` | Na2S・9H2O | {"unit": "G_PER_L", "value": "0.1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J635 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[9].concentration` | (NH4)2SO4 | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J635 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[10].concentration` | L--Cysteine・HCl・H2O | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J635 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[11].concentration` | peptone | {"unit": "G_PER_L", "value": "0.2"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J635 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[12].concentration` | Carbon dioxide gas | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J635 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[13].concentration` | Nitrogen gas | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J635 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J635 | {<br>                        "step": "Use Medium No. 634 supplemented with 0.5 g/L (final conc.) yeast extract and 0.2 g/L peptone instead of sodium succinate."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
