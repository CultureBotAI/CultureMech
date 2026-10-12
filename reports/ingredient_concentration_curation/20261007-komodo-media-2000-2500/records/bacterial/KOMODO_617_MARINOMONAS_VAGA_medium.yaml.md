# KOMODO Concentration Review: MARINOMONAS VAGA medium

- Record: data/normalized_yaml/bacterial/KOMODO_617_MARINOMONAS_VAGA_medium.yaml
- ID: CultureMech:006109
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7779ee5f5f262e69cf2fc47b7d1308479336846ae20ce6c45ba0eb9742c7c531`
- Proposed/result SHA256: `7779ee5f5f262e69cf2fc47b7d1308479336846ae20ce6c45ba0eb9742c7c531`
- Source: https://mediadive.dsmz.de/rest/medium/617
- Source SHA256: ce89637808725c625fcbe2d1d83f90fc7b6ad152736cacfc2def16183bbd64c8
- Retrieved: 2026-10-07T12:16:28.757547+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Beef extract | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/617 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Peptone | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/617 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | NaCl | {"unit": "G_PER_L", "value": "30"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/617 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/617 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | Tap water | {"unit": "G_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/617 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `parent_media` | marinomonas_vaga_medium | {"id": "CultureMech:001746", "name": "marinomonas_vaga_medium", "notes": "KOMODO record states DSMZ Medium 617 provenance and exactly matches the single same-category DSMZ parent signature.", "path": "data/normalized_yaml/bacterial/marinomonas_vaga_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Beef extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/617 | {<br>                        "recipe_order": 1,<br>                        "compound": "Beef extract",<br>                        "compound_id": 85,<br>                        "attribute": "Lab Lemco",<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Peptone | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/617 | {<br>                        "recipe_order": 2,<br>                        "compound": "Peptone",<br>                        "compound_id": 1,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/617 | {<br>                        "recipe_order": 3,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 30,<br>                        "unit": "g",<br>                        "g_l": 30,<br>                        "mmol_l": 513.347,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/617 | {<br>                        "recipe_order": 4,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | Tap water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/617 | {<br>                        "recipe_order": 5,<br>                        "compound": "Tap water",<br>                        "compound_id": 322,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |

## Source Mapping

KOMODO accession `617`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium617.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=617' >617</a></TD>
					<TD>MARINOMONAS VAGA medium</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium617.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium617.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
