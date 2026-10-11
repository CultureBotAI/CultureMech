# Solution Concentration Review: Solution G

- Record: data/normalized_yaml/bacterial/mediadive_1493_Solution_G.yaml
- ID: CultureMech:010963
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3ebbe4e5cfdea07375d4b125bf5566fa2bcdb299ac0da12377dd0940f5264180`
- Proposed/result SHA256: `3ebbe4e5cfdea07375d4b125bf5566fa2bcdb299ac0da12377dd0940f5264180`
- Source: https://mediadive.dsmz.de/rest/solution/1493
- Source SHA256: ebb473273c9122c02fedb7f161ac3be509938e8a1463941d3df31ed5ea6f61c5
- Retrieved: 2026-10-07T08:53:20.157401+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Hexadecane | {"unit": "PERCENT_V_V", "value": "900.0000000000001"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1493 | {<br>                "recipe_order": 1,<br>                "compound": "Hexadecane",<br>                "compound_id": 687,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 13.5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=687) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Tetrachloroethene | {"unit": "PERCENT_V_V", "value": "100.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1493 | {<br>                "recipe_order": 2,<br>                "compound": "Tetrachloroethene",<br>                "compound_id": 688,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=688) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
