# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_4346_Solution_B.yaml
- ID: CultureMech:013349
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ae4e4e9b2161da98ec475d4e356db0cff14043a9c81c49b667cf2c3357753f56`
- Proposed/result SHA256: `c8e14de15154372d8361c9bd7b8e5e2613d4d4346aa07cdd3443b66c8079080a`
- Source: https://mediadive.dsmz.de/rest/solution/4346
- Source SHA256: 3b51169106ab2e8137914017ca9bce9cd3ad21a7b7cd1a74728a3b325acc6fb8
- Retrieved: 2026-10-07T09:42:56.949548+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sodium oleate | {"unit": "G_PER_L", "value": "1.5"} | {"unit": "G_PER_L", "value": "1.5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4346 | {<br>                "recipe_order": 1,<br>                "compound": "Sodium oleate",<br>                "compound_id": 1801,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.15,<br>                "unit": "g",<br>                "g_l": 1.5,<br>                "mmol_l": 4.92703,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1801) | Provider explicitly reports g_l=1.5. Arithmetic check: 0.15 g * 1 g/g / (100 ml / 1000 ml per L) = 1.5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4346 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
