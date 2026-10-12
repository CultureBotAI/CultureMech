# Solution Concentration Review: Fe-EDTA complex

- Record: data/normalized_yaml/bacterial/mediadive_6421_Fe-EDTA_complex.yaml
- ID: CultureMech:015025
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `480504a4993bbc791e3e91ead9249959b690cf93f13713dc4256a2b60508a2d8`
- Proposed/result SHA256: `67426b8f2c80b4914fcf317adf8d1bcb70fda79bb4ddf0b94c45c2a4d8daf752`
- Source: https://mediadive.dsmz.de/rest/solution/6421
- Source SHA256: c0e70dc0fc8b520da4536d93328f179fb0d838df16609a91850cabced2623de7
- Retrieved: 2026-10-07T10:02:38.158164+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeCl3 x 6 H2O | {"unit": "G_PER_L", "value": "0.27"} | {"unit": "G_PER_L", "value": "0.27"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6421 | {<br>                "recipe_order": 1,<br>                "compound": "FeCl3 x 6 H2O",<br>                "compound_id": 82,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 135,<br>                "unit": "mg",<br>                "g_l": 0.27,<br>                "mmol_l": 0.998905,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=82) | Provider explicitly reports g_l=0.27. Arithmetic check: 135 mg * 0.001 g/mg / (500 ml / 1000 ml per L) = 0.27 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 500. | applied |
| `composition[1].concentration` | Na2-EDTA x 2 H2O | {"unit": "G_PER_L", "value": "0.372"} | {"unit": "G_PER_L", "value": "0.372"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6421 | {<br>                "recipe_order": 2,<br>                "compound": "Na2-EDTA x 2 H2O",<br>                "compound_id": 676,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 186,<br>                "unit": "mg",<br>                "g_l": 0.372,<br>                "mmol_l": 1.10646,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=676) | Provider explicitly reports g_l=0.372. Arithmetic check: 186 mg * 0.001 g/mg / (500 ml / 1000 ml per L) = 0.372 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 500. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
