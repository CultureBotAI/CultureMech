# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_2550_Solution_E.yaml
- ID: CultureMech:011893
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `695fe791918dd6fdb55f12453f5447960a841014036bdc82381f2a5789aef06a`
- Proposed/result SHA256: `695fe791918dd6fdb55f12453f5447960a841014036bdc82381f2a5789aef06a`
- Source: https://mediadive.dsmz.de/rest/solution/2550
- Source SHA256: f2ba250905410ac2686433aaf43065734b7729349d8c74e6dc2eb6a5e1d8a063
- Retrieved: 2026-10-07T09:13:32.188032+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Toluene | {"unit": "PERCENT_V_V", "value": "580.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2550 | {<br>                "recipe_order": 1,<br>                "compound": "Toluene",<br>                "compound_id": 1820,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 58,<br>                "unit": "\u00b5l",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1820) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2550 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
