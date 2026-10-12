# Medium Concentration Review: NSW

- Record: data/normalized_yaml/bacterial/nsw.yaml
- ID: CultureMech:000384
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a459508e4c36587ce99aeadbe903cbf2c6d192955eea919aff15d40a2a8bf527`
- Proposed/result SHA256: `a459508e4c36587ce99aeadbe903cbf2c6d192955eea919aff15d40a2a8bf527`
- Source: https://mediadive.dsmz.de/rest/medium/C71
- Source SHA256: 92c809371fdca738feca23fbbb39d97785e0861d301125e45445486f6163a2e9
- Retrieved: 2026-10-07T13:47:51.852031+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Natural filtered seawater | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/C71 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `source.data.solutions[0].recipe[0]` | Natural sea water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/C71 | {<br>                        "recipe_order": 2,<br>                        "compound": "Natural sea water",<br>                        "compound_id": 2152,<br>                        "attribute": "filtered",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/C71 | {<br>                        "step": "Filter natural seawater through GF/C filters and autoclave at 15 psi for 15 minutes."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
