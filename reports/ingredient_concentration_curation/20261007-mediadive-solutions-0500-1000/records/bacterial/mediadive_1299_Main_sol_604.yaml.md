# Solution Concentration Review: Main sol. 604

- Record: data/normalized_yaml/bacterial/mediadive_1299_Main_sol_604.yaml
- ID: CultureMech:010788
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `faad64cd435fe35f50b197da8cc1c1e9146091aef32ed317356602abe3dc5108`
- Proposed/result SHA256: `faad64cd435fe35f50b197da8cc1c1e9146091aef32ed317356602abe3dc5108`
- Source: https://mediadive.dsmz.de/rest/solution/1299
- Source SHA256: d0e95627710dfce41f5422c4433d721b61da4979e95378d3b9f8b6f18fadc797
- Retrieved: 2026-10-07T08:51:13.505473+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Marine agar 2216 | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1299 | {<br>                "recipe_order": 1,<br>                "compound": "Marine agar 2216",<br>                "compound_id": 1628,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Difco 0979",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1628) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
