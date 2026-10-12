# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_1076_Solution_B.yaml
- ID: CultureMech:010591
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `02f96568d36d37b351884ad59d148006aeeb6cfa2612bfd4c1587b4affd7567c`
- Proposed/result SHA256: `506d270c87d649aee5f2b778d3796321b1ff823a57e96c1e1928c5d06707068f`
- Source: https://mediadive.dsmz.de/rest/solution/1076
- Source SHA256: 0aca9cb4773a7b8f38b239a9c839057233ca3a33f54751d475297cc3993f03e0
- Retrieved: 2026-10-07T08:48:50.624701+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2CO3 | {"unit": "G_PER_L", "value": "50"} | {"unit": "G_PER_L", "value": "50"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1076 | {<br>                "recipe_order": 1,<br>                "compound": "Na2CO3",<br>                "compound_id": 32,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.5,<br>                "unit": "g",<br>                "g_l": 50,<br>                "mmol_l": 471.752,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=32) | Provider explicitly reports g_l=50. Arithmetic check: 1.5 g * 1 g/g / (30 ml / 1000 ml per L) = 5E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 30. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0000000000001"} | {"unit": "L", "value": "0.03"} | correct | https://mediadive.dsmz.de/rest/solution/1076 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 30,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 30 ml per prepared batch: 30 / 1000 = 0.03 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 30. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
