# Solution Concentration Review: Main sol. 1638

- Record: data/normalized_yaml/bacterial/mediadive_3402_Main_sol_1638.yaml
- ID: CultureMech:012542
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1b0d66806c7782f16c2ad9e125df7ce9b494d643b248676e2b3e0c3c4672b4ea`
- Proposed/result SHA256: `1b0d66806c7782f16c2ad9e125df7ce9b494d643b248676e2b3e0c3c4672b4ea`
- Source: https://mediadive.dsmz.de/rest/solution/3402
- Source SHA256: b0a27e5f22dda8b39c395f0aa16e2af0cae58c79f1372ab13160fc62f67c4256
- Retrieved: 2026-10-07T09:21:09.757833+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | MEM-Medium | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3402 | {<br>                "recipe_order": 1,<br>                "compound": "MEM-Medium",<br>                "compound_id": 1377,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Gibco 31095-029",<br>                "amount": 1,<br>                "unit": "x",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1377) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
