# Medium Concentration Review: MARINE AGAR 2216 (pH 9.0)

- Record: data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml
- ID: CultureMech:015373
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e4a25a0016b76efb3eba713e5f2c0919cd0a0c1e31da2c5c3e2de8136334805f`
- Proposed/result SHA256: `e4a25a0016b76efb3eba713e5f2c0919cd0a0c1e31da2c5c3e2de8136334805f`
- Source: https://mediadive.dsmz.de/rest/medium/J1016
- Source SHA256: d9687806dd74a6152fbcde714f0671c09640e13434ada4c411835f485b2c9983
- Retrieved: 2026-10-07T15:18:08.156004+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Marine agar 2216 (BD-Difco) | {"unit": "G_PER_L", "value": "55.1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1016 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[1].concentration` | Distilled water | {"unit": "L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1016 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].concentration` | 10% Na2CO3 solution | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1016 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].composition[0].concentration` | Na2CO3 | {"unit": "PERCENT_W_V", "value": "10.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1016 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | marine_agar_2216 | {"id": "CultureMech:015393", "name": "marine_agar_2216", "notes": "JCM Medium 1016 adjusts JCM Medium 118 Marine Agar 2216 to pH 9.0.", "path": "data/normalized_yaml/specialized/marine_agar_2216.yaml", "relationship": "PH_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1016 | {<br>                        "step": "Prepare Marine agar 2216 (see Medium No. 118). After autoclaving, adjust pH to 9.0 with sterilized 10% Na2CO3 solution."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
