# Solution Concentration Review: Glutathione solution 14%(w/v)

- Record: data/normalized_yaml/bacterial/mediadive_5570_Glutathione_solution_14_w_v.yaml
- ID: CultureMech:014449
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7bc5ca6c31eba13b544a50222540940efd3a072de356ef13be0ad815181a9dd8`
- Proposed/result SHA256: `7060bf84cb7b7b324c4bde2e79456f221264e9e3a4c299b0fa73bc4b29b0d192`
- Source: https://mediadive.dsmz.de/rest/solution/5570
- Source SHA256: ec08cbf407132c16f005322027a3297053726ba31e6212562618ead165fd826d
- Retrieved: 2026-10-07T09:56:08.464536+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Glutathione | {"unit": "G_PER_L", "value": "140"} | {"unit": "G_PER_L", "value": "140"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5570 | {<br>                "recipe_order": 1,<br>                "compound": "Glutathione",<br>                "compound_id": 1819,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 7,<br>                "unit": "g",<br>                "g_l": 140,<br>                "mmol_l": 455.551,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1819) | Provider explicitly reports g_l=140. Arithmetic check: 7 g * 1 g/g / (50 ml / 1000 ml per L) = 1.4E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5570 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
