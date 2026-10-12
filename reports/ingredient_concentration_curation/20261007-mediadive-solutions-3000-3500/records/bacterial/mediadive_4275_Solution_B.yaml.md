# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_4275_Solution_B.yaml
- ID: CultureMech:013286
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `720d20fc32ffa06ba66397aec4b2e3ecad7e159cbd3be177d95faafc4d3ca435`
- Proposed/result SHA256: `fd4a6f0e35d7ae73d86e1bbf1319d8c93e0f909747bc21e924800b0d96f045ae`
- Source: https://mediadive.dsmz.de/rest/solution/4275
- Source SHA256: 7d8c64ba65de1b3ec99584c8d5f35f979a28dce1432c97eb08eb474a52cc626d
- Retrieved: 2026-10-07T09:42:13.176693+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sodium lactate | {"unit": "G_PER_L", "value": "22.4"} | {"unit": "G_PER_L", "value": "22.4"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4275 | {<br>                "recipe_order": 1,<br>                "compound": "Sodium lactate",<br>                "compound_id": 1392,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.24,<br>                "unit": "g",<br>                "g_l": 22.4,<br>                "mmol_l": 199.893,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1392) | Provider explicitly reports g_l=22.4. Arithmetic check: 2.24 g * 1 g/g / (100 ml / 1000 ml per L) = 22.4 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/4275 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
