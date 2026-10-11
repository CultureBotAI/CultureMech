# Medium Concentration Review: MODIFIED MARINE AGAR 2216

- Record: data/normalized_yaml/specialized/JCM_J913_MODIFIED_MARINE_AGAR_2216.yaml
- ID: CultureMech:015424
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `70a7da14028f47c2ab65967146b7ca1a6b00e55e777a8f5669eeb097f69f0d73`
- Proposed/result SHA256: `70a7da14028f47c2ab65967146b7ca1a6b00e55e777a8f5669eeb097f69f0d73`
- Source: https://mediadive.dsmz.de/rest/medium/J913
- Source SHA256: ad54dd115293dab36f18901591f5d4f6a93bed2857966e8379585881cae10953
- Retrieved: 2026-10-07T14:41:14.466187+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Marine agar 2216 | {"unit": "G_PER_L", "value": "55.1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J913 | {<br>                        "recipe_order": 1,<br>                        "compound": "Marine agar 2216",<br>                        "compound_id": 1628,<br>                        "attribute": "BD-Difco",<br>                        "amount": 55.1,<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[1].concentration` | Casitone | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J913 | {<br>                        "recipe_order": 2,<br>                        "compound": "Casitone",<br>                        "compound_id": 84,<br>                        "attribute": "BD-Difco",<br>                        "amount": 1,<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[2].concentration` | Soytone | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J913 | {<br>                        "recipe_order": 3,<br>                        "compound": "Soytone",<br>                        "compound_id": 667,<br>                        "attribute": "BD-Difco) or Phytone peptone (BD-BBL",<br>                        "amount": 1,<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[3].concentration` | Malt extract | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J913 | {<br>                        "recipe_order": 4,<br>                        "compound": "Malt extract",<br>                        "compound_id": 116,<br>                        "attribute": "BD-Difco",<br>                        "amount": 1,<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J913 | {<br>                        "step": "Adjust pH to 7.5."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
