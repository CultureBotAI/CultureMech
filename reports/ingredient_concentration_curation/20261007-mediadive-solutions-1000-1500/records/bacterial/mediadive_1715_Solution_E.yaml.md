# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_1715_Solution_E.yaml
- ID: CultureMech:011166
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `4c23cf05b3b08793302d13a5843bd998924b9ba4bcd6ba78d09615a6501a1bbb`
- Proposed/result SHA256: `cbf690c9045451ff1f5b33bf2bad59846f1b0835923f858e8aa4b045f5fba72d`
- Source: https://mediadive.dsmz.de/rest/solution/1715
- Source SHA256: a1143bb5f2f7503f1f9608b9175b25571280c7bc33b45420e0b900695d808fed
- Retrieved: 2026-10-07T08:55:46.953119+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2-fumarate | {"unit": "G_PER_L", "value": "160"} | {"unit": "G_PER_L", "value": "160"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1715 | {<br>                "recipe_order": 1,<br>                "compound": "Na2-fumarate",<br>                "compound_id": 276,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 8,<br>                "unit": "g",<br>                "g_l": 160,<br>                "mmol_l": 999.775,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=276) | Provider explicitly reports g_l=160. Arithmetic check: 8 g * 1 g/g / (50 ml / 1000 ml per L) = 1.6E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.05"} | correct | https://mediadive.dsmz.de/rest/solution/1715 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 50 ml per prepared batch: 50 / 1000 = 0.05 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
