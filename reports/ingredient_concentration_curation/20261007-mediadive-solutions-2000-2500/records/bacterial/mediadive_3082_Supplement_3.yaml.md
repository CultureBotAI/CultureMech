# Solution Concentration Review: Supplement 3

- Record: data/normalized_yaml/bacterial/mediadive_3082_Supplement_3.yaml
- ID: CultureMech:012307
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `335cfb2b4d7aa33521aee30be034b49e4b28d12487f6f9c186c7e90fd7dd059a`
- Proposed/result SHA256: `335cfb2b4d7aa33521aee30be034b49e4b28d12487f6f9c186c7e90fd7dd059a`
- Source: https://mediadive.dsmz.de/rest/solution/3082
- Source SHA256: 21dfee5cf1a01ec1328e0d74a36454634599cc7a664ba2ec58f85a9ad916d756
- Retrieved: 2026-10-07T09:18:20.612651+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Glutathione | {"unit": "G_PER_L", "value": "153.66"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3082 | {<br>                "recipe_order": 1,<br>                "compound": "Glutathione",<br>                "compound_id": 1819,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.5,<br>                "unit": "M",<br>                "g_l": 153.66,<br>                "mmol_l": 500,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1819) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3082 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
