# Solution Concentration Review: Main sol. 1621

- Record: data/normalized_yaml/bacterial/mediadive_3368_Main_sol_1621.yaml
- ID: CultureMech:012516
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2ad4b07451cbc0e7ee6c8ff07da9ca939a04fa33317212a1626f2ee3a36c2845`
- Proposed/result SHA256: `9abe4c86ba7462cf0e9435e9f397dd0b73fd7117207bf8edc27ad9dc9ee84e27`
- Source: https://mediadive.dsmz.de/rest/solution/3368
- Source SHA256: 14d8e5362ea3dd32ddc7f763c802d1ce09867c3faf4d1ce815118c376134cee5
- Retrieved: 2026-10-07T09:20:50.856125+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Marine Broth | {"unit": "G_PER_L", "value": "7.48"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3368 | {<br>                "recipe_order": 1,<br>                "compound": "Marine Broth",<br>                "compound_id": 545,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Becton Dickinson",<br>                "amount": 7.48,<br>                "unit": "g",<br>                "g_l": 7.48,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=545) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Sea water | {"unit": "PERCENT_V_V", "value": "750"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3368 | {<br>                "recipe_order": 2,<br>                "compound": "Sea water",<br>                "compound_id": 286,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "artificial",<br>                "amount": 750,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=286) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "250"} | {"unit": "L", "value": "0.25"} | correct | https://mediadive.dsmz.de/rest/solution/3368 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 250,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Source water addition is 250 ml per prepared batch: 250 / 1000 = 0.25 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
