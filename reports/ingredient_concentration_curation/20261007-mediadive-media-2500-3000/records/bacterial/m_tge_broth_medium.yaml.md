# Medium Concentration Review: m TGE BROTH MEDIUM

- Record: data/normalized_yaml/bacterial/m_tge_broth_medium.yaml
- ID: CultureMech:003139
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a7e2065aa95ca892e603fd6237dfecbda088a512055cc91da998524e93ddad2d`
- Proposed/result SHA256: `a7e2065aa95ca892e603fd6237dfecbda088a512055cc91da998524e93ddad2d`
- Source: https://mediadive.dsmz.de/rest/medium/J795
- Source SHA256: 0ba5a8fc6173c61540ef5038bf07230236770145bf697c7fa169987776192603
- Retrieved: 2026-10-07T14:39:39.862922+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Bacto m TGE broth (BD-Difco) | {"unit": "G_PER_L", "value": "18.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J795 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Bacto m TGE broth, Bacto m TGE broth (BD-Difco) | unchanged |
| `ingredients[1].concentration` | Distilled water | {"unit": "L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J795 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Bacto m TGE broth, Bacto m TGE broth (BD-Difco) | unchanged |
| `variant_children[0]` | m_tge_gp_medium | {"id": "CultureMech:003197", "name": "m_tge_gp_medium", "notes": "JCM Medium 851 supplements JCM Medium 795 with 5.0 g/L glycerol and 0.1 mM KH2PO4.", "path": "data/normalized_yaml/bacterial/m_tge_gp_medium.yaml", "relationship": "SUPPLEMENTED_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Bacto m TGE broth | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J795 | {<br>                        "recipe_order": 1,<br>                        "compound": "Bacto m TGE broth",<br>                        "compound_id": 1896,<br>                        "attribute": "BD-Difco",<br>                        "amount": 18,<br>                        "unit": "g",<br>                        "g_l": 18,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J795 | {<br>                        "recipe_order": 2,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J795 | {<br>                        "step": "For preparation of solid medium, add 15.0 g/L agar."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
