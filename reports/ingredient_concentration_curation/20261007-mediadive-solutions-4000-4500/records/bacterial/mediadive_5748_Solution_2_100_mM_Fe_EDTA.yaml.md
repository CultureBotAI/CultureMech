# Solution Concentration Review: Solution 2 (100 mM Fe EDTA)

- Record: data/normalized_yaml/bacterial/mediadive_5748_Solution_2_100_mM_Fe_EDTA.yaml
- ID: CultureMech:014603
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7830180c74665dc297ccf47b9656851554ea4bee1a9fd8fd173574785b127155`
- Proposed/result SHA256: `8edd76fa9e0888e87ec1ebf76ec322c78b8ac69ae460a1566249fc03263cb2eb`
- Source: https://mediadive.dsmz.de/rest/solution/5748
- Source SHA256: 98dac034a1871e97006694190fecb13eb858fdf08bb63d14643b9fa560cebd92
- Retrieved: 2026-10-07T09:57:57.828610+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Fe(III)-EDTA | {"unit": "G_PER_L", "value": "36.05"} | {"unit": "G_PER_L", "value": "36.05"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5748 | {<br>                "recipe_order": 1,<br>                "compound": "Fe(III)-EDTA",<br>                "compound_id": 952,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 36.05,<br>                "unit": "g",<br>                "g_l": 36.05,<br>                "mmol_l": 104.779,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=952) | Provider explicitly reports g_l=36.05. Arithmetic check: 36.05 g * 1 g/g / (1000 ml / 1000 ml per L) = 36.05 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5748 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
