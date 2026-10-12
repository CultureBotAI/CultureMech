# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_111_Solution_B.yaml
- ID: CultureMech:010622
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `11a0b268b1670aeded646aae97872b57eebd2edcd7b387c56236ebf085379a07`
- Proposed/result SHA256: `dfa487b86e16bc5ba5a816cd4f67e89ebe380b0ed29cef2cf0840476c094b875`
- Source: https://mediadive.dsmz.de/rest/solution/111
- Source SHA256: eeeeb9ceedba3a2d515b0c4913b4c832e101e739c48aa7a18a0874439af8bbc9
- Retrieved: 2026-10-07T08:20:24.934511+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "2"} | {"unit": "G_PER_L", "value": "2"} | evidence_only | https://mediadive.dsmz.de/rest/solution/111 | {<br>                "recipe_order": 1,<br>                "compound": "MgSO4 x 7 H2O",<br>                "compound_id": 8,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.1,<br>                "unit": "g",<br>                "g_l": 2,<br>                "mmol_l": 8.11438,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=8) | Provider explicitly reports g_l=2. Arithmetic check: 0.1 g * 1 g/g / (50 ml / 1000 ml per L) = 2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.05"} | correct | https://mediadive.dsmz.de/rest/solution/111 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 50 ml per prepared batch: 50 / 1000 = 0.05 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
