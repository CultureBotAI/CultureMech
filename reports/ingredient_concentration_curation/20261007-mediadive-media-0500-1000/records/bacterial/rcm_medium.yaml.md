# Medium Concentration Review: RCM MEDIUM

- Record: data/normalized_yaml/bacterial/rcm_medium.yaml
- ID: CultureMech:001765
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d46a32c1c75c049c55e2a604f80ec1fe20d0c81f69ba8ee65db12227b844a6bf`
- Proposed/result SHA256: `d46a32c1c75c049c55e2a604f80ec1fe20d0c81f69ba8ee65db12227b844a6bf`
- Source: https://mediadive.dsmz.de/rest/medium/634
- Source SHA256: 08d5145d37c11531b461cde2a1bc8c197290bb618ade5ace80ba24b21afea94e
- Retrieved: 2026-10-07T12:16:43.764449+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | dehydrated RCM medium | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/634 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Distilled water | unchanged |
| `ingredients[1].concentration` | Sodium resazurin | {"unit": "G_PER_L", "value": "0.0005"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/634 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Distilled water | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/634 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Distilled water | unchanged |
| `source.data.solutions[0].recipe[0]` | dehydrated RCM medium | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/634 | {<br>                        "recipe_order": 1,<br>                        "compound": "dehydrated RCM medium",<br>                        "compound_id": 2126,<br>                        "attribute": "dissolved in distilled water",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Sodium resazurin | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/634 | {<br>                        "recipe_order": 2,<br>                        "compound": "Sodium resazurin",<br>                        "compound_id": 1852,<br>                        "attribute": "0.1% w/v",<br>                        "amount": 0.5,<br>                        "unit": "ml",<br>                        "g_l": 0.0005,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/634 | {<br>                        "step": "Dissolve dehydrated RCM medium (available from BD-BBL, OXOID or MERCK) in distilled water and add 0.5 ml/l Na-resazurin solution (0.1% w/v), bring to the boil and cool to room temperature while sparging with 100% N2 gas. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
