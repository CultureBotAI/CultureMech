# Solution Concentration Review: Seawater

- Record: data/normalized_yaml/bacterial/mediadive_1801_Seawater.yaml
- ID: CultureMech:011231
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5ddd205315edef537862567ee0255fee9fc697220ca4ed8aa87eb9256ebb7dce`
- Proposed/result SHA256: `5f065e84ba52fd60223785bbca506de054f7b4767ba54fb36263e3276bbb9454`
- Source: https://mediadive.dsmz.de/rest/solution/1801
- Source SHA256: d1269f65c0917a49e9c707b4f2032533a4e059139a2353fd7e43e37b0a28bbbc
- Retrieved: 2026-10-07T08:56:31.696118+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sea Salt | {"unit": "G_PER_L", "value": "32"} | {"unit": "G_PER_L", "value": "32"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1801 | {<br>                "recipe_order": 1,<br>                "compound": "Sea Salt",<br>                "compound_id": 423,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 32,<br>                "unit": "g",<br>                "g_l": 32,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=423) | Provider explicitly reports g_l=32. Arithmetic check: 32 g * 1 g/g / (1000 ml / 1000 ml per L) = 32 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1801 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
