# Solution Concentration Review: Ammonium chloride solution

- Record: data/normalized_yaml/bacterial/mediadive_6306_Ammonium_chloride_solution.yaml
- ID: CultureMech:014978
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5d7372a71e8c18d5b21819feadde4f7e8c87dbe8c8a08fde815a2b3ef9c52552`
- Proposed/result SHA256: `4fb30d1266382157a46158be066c28868165bfb2241e49f3ef757176b23dd2a1`
- Source: https://mediadive.dsmz.de/rest/solution/6306
- Source SHA256: d9c50e795c7a5280bae3ef8c048cee2c339a520ef4989ca174bc7d00a777dc5d
- Retrieved: 2026-10-07T10:02:09.301657+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Ammonium chloride | {"unit": "G_PER_L", "value": "8"} | {"unit": "G_PER_L", "value": "8"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6306 | {<br>                "recipe_order": 2,<br>                "compound": "Ammonium chloride",<br>                "compound_id": 57,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.8,<br>                "unit": "g",<br>                "g_l": 8,<br>                "mmol_l": 149.561,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=57) | Provider explicitly reports g_l=8. Arithmetic check: 0.8 g * 1 g/g / (100 ml / 1000 ml per L) = 8 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/6306 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
