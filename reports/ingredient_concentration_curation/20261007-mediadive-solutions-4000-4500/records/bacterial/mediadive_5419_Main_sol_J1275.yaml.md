# Solution Concentration Review: Main sol. J1275

- Record: data/normalized_yaml/bacterial/mediadive_5419_Main_sol_J1275.yaml
- ID: CultureMech:014331
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `da7a028b608c7c893173c9bb4d831dbb05029be4fd098ed571a43785e684e86f`
- Proposed/result SHA256: `1e928cd18dae492a8d3f17dbecc9fbed0dd7c47115ac2c8e0327e3640c8645e0`
- Source: https://mediadive.dsmz.de/rest/solution/5419
- Source SHA256: c0f8a50042ef7eba2c3b729a810dd09839c54d49adeb179a718dfcc69cf17314
- Retrieved: 2026-10-07T09:54:46.777982+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Tryptone | {"unit": "G_PER_L", "value": "0.5"} | {"unit": "G_PER_L", "value": "0.5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5419 | {<br>                "recipe_order": 2,<br>                "compound": "Tryptone",<br>                "compound_id": 71,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.5,<br>                "unit": "g",<br>                "g_l": 0.5,<br>                "mmol_l": 7.03433,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=71) | Provider explicitly reports g_l=0.5. Arithmetic check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Modified Brock's salt base solution | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5419 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Modified Brock's salt base solution",<br>                "solution_id": 3819,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
