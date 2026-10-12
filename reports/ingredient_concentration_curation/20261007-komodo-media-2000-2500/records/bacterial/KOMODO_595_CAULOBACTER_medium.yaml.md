# KOMODO Concentration Review: CAULOBACTER medium

- Record: data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml
- ID: CultureMech:006076
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b68f967ed4f5e15928e60420f6971e30ff406ea289108d9f58dd521cf18a0617`
- Proposed/result SHA256: `7de6ae7976778f784205c2a53ec2629df407f5f17111a786fb3820209e5880d0`
- Source: https://mediadive.dsmz.de/rest/medium/595
- Source SHA256: f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00
- Retrieved: 2026-10-07T12:16:07.516338+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Bacto peptone | {"unit": "G_PER_L", "value": "2"} | {"unit": "G_PER_L", "value": "2"} | evidence_only | https://mediadive.dsmz.de/rest/medium/595 | {<br>                        "recipe_order": 1,<br>                        "compound": "Bacto peptone",<br>                        "compound_id": 19,<br>                        "amount": 2,<br>                        "unit": "g",<br>                        "g_l": 2,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Provider explicitly reports g_l=2; check: 2 g * 1 g/g / (1000 ml / 1000 ml per L) = 2 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 595 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/595 | {<br>                        "recipe_order": 2,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "attribute": "BD 212750",<br>                        "amount": 1,<br>                        "unit": "g",<br>                        "g_l": 1,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[2].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "0.2"} | {"unit": "G_PER_L", "value": "0.2"} | evidence_only | https://mediadive.dsmz.de/rest/medium/595 | {<br>                        "recipe_order": 3,<br>                        "compound": "MgSO4 x 7 H2O",<br>                        "compound_id": 8,<br>                        "amount": 0.2,<br>                        "unit": "g",<br>                        "g_l": 0.2,<br>                        "mmol_l": 0.811438,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Provider explicitly reports g_l=0.2; check: 0.2 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.2 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 595 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `ingredients[3].concentration` | Tap water | {"unit": "G_PER_L", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/595 | {<br>                        "recipe_order": 4,<br>                        "compound": "Tap water",<br>                        "compound_id": 322,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Liquid dose, percent basis, molar conversion, or other unit needs source-specific review; no water-based final volume is inferred. | unchanged |
| `ingredients[4].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | {"unit": "G_PER_L", "value": "15"} | evidence_only | https://mediadive.dsmz.de/rest/medium/595 | {<br>                        "recipe_order": 5,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "condition": "for solid medium",<br>                        "amount": 15,<br>                        "unit": "g/l",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Provider explicitly reports g_l=15; check: 15 g/l * 1 = 15 g/L; the source already gives a rate, so it is not divided by volume again. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Source condition 'for solid medium' matches local physical_state=SOLID_AGAR. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 595 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `parent_media` | caulobacter_medium | {"id": "CultureMech:001722", "name": "caulobacter_medium", "notes": "KOMODO record states DSMZ Medium 595 provenance and exactly matches the single same-category DSMZ parent signature.", "path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/595 | {<br>                        "step": "Add 15.0 g/l agar for solid medium."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `595`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=595' >595</a></TD>
					<TD>CAULOBACTER medium</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
