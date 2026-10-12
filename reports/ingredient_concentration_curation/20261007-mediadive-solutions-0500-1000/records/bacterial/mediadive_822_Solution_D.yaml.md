# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_822_Solution_D.yaml
- ID: CultureMech:015192
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `4959a3eb8fb7afd965fca245c9d11947ef719da63a77ffe8cd4e9783c3fc8346`
- Proposed/result SHA256: `4959a3eb8fb7afd965fca245c9d11947ef719da63a77ffe8cd4e9783c3fc8346`
- Source: https://mediadive.dsmz.de/rest/solution/822
- Source SHA256: e8e28e91f7a6fe616457a21e9b880f004adc44ac944aa353cebc277f7cb2622c
- Retrieved: 2026-10-07T08:46:51.371064+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Rabbit serum | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/822 | {<br>                "recipe_order": 1,<br>                "compound": "Rabbit serum",<br>                "compound_id": 464,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "",<br>                "attribute": "inactivated, GIBCO 037-06120M",<br>                "amount": 86,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": 526320,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=464) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
