# KOMODO Concentration Review: MY medium

- Record: data/normalized_yaml/bacterial/KOMODO_753_MY_medium.yaml
- ID: CultureMech:006405
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ce2d85c84ed0c39803ee9cc21bc94c2df9bbd2fbed379813412d4217388a6d92`
- Proposed/result SHA256: `3a1a684346ce8ab2be4bb05da3893bed3cd36bcb68c31e99d996dbff4767548a`
- Source: https://mediadive.dsmz.de/rest/medium/753
- Source SHA256: 3ef432d1b9b738afcedd8dc233e061ba6ed322b4307dadb277424789a8dd18b0
- Retrieved: 2026-10-07T12:18:24.101174+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/753 | {<br>                        "recipe_order": 1,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "attribute": "Difco 0127",<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[1].concentration` | Maltose | {"unit": "G_PER_L", "value": "20"} | {"unit": "G_PER_L", "value": "20"} | evidence_only | https://mediadive.dsmz.de/rest/medium/753 | {<br>                        "recipe_order": 2,<br>                        "compound": "Maltose",<br>                        "compound_id": 171,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 58.4283,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Provider explicitly reports g_l=20; check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) = 20 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 753 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `ingredients[2].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "2"} | {"unit": "G_PER_L", "value": "2"} | evidence_only | https://mediadive.dsmz.de/rest/medium/753 | {<br>                        "recipe_order": 3,<br>                        "compound": "KH2PO4",<br>                        "compound_id": 11,<br>                        "amount": 2,<br>                        "unit": "g",<br>                        "g_l": 2,<br>                        "mmol_l": 14.6967,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Provider explicitly reports g_l=2; check: 2 g * 1 g/g / (1000 ml / 1000 ml per L) = 2 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 753 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `ingredients[3].concentration` | NaCl | {"unit": "G_PER_L", "value": "5"} | {"unit": "G_PER_L", "value": "5"} | evidence_only | https://mediadive.dsmz.de/rest/medium/753 | {<br>                        "recipe_order": 4,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "mmol_l": 85.5578,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Provider explicitly reports g_l=5; check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 753 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `parent_media` | my_medium | {"id": "CultureMech:001886", "name": "my_medium", "notes": "KOMODO record states DSMZ Medium 753 provenance and exactly matches the single same-category DSMZ parent signature.", "path": "data/normalized_yaml/bacterial/my_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[4]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/753 | {<br>                        "recipe_order": 5,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/753 | {<br>                        "step": "Adjust pH for final pH 6.0. Autoclave at 121\u00b0C for 15 minutes."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `753`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium753.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=753' >753</a></TD>
					<TD>MY medium</TD>
					<TD> 6.0</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium753.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium753.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
