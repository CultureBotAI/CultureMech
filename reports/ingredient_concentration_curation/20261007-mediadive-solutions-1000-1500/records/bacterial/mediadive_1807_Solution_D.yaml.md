# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_1807_Solution_D.yaml
- ID: CultureMech:011236
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `34e6e4c7f798548aee41217c53607b4b68fe80b18a123385c465e2b3237b4d48`
- Proposed/result SHA256: `270d56cf5f4a61be2e2c5a162ad9c5cb002c2f6d70d3708fb3ba9dc66f3cca0a`
- Source: https://mediadive.dsmz.de/rest/solution/1807
- Source SHA256: 923f611ca7c370b12566454c0185c228fc93085addcbff8c8839158cc9bdcc19
- Retrieved: 2026-10-07T08:56:35.640177+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1807 | {<br>                "recipe_order": 1,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "OXOID",<br>                "amount": 0.2,<br>                "unit": "g",<br>                "g_l": 20,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=16) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/1807 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
