# KOMODO Concentration Review: GINGER BEER PLANT medium

- Record: data/normalized_yaml/bacterial/KOMODO_267_GINGER_BEER_PLANT_medium.yaml
- ID: CultureMech:004670
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0e4a18f1ebdd1287fb58ae79a57dbf589b17f4df5c7f015c7d513380f9e475bc`
- Proposed/result SHA256: `7ec47986b2218552368f3bb5b1dc6c53abbeb71659001794bc6499c98963b166`
- Source: https://mediadive.dsmz.de/rest/medium/267
- Source SHA256: 711d5a81a5598202f48d430372e88209c4d9505a401a14c4168e2620aaeb62f1
- Retrieved: 2026-10-07T10:44:38.351147+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Sugar beet molasses | {"unit": "G_PER_L", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/267 | {<br>                        "recipe_order": 1,<br>                        "compound": "Sugar beet molasses",<br>                        "compound_id": 346,<br>                        "amount": 100,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Liquid dose, percent basis, molar conversion, or other unit needs source-specific review; no water-based final volume is inferred. | unchanged |
| `ingredients[1].concentration` | Ginger | {"unit": "G_PER_L", "value": "1.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/267 | {<br>                        "recipe_order": 2,<br>                        "compound": "Ginger",<br>                        "compound_id": 347,<br>                        "condition": "",<br>                        "attribute": "powdered",<br>                        "amount": 1.5,<br>                        "unit": "g",<br>                        "g_l": 1.5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[2].concentration` | Citric acid | {"unit": "G_PER_L", "value": "1.5"} | {"unit": "G_PER_L", "value": "1.5"} | evidence_only | https://mediadive.dsmz.de/rest/medium/267 | {<br>                        "recipe_order": 3,<br>                        "compound": "Citric acid",<br>                        "compound_id": 348,<br>                        "amount": 1.5,<br>                        "unit": "g",<br>                        "g_l": 1.5,<br>                        "mmol_l": 7.80762,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Provider explicitly reports g_l=1.5; check: 1.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 267 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `ingredients[3].concentration` | Tap water | {"unit": "G_PER_L", "value": "900"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/267 | {<br>                        "recipe_order": 4,<br>                        "compound": "Tap water",<br>                        "compound_id": 322,<br>                        "amount": 900,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Liquid dose, percent basis, molar conversion, or other unit needs source-specific review; no water-based final volume is inferred. | unchanged |
| `parent_media` | ginger_beer_plant_medium | {"id": "CultureMech:001366", "name": "ginger_beer_plant_medium", "notes": "KOMODO record explicitly cites DSMZ Medium 267; one unlinked DSMZ parent record exists and the local physical state, pH, ingredient, and concentration signatures match exactly.", "path": "data/normalized_yaml/bacterial/ginger_beer_plant_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/267 | {<br>                        "step": "Inoculate with c. 20 ml of grains of \"ginger beer plant\"."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `267`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium267.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=267' >267</a></TD>
					<TD>GINGER BEER PLANT medium</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium267.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium267.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
