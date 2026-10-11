# Medium Concentration Review: BLOOD AGAR

- Record: data/normalized_yaml/bacterial/blood_agar.yaml
- ID: CultureMech:003056
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `22f1fe536d003790d347feee506aaf10b0ffea0432abf08af2a124cecab0dc83`
- Proposed/result SHA256: `22f1fe536d003790d347feee506aaf10b0ffea0432abf08af2a124cecab0dc83`
- Source: https://mediadive.dsmz.de/rest/medium/J70
- Source SHA256: 61d740af8c84d10ead8de780ee2d7b9c5869fe0083e6c33cef35fcd8d25eb81f
- Retrieved: 2026-10-07T14:01:38.826082+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Heart muscle infusion solids | {"unit": "G_PER_L", "value": "2.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J70 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Pancreatic digest of casein | {"unit": "G_PER_L", "value": "13.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J70 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J70 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Sodium chloride | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J70 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | Agar | {"unit": "G_PER_L", "value": "15.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J70 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | Defibrinated rabbit blood | {"unit": "PERCENT_V_V", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J70 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `variant_children[0]` | blood_agar | {"id": "CultureMech:010030", "name": "blood_agar", "notes": "TOGO import of the same source-catalogue formulation.", "path": "data/normalized_yaml/bacterial/TOGO_M62_Blood_Agar.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J70 | {<br>                        "step": "Prepare Blood agar base (BD-Difco) according to the direction, sterilize and cool to about 45C. Aseptically add final 5% sterile defibrinated rabbit blood. Mix and quickly dispense into sterile test tubes."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
