# Medium Concentration Review: GAM Broth, mod. (Gifu Anaerobic Medium Broth, modified)

- Record: data/normalized_yaml/specialized/gam_broth_mod_gifu_anaerobic_medium_broth_modified.yaml
- ID: CultureMech:015348
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `39e4146e89334976c51b68a68031ff9eaa28f2eb87f6a7ddb1f27a6ac85679ab`
- Proposed/result SHA256: `39e4146e89334976c51b68a68031ff9eaa28f2eb87f6a7ddb1f27a6ac85679ab`
- Source: https://mediadive.dsmz.de/rest/medium/1715
- Source SHA256: 88ee20a931b976738e1bff0a5787734ec65ff777b482f6494cbc8ca6986d1be2
- Retrieved: 2026-10-07T13:45:45.725168+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | DI water | {"unit": "L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1715 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): DI water, Deionized water, GAM Broth mod. powder, GAM Broth mod. powder (HyServe) | unchanged |
| `ingredients[1].concentration` | GAM Broth mod. powder (HyServe) | {"unit": "G_PER_L", "value": "41.7"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1715 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): DI water, Deionized water, GAM Broth mod. powder, GAM Broth mod. powder (HyServe) | unchanged |
| `source.data.solutions[0].recipe[0]` | GAM Broth mod. powder | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1715 | {<br>                        "recipe_order": 1,<br>                        "compound": "GAM Broth mod. powder",<br>                        "compound_id": 1564,<br>                        "attribute": "HyServe",<br>                        "amount": 41.7,<br>                        "unit": "g",<br>                        "g_l": 41.7,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Deionized water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1715 | {<br>                        "recipe_order": 2,<br>                        "compound": "Deionized water",<br>                        "compound_id": 418,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1715 | {<br>                        "step": "Suspend the dehydrated medium in deionized water, and heat do dissolve the medium, sterilize by autoclaving at 115 \u00b0C for 15 minutes."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
