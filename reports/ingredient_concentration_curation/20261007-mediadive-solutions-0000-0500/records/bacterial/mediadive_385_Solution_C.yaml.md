# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_385_Solution_C.yaml
- ID: CultureMech:012933
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f91ec75ccfc4ef529bb8300fcbb8a9a6ef0b574fc51f9fd699734f49d3138f66`
- Proposed/result SHA256: `ec1f8780270b5a741df476fc8c83dd3a033736a5058204609f8c938d2bfc0fce`
- Source: https://mediadive.dsmz.de/rest/solution/385
- Source SHA256: 6b52ca6049ae9b2bec1eea72b41f614843cfcd576fd2375f9e6d902a40c10180
- Retrieved: 2026-10-07T08:23:01.496800+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na-propionate | {"unit": "G_PER_L", "value": "150"} | {"unit": "G_PER_L", "value": "150"} | evidence_only | https://mediadive.dsmz.de/rest/solution/385 | {<br>                "recipe_order": 1,<br>                "compound": "Na-propionate",<br>                "compound_id": 301,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.5,<br>                "unit": "g",<br>                "g_l": 150,<br>                "mmol_l": 1561.52,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=301) | Provider explicitly reports g_l=150. Arithmetic check: 1.5 g * 1 g/g / (10 ml / 1000 ml per L) = 1.5E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/385 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
