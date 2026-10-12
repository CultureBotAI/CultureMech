# Solution Concentration Review: Main sol. J75

- Record: data/normalized_yaml/bacterial/mediadive_3701_Main_sol_J75.yaml
- ID: CultureMech:012783
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `11c4761dc102f9abb72181394dcf7e3370e0f15a58354b2062c0af97db3ef338`
- Proposed/result SHA256: `d0c3b9ad73e93fda4ab10f756625aa90834d39929db77ed911c069772373df3b`
- Source: https://mediadive.dsmz.de/rest/solution/3701
- Source SHA256: 1a39a02b360640197ef14b895d7655202166c6cf1114c9d55aed37250b651a8a
- Retrieved: 2026-10-07T09:24:02.253389+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Trypticase soy agar | {"unit": "G_PER_L", "value": "40"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3701 | {<br>                "recipe_order": 1,<br>                "compound": "Trypticase soy agar",<br>                "compound_id": 1617,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-BBL",<br>                "amount": 40,<br>                "unit": "g",<br>                "g_l": 40,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1617) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/3701 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
