# KOMODO Concentration Review: NUTRIENT BROTH WITH 10% HORSE SERUM

- Record: data/normalized_yaml/bacterial/KOMODO_302_NUTRIENT_BROTH_WITH_10_HORSE_SERUM.yaml
- ID: CultureMech:004809
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `287ad584a546308523476bd1f8f700540d74a374afd699e270cfbf5d85b37fb4`
- Proposed/result SHA256: `287ad584a546308523476bd1f8f700540d74a374afd699e270cfbf5d85b37fb4`
- Source: https://mediadive.dsmz.de/rest/medium/302
- Source SHA256: 6f2d801cab0235c22da48be670cc15236445b6586df23e89603a912e8888dce2
- Retrieved: 2026-10-07T10:45:03.608630+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Peptone | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/302 | {<br>                        "recipe_order": 1,<br>                        "compound": "Peptone",<br>                        "compound_id": 1,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source g_l disagrees with its amount/unit/provider-volume arithmetic. | unchanged |
| `ingredients[1].concentration` | Meat extract | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/302 | {<br>                        "recipe_order": 2,<br>                        "compound": "Meat extract",<br>                        "compound_id": 2,<br>                        "amount": 3,<br>                        "unit": "g",<br>                        "g_l": 3,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source g_l disagrees with its amount/unit/provider-volume arithmetic. | unchanged |
| `ingredients[2].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/302 | {<br>                        "recipe_order": 3,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "condition": "if necessary",<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Conditional source row is not established for this physical state/formulation. | unchanged |
| `ingredients[3].concentration` | Horse serum | {"unit": "G_PER_L", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/302 | {<br>                        "recipe_order": 5,<br>                        "compound": "Horse serum",<br>                        "compound_id": 146,<br>                        "attribute": "sterile",<br>                        "amount": 100,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `parent_media` | nutrient_broth_with_10_horse_serum | {"id": "CultureMech:001402", "name": "nutrient_broth_with_10_horse_serum", "notes": "KOMODO record explicitly cites DSMZ Medium 302; one unlinked DSMZ parent record exists and the local physical state, pH, ingredient, and concentration signatures match exactly.", "path": "data/normalized_yaml/bacterial/nutrient_broth_with_10_horse_serum.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[3]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/302 | {<br>                        "recipe_order": 4,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/302 | {<br>                        "step": "Adjust pH to 7.0. For Bacillus strains the addition of 10.0 mg MnSO4 x H2O is recommended for sporulation."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
| `source.data.solutions[0].steps[1]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/302 | {<br>                        "recipe_order": 5,<br>                        "step": "To autoclaved medium add:"<br>                    } | $.data.solutions[0].steps[1] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `302`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium302.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=302' >302</a></TD>
					<TD>NUTRIENT BROTH WITH 10% HORSE SERUM</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium302.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium302.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
