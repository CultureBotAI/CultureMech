# Solution Concentration Review: Main sol. J805

- Record: data/normalized_yaml/bacterial/mediadive_4754_Main_sol_J805.yaml
- ID: CultureMech:013701
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0c19e6a00899b27ae3a8578444198d1355f7e3e51fb8c139290838f59652d0d9`
- Proposed/result SHA256: `683388ceb96249761c3a916880b0808ef2087db68d2356497ddd188f814ff2af`
- Source: https://mediadive.dsmz.de/rest/solution/4754
- Source SHA256: f77c50a2179ad789eb5e53ec73597b5e2aae19ac6fa0d6476ff4d6fe544cbaf7
- Retrieved: 2026-10-07T09:47:10.843200+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | R2A Broth | {"unit": "G_PER_L", "value": "0.32"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4754 | {<br>                "recipe_order": 1,<br>                "compound": "R2A Broth",<br>                "compound_id": 1402,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "DAIGO) (Nihon Pharm. Co.",<br>                "amount": 0.32,<br>                "unit": "g",<br>                "g_l": 0.32,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1402) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4754 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
