# Medium Concentration Review: MW

- Record: data/normalized_yaml/bacterial/mw.yaml
- ID: CultureMech:000369
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `84ac2b45549ac339f4f4b21758cdefdf59477ecf994ac78f1f9b381595c2ec32`
- Proposed/result SHA256: `84ac2b45549ac339f4f4b21758cdefdf59477ecf994ac78f1f9b381595c2ec32`
- Source: https://mediadive.dsmz.de/rest/medium/C58
- Source SHA256: 7369bfefce59608314c764086e8fd89539072c106a36727d55a7a0c9c856fa6d
- Retrieved: 2026-10-07T13:47:41.581518+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Volvic mineral water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/C58 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `source.data.solutions[0].recipe[0]` | Mineral water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/C58 | {<br>                        "recipe_order": 2,<br>                        "compound": "Mineral water",<br>                        "compound_id": 2359,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/C58 | {<br>                        "step": "There are many proprietary brands of bottled mineral water. At present the CCAP uses \"Volvic\". Dispense into suitable vessels and autoclave at 15 psi for 15 minutes."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
