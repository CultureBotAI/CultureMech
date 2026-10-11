# Medium Concentration Review: HEMIN MEDIUM FOR MYCOBACTERIUM

- Record: data/normalized_yaml/bacterial/hemin_medium_for_mycobacterium.yaml
- ID: CultureMech:001783
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c8c238ac0fc92366f4f9cb19a0dca2e5e525e35200ecd3e26aec32e9150a2360`
- Proposed/result SHA256: `c8c238ac0fc92366f4f9cb19a0dca2e5e525e35200ecd3e26aec32e9150a2360`
- Source: https://mediadive.dsmz.de/rest/medium/645a
- Source SHA256: 3352200f99d29fd931608356ae62d63ff4c93521850c4999648a726810c65027
- Retrieved: 2026-10-07T12:16:56.040852+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Middlebrook 7H10 agar | {"unit": "G_PER_L", "value": "900"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/645a | {<br>                        "recipe_order": 1,<br>                        "compound": "Middlebrook 7H10 agar",<br>                        "compound_id": 1748,<br>                        "attribute": "Difco 0627",<br>                        "amount": 900,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[1].concentration` | OADC Enrichment | {"unit": "G_PER_L", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/645a | {<br>                        "recipe_order": 2,<br>                        "compound": "OADC Enrichment",<br>                        "compound_id": 2129,<br>                        "attribute": "Difco 0722",<br>                        "amount": 100,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[2].concentration` | Haemin | {"unit": "MICROMOLAR", "value": "60"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/645a | {<br>                        "recipe_order": 3,<br>                        "compound": "Haemin",<br>                        "compound_id": 149,<br>                        "attribute": "solubilized with 1N NaOH",<br>                        "amount": 60,<br>                        "unit": "\u03bcM",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/645a | {<br>                        "step": "Middlebrook 7H10 (Difco 0627) with OADC Enrichment (Difco 0722) with 60 micromoles hemin. Hemin must be solubilized with 1N NAOH."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
