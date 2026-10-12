# Medium Concentration Review: R AGAR WITH 10% NaCl

- Record: data/normalized_yaml/bacterial/r_agar_with_10_nacl.yaml
- ID: CultureMech:003224
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0adce80a102d23a32b04d0fc191c7682e49fb2a951f819368ebf5a62645588ec`
- Proposed/result SHA256: `0adce80a102d23a32b04d0fc191c7682e49fb2a951f819368ebf5a62645588ec`
- Source: https://mediadive.dsmz.de/rest/medium/J877
- Source SHA256: 6d4365ef7e128ff7c6f6f4c496d8740f4715c41e6823587e4c17ae6cfde969b0
- Retrieved: 2026-10-07T14:40:45.486903+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "100"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J877 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].concentration` | R agar | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J877 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | r_agar | {"id": "CultureMech:002627", "name": "r_agar", "notes": "Adds 100 g/L NaCl to JCM Medium 26 R Agar.", "path": "data/normalized_yaml/bacterial/r_agar.yaml", "relationship": "SALINITY_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | R agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J877 | {<br>                        "recipe_order": 1,<br>                        "compound": "R agar",<br>                        "compound_id": 1619,<br>                        "attribute": "see Medium No. 26",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J877 | {<br>                        "recipe_order": 2,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 100,<br>                        "unit": "g",<br>                        "g_l": 100,<br>                        "mmol_l": 1711.16,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
