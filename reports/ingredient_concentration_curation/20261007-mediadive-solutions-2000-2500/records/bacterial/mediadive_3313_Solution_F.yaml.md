# Solution Concentration Review: Solution F

- Record: data/normalized_yaml/bacterial/mediadive_3313_Solution_F.yaml
- ID: CultureMech:012475
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `03ef3e859ca94db8676de3bb992f1675a2c2ece088fd957538cc98eb2c8ed2a1`
- Proposed/result SHA256: `03ef3e859ca94db8676de3bb992f1675a2c2ece088fd957538cc98eb2c8ed2a1`
- Source: https://mediadive.dsmz.de/rest/solution/3313
- Source SHA256: fe72d5c5381c56542b4b7a4ff06d01ed8b3521152afb18ee9640a16c6a04e6d6
- Retrieved: 2026-10-07T09:20:18.676578+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Methanol | {"unit": "G_PER_L", "value": "792"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3313 | {<br>                "recipe_order": 1,<br>                "compound": "Methanol",<br>                "compound_id": 226,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "ml",<br>                "g_l": 792,<br>                "mmol_l": 24717.6,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=226) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
