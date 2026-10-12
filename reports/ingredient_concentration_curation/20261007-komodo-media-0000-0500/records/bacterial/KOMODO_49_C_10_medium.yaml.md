# KOMODO Concentration Review: C/10 medium

- Record: data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml
- ID: CultureMech:005633
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `4d20f9db10ee595a29ddafa97b4d0068d262f2447046b4aae77ae871ae37fb53`
- Proposed/result SHA256: `acff23ec468fb4f8eac822580d03e4de1a3ca6489d9a1e00411fb71a764dbf0e`
- Source: https://mediadive.dsmz.de/rest/medium/49
- Source SHA256: 5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943
- Retrieved: 2026-10-07T10:41:20.695432+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Casitone | {"unit": "G_PER_L", "value": "3"} | {"unit": "G_PER_L", "value": "3"} | evidence_only | https://mediadive.dsmz.de/rest/medium/49 | {<br>                        "recipe_order": 1,<br>                        "compound": "Casitone",<br>                        "compound_id": 84,<br>                        "amount": 3,<br>                        "unit": "g",<br>                        "g_l": 3,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 49 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `ingredients[1].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "1.36"} | {"unit": "G_PER_L", "value": "1.36"} | evidence_only | https://mediadive.dsmz.de/rest/medium/49 | {<br>                        "recipe_order": 2,<br>                        "compound": "CaCl2 x 2 H2O",<br>                        "compound_id": 7,<br>                        "amount": 1.36,<br>                        "unit": "g",<br>                        "g_l": 1.36,<br>                        "mmol_l": 9.25076,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Provider explicitly reports g_l=1.36; check: 1.36 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.36 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 49 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `ingredients[2].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | {"unit": "G_PER_L", "value": "15"} | evidence_only | https://mediadive.dsmz.de/rest/medium/49 | {<br>                        "recipe_order": 3,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Provider explicitly reports g_l=15; check: 15 g * 1 g/g / (1000 ml / 1000 ml per L) = 15 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. KOMODO accession 49 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants. | applied |
| `variant_children[0]` | medium_49_modified_for_dsm_435 | {"id": "CultureMech:005616", "name": "medium_49_modified_for_dsm_435", "notes": "Same ingredient and concentration signature; review as possible duplicate source record.", "path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `parent_media` | c_10_medium | {"id": "CultureMech:001627", "name": "c_10_medium", "notes": "KOMODO record states DSMZ Medium 49 provenance and exactly matches the single same-category DSMZ parent signature.", "path": "data/normalized_yaml/bacterial/c_10_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[3]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/49 | {<br>                        "recipe_order": 4,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/49 | {<br>                        "step": "Adjust pH to 7.2 before adding agar."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `49`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium49.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=49' >49</a></TD>
					<TD>C/10 medium</TD>
					<TD> 7.2</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium49.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium49.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
