# Solution Concentration Review: Lactic acid whey

- Record: data/normalized_yaml/bacterial/mediadive_911_Lactic_acid_whey.yaml
- ID: CultureMech:015267
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f0aa2a1ff2d3a79325a01db32bd57c353c26af7cf78e626b416a1f3d4f7aa438`
- Proposed/result SHA256: `f0aa2a1ff2d3a79325a01db32bd57c353c26af7cf78e626b416a1f3d4f7aa438`
- Source: https://mediadive.dsmz.de/rest/solution/911
- Source SHA256: c8f20acb7884d23ee7c2d3cc113b72bbda31b7fb22f401f754ed36b9131815d4
- Retrieved: 2026-10-07T08:47:44.328307+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Skim milk | {"unit": "G_PER_L", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/911 | {<br>                "recipe_order": 1,<br>                "compound": "Skim milk",<br>                "compound_id": 262,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "%",<br>                "g_l": 100,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=262) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
