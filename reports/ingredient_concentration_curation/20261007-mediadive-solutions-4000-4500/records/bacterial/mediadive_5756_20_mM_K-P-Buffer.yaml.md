# Solution Concentration Review: 20 mM K-P-Buffer

- Record: data/normalized_yaml/bacterial/mediadive_5756_20_mM_K-P-Buffer.yaml
- ID: CultureMech:014612
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `4db728d8a6f4942ab91d090841e11cc86a5a3b399f4bd05e82b42a229f9be208`
- Proposed/result SHA256: `4db728d8a6f4942ab91d090841e11cc86a5a3b399f4bd05e82b42a229f9be208`
- Source: https://mediadive.dsmz.de/rest/solution/5756
- Source SHA256: be835a8d8677261cebc3a066fe0a70344f45c3983bc0880be751aa531d9c0ecd
- Retrieved: 2026-10-07T09:58:04.110669+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "2.26429"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5756 | {<br>                "recipe_order": 1,<br>                "compound": "K2HPO4",<br>                "compound_id": 10,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.1 M",<br>                "amount": 130,<br>                "unit": "ml",<br>                "g_l": 2.26429,<br>                "mmol_l": 13,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=10) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "0.952595"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5756 | {<br>                "recipe_order": 2,<br>                "compound": "KH2PO4",<br>                "compound_id": 11,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.1 M",<br>                "amount": 70,<br>                "unit": "ml",<br>                "g_l": 0.952595,<br>                "mmol_l": 7,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=11) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "800"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5756 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 800,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
