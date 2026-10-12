# Medium Concentration Review: ANAEROBIC BRAIN HEART INFUSION BROTH

- Record: data/normalized_yaml/specialized/anaerobic_brain_heart_infusion_broth.yaml
- ID: CultureMech:015416
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `fbcd441259f5a074e198561a646f23d7adb5475642878166c3f79eff265ce3e9`
- Proposed/result SHA256: `fbcd441259f5a074e198561a646f23d7adb5475642878166c3f79eff265ce3e9`
- Source: https://mediadive.dsmz.de/rest/medium/J723
- Source SHA256: c14fde973515aa584f737b6d2ae6abd1471fa7b0a83863e253d003793011aff8
- Retrieved: 2026-10-07T14:38:40.670816+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Brain heart infusion broth | {"unit": "G_PER_L", "value": "36.6337"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J723 | {<br>                        "recipe_order": 1,<br>                        "compound": "Brain heart infusion broth",<br>                        "compound_id": 827,<br>                        "attribute": "BD-Difco",<br>                        "amount": 37,<br>                        "unit": "g",<br>                        "g_l": 36.6337,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[1].concentration` | L-Cysteine HCl x H2O | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J723 | {<br>                        "recipe_order": 3,<br>                        "compound": "L-Cysteine HCl x H2O",<br>                        "compound_id": 770,<br>                        "attribute": "5%",<br>                        "amount": 5,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[2].concentration` | Na2S x 9 H2O | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J723 | {<br>                        "recipe_order": 4,<br>                        "compound": "Na2S x 9 H2O",<br>                        "compound_id": 54,<br>                        "attribute": "5%",<br>                        "amount": 5,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `source.data.solutions[0].recipe[1]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J723 | {<br>                        "recipe_order": 2,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J723 | {<br>                        "recipe_order": 3,<br>                        "step": "Prepare the medium anaerobically under a N2 atmosphere. Prior to inoculation, add per liter the following solutions (autoclaved and stored under a N2 atmosphere) aseptically and anaerobically: "<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
