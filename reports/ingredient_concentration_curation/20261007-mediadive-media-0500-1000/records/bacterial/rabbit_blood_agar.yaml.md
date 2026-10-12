# Medium Concentration Review: RABBIT BLOOD AGAR

- Record: data/normalized_yaml/bacterial/rabbit_blood_agar.yaml
- ID: CultureMech:001784
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5e10ab42d2af58d19c8d8564ab3dc688ba84a885070dacd565c3e78e63814b3b`
- Proposed/result SHA256: `5e10ab42d2af58d19c8d8564ab3dc688ba84a885070dacd565c3e78e63814b3b`
- Source: https://mediadive.dsmz.de/rest/medium/646
- Source SHA256: fc6f9b5dcf1a1f149b058adb72ac0f096356b36d3ac2293edc2262f5b26aa806
- Retrieved: 2026-10-07T12:16:56.823785+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Blood Agar Base from Difco 0045 | {"unit": "G_PER_L", "value": "40.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/646 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Blood Agar Base, Blood Agar Base from Difco 0045, Rabbit blood, Sterile defibrinated rabbit blood | unchanged |
| `ingredients[1].concentration` | Sterile defibrinated rabbit blood | {"unit": "PERCENT_V_V", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/646 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Blood Agar Base, Blood Agar Base from Difco 0045, Rabbit blood, Sterile defibrinated rabbit blood | unchanged |
| `variant_children[0]` | rabbit_blood_agar | {"id": "CultureMech:006192", "name": "rabbit_blood_agar", "notes": "KOMODO record states DSMZ Medium 646 provenance and mirrors the same rabbit blood agar formulation.", "path": "data/normalized_yaml/bacterial/KOMODO_646_RABBIT_BLOOD_AGAR.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Blood Agar Base | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/646 | {<br>                        "recipe_order": 2,<br>                        "compound": "Blood Agar Base",<br>                        "compound_id": 2130,<br>                        "attribute": "Difco 0045",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Rabbit blood | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/646 | {<br>                        "recipe_order": 3,<br>                        "compound": "Rabbit blood",<br>                        "compound_id": 1927,<br>                        "attribute": "sterile, defibrinated",<br>                        "amount": 5,<br>                        "unit": "%",<br>                        "g_l": 50,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/646 | {<br>                        "step": "Prepare Blood Agar Base from Difco 0045 according to directions on the bottle (40.0 g/l). Sterilize and cool to 45\u00b0C. Aseptically add 5% sterile defibrinated rabbit blood or sheep blood, mix well."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
