# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_861_Solution_C.yaml
- ID: CultureMech:015223
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c5d4e26c30b9a9ec01b9998836678e8c6ff55f58651c00e9835f314b2ecc9cba`
- Proposed/result SHA256: `6ea699080e476dee2f41989f46e52ec7effc5b0034fb909bbdf0a736a369783a`
- Source: https://mediadive.dsmz.de/rest/solution/861
- Source SHA256: adc7ac5036144f6c12d456b47e3fd25ca1b3df7a40de3cced40d23bbfa4580f0
- Retrieved: 2026-10-07T08:47:13.618463+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Ferric ammonium citrate | {"unit": "G_PER_L", "value": "2.5"} | {"unit": "G_PER_L", "value": "2.5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/861 | {<br>                "recipe_order": 1,<br>                "compound": "Ferric ammonium citrate",<br>                "compound_id": 97,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.05,<br>                "unit": "g",<br>                "g_l": 2.5,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=97) | Provider explicitly reports g_l=2.5. Arithmetic check: 0.05 g * 1 g/g / (20 ml / 1000 ml per L) = 2.5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 20. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.02"} | correct | https://mediadive.dsmz.de/rest/solution/861 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 20 ml per prepared batch: 20 / 1000 = 0.02 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 20. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
