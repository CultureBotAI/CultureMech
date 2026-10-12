# KOMODO Concentration Review: V-8 JUICE AGAR

- Record: data/normalized_yaml/bacterial/KOMODO_310_V-8_JUICE_AGAR.yaml
- ID: CultureMech:004948
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2254d1cd732bdcc8574f8edf07a65ea40e3af8c046f22a52727870adca0f8a70`
- Proposed/result SHA256: `41b4fa2ddb491766c44cc0202f1b2ad7ec45f47396883b388e5a0b9ca53509f2`
- Source: https://mediadive.dsmz.de/rest/medium/310
- Source SHA256: 8faa9370a1cc8350add26a061bbb7240f1c81c1a700a7b48034e3be6d09d7842
- Retrieved: 2026-10-07T10:45:08.288140+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | V-8 Juice | {"unit": "G_PER_L", "value": "200"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/310 | {<br>                        "recipe_order": 1,<br>                        "compound": "V-8 Juice",<br>                        "compound_id": 363,<br>                        "attribute": "if not available replace with tomato mash",<br>                        "amount": 200,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[1].concentration` | CaCO3 | {"unit": "G_PER_L", "value": "3"} | {"unit": "G_PER_L", "value": "3"} | evidence_only | https://mediadive.dsmz.de/rest/medium/310 | {<br>                        "recipe_order": 2,<br>                        "compound": "CaCO3",<br>                        "compound_id": 13,<br>                        "amount": 3,<br>                        "unit": "g",<br>                        "g_l": 3,<br>                        "mmol_l": 29.973,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 310 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `ingredients[2].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | {"unit": "G_PER_L", "value": "15"} | evidence_only | https://mediadive.dsmz.de/rest/medium/310 | {<br>                        "recipe_order": 3,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Provider explicitly reports g_l=15; check: 15 g * 1 g/g / (1000 ml / 1000 ml per L) = 15 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 310 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `parent_media` | v_8_juice_agar | {"id": "CultureMech:001408", "name": "v_8_juice_agar", "notes": "KOMODO record explicitly cites DSMZ Medium 310; one unlinked DSMZ parent record exists and the local physical state, pH, ingredient, and concentration signatures match exactly.", "path": "data/normalized_yaml/bacterial/v_8_juice_agar.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[3]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/310 | {<br>                        "recipe_order": 4,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/310 | {<br>                        "step": "Fill up with distilled water to 1000.0 ml. Adjust pH to 7.2."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `310`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium310.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=310' >310</a></TD>
					<TD>V-8 JUICE AGAR</TD>
					<TD> 7.2</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium310.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium310.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
