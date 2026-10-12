# Medium Concentration Review: COLUMBIA BLOOD AGAR WITH 10% HORSE BLOOD

- Record: data/normalized_yaml/bacterial/columbia_blood_agar_with_10_horse_blood.yaml
- ID: CultureMech:002579
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1fb4660d4c6a72c5040057dca1fb0ecf7a885bbeae0ac767503de245969d77b5`
- Proposed/result SHA256: `1fb4660d4c6a72c5040057dca1fb0ecf7a885bbeae0ac767503de245969d77b5`
- Source: https://mediadive.dsmz.de/rest/medium/J218
- Source SHA256: 136f34a4f15bae4764f0f37d6c89359e8d69ae875bf7d358f26906cd169d6d00
- Retrieved: 2026-10-07T14:03:34.303759+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Pancreatic digest of casein | {"unit": "G_PER_L", "value": "10.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J218 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Peptic digest of animal tissue | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J218 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Beef extract | {"unit": "G_PER_L", "value": "3.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J218 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J218 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | Corn starch | {"unit": "G_PER_L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J218 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | Sodium chloride | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J218 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | Agar | {"unit": "G_PER_L", "value": "13.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J218 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | Defibrinated horse blood | {"unit": "PERCENT_V_V", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J218 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `variant_children[0]` | columbia_blood_agar_with_10_horse_blood | {"id": "CultureMech:008712", "name": "columbia_blood_agar_with_10_horse_blood", "notes": "TOGO import of the same source-catalogue formulation.", "path": "data/normalized_yaml/bacterial/TOGO_M211_Columbia_Blood_Agar_With_10_Horse_Blood.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J218 | {<br>                        "step": "Prepare Columbia blood agar base (Oxoid CM331) according to the direction, sterilize and cool to about 45C. Aseptically add 10% (final) sterile defibrinated horse blood. Mix and quickly dispense into sterile test tubes or petri dishes."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
