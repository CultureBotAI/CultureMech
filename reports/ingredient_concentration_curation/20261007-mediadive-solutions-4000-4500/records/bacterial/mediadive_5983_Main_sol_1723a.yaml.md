# Solution Concentration Review: Main sol. 1723a

- Record: data/normalized_yaml/bacterial/mediadive_5983_Main_sol_1723a.yaml
- ID: CultureMech:014724
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `612cab8abd19b08a9adcc7d0dba7cd352c38e226256d83e2dbe93d68817852f9`
- Proposed/result SHA256: `612cab8abd19b08a9adcc7d0dba7cd352c38e226256d83e2dbe93d68817852f9`
- Source: https://mediadive.dsmz.de/rest/solution/5983
- Source SHA256: d526b1360010ce60487d33bdf93a1def815aa91a15dc147eb147905046e86a2e
- Retrieved: 2026-10-07T09:59:12.354733+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Artificial Sea Salt | {"unit": "G_PER_L", "value": "12.4"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/5983 | unknown / not asserted | unknown / not asserted | Exact solution ID/name mismatch; do not substitute a similar formulation. | unchanged |
| `composition[1].concentration` | NaNO3 | {"unit": "G_PER_L", "value": "0.075"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/5983 | unknown / not asserted | unknown / not asserted | Exact solution ID/name mismatch; do not substitute a similar formulation. | unchanged |
| `composition[2].concentration` | NaH2PO4 x H2O | {"unit": "G_PER_L", "value": "0.005"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/5983 | unknown / not asserted | unknown / not asserted | Exact solution ID/name mismatch; do not substitute a similar formulation. | unchanged |
| `composition[3].concentration` | Wheat Grains | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/5983 | unknown / not asserted | unknown / not asserted | Exact solution ID/name mismatch; do not substitute a similar formulation. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/5983 | unknown / not asserted | unknown / not asserted | Exact solution ID/name mismatch; do not substitute a similar formulation. | unchanged |
| `source.recipe[3]` | f/2 Trace Metal Mix | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5983 | {<br>                "recipe_order": 4,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "f/2 Trace Metal Mix",<br>                "solution_id": 5854,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[4]` | Vitamin 3 Mix | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5983 | {<br>                "recipe_order": 8,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Vitamin 3 Mix",<br>                "solution_id": 5855,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[4] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
