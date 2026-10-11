# Medium Concentration Review: HORIKOSHI-I MEDIUM WITH 2% NaCl

- Record: data/normalized_yaml/bacterial/horikoshi_i_medium_with_2_nacl.yaml
- ID: CultureMech:002765
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2a4cce9383f6b2b94847f33ec086dc7c79c7bafd6972f12b71c46eb0da41b4c2`
- Proposed/result SHA256: `2a4cce9383f6b2b94847f33ec086dc7c79c7bafd6972f12b71c46eb0da41b4c2`
- Source: https://mediadive.dsmz.de/rest/medium/J409
- Source SHA256: 4a4fbad94929d4b4024305c5e45b487493efd82b6a82cbacb3ba28e7b6ca9673
- Retrieved: 2026-10-07T14:06:13.497384+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J409 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].concentration` | Horikoshi-I medium | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J409 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | horikoshi_i_medium | {"id": "CultureMech:002542", "name": "horikoshi_i_medium", "notes": "Adds 20 g/L NaCl to JCM Medium 181 Horikoshi-I medium.", "path": "data/normalized_yaml/bacterial/horikoshi_i_medium.yaml", "relationship": "SALINITY_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Horikoshi-I medium | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J409 | {<br>                        "recipe_order": 1,<br>                        "compound": "Horikoshi-I medium",<br>                        "compound_id": 1740,<br>                        "attribute": "see Medium No. 181",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J409 | {<br>                        "recipe_order": 2,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 342.231,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
