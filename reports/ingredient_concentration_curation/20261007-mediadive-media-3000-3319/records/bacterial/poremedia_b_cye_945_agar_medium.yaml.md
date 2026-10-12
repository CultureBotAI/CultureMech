# Medium Concentration Review: POREMEDIA B-CYE&#945; AGAR MEDIUM

- Record: data/normalized_yaml/bacterial/poremedia_b_cye_945_agar_medium.yaml
- ID: CultureMech:002267
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `479a7dbadff8a5ff532b6e5176b9a76e31617a3b90256973a7ee2595800bdd81`
- Proposed/result SHA256: `479a7dbadff8a5ff532b6e5176b9a76e31617a3b90256973a7ee2595800bdd81`
- Source: https://mediadive.dsmz.de/rest/medium/J1087
- Source SHA256: 230f9766dce0c513b5240c2a8734054750957802c4e2a558de7b77cf896eae0c
- Retrieved: 2026-10-07T15:19:08.140399+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | POREMEDIA B-CYE alpha Agar Medium (Eiken Chemical) | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1087 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1087 | {<br>                        "step": "Use the commercially available medium manufactured by Eiken Chemical Co., Ltd."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
