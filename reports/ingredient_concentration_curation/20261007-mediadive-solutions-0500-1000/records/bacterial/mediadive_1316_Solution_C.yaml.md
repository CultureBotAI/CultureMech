# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_1316_Solution_C.yaml
- ID: CultureMech:010803
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9a2366b77fcbce0976973a388c7e06b953629bc1e7d90f5c0ef46681376f5a0e`
- Proposed/result SHA256: `75f0132955ee22829bf2057afd88a48c37f7d51498217f8db3dc4e08573948c0`
- Source: https://mediadive.dsmz.de/rest/solution/1316
- Source SHA256: 4686a6f2a3d761a3db62df7ab3c8993dbe4ff5d653a45017c28469394c0a1e87
- Retrieved: 2026-10-07T08:51:23.820275+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na-butyrate | {"unit": "G_PER_L", "value": "120"} | {"unit": "G_PER_L", "value": "120"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1316 | {<br>                "recipe_order": 1,<br>                "compound": "Na-butyrate",<br>                "compound_id": 232,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.2,<br>                "unit": "g",<br>                "g_l": 120,<br>                "mmol_l": 1090.05,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=232) | Provider explicitly reports g_l=120. Arithmetic check: 1.2 g * 1 g/g / (10 ml / 1000 ml per L) = 1.2E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/1316 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
