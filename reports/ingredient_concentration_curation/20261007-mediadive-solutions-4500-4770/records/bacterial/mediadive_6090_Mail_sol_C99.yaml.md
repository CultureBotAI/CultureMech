# Solution Concentration Review: Mail sol. C99

- Record: data/normalized_yaml/bacterial/mediadive_6090_Mail_sol_C99.yaml
- ID: CultureMech:014796
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5eb24446655268ba6c36e048d69fb42b81e5eeec5bbe962ff7e82f13429452b7`
- Proposed/result SHA256: `5eb24446655268ba6c36e048d69fb42b81e5eeec5bbe962ff7e82f13429452b7`
- Source: https://mediadive.dsmz.de/rest/solution/6090
- Source SHA256: de2e509010543ea7ed9566d193fa8d598aaf00f758b92fc40d7ff66bb3afe514
- Retrieved: 2026-10-07T10:00:00.095215+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Soil | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6090 | {<br>                "recipe_order": 2,<br>                "compound": "Soil",<br>                "compound_id": 2350,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "air-dried, sieved, garden loam",<br>                "amount": null,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2350) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
