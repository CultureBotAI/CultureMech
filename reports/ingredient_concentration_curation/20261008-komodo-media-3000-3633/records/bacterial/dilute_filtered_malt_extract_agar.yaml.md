# KOMODO Concentration Review: DILUTE FILTERED MALT EXTRACT AGAR

- Record: data/normalized_yaml/bacterial/dilute_filtered_malt_extract_agar.yaml
- ID: CultureMech:004153
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `da0951e3b56ee611032a2cd01e949a2bb23e1a19cb9e59dcc95a3d7d465d9ab7`
- Proposed/result SHA256: `da0951e3b56ee611032a2cd01e949a2bb23e1a19cb9e59dcc95a3d7d465d9ab7`
- Source: https://mediadive.dsmz.de/rest/medium/1427
- Source SHA256: 89312343bb3c35c65a6a6ce30fc120b840bb2cfbf3486301b61ea6036a223ff1
- Retrieved: 2026-10-07T13:41:42.069980+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Malt extract | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1427 | {<br>                        "recipe_order": 1,<br>                        "compound": "Malt extract",<br>                        "compound_id": 116,<br>                        "attribute": "food grade",<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 50,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[1].concentration` | Agar | {"unit": "G_PER_L", "value": "15.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1427 | {<br>                        "recipe_order": 3,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 150,<br>                        "mmol_l": 445.991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1427 | {<br>                        "recipe_order": 2,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 100,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1427 | {<br>                        "recipe_order": 3,<br>                        "step": "Autoclave for 15 min. and filter the cooled liquid until clear; fill up to 1 L. "<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
| `source.data.solutions[0].steps[1]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1427 | {<br>                        "step": "Autoclave at 121\u00b0C for 15 min."<br>                    } | $.data.solutions[0].steps[1] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `1427`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1427.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1427' >1427</a></TD>
					<TD>DILUTE FILTERED MALT EXTRACT AGAR</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1427.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1427.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
