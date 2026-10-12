# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_732_Solution_C.yaml
- ID: CultureMech:015138
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `8383668af45ea59d257ffc4f1b592e787122686a79cb1b93e5815154154e68ff`
- Proposed/result SHA256: `ea30ae5cec0c7a48783c69e27f4c8e7182e556cabd375939eded878b20534ca8`
- Source: https://mediadive.dsmz.de/rest/solution/732
- Source SHA256: 4174daf85ddcd40def7152816e139b007b2087df30e787c76ceb3559f2ee0790
- Retrieved: 2026-10-07T08:46:16.848916+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na-pyruvate | {"unit": "G_PER_L", "value": "125"} | {"unit": "G_PER_L", "value": "125"} | evidence_only | https://mediadive.dsmz.de/rest/solution/732 | {<br>                "recipe_order": 2,<br>                "compound": "Na-pyruvate",<br>                "compound_id": 113,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.5,<br>                "unit": "g",<br>                "g_l": 125,<br>                "mmol_l": 1135.91,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=113) | Provider explicitly reports g_l=125. Arithmetic check: 2.5 g * 1 g/g / (20 ml / 1000 ml per L) = 125 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 20. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.02"} | correct | https://mediadive.dsmz.de/rest/solution/732 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 20 ml per prepared batch: 20 / 1000 = 0.02 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 20. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
