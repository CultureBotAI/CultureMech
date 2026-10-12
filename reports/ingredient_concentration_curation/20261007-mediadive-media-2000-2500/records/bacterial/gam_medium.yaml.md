# Medium Concentration Review: GAM MEDIUM

- Record: data/normalized_yaml/bacterial/gam_medium.yaml
- ID: CultureMech:003184
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ce89080307c14fdc35985bbebbca454db9fd9efd0255a748f102cf53d36a6acb`
- Proposed/result SHA256: `ce89080307c14fdc35985bbebbca454db9fd9efd0255a748f102cf53d36a6acb`
- Source: https://mediadive.dsmz.de/rest/medium/J83
- Source SHA256: 3d74508e9f49c365f4e0c36e5a2949ce421361677b29f1bfd22f139e900b4a07
- Retrieved: 2026-10-07T14:01:48.199890+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | GAM broth (Nissui) | {"unit": "G_PER_L", "value": "59.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J83 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Distilled water | {"unit": "L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J83 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | GAM broth | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J83 | {<br>                        "recipe_order": 1,<br>                        "compound": "GAM broth",<br>                        "compound_id": 1620,<br>                        "attribute": "Nissui",<br>                        "amount": 59,<br>                        "unit": "g",<br>                        "g_l": 59,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J83 | {<br>                        "recipe_order": 2,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
