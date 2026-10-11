# Solution Concentration Review: Solution 2 (Fe EDTA)

- Record: data/normalized_yaml/bacterial/mediadive_5670_Solution_2_Fe_EDTA.yaml
- ID: CultureMech:014535
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `066bacd59fe11b6ddb5d23d83b6fea198bb6b2f85f3c46f78e1453a9da40be69`
- Proposed/result SHA256: `5f04bddc73faae499e3f845514533a0e54ed7f18f26b8cbd810502d832f27b9d`
- Source: https://mediadive.dsmz.de/rest/solution/5670
- Source SHA256: 737a720d3051e2293cd3f011c79b3802d20bdcacae745f4e8a466c79298e627a
- Retrieved: 2026-10-07T09:57:08.708312+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Fe(III)-EDTA | {"unit": "G_PER_L", "value": "3.8"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5670 | {<br>                "recipe_order": 5,<br>                "compound": "Fe(III)-EDTA",<br>                "compound_id": 952,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Sigma, 03650",<br>                "amount": 3.8,<br>                "unit": "g",<br>                "g_l": 3.8,<br>                "mmol_l": 11.0447,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=952) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5670 | {<br>                "recipe_order": 6,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
