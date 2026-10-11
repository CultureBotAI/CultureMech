# KOMODO Concentration Review: STANDARD I + MALT AGAR

- Record: data/normalized_yaml/bacterial/standard_i_malt_agar.yaml
- ID: CultureMech:006156
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f6e56bd5a87af86fac5843a68c278d1fed753d84f06d8aef22bad62049dd7e15`
- Proposed/result SHA256: `7acbfa7a1dafdd8ba6fc69d583ab51e40188b63a4a35e3690065cf4d5279c81b`
- Source: https://mediadive.dsmz.de/rest/medium/637
- Source SHA256: a43cd0081913c7e27ec4de605382c11484dcb17455a70f828dcc256366485ccb
- Retrieved: 2026-10-07T12:16:48.608393+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Standard I Broth | {"unit": "G_PER_L", "value": "25"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/637 | {<br>                        "recipe_order": 1,<br>                        "compound": "Standard I Broth",<br>                        "compound_id": 630,<br>                        "attribute": "Merck",<br>                        "amount": 25,<br>                        "unit": "g",<br>                        "g_l": 25,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[1].concentration` | Malt extract | {"unit": "G_PER_L", "value": "10"} | {"unit": "G_PER_L", "value": "10"} | evidence_only | https://mediadive.dsmz.de/rest/medium/637 | {<br>                        "recipe_order": 2,<br>                        "compound": "Malt extract",<br>                        "compound_id": 116,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Provider explicitly reports g_l=10; check: 10 g * 1 g/g / (1000 ml / 1000 ml per L) = 10 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 637 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `ingredients[2].concentration` | CaCO3 | {"unit": "G_PER_L", "value": "2"} | {"unit": "G_PER_L", "value": "2"} | evidence_only | https://mediadive.dsmz.de/rest/medium/637 | {<br>                        "recipe_order": 3,<br>                        "compound": "CaCO3",<br>                        "compound_id": 13,<br>                        "amount": 2,<br>                        "unit": "g",<br>                        "g_l": 2,<br>                        "mmol_l": 19.982,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Provider explicitly reports g_l=2; check: 2 g * 1 g/g / (1000 ml / 1000 ml per L) = 2 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 637 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `ingredients[3].concentration` | Agar | {"unit": "G_PER_L", "value": "12"} | {"unit": "G_PER_L", "value": "12"} | evidence_only | https://mediadive.dsmz.de/rest/medium/637 | {<br>                        "recipe_order": 4,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 12,<br>                        "unit": "g",<br>                        "g_l": 12,<br>                        "mmol_l": 35.6792,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Provider explicitly reports g_l=12; check: 12 g * 1 g/g / (1000 ml / 1000 ml per L) = 12 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 637 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `source.data.solutions[0].recipe[4]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/637 | {<br>                        "recipe_order": 5,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/637 | {<br>                        "step": "pH 7.2"<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `637`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium637.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=637' >637</a></TD>
					<TD>STANDARD I + MALT AGAR</TD>
					<TD> 7.2</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium637.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium637.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
