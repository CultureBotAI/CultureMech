# KOMODO Concentration Review: YPS medium

- Record: data/normalized_yaml/bacterial/KOMODO_1168_YPS_medium.yaml
- ID: CultureMech:003886
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3bde5e87b3a35c67f7432ddfb3577fbf74064181f18e12a7061002f1a650467c`
- Proposed/result SHA256: `3bde5e87b3a35c67f7432ddfb3577fbf74064181f18e12a7061002f1a650467c`
- Source: https://mediadive.dsmz.de/rest/medium/1168
- Source SHA256: dd3d4058458d0f6aa2b214867669d8aa8bf61e0dbf22fcb817bd81ce3bdfd1fa
- Retrieved: 2026-10-07T13:18:16.287077+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "4.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1168 | {<br>                        "recipe_order": 1,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 4,<br>                        "unit": "g",<br>                        "g_l": 4,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[1].concentration` | Peptone | {"unit": "G_PER_L", "value": "2.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1168 | {<br>                        "recipe_order": 2,<br>                        "compound": "Peptone",<br>                        "compound_id": 1,<br>                        "amount": 2,<br>                        "unit": "g",<br>                        "g_l": 2,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[2].concentration` | Sea Salt | {"unit": "G_PER_L", "value": "25.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1168 | {<br>                        "recipe_order": 3,<br>                        "compound": "Sea Salt",<br>                        "compound_id": 423,<br>                        "attribute": "Sigma",<br>                        "amount": 25,<br>                        "unit": "g",<br>                        "g_l": 25,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[3].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1168 | {<br>                        "recipe_order": 4,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[4].concentration` | Agar | {"unit": "G_PER_L", "value": "15.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1168 | {<br>                        "recipe_order": 5,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "condition": "for solid medium",<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `parent_media` | yps_medium | {"id": "CultureMech:000610", "name": "yps_medium", "notes": "KOMODO record explicitly cites DSMZ Medium 1168; one unlinked DSMZ parent record exists and the local physical state, pH, ingredient, and concentration signatures match exactly.", "path": "data/normalized_yaml/bacterial/yps_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1168 | {<br>                        "step": "Agar may be added (15 g/l) to solidify the medium."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `1168`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1168.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1168' >1168</a></TD>
					<TD>YPS medium</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1168.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1168.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
