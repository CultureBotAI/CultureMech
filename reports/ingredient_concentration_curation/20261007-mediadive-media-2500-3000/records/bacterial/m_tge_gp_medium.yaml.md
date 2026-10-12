# Medium Concentration Review: m TGE-GP MEDIUM

- Record: data/normalized_yaml/bacterial/m_tge_gp_medium.yaml
- ID: CultureMech:003197
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `bb3b72e7c248596949ad673d8e86e2d682fc9b89740e68a2f88df91051361f69`
- Proposed/result SHA256: `bb3b72e7c248596949ad673d8e86e2d682fc9b89740e68a2f88df91051361f69`
- Source: https://mediadive.dsmz.de/rest/medium/J851
- Source SHA256: 7af70a8fc9061945c0b4d514e333ff89894cc87bb524735eb0f9a27d6e364d9b
- Retrieved: 2026-10-07T14:40:24.213692+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Bacto m TGE broth (BD-Difco) | {"unit": "G_PER_L", "value": "18.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J851 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Distilled water | {"unit": "L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J851 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Glycerol | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J851 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | KH2PO4 | {"unit": "MILLIMOLAR", "value": "0.1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J851 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `parent_media` | m_tge_broth_medium | {"id": "CultureMech:003139", "name": "m_tge_broth_medium", "notes": "JCM Medium 851 supplements JCM Medium 795 with 5.0 g/L glycerol and 0.1 mM KH2PO4.", "path": "data/normalized_yaml/bacterial/m_tge_broth_medium.yaml", "relationship": "SUPPLEMENTED_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J851 | {<br>                        "step": "Use Medium No. 795 with 5.0 g/L (final) glycerol and 0.1 mM (final) KH2PO4."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
