# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_1077_Solution_E.yaml
- ID: CultureMech:010592
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `fd86c3280b1ea5a174125052ca89d08db3276a2d422c0e2f3fe01b8b18d2fa4f`
- Proposed/result SHA256: `31f80bdfad715cf279765b09093d04dae17c0b5ec6ef25996597f99ac7669314`
- Source: https://mediadive.dsmz.de/rest/solution/1077
- Source SHA256: a474f459029d9ff461264714d665c09895ab81af349852428ad98d43c8ebcb07
- Retrieved: 2026-10-07T08:48:51.416999+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2HAsO4 x 7 H2O | {"unit": "G_PER_L", "value": "310"} | {"unit": "G_PER_L", "value": "310"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1077 | {<br>                "recipe_order": 1,<br>                "compound": "Na2HAsO4 x 7 H2O",<br>                "compound_id": 520,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3.1,<br>                "unit": "g",<br>                "g_l": 310,<br>                "mmol_l": 993.545,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=520) | Provider explicitly reports g_l=310. Arithmetic check: 3.1 g * 1 g/g / (10 ml / 1000 ml per L) = 3.1E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/1077 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
