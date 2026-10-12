# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_1400_Solution_B.yaml
- ID: CultureMech:010885
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `228596c5bab716f42024d68bddc2b9abd72952ba76f84696b72c05d342067308`
- Proposed/result SHA256: `67de7cff85a2ba5012f1e9bc12ce9b5e40ba5f46938c9d41af6d3db6048a12fe`
- Source: https://mediadive.dsmz.de/rest/solution/1400
- Source SHA256: ba63409063c2f917fe037941870d243507868a7d3186bf2256c558f57e7a3f7a
- Retrieved: 2026-10-07T08:52:24.826844+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "146.844"} | {"unit": "G_PER_L", "value": "146.844"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1400 | {<br>                "recipe_order": 1,<br>                "compound": "FeSO4 x 7 H2O",<br>                "compound_id": 12,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 44.2,<br>                "unit": "g",<br>                "g_l": 146.844,<br>                "mmol_l": 528.187,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=12) | Provider explicitly reports g_l=146.844. Arithmetic check: 44.2 g * 1 g/g / (301 ml / 1000 ml per L) = 146.8438538205980066445182724 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 301. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "996.6777408637873"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1400 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 300,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `composition[2].concentration` | H2SO4 | {"unit": "PERCENT_V_V", "value": "3.3222591362126246"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1400 | {<br>                "recipe_order": 3,<br>                "compound": "H2SO4",<br>                "compound_id": 122,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "10 N",<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=122) | Optional/conditional source row needs separate formulation review. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
