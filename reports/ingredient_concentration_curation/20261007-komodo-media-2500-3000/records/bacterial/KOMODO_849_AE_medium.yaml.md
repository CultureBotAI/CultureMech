# KOMODO Concentration Review: AE medium

- Record: data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml
- ID: CultureMech:006656
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3c53299493bac8510d1e357092c297a071d5a7935154424e3a121838afa96829`
- Proposed/result SHA256: `3c53299493bac8510d1e357092c297a071d5a7935154424e3a121838afa96829`
- Source: https://mediadive.dsmz.de/rest/medium/849
- Source SHA256: 9d7044ae808a631adc1f91f3903f2e9267aa51618470158d2e457c4b3c65d4d8
- Retrieved: 2026-10-07T12:19:58.266207+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Glucose | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/849 | {<br>                        "recipe_order": 1,<br>                        "compound": "Glucose",<br>                        "compound_id": 5,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "mmol_l": 27.7531,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "3.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/849 | {<br>                        "recipe_order": 2,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 3,<br>                        "unit": "g",<br>                        "g_l": 3,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[2].concentration` | Peptone | {"unit": "G_PER_L", "value": "4.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/849 | {<br>                        "recipe_order": 3,<br>                        "compound": "Peptone",<br>                        "compound_id": 1,<br>                        "amount": 4,<br>                        "unit": "g",<br>                        "g_l": 4,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[3].concentration` | Absolute ethanol | {"unit": "ML_PER_L", "value": "30.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/849 | {<br>                        "recipe_order": 4,<br>                        "compound": "Absolute ethanol",<br>                        "compound_id": 788,<br>                        "amount": 30,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[4].concentration` | Glacial acetic acid | {"unit": "ML_PER_L", "value": "30.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/849 | {<br>                        "recipe_order": 5,<br>                        "compound": "Glacial acetic acid",<br>                        "compound_id": 787,<br>                        "amount": 30,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[5].concentration` | Agar | {"unit": "G_PER_L", "value": "9.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/849 | {<br>                        "recipe_order": 6,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 9,<br>                        "unit": "g",<br>                        "g_l": 9,<br>                        "mmol_l": 26.7594,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[5] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[6].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "940.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/849 | {<br>                        "recipe_order": 7,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 940,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[6] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `parent_media` | ae_medium | {"id": "CultureMech:002006", "name": "ae_medium", "notes": "KOMODO record states DSMZ Medium 849 provenance and exactly matches the single same-category DSMZ parent signature.", "path": "data/normalized_yaml/bacterial/ae_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/849 | {<br>                        "step": "Both liquid and solid media are prepared by autoclaving the medium without the addition of glacial acetic acid and absolute ethanol. Glacial acetic acid and absolute ethanol are sterilised either by filtration (use Teflon filters) or they may be autoclaved in completely closed screw cap glass bottles sealed with a Teflon coated septum. A double layer system das not appear to be essential for the growth of this organism, however, plates should be incubated in sealed containers to keep the humidity high (> 90%)."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `849`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium849.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=849' >849</a></TD>
					<TD>AE medium</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium849.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium849.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
