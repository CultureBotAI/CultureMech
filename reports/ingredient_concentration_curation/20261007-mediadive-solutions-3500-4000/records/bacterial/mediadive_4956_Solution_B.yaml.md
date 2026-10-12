# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_4956_Solution_B.yaml
- ID: CultureMech:013879
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `68190da66614c7d54a2d0ebf4cfc8e119a448dc13cb7c40ab2f87ab4c6fd52ad`
- Proposed/result SHA256: `ef4913f0dbe551f1171a78a7ae047f39f3b1147b475a1127cc8172509a19c8ed`
- Source: https://mediadive.dsmz.de/rest/solution/4956
- Source SHA256: bf6ccd6e27372a591af9ef85da0746c2d056f71706a8f62e0c9a20fcbe514e20
- Retrieved: 2026-10-07T09:49:19.761499+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | MgCl2 x 6 H2O | {"unit": "G_PER_L", "value": "80"} | {"unit": "G_PER_L", "value": "80"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4956 | {<br>                "recipe_order": 1,<br>                "compound": "MgCl2 x 6 H2O",<br>                "compound_id": 79,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.8,<br>                "unit": "g",<br>                "g_l": 80,<br>                "mmol_l": 393.501,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=79) | Provider explicitly reports g_l=80. Arithmetic check: 0.8 g * 1 g/g / (10 ml / 1000 ml per L) = 8E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/4956 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
