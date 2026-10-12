# Solution Concentration Review: Solution G

- Record: data/normalized_yaml/bacterial/mediadive_2124_Solution_G.yaml
- ID: CultureMech:011524
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `38835f2b9a7c0a1e946a18d8f71ef5d334485f5ab2eb42da6f5d8c25ba6d0954`
- Proposed/result SHA256: `ef1a5bba1b3b8f85ee1e1679c16b0e0aadfe7cec986ea6057c9aa121efa842b5`
- Source: https://mediadive.dsmz.de/rest/solution/2124
- Source SHA256: ec04efe208cf7fdbdada3a836f4c0dcb13ed85a155ad93fe4e40c919e7bbf9ab
- Retrieved: 2026-10-07T09:09:15.514257+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "900.0"} | {"unit": "L", "value": "0.009"} | correct | https://mediadive.dsmz.de/rest/solution/2124 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 9,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 9 ml per prepared batch: 9 / 1000 = 0.009 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Trace element solution SL-10 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2124 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Trace element solution SL-10",<br>                "solution_id": 595,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
