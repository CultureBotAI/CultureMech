# Solution Concentration Review: Solution G

- Record: data/normalized_yaml/bacterial/mediadive_1228_Solution_G.yaml
- ID: CultureMech:010722
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `78cfaeb08371368cd84809b67d6b5b942703360ff5aca4fd9533a9960b558a06`
- Proposed/result SHA256: `78cfaeb08371368cd84809b67d6b5b942703360ff5aca4fd9533a9960b558a06`
- Source: https://mediadive.dsmz.de/rest/solution/1228
- Source SHA256: 983c6f127604af2397c0696a2d50b45f3c781d9921ff8af833820db5357a8386
- Retrieved: 2026-10-07T08:50:24.304894+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Dithiothreitol | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1228 | {<br>                "recipe_order": 1,<br>                "compound": "Dithiothreitol",<br>                "compound_id": 574,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "100 mM solution",<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=574) | Optional/conditional source row needs separate formulation review. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
