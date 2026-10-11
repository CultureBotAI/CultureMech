# Solution Concentration Review: Main sol. 800

- Record: data/normalized_yaml/bacterial/mediadive_1630_Main_sol_800.yaml
- ID: CultureMech:011087
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `394b716fa24d3f353cdaf5c69600fb06a110496246769d190ea7325e231d7237`
- Proposed/result SHA256: `394b716fa24d3f353cdaf5c69600fb06a110496246769d190ea7325e231d7237`
- Source: https://mediadive.dsmz.de/rest/solution/1630
- Source SHA256: f8376040d4fdab74917a46b3abf7791e32106fc4486178a8632f18b8ebd7a458
- Retrieved: 2026-10-07T08:54:50.037555+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Wilkins Chalgrene Anaerobe Broth | {"unit": "PERCENT_V_V", "value": "833.3333333333333"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1630 | {<br>                "recipe_order": 1,<br>                "compound": "Wilkins Chalgrene Anaerobe Broth",<br>                "compound_id": 2140,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Oxoid CM 643",<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2140) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | 5-Aminovaleric acid | {"unit": "PERCENT_V_V", "value": "41.666666666666664"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1630 | {<br>                "recipe_order": 2,<br>                "compound": "5-Aminovaleric acid",<br>                "compound_id": 538,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "w/v) NaHCO3 (flushed with N2 + CO2",<br>                "amount": 0.5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=538) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Fildes Enrichment | {"unit": "PERCENT_V_V", "value": "83.33333333333333"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1630 | {<br>                "recipe_order": 3,<br>                "compound": "Fildes Enrichment",<br>                "compound_id": 744,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BBL 20810) (under N2",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=744) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[3].concentration` | 3-Hydroxybenzoic acid | {"unit": "PERCENT_V_V", "value": "8.333333333333334"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/1630 | unknown / not asserted | unknown / not asserted | Ambiguous source rows for this compound ID. | unchanged |
| `composition[4].concentration` | 3-Hydroxybenzoic acid | {"unit": "PERCENT_V_V", "value": "8.333333333333334"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/1630 | unknown / not asserted | unknown / not asserted | Ambiguous source rows for this compound ID. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
