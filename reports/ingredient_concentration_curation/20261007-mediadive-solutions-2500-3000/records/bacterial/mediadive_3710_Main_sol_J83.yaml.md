# Solution Concentration Review: Main sol. J83

- Record: data/normalized_yaml/bacterial/mediadive_3710_Main_sol_J83.yaml
- ID: CultureMech:012792
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1c7ac62031faa04e4ee5bbccd6dd6cd512cb16a004cb9e809bc7d0264b1f232e`
- Proposed/result SHA256: `478c5b600ce7f0c478e0d846da8e184363b9a656c370ee59ad0ae58ab706e9e6`
- Source: https://mediadive.dsmz.de/rest/solution/3710
- Source SHA256: 1a81bc582d77a67c745f3fd3e1bda94525a005369b3800b69cfdd90b52cf320f
- Retrieved: 2026-10-07T09:24:08.497798+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | GAM broth | {"unit": "G_PER_L", "value": "59"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3710 | {<br>                "recipe_order": 1,<br>                "compound": "GAM broth",<br>                "compound_id": 1620,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Nissui",<br>                "amount": 59,<br>                "unit": "g",<br>                "g_l": 59,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1620) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/3710 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
