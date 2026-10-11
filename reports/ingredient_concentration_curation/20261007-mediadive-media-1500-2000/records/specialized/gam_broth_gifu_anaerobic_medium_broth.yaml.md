# Medium Concentration Review: GAM Broth (Gifu Anaerobic Medium Broth)

- Record: data/normalized_yaml/specialized/gam_broth_gifu_anaerobic_medium_broth.yaml
- ID: CultureMech:015347
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `13a906ef1ce17ad36559def928d3525ed883b5335312317ff8ba2d5bdb2e50df`
- Proposed/result SHA256: `13a906ef1ce17ad36559def928d3525ed883b5335312317ff8ba2d5bdb2e50df`
- Source: https://mediadive.dsmz.de/rest/medium/1713
- Source SHA256: 58ab6ac780d87a061313c5298c7d4a73c250b11c42a1ed2c19998d6a12099ff3
- Retrieved: 2026-10-07T13:45:44.171356+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | DI water | {"unit": "L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1713 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): DI water, Deionized water, GAM Broth powder, GAM Broth powder (HyServe) | unchanged |
| `ingredients[1].concentration` | GAM Broth powder (HyServe) | {"unit": "G_PER_L", "value": "59.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1713 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): DI water, Deionized water, GAM Broth powder, GAM Broth powder (HyServe) | unchanged |
| `source.data.solutions[0].recipe[0]` | GAM Broth powder | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1713 | {<br>                        "recipe_order": 1,<br>                        "compound": "GAM Broth powder",<br>                        "compound_id": 1563,<br>                        "attribute": "HyServe",<br>                        "amount": 59,<br>                        "unit": "g",<br>                        "g_l": 59,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Deionized water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1713 | {<br>                        "recipe_order": 2,<br>                        "compound": "Deionized water",<br>                        "compound_id": 418,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1713 | {<br>                        "step": "Suspend the dehydrated medium in deionized water, and heat do dissolve the medium, sterilize by autoclaving at 115 \u00b0C for 15 minutes."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
