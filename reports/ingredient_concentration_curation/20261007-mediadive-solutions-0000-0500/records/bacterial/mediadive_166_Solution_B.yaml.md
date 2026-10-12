# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_166_Solution_B.yaml
- ID: CultureMech:011125
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `20b7bf07043daeaa06a3fbc431c5ffccc36c4dda1b90d701eb96d8cfafa298bf`
- Proposed/result SHA256: `d7a21755878fbeeb756a4576d3b657b955ab6dd287cbb6503013271744106f7b`
- Source: https://mediadive.dsmz.de/rest/solution/166
- Source SHA256: 2627ad9ae512f69898a5c817ce8d43e9ff0deb809f716b7d18faf496c026f4ff
- Retrieved: 2026-10-07T08:20:55.051472+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Ethanol | {"unit": "PERCENT_V_V", "value": "99.99999999999999"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/166 | {<br>                "recipe_order": 1,<br>                "compound": "Ethanol",<br>                "compound_id": 201,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.3,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=201) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "900.0"} | {"unit": "L", "value": "0.0027"} | correct | https://mediadive.dsmz.de/rest/solution/166 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.7,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 2.7 ml per prepared batch: 2.7 / 1000 = 0.0027 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 3. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
