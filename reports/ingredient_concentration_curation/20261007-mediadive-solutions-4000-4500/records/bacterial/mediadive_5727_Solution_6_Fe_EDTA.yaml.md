# Solution Concentration Review: Solution 6 (Fe EDTA)

- Record: data/normalized_yaml/bacterial/mediadive_5727_Solution_6_Fe_EDTA.yaml
- ID: CultureMech:014589
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6ae0667cba96ff03a132b5439602d0f66a53955f63b1d970516a294aaca0dab3`
- Proposed/result SHA256: `a51e74a4ec901a24a03c2964daa0df5511381732758f4dc8237db49ad08b2270`
- Source: https://mediadive.dsmz.de/rest/solution/5727
- Source SHA256: 691036e74e14e77c4f8f34e9c38754213eb306aa409721127d611dbdeb5c4b23
- Retrieved: 2026-10-07T09:57:47.676811+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Fe(III)-EDTA | {"unit": "G_PER_L", "value": "3.8"} | {"unit": "G_PER_L", "value": "3.8"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5727 | {<br>                "recipe_order": 1,<br>                "compound": "Fe(III)-EDTA",<br>                "compound_id": 952,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3.8,<br>                "unit": "g",<br>                "g_l": 3.8,<br>                "mmol_l": 11.0447,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=952) | Provider explicitly reports g_l=3.8. Arithmetic check: 3.8 g * 1 g/g / (1000 ml / 1000 ml per L) = 3.8 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5727 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
