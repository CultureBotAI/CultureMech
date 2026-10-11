# Solution Concentration Review: Cellobiose (10%)

- Record: data/normalized_yaml/bacterial/mediadive_3461_Cellobiose_10.yaml
- ID: CultureMech:012586
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `01acbbd4443283e7e40f2efefc9cf853f430e991669a19042f3b7469ffdd9422`
- Proposed/result SHA256: `d3ae7bb2b6ac06161a2bd390477c0fbdc8c76894b6dab40c1b70b0589a03396b`
- Source: https://mediadive.dsmz.de/rest/solution/3461
- Source SHA256: 3aa071ca58a01cee5d40abf820c5a2ddc57997b8e0394b2a2f1c8046dae2cfb9
- Retrieved: 2026-10-07T09:21:41.057357+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3461 | {<br>                "recipe_order": 1,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `composition[1].concentration` | Cellobiose | {"unit": "G_PER_L", "value": "100"} | {"unit": "G_PER_L", "value": "100"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3461 | {<br>                "recipe_order": 2,<br>                "compound": "Cellobiose",<br>                "compound_id": 214,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "g",<br>                "g_l": 100,<br>                "mmol_l": 292.141,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=214) | Provider explicitly reports g_l=100. Arithmetic check: 10 g * 1 g/g / (100 ml / 1000 ml per L) = 1.0E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
