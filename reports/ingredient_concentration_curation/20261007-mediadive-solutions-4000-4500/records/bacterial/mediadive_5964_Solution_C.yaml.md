# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_5964_Solution_C.yaml
- ID: CultureMech:014716
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b6baedf239705dbe3724b8dcf0d4d25d990512fc23356affec58024ce5252e4c`
- Proposed/result SHA256: `6244146bb03ea4b13434b77d35533ab75c87873a1c166369c23675b6baa59a23`
- Source: https://mediadive.dsmz.de/rest/solution/5964
- Source SHA256: 2a8d132806fdca7baef9d490ea8b3adde8de65e8748dde804c42675637351c1d
- Retrieved: 2026-10-07T09:59:07.685294+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na-acetate | {"unit": "G_PER_L", "value": "136"} | {"unit": "G_PER_L", "value": "136"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5964 | {<br>                "recipe_order": 2,<br>                "compound": "Na-acetate",<br>                "compound_id": 23,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.36,<br>                "unit": "g",<br>                "g_l": 136,<br>                "mmol_l": 1657.85,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=23) | Provider explicitly reports g_l=136. Arithmetic check: 1.36 g * 1 g/g / (10 ml / 1000 ml per L) = 136 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/5964 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
