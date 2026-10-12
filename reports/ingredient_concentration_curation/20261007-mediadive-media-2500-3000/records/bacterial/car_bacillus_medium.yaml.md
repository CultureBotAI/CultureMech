# Medium Concentration Review: CAR BACILLUS MEDIUM

- Record: data/normalized_yaml/bacterial/car_bacillus_medium.yaml
- ID: CultureMech:003345
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e86c1ff90e7fc4355bdd281b65409a90ec6e7c75e089c7071beb252b2f4a0cd8`
- Proposed/result SHA256: `e86c1ff90e7fc4355bdd281b65409a90ec6e7c75e089c7071beb252b2f4a0cd8`
- Source: https://mediadive.dsmz.de/rest/medium/J996
- Source SHA256: f29d9f7f4ab62bf392ebf4e7a5d493c9b542cf18bf263311f306e6ce686ca389
- Retrieved: 2026-10-07T14:42:23.321835+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `solutions[0].concentration` | Clarified Vero E6 cell culture supernatant fluid | {"unit": "PERCENT_V_V", "value": "100"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J996 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].composition[0].concentration` | Iscove's Modified Dulbecco's Medium (IMDM, GlutaMAX) | {"unit": "PERCENT_V_V", "value": "90"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J996 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].composition[1].concentration` | Fetal bovine serum | {"unit": "PERCENT_V_V", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J996 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J996 | {<br>                        "step": "Use the Vero E6 cell culture supernatant fluid (see below). Incubate the microorganism in the supernatant fluid in a polystyrene culture flask (75 cm2 flask, canted neck, vent cap, coated with Ultra-Low Attachment Surface, Corning: Cat. No. 3814) at 37C under 5% CO2."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
| `source.data.solutions[1].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J996 | {<br>                        "step": "Incubate Vero E6 cells (ATCC CRL-1586) in Iscove's Modified Dulbecco's Medium (IMDM, GlutaMAXTM) (Life Technologies: Cat. No. 31980030) supplemented with 10% fetal bovine serum (FBS; inactivated at 56C for 30 min) at 37C under 5% CO2. After cultivation, centrifuge the culture medium. Use the supernatant fluid for cultivation of the microorganism as described above."<br>                    } | $.data.solutions[1].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
