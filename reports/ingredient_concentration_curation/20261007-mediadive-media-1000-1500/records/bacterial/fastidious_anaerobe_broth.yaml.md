# Medium Concentration Review: FASTIDIOUS ANAEROBE BROTH

- Record: data/normalized_yaml/bacterial/fastidious_anaerobe_broth.yaml
- ID: CultureMech:000654
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `303f540bdc3cb89aa98a2f1e908e3f6ec8ed5a9df81693d73f9cd2442c4c4b63`
- Proposed/result SHA256: `303f540bdc3cb89aa98a2f1e908e3f6ec8ed5a9df81693d73f9cd2442c4c4b63`
- Source: https://mediadive.dsmz.de/rest/medium/1203a
- Source SHA256: acae543a1340c34e2f1e9355565178e351f7845058249addcf17942f85303996
- Retrieved: 2026-10-07T13:18:46.364268+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | DI water | {"unit": "L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1203a | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): DI water, Deionized water, Fastidious Anaerobe Basal Broth, Fastidious Anaerobe Basal Broth (OXOID) | unchanged |
| `ingredients[1].concentration` | Fastidious Anaerobe Basal Broth (OXOID) | {"unit": "G_PER_L", "value": "35.4"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1203a | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): DI water, Deionized water, Fastidious Anaerobe Basal Broth, Fastidious Anaerobe Basal Broth (OXOID) | unchanged |
| `source.data.solutions[0].recipe[0]` | Fastidious Anaerobe Basal Broth | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1203a | {<br>                        "recipe_order": 1,<br>                        "compound": "Fastidious Anaerobe Basal Broth",<br>                        "compound_id": 1079,<br>                        "attribute": "OXOID",<br>                        "amount": 35.4,<br>                        "unit": "g",<br>                        "g_l": 35.4,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Deionized water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1203a | {<br>                        "recipe_order": 2,<br>                        "compound": "Deionized water",<br>                        "compound_id": 418,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1203a | {<br>                        "step": "Boil medium and cool under N2, distribute under N2 and sterilize by autoclaving at 121\u00b0C for 20 minutes."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
