# Solution Concentration Review: MS Buffer

- Record: data/normalized_yaml/bacterial/mediadive_2297_MS_Buffer.yaml
- ID: CultureMech:011678
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f98a335d18b871b79a4e65f17ca043fc802b9df17ee06c82b20aab57c370c5ae`
- Proposed/result SHA256: `f98a335d18b871b79a4e65f17ca043fc802b9df17ee06c82b20aab57c370c5ae`
- Source: https://mediadive.dsmz.de/rest/solution/2297
- Source SHA256: a56f98af1b622ecba88f9e67acdea8a961f77c5781fb4fefc221527d4b57ef41
- Retrieved: 2026-10-07T09:11:04.777883+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaOH | {"unit": "G_PER_L", "value": "3.9997"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2297 | {<br>                "recipe_order": 1,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "mM",<br>                "g_l": 3.9997,<br>                "mmol_l": 100,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=256) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
