# Solution Concentration Review: Methanol solution

- Record: data/normalized_yaml/bacterial/mediadive_4592_Methanol_solution.yaml
- ID: CultureMech:013556
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `afa8c90dfb15faa6b18d85f3cbf84ebff037ba5dc848ba22490b1ef41b38d514`
- Proposed/result SHA256: `f36850fa2429f111f60f9ae1746ad9ce5a55c5861d7220e8cd9dbbdcf1c30c8e`
- Source: https://mediadive.dsmz.de/rest/solution/4592
- Source SHA256: 65b2a0f190c0c4dbbbfb0c0654608eb43b1a9d48078e7898d95d67bcc77eb533
- Retrieved: 2026-10-07T09:45:24.495179+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Methanol | {"unit": "PERCENT_V_V", "value": "43.84615384615384"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4592 | {<br>                "recipe_order": 1,<br>                "compound": "Methanol",<br>                "compound_id": 226,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.28,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=226) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "961.5384615384615"} | {"unit": "L", "value": "0.05"} | correct | https://mediadive.dsmz.de/rest/solution/4592 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 50 ml per prepared batch: 50 / 1000 = 0.05 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 52. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
