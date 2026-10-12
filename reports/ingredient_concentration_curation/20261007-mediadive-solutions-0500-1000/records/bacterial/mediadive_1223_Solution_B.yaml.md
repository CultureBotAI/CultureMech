# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_1223_Solution_B.yaml
- ID: CultureMech:010719
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e23fc06ab311a701db482ed48f502d5d4a536a14a07ab7fb3149f68991d6c2b1`
- Proposed/result SHA256: `e23fc06ab311a701db482ed48f502d5d4a536a14a07ab7fb3149f68991d6c2b1`
- Source: https://mediadive.dsmz.de/rest/solution/1223
- Source SHA256: e5d9317f958c7489a3972f22e6dab2b94f0384b1e1a31a8e0e10f1a78832cba8
- Retrieved: 2026-10-07T08:50:21.957870+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaHCO3 | {"unit": "PERCENT_V_V", "value": "1000.0000000000001"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1223 | {<br>                "recipe_order": 1,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "5% w/v solution",<br>                "attribute": null,<br>                "amount": 30,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=55) | Optional/conditional source row needs separate formulation review. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
