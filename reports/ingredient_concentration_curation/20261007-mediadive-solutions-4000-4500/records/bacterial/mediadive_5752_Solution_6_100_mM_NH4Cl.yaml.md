# Solution Concentration Review: Solution 6 (100 mM NH4Cl)

- Record: data/normalized_yaml/bacterial/mediadive_5752_Solution_6_100_mM_NH4Cl.yaml
- ID: CultureMech:014608
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ba623a462a196f5240e21a1abd74073674a06a4018e943d7e6847cdf40a05aab`
- Proposed/result SHA256: `f2dc07b44f62c51dd48b060238de533faa5e38611f1ec54cbd2e8a2d768348f9`
- Source: https://mediadive.dsmz.de/rest/solution/5752
- Source SHA256: 78d6b800c7c77eab61e82b833a472d0f99f54413bb59e76167be7bb2aaa3e98a
- Retrieved: 2026-10-07T09:58:00.992309+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NH4Cl | {"unit": "G_PER_L", "value": "5.3"} | {"unit": "G_PER_L", "value": "5.3"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5752 | {<br>                "recipe_order": 1,<br>                "compound": "NH4Cl",<br>                "compound_id": 42,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5.3,<br>                "unit": "g",<br>                "g_l": 5.3,<br>                "mmol_l": 99.0839,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=42) | Provider explicitly reports g_l=5.3. Arithmetic check: 5.3 g * 1 g/g / (1000 ml / 1000 ml per L) = 5.3 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5752 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
