# Medium Concentration Review: ACIDIC YEAST EXTRACT-MALT EXTRACT AGAR (pH 5.0)

- Record: data/normalized_yaml/fungal/acidic_yeast_extract_malt_extract_agar_ph_5_0.yaml
- ID: CultureMech:010525
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `47cafa8243b3ed05f82f38474e8e8cf16d5edd91c25d74865e8c822c037df18e`
- Proposed/result SHA256: `47cafa8243b3ed05f82f38474e8e8cf16d5edd91c25d74865e8c822c037df18e`
- Source: https://mediadive.dsmz.de/rest/medium/J415
- Source SHA256: 3459866879e6150ba191fada657ce02e1ef8becdb39e102c0d77708cb59c6be6
- Retrieved: 2026-10-07T14:06:18.316170+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "4"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J415 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Malt extract | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J415 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Glucose | {"unit": "G_PER_L", "value": "4"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J415 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Agar | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J415 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J415 | {<br>                        "step": "Prepare Yeast extract-malt extract agar (ISP-2) (see Medium No. 43) and adjust pH to 5.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
