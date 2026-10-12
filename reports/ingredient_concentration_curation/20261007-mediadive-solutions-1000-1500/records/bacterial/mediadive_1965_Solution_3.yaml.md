# Solution Concentration Review: Solution 3

- Record: data/normalized_yaml/bacterial/mediadive_1965_Solution_3.yaml
- ID: CultureMech:011368
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a7a1ff0dae2dd8db4e7b396ae94882d01e3542cd81e49de69bd52c2c3942afb6`
- Proposed/result SHA256: `25af1e03919c91e07589fe096574e4c321e5b8d1a2e8c6ce901c664a23441d60`
- Source: https://mediadive.dsmz.de/rest/solution/1965
- Source SHA256: cd07b748162e5fc66d00e24cb37f498bad1e971b9ba359431e455d7a8cc22ed4
- Retrieved: 2026-10-07T08:58:10.776603+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeCl2 x 4 H2O | {"unit": "G_PER_L", "value": "0.04"} | {"unit": "G_PER_L", "value": "0.04"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1965 | {<br>                "recipe_order": 1,<br>                "compound": "FeCl2 x 4 H2O",<br>                "compound_id": 260,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "mg",<br>                "g_l": 0.04,<br>                "mmol_l": 0.201195,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=260) | Provider explicitly reports g_l=0.04. Arithmetic check: 2 mg * 0.001 g/mg / (50 ml / 1000 ml per L) = 0.04 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.05"} | correct | https://mediadive.dsmz.de/rest/solution/1965 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 50 ml per prepared batch: 50 / 1000 = 0.05 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
