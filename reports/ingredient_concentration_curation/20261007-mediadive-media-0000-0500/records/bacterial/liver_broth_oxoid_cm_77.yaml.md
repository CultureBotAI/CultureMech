# Medium Concentration Review: LIVER BROTH (Oxoid CM 77)

- Record: data/normalized_yaml/bacterial/liver_broth_oxoid_cm_77.yaml
- ID: CultureMech:001915
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e26fd122ff3e111857d6fc01d155cba927151c21cd012c02576b840bdaec9f9b`
- Proposed/result SHA256: `e26fd122ff3e111857d6fc01d155cba927151c21cd012c02576b840bdaec9f9b`
- Source: https://mediadive.dsmz.de/rest/medium/77
- Source SHA256: fb4b6a8a88ca1fc458a9743fd371431bf9cb48e27a0e80c48ab9f98bc11f59f6
- Retrieved: 2026-10-07T10:41:43.510902+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Liver Broth (Oxoid CM 77) | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/77 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | N2 gas | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/77 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/77 | {<br>                        "step": "Prepare the medium according to directions on the bottle under 100% N2 gas atmosphere."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
