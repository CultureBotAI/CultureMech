# Solution Concentration Review: Main sol. J730

- Record: data/normalized_yaml/bacterial/mediadive_4656_Main_sol_J730.yaml
- ID: CultureMech:013614
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `114204de729aea327e40523180347d0a4ea0fa8187668749b7128a119b2d3556`
- Proposed/result SHA256: `90403c47bc1f38de5c293f5e800528997c4e06072a8abe9c68cd8fbcb9118642`
- Source: https://mediadive.dsmz.de/rest/solution/4656
- Source SHA256: 1d48057a6402188c7896f6294cf4e396e6383e8aace07384ee5e273e959340c8
- Retrieved: 2026-10-07T09:46:06.580590+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Lactobacilli MRS broth | {"unit": "G_PER_L", "value": "55"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4656 | {<br>                "recipe_order": 1,<br>                "compound": "Lactobacilli MRS broth",<br>                "compound_id": 1711,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 55,<br>                "unit": "g",<br>                "g_l": 55,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1711) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "100"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/4656 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[1]` | Rye-bran extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4656 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Rye-bran extract",<br>                "solution_id": 4657,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 900,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
