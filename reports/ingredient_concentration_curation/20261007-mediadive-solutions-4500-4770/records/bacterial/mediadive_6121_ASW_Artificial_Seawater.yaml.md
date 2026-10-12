# Solution Concentration Review: ASW (Artificial Seawater)

- Record: data/normalized_yaml/bacterial/mediadive_6121_ASW_Artificial_Seawater.yaml
- ID: CultureMech:014825
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6ca60fa5a28ed1387f0c296962da726eb0223c8ad360a039151278dc6413b73a`
- Proposed/result SHA256: `178b5ab4af4b546c075b8a6e5939e21f4763f96f8e2925a126324aa27df553b4`
- Source: https://mediadive.dsmz.de/rest/solution/6121
- Source SHA256: 065763f1463ccf734e00da627c82a0edca08937139b9da5933ac2751c8657503
- Retrieved: 2026-10-07T10:00:19.715576+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Tricine | {"unit": "G_PER_L", "value": "0.5"} | {"unit": "G_PER_L", "value": "0.5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6121 | {<br>                "recipe_order": 2,<br>                "compound": "Tricine",<br>                "compound_id": 2349,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.5,<br>                "unit": "g",<br>                "g_l": 0.5,<br>                "mmol_l": 2.79065,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2349) | Provider explicitly reports g_l=0.5. Arithmetic check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[1]` | Extra salts | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6121 | {<br>                "recipe_order": 3,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Extra salts",<br>                "solution_id": 6122,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3.75,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[2]` | SE1 (Soil Extract 1) | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6121 | {<br>                "recipe_order": 4,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "SE1 (Soil Extract 1)",<br>                "solution_id": 6251,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 25,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
