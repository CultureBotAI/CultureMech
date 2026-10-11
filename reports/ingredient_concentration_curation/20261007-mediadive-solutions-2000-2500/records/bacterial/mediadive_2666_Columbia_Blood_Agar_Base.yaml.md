# Solution Concentration Review: Columbia Blood Agar Base

- Record: data/normalized_yaml/bacterial/mediadive_2666_Columbia_Blood_Agar_Base.yaml
- ID: CultureMech:011988
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e5be5342ffb17e27a0d7e6631d716ab7c18fb4d99617fdce18f26ab3cb0cc790`
- Proposed/result SHA256: `e5be5342ffb17e27a0d7e6631d716ab7c18fb4d99617fdce18f26ab3cb0cc790`
- Source: https://mediadive.dsmz.de/rest/solution/2666
- Source SHA256: 4ce8d8ea0cf41b7aea4b0955366ac22b6305d08f395220c5a9491e8e4d69229d
- Retrieved: 2026-10-07T09:14:39.988304+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Bacto peptone | {"unit": "G_PER_L", "value": "9.52381"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/2666 | unknown / not asserted | unknown / not asserted | Ambiguous source rows for this compound ID. | unchanged |
| `composition[1].concentration` | Bacto peptone | {"unit": "G_PER_L", "value": "9.52381"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/2666 | unknown / not asserted | unknown / not asserted | Ambiguous source rows for this compound ID. | unchanged |
| `composition[2].concentration` | Tryptic Digest of beef heart | {"unit": "G_PER_L", "value": "2.85714"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2666 | {<br>                "recipe_order": 3,<br>                "compound": "Tryptic Digest of beef heart",<br>                "compound_id": 662,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3,<br>                "unit": "g",<br>                "g_l": 2.85714,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=662) | No positive provider-declared stock volume | unchanged |
| `composition[3].concentration` | Corn starch | {"unit": "G_PER_L", "value": "0.952381"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2666 | {<br>                "recipe_order": 4,<br>                "compound": "Corn starch",<br>                "compound_id": 663,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 0.952381,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=663) | No positive provider-declared stock volume | unchanged |
| `composition[4].concentration` | NaCl | {"unit": "G_PER_L", "value": "4.7619"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2666 | {<br>                "recipe_order": 5,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 4.7619,<br>                "mmol_l": 81.4837,<br>                "optional": 0<br>            } | $.data.recipe[4] (compound_id=43) | No positive provider-declared stock volume | unchanged |
| `composition[5].concentration` | Agar | {"unit": "G_PER_L", "value": "14.2857"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2666 | {<br>                "recipe_order": 6,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 15,<br>                "unit": "g",<br>                "g_l": 14.2857,<br>                "mmol_l": 42.4753,<br>                "optional": 0<br>            } | $.data.recipe[5] (compound_id=3) | No positive provider-declared stock volume | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
