# Medium Concentration Review: METHANOL-UTILIZING BACTERIA MEDIUM D

- Record: data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_d.yaml
- ID: CultureMech:002435
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ab81eea418d9a4e0837c3845c8d767c6012cf35a4693b95939ae269042c62c6c`
- Proposed/result SHA256: `ab81eea418d9a4e0837c3845c8d767c6012cf35a4693b95939ae269042c62c6c`
- Source: https://mediadive.dsmz.de/rest/medium/J126
- Source SHA256: b97f239827a0f305d540a0512f55711d90f4714deb58084a1fb4cac2f05f1b1f
- Retrieved: 2026-10-07T14:02:21.889703+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `solutions[0].concentration` | Methanol-utilizing bacteria medium B | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J126 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[1].concentration` | Filter-sterilized 10% NaCO3 solution | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J126 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | methanol_utilizing_bacteria_medium_b | {"id": "CultureMech:003144", "name": "methanol_utilizing_bacteria_medium_b", "notes": "JCM Medium 126 supplements Methanol-Utilizing Bacteria Medium B with filter-sterilized 10% NaCO3 solution to adjust pH to 9.0.", "path": "data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_b.yaml", "relationship": "SUPPLEMENTED_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Methanol-utilizing bacteria medium B | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J126 | {<br>                        "recipe_order": 1,<br>                        "compound": "Methanol-utilizing bacteria medium B",<br>                        "compound_id": 1633,<br>                        "attribute": "see Medium No. 79",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J126 | {<br>                        "step": "Adjust pH to 9.0 with filter-sterilized 10% NaCO3 solution."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
