# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_759_Solution_C.yaml
- ID: CultureMech:015144
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0e17d3fe03e80f288fe58f0a035131c85b4ed80f8ed34acf6a82559d87cb6297`
- Proposed/result SHA256: `cf946745fd6336d1fcb91871840b319ca87b2e44513d89de48cc95b82efc40fb`
- Source: https://mediadive.dsmz.de/rest/solution/759
- Source SHA256: 9c2195ca3f8d134ab0169c44fb364172df1e0427b0a08a8057e8a608d6c163d2
- Retrieved: 2026-10-07T08:46:19.965265+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na-pyruvate | {"unit": "G_PER_L", "value": "250"} | {"unit": "G_PER_L", "value": "250"} | evidence_only | https://mediadive.dsmz.de/rest/solution/759 | {<br>                "recipe_order": 1,<br>                "compound": "Na-pyruvate",<br>                "compound_id": 113,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 250,<br>                "mmol_l": 2271.82,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=113) | Provider explicitly reports g_l=250. Arithmetic check: 1 g * 1 g/g / (4 ml / 1000 ml per L) = 2.5E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 4. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.004"} | correct | https://mediadive.dsmz.de/rest/solution/759 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 4,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 4 ml per prepared batch: 4 / 1000 = 0.004 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 4. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
