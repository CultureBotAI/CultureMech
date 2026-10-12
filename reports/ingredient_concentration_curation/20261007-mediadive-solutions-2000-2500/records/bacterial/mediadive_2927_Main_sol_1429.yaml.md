# Solution Concentration Review: Main sol. 1429

- Record: data/normalized_yaml/bacterial/mediadive_2927_Main_sol_1429.yaml
- ID: CultureMech:012180
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6cf066c6579fdff7d84f8af00c3f71eae4361c67285d02c964d37b41295af832`
- Proposed/result SHA256: `c0d6465c65de33dec20535b90255b747eff24b7e5455aeac55c3423e7ea9d10f`
- Source: https://mediadive.dsmz.de/rest/solution/2927
- Source SHA256: 0ea6d852c2a6d4c71b34649d7df7fa9ce1cbb2cd141c13c9bd06282a2277a4e2
- Retrieved: 2026-10-07T09:16:53.100163+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | SABOURAUD- Glucose-Bouillon | {"unit": "G_PER_L", "value": "30"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2927 | {<br>                "recipe_order": 1,<br>                "compound": "SABOURAUD- Glucose-Bouillon",<br>                "compound_id": 1279,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Merck 108339, 2 %",<br>                "amount": 30,<br>                "unit": "g",<br>                "g_l": 30,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1279) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | {"unit": "G_PER_L", "value": "15"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2927 | {<br>                "recipe_order": 2,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 15,<br>                "unit": "g",<br>                "g_l": 15,<br>                "mmol_l": 44.5991,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=3) | Provider explicitly reports g_l=15. Arithmetic check: 15 g * 1 g/g / (1000 ml / 1000 ml per L) = 15 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/2927 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
