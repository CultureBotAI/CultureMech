# Medium Concentration Review: COLUMBIA BLOOD AGAR WITH 5% HORSE BLOOD

- Record: data/normalized_yaml/bacterial/columbia_blood_agar_with_5_horse_blood.yaml
- ID: CultureMech:002640
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6ae72c92a3b4f3c29fcf489121a9c07d4878a4cbbd2a0a50eb3764bc646323d3`
- Proposed/result SHA256: `6ae72c92a3b4f3c29fcf489121a9c07d4878a4cbbd2a0a50eb3764bc646323d3`
- Source: https://mediadive.dsmz.de/rest/medium/J282
- Source SHA256: 3a09193c8d302875f3f8afe7de6a192665f2c51d640bc01c42a1237c5ece85c2
- Retrieved: 2026-10-07T14:04:26.089537+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Pancreatic digest of casein | {"unit": "G_PER_L", "value": "10.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J282 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Peptic digest of animal tissue | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J282 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Beef extract | {"unit": "G_PER_L", "value": "3.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J282 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J282 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | Corn starch | {"unit": "G_PER_L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J282 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | Sodium chloride | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J282 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | Agar | {"unit": "G_PER_L", "value": "13.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J282 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | Defibrinated horse blood | {"unit": "PERCENT_V_V", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J282 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `variant_children[0]` | columbia_blood_agar_with_5_horse_blood | {"id": "CultureMech:009317", "name": "columbia_blood_agar_with_5_horse_blood", "notes": "TOGO import of the same source-catalogue formulation.", "path": "data/normalized_yaml/bacterial/TOGO_M276_Columbia_Blood_Agar_With_5_Horse_Blood.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J282 | {<br>                        "step": "Prepare Columbia blood agar base (Oxoid CM331) according to the direction, sterilize and cool to about 45C. Aseptically add 5% (final) sterile defibrinated horse blood. Mix and quickly dispense into sterile test tubes or petri dishes."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
