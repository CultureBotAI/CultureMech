# Medium Concentration Review: HALF STRENGTH NUTRIENT BROTH OR AGAR

- Record: data/normalized_yaml/bacterial/half_strength_nutrient_broth_or_agar.yaml
- ID: CultureMech:001813
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `500b5425cfd52fe8bc3f3c9d861adc945e69046bf860d0db912818418ba330cd`
- Proposed/result SHA256: `500b5425cfd52fe8bc3f3c9d861adc945e69046bf860d0db912818418ba330cd`
- Source: https://mediadive.dsmz.de/rest/medium/672
- Source SHA256: ffdc3f9b74f2e911232956c1a8d0c0aa4fba54b5ff5ad27a7e334b773b48bffd
- Retrieved: 2026-10-07T12:17:21.065007+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Difco 0003 or Difco 0001 | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/672 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Difco 0001, Difco 0003 or Difco 0001 | unchanged |
| `variant_children[0]` | half_strength_nutrient_broth_or_agar | {"id": "CultureMech:006268", "name": "half_strength_nutrient_broth_or_agar", "notes": "KOMODO Medium 672 is a source-catalogue duplicate of DSMZ Medium 672.", "path": "data/normalized_yaml/bacterial/KOMODO_672_HALF_STRENGTH_NUTRIENT_BROTH_OR_AGAR.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Difco 0001 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/672 | {<br>                        "recipe_order": 1,<br>                        "compound": "Difco 0001",<br>                        "compound_id": 2132,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/672 | {<br>                        "step": "Difco 0003 or Difco 0001"<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
