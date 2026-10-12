# Solution Concentration Review: Peptone mixture

- Record: data/normalized_yaml/bacterial/mediadive_5567_Peptone_mixture.yaml
- ID: CultureMech:014445
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c393fec4d073aebbcbbf471731d8ae66242661fdd96ce083fe88645c0a2b2c77`
- Proposed/result SHA256: `608e324a091e15e9f8a4a32f24dd411b10d75f1b5c3f677b611037ff7474ce72`
- Source: https://mediadive.dsmz.de/rest/solution/5567
- Source SHA256: 58f8ab24fdc251078688fa94f5d1b55cfe990793f6bb84469128ae14cf7a2d30
- Retrieved: 2026-10-07T09:56:06.114561+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Tryptone peptone | {"unit": "G_PER_L", "value": "32"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5567 | {<br>                "recipe_order": 1,<br>                "compound": "Tryptone peptone",<br>                "compound_id": 164,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Difco 0123-17",<br>                "amount": 1.6,<br>                "unit": "g",<br>                "g_l": 32,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=164) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Casamino acids | {"unit": "G_PER_L", "value": "32"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5567 | {<br>                "recipe_order": 2,<br>                "compound": "Casamino acids",<br>                "compound_id": 101,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Difco 0230-17",<br>                "amount": 1.6,<br>                "unit": "g",<br>                "g_l": 32,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=101) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "32"} | {"unit": "G_PER_L", "value": "32"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5567 | {<br>                "recipe_order": 3,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.6,<br>                "unit": "g",<br>                "g_l": 32,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=16) | Provider explicitly reports g_l=32. Arithmetic check: 1.6 g * 1 g/g / (50 ml / 1000 ml per L) = 32 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
