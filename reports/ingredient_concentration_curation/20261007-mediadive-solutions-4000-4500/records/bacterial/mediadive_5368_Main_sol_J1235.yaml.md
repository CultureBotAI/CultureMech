# Solution Concentration Review: Main sol. J1235

- Record: data/normalized_yaml/bacterial/mediadive_5368_Main_sol_J1235.yaml
- ID: CultureMech:014278
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c9c4e9cf75fa924dd7f11e47bf095fe1e762768116c9ef0da5d46aa8d7a06745`
- Proposed/result SHA256: `c56e3ee4086ae59dfd0c8c839b76a59f29e996687092a5a999671e0eabe481b6`
- Source: https://mediadive.dsmz.de/rest/solution/5368
- Source SHA256: 7ee45bab447efd4079672c7a09aa4627b2dd380c2a406992d396dbb9897c84f4
- Retrieved: 2026-10-07T09:54:07.227861+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | R2A agar | {"unit": "G_PER_L", "value": "18.2"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5368 | {<br>                "recipe_order": 1,<br>                "compound": "R2A agar",<br>                "compound_id": 1844,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 18.2,<br>                "unit": "g",<br>                "g_l": 18.2,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1844) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Disodium fumarate | {"unit": "G_PER_L", "value": "3.2"} | {"unit": "G_PER_L", "value": "3.2"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5368 | {<br>                "recipe_order": 2,<br>                "compound": "Disodium fumarate",<br>                "compound_id": 1076,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3.2,<br>                "unit": "g",<br>                "g_l": 3.2,<br>                "mmol_l": 19.995,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1076) | Provider explicitly reports g_l=3.2. Arithmetic check: 3.2 g * 1 g/g / (1000 ml / 1000 ml per L) = 3.2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5368 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
