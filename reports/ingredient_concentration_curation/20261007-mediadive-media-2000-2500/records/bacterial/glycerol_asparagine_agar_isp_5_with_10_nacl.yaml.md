# Medium Concentration Review: GLYCEROL-ASPARAGINE AGAR (ISP-5) WITH 10% NaCl

- Record: data/normalized_yaml/bacterial/glycerol_asparagine_agar_isp_5_with_10_nacl.yaml
- ID: CultureMech:002767
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `03643de102bd904cea9f79a68148ae44a24f505510912172e507674c17e9eba8`
- Proposed/result SHA256: `03643de102bd904cea9f79a68148ae44a24f505510912172e507674c17e9eba8`
- Source: https://mediadive.dsmz.de/rest/medium/J410
- Source SHA256: 6b658875da62d8307f8d81eac0fe62a2b89ee002045bf8e56fe2229f6d87f6f3
- Retrieved: 2026-10-07T14:06:14.289436+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "100"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J410 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].concentration` | Glycerol-Asparagine Agar (ISP-5) | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J410 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | glycerol_asparagine_agar_isp_5 | {"id": "CultureMech:002957", "name": "glycerol_asparagine_agar_isp_5", "notes": "Adds 100 g/L NaCl to JCM Medium 60 Glycerol-Asparagine Agar (ISP-5).", "path": "data/normalized_yaml/bacterial/glycerol_asparagine_agar_isp_5.yaml", "relationship": "SALINITY_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Glycerol-asparagine agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J410 | {<br>                        "recipe_order": 1,<br>                        "compound": "Glycerol-asparagine agar",<br>                        "compound_id": 1754,<br>                        "attribute": "ISP-5) (see Medium No. 60",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J410 | {<br>                        "recipe_order": 2,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 100,<br>                        "unit": "g",<br>                        "g_l": 100,<br>                        "mmol_l": 1711.16,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
