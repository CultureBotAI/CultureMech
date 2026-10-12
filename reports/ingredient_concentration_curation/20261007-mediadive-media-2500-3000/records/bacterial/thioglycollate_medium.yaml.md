# Medium Concentration Review: THIOGLYCOLLATE MEDIUM

- Record: data/normalized_yaml/bacterial/thioglycollate_medium.yaml
- ID: CultureMech:002878
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `fbb9db0d2556cfb0ef63ac7c645778253889b3516ef9f3f1a90390b4e24ab997`
- Proposed/result SHA256: `fbb9db0d2556cfb0ef63ac7c645778253889b3516ef9f3f1a90390b4e24ab997`
- Source: https://mediadive.dsmz.de/rest/medium/J529
- Source SHA256: 2c286a10272890a3cd75ef7570187a8c2ca9416fe477c1cd77ae2e68c1e5d453
- Retrieved: 2026-10-07T14:36:05.294175+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J529 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[1].concentration` | Thioglycollate medium (Sigma) | {"unit": "G_PER_L", "value": "29.8"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J529 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `source.data.solutions[0].recipe[0]` | Thioglycolate | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J529 | {<br>                        "recipe_order": 1,<br>                        "compound": "Thioglycolate",<br>                        "compound_id": 287,<br>                        "attribute": "Sigma",<br>                        "amount": 29.8,<br>                        "unit": "g",<br>                        "g_l": 29.8,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J529 | {<br>                        "recipe_order": 2,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J529 | {<br>                        "step": "Comment: The medium is semisolid. For strain JCM 13596, prepare the medium anaerobically (under N2)."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
