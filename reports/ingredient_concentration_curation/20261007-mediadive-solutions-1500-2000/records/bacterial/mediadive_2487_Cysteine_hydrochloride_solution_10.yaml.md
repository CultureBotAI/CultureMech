# Solution Concentration Review: Cysteine hydrochloride solution (10%)

- Record: data/normalized_yaml/bacterial/mediadive_2487_Cysteine_hydrochloride_solution_10.yaml
- ID: CultureMech:011851
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `08ab2c98d078d3c28df1a54ed54fa2630983d8d95aac92a523dc367420bfff0e`
- Proposed/result SHA256: `108a8a10376dac96576dea1aecec57afd85ae45877f9a7422fd5b91d06da2166`
- Source: https://mediadive.dsmz.de/rest/solution/2487
- Source SHA256: f96d762847e9457aabd7d48e222905c90d7fdd4f42fe33b87b6f752120aa8f0e
- Retrieved: 2026-10-07T09:13:04.683162+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Cysteine hydrochloride | {"unit": "G_PER_L", "value": "100"} | {"unit": "G_PER_L", "value": "100"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2487 | {<br>                "recipe_order": 1,<br>                "compound": "Cysteine hydrochloride",<br>                "compound_id": 1114,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "g",<br>                "g_l": 100,<br>                "mmol_l": 634.437,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1114) | Provider explicitly reports g_l=100. Arithmetic check: 10 g * 1 g/g / (100 ml / 1000 ml per L) = 1.0E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2487 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
