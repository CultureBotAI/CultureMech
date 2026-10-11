# KOMODO Concentration Review: TY medium

- Record: data/normalized_yaml/bacterial/KOMODO_1143_TY_medium.yaml
- ID: CultureMech:003854
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7ce4a55d176545d944382b1b732cd8f038f4282384b43e2b60ce2ff06de76d83`
- Proposed/result SHA256: `2d1686a9f0893c61ac0776911c1662e719aa5f6ab92cec043ba86ce74d931012`
- Source: https://mediadive.dsmz.de/rest/medium/1143
- Source SHA256: 01fc9cd56acd5b62b5e41f8864ee7640b8d49984fdb3a9bcb2e46ba9774ba277
- Retrieved: 2026-10-07T13:17:53.993315+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Tryptone | {"unit": "G_PER_L", "value": "5"} | {"unit": "G_PER_L", "value": "5"} | evidence_only | https://mediadive.dsmz.de/rest/medium/1143 | {<br>                        "recipe_order": 1,<br>                        "compound": "Tryptone",<br>                        "compound_id": 71,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "mmol_l": 70.3433,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Provider explicitly reports g_l=5; check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 1143 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "3"} | {"unit": "G_PER_L", "value": "3"} | evidence_only | https://mediadive.dsmz.de/rest/medium/1143 | {<br>                        "recipe_order": 2,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 3,<br>                        "unit": "g",<br>                        "g_l": 3,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 1143 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `ingredients[2].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "0.9"} | {"unit": "G_PER_L", "value": "0.9"} | evidence_only | https://mediadive.dsmz.de/rest/medium/1143 | {<br>                        "recipe_order": 3,<br>                        "compound": "CaCl2 x 2 H2O",<br>                        "compound_id": 7,<br>                        "amount": 0.9,<br>                        "unit": "g",<br>                        "g_l": 0.9,<br>                        "mmol_l": 6.12182,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Provider explicitly reports g_l=0.9; check: 0.9 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.9 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 1143 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `parent_media` | ty_medium | {"id": "CultureMech:000581", "name": "ty_medium", "notes": "Exact DSMZ/KOMODO medium-number match with matching ingredient and concentration signature.", "path": "data/normalized_yaml/bacterial/ty_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[3]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1143 | {<br>                        "recipe_order": 4,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1143 | {<br>                        "step": "Adjust to pH 6.8"<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `1143`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1143.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1143' >1143</a></TD>
					<TD>TY medium</TD>
					<TD> 6.8</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1143.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1143.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
