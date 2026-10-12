# Solution Concentration Review: Main sol. J1293

- Record: data/normalized_yaml/bacterial/mediadive_5443_Main_sol_J1293.yaml
- ID: CultureMech:014349
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `30a90352f85c50932dd4bf7d9f1d930c972b403fce5bada22a351e951fdbe8b1`
- Proposed/result SHA256: `470750ee023db9cbfec40a341779bd4b690db79c55e129d581eaceb763803c5c`
- Source: https://mediadive.dsmz.de/rest/solution/5443
- Source SHA256: 963d6bdcdaefedb23e6002a84302747dfcd8c5d02dafabc53c4f191899c11cc6
- Retrieved: 2026-10-07T09:55:00.959635+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Ferrihydrite | {"unit": "G_PER_L", "value": "1.97628"} | {"unit": "G_PER_L", "value": "1.97628"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5443 | {<br>                "recipe_order": 2,<br>                "compound": "Ferrihydrite",<br>                "compound_id": 2057,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "g",<br>                "g_l": 1.97628,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2057) | Provider explicitly reports g_l=1.97628. Arithmetic check: 2 g * 1 g/g / (1012 ml / 1000 ml per L) = 1.976284584980237154150197628 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1012. | applied |
| `composition[1].concentration` | NaHCO3 | {"unit": "PERCENT_V_V", "value": "12.351778656126482"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5443 | {<br>                "recipe_order": 3,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "8%",<br>                "amount": 12.5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=55) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Modified MJ synthetic seawater C | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5443 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Modified MJ synthetic seawater C",<br>                "solution_id": 5444,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
