# KOMODO Concentration Review: MEDIUM 550 MODIFIED FOR DSM 17572

- Record: data/normalized_yaml/bacterial/medium_550_modified_for_dsm_17572.yaml
- ID: CultureMech:005998
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ee7831831ca0c460b4d4a878aa2528a1c39aae5cd37599afac63d52cdce64aa8`
- Proposed/result SHA256: `ee7831831ca0c460b4d4a878aa2528a1c39aae5cd37599afac63d52cdce64aa8`
- Source: https://mediadive.dsmz.de/rest/medium/550
- Source SHA256: 0fdc4d50eace9aeb437326bde2301c0c4154d7d94e91afb9e315c26ccb88cddf
- Retrieved: 2026-10-07T12:15:38.265384+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Czapek Dox agar | {"unit": "G_PER_L", "value": "48"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/550 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "2"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/550 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[2].concentration` | Casamino acids | {"unit": "G_PER_L", "value": "6.1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/550 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[3].concentration` | Tryptophan | {"unit": "G_PER_L", "value": "0.02"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/550 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[4].concentration` | Agar | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/550 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `parent_media` | cyc_medium_modified_following_cross_and_attwell_1973 | {"id": "CultureMech:005999", "name": "cyc_medium_modified_following_cross_and_attwell_1973", "path": "data/normalized_yaml/bacterial/KOMODO_550_CYC-MEDIUM_modified_following_Cross_and_Attwell_1973.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Czapek Dox agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/550 | {<br>                        "recipe_order": 1,<br>                        "compound": "Czapek Dox agar",<br>                        "compound_id": 565,<br>                        "attribute": "Merck",<br>                        "amount": 48,<br>                        "unit": "g",<br>                        "g_l": 48,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/550 | {<br>                        "recipe_order": 2,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "attribute": "Oxoid",<br>                        "amount": 2,<br>                        "unit": "g",<br>                        "g_l": 2,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Casamino acids | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/550 | {<br>                        "recipe_order": 3,<br>                        "compound": "Casamino acids",<br>                        "compound_id": 101,<br>                        "attribute": "Difco",<br>                        "amount": 6.1,<br>                        "unit": "g",<br>                        "g_l": 6.1,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Tryptophan | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/550 | {<br>                        "recipe_order": 4,<br>                        "compound": "Tryptophan",<br>                        "compound_id": 566,<br>                        "amount": 0.02,<br>                        "unit": "g",<br>                        "g_l": 0.02,<br>                        "mmol_l": 0.0979312,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/550 | {<br>                        "recipe_order": 5,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[5]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/550 | {<br>                        "recipe_order": 6,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[5] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/550 | {<br>                        "step": "pH 7.2"<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `550_17572`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium550.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=550_17572' >550_17572</a></TD>
					<TD>MEDIUM 550 MODIFIED FOR DSM 17572</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium550.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium550.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
