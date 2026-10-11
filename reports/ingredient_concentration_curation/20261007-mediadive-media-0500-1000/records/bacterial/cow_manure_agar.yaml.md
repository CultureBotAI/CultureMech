# Medium Concentration Review: COW MANURE AGAR

**Corrected by follow-up:** the [applied extraction repair](../../../20261007-extraction-boundaries/657.md)
separates manure and initial water from the recovered extract, removes the
unsupported manure concentration, and records the source-explicit one-liter
make-up before agar addition. The original rows and hashes below remain historical.

- Record: data/normalized_yaml/bacterial/cow_manure_agar.yaml
- ID: CultureMech:001794
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `db28722a4fd5b89c72a6634f63f72dbc38d30ac0a4a0d7806173bf8222f4ffd6`
- Proposed/result SHA256: `f2cc6b272b650efa43d6298a9cd644f0f7498beb5c4ed54d52fe8ab6c29d2dd4`
- Source: https://mediadive.dsmz.de/rest/medium/657
- Source SHA256: 298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51
- Retrieved: 2026-10-07T12:17:06.429209+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Dry cow-manure | {"unit": "G_PER_L", "value": "50"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/657 | {<br>                        "recipe_order": 1,<br>                        "compound": "Dry cow-manure",<br>                        "compound_id": 2131,<br>                        "amount": 50,<br>                        "unit": "g",<br>                        "g_l": 50,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Extraction input and recovered medium are different preparation stages. Source g_l alone cannot establish retained solids or extract yield; explicit input-loading evidence and stock-boundary review are required. | unchanged |
| `ingredients[1].concentration` | Tap water | {"unit": "G_PER_L", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/657 | {<br>                        "recipe_order": 2,<br>                        "compound": "Tap water",<br>                        "compound_id": 322,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Liquid dose, percent basis, molar conversion, or other unit needs source-specific review; no water-based final volume is inferred. | unchanged |
| `ingredients[2].concentration` | Agar | {"unit": "G_PER_L", "value": "20"} | {"unit": "G_PER_L", "value": "20"} | evidence_only | https://mediadive.dsmz.de/rest/medium/657 | {<br>                        "recipe_order": 3,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 59.4654,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Provider explicitly reports g_l=20; check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) = 20 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. | applied |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/657 | {<br>                        "step": "Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first through cheesecloth and then paper. Make up volume to one liter. Add 20 g agar."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
