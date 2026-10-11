# Solution Concentration Review: L-Cysteine 10% w/v

- Record: data/normalized_yaml/bacterial/mediadive_6565_L-Cysteine_10_w_v.yaml
- ID: CultureMech:015064
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `67f252654cbaf6382c7edba359c1250e97f94720e60b007b90c81594893a0235`
- Proposed/result SHA256: `df640672fb25e933ff7d5aab0116bb6a58a4059e0e0ce32888f2b2f0dc4e6109`
- Source: https://mediadive.dsmz.de/rest/solution/6565
- Source SHA256: 7509fdfd46d94ec10d31c422519ef5022b6eaa6923cc134ef858ad3d2ea55f30
- Retrieved: 2026-10-07T10:03:00.130578+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | L-Cysteine | {"unit": "G_PER_L", "value": "100"} | {"unit": "G_PER_L", "value": "100"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6565 | {<br>                "recipe_order": 2,<br>                "compound": "L-Cysteine",<br>                "compound_id": 671,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "g",<br>                "g_l": 100,<br>                "mmol_l": 825.355,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=671) | Provider explicitly reports g_l=100. Arithmetic check: 10 g * 1 g/g / (100 ml / 1000 ml per L) = 1.0E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
