# Medium Concentration Review: ARCHAEOGLOBUS MCR MEDIUM

- Record: data/normalized_yaml/archaea/archaeoglobus_mcr_medium.yaml
- ID: CultureMech:002362
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `229601536cf72eee93ba3183fa5de76b9f59c9e1d0c7cb86e51003230559bd51`
- Proposed/result SHA256: `229601536cf72eee93ba3183fa5de76b9f59c9e1d0c7cb86e51003230559bd51`
- Source: https://mediadive.dsmz.de/rest/medium/J1195
- Source SHA256: 0f927a73c6c758f1c560c0f13b62eaa64450e28d1509ee44b7cbef4ad57299a3
- Retrieved: 2026-10-07T15:20:40.783653+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Na2SO4 | {"unit": "G_PER_L", "value": "2.8"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1195 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `solutions[0].concentration` | METHANOTHERMOCOCCUS HHB MEDIUM (see Medium [M1279]) | {"unit": "L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1195 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `parent_media` | methanothermococcus_hhb_medium | {"id": "CultureMech:002361", "name": "methanothermococcus_hhb_medium", "notes": "JCM Medium J1195 uses JCM Medium J1194 Methanothermococcus HHB Medium and supplements it with 2.8 g/L Na2SO4; CultureMech recovered the J1195 row from the source-equivalent TOGO M1280 snapshot.", "path": "data/normalized_yaml/archaea/methanothermococcus_hhb_medium.yaml", "relationship": "SUPPLEMENTED_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1195 | {<br>                        "step": "Use Medium No. 1194 supplemented with 2.8 g/L Na2SO4."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
