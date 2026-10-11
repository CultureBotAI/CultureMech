# Solution Concentration Review: Main sol. 465i

- Record: data/normalized_yaml/bacterial/mediadive_957_Main_sol_465i.yaml
- ID: CultureMech:015294
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5cd7c1e487db34e1bf80f3c0273c044f0505f430601f0a14f3d1536569c4ad50`
- Proposed/result SHA256: `5cd7c1e487db34e1bf80f3c0273c044f0505f430601f0a14f3d1536569c4ad50`
- Source: https://mediadive.dsmz.de/rest/solution/957
- Source SHA256: 4395a3d0ead8de23b34c3e45c3b6288b1caba6250adae27afa84bc3dbfe8d1f9
- Retrieved: 2026-10-07T08:48:03.295134+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | 2-chloro-4(ethylamino)-6-(isopropylamino)-1,3,5-triazine | {"unit": "MG_PER_L", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/957 | {<br>                "recipe_order": 1,<br>                "compound": "2-chloro-4(ethylamino)-6-(isopropylamino)-1,3,5-triazine",<br>                "compound_id": 2120,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "adjust if required",<br>                "attribute": "suspend 10 mg/ml in methanol",<br>                "amount": 100,<br>                "unit": "mg/l",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2120) | Optional/conditional source row needs separate formulation review. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[1]` | Main sol. 465 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/957 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 465",<br>                "solution_id": 945,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
