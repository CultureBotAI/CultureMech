# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_2119_Solution_B.yaml
- ID: CultureMech:011519
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0be0b283b9b7b84ba9cfd0425a0b6bc56a3cf1dad7d2269c5550fd2f6c1961a0`
- Proposed/result SHA256: `84adca26aefc5a4f478ed7c4c8010ee3d3666a8e364b6f217baa2253696139bd`
- Source: https://mediadive.dsmz.de/rest/solution/2119
- Source SHA256: 852a625c44e27890cae8b3b8f9a4415134d8c91a52ca36f2a6338dba11a2d8a5
- Retrieved: 2026-10-07T09:09:12.396482+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2SeO4 | {"unit": "G_PER_L", "value": "189"} | {"unit": "G_PER_L", "value": "189"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2119 | {<br>                "recipe_order": 1,<br>                "compound": "Na2SeO4",<br>                "compound_id": 375,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.89,<br>                "unit": "g",<br>                "g_l": 189,<br>                "mmol_l": 1000.26,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=375) | Provider explicitly reports g_l=189. Arithmetic check: 1.89 g * 1 g/g / (10 ml / 1000 ml per L) = 189 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/2119 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
