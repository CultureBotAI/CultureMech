# Solution Concentration Review: Riboflavin solution 0.0013986 g/L

- Record: data/normalized_yaml/bacterial/mediadive_5546_Riboflavin_solution_0_0013986_g_L.yaml
- ID: CultureMech:014424
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `39c24c357005e21c52f054ef459f8ae15c18c1b7758e986e7546ee462a91b547`
- Proposed/result SHA256: `7c9d9ff2a6f0cb39305b75e85ce1307ec85617267efcfe5b26fa1e0ccd890a8f`
- Source: https://mediadive.dsmz.de/rest/solution/5546
- Source SHA256: d2786dfc0112d7028782bef7278e704985897344c64286aa54c539e715c0a0e1
- Retrieved: 2026-10-07T09:55:51.211193+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Riboflavin | {"unit": "G_PER_L", "value": "0.0013986"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/5546 | {<br>                "recipe_order": 1,<br>                "compound": "Riboflavin",<br>                "compound_id": 136,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "mg",<br>                "g_l": 0.0013986,<br>                "mmol_l": 0.00371573,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=136) | Source g_l disagrees with amount/unit/volume | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/5546 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
