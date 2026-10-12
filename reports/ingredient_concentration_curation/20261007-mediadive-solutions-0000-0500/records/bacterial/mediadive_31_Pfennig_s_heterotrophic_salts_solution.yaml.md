# Solution Concentration Review: Pfennig's heterotrophic salts solution

- Record: data/normalized_yaml/bacterial/mediadive_31_Pfennig_s_heterotrophic_salts_solution.yaml
- ID: CultureMech:012400
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c1c8869ce16109a8025261592039f3b7698b8c4221c896e2783f2250b6c4629d`
- Proposed/result SHA256: `c1c8869ce16109a8025261592039f3b7698b8c4221c896e2783f2250b6c4629d`
- Source: https://mediadive.dsmz.de/rest/solution/31
- Source SHA256: 8e1ea438988ea13a9b741f6425004f1bb232dac6673fb84f93f0047c2bdaa89c
- Retrieved: 2026-10-07T08:19:30.824708+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Ammonium chloride | {"unit": "G_PER_L", "value": "13.4615"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/31 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `composition[1].concentration` | Ammonium acetate | {"unit": "G_PER_L", "value": "9.61539"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/31 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `composition[2].concentration` | Pyruvic acid sodium salt | {"unit": "G_PER_L", "value": "9.61539"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/31 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `composition[3].concentration` | Dextrose | {"unit": "G_PER_L", "value": "9.61539"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/31 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `composition[4].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "19.2308"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/31 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `composition[5].concentration` | KCl | {"unit": "G_PER_L", "value": "13.4615"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/31 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `composition[6].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "13.4615"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/31 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `composition[7].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "961.5384615384615"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/31 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/31 | unknown / not asserted | unknown / not asserted | Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review. | unchanged |
| `source.recipe[5]` | Trace element solution SL-12 B | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/31 | {<br>                "recipe_order": 8,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Trace element solution SL-12 B",<br>                "solution_id": 33,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[5] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
