# KOMODO Concentration Review: BM MEDIUM

- Record: data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml
- ID: CultureMech:003929
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `443356164beab26bd0466f1be4680f8274148317c772bdae9e901759bb0e201f`
- Proposed/result SHA256: `443356164beab26bd0466f1be4680f8274148317c772bdae9e901759bb0e201f`
- Source: https://mediadive.dsmz.de/rest/medium/1192
- Source SHA256: 711656f5e6453135942f164de22b17c7ce3a870e3fb19aefeaa341a9e1262182
- Retrieved: 2026-10-07T13:18:36.667926+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Difco marine broth | {"unit": "G_PER_L", "value": "37.4"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1192 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Biotin | {"unit": "G_PER_L", "value": "2e-05"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1192 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Vitamin B12 | {"unit": "G_PER_L", "value": "1e-06"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1192 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Methanol | {"unit": "G_PER_L", "value": "3.168"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1192 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1192 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `parent_media` | bm_medium | {"id": "CultureMech:000635", "name": "bm_medium", "notes": "KOMODO record explicitly cites DSMZ Medium 1192; one unlinked DSMZ parent record exists and the local physical state, pH, ingredient, and concentration signatures match exactly.", "path": "data/normalized_yaml/bacterial/bm_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Difco marine broth | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1192 | {<br>                        "recipe_order": 1,<br>                        "compound": "Difco marine broth",<br>                        "compound_id": 530,<br>                        "attribute": "Difco 2216",<br>                        "amount": 37.4,<br>                        "unit": "g",<br>                        "g_l": 37.4,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1192 | {<br>                        "recipe_order": 2,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Biotin | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1192 | {<br>                        "recipe_order": 3,<br>                        "compound": "Biotin",<br>                        "compound_id": 46,<br>                        "amount": 20,<br>                        "unit": "\u00b5g",<br>                        "g_l": 2.0e-5,<br>                        "mmol_l": 8.18632e-5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Vitamin B12 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1192 | {<br>                        "recipe_order": 4,<br>                        "compound": "Vitamin B12",<br>                        "compound_id": 18,<br>                        "amount": 1,<br>                        "unit": "\u00b5g",<br>                        "g_l": 1.0e-6,<br>                        "mmol_l": 7.3779e-7,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | Methanol | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1192 | {<br>                        "recipe_order": 5,<br>                        "compound": "Methanol",<br>                        "compound_id": 226,<br>                        "amount": 4,<br>                        "unit": "ml",<br>                        "g_l": 3.168,<br>                        "mmol_l": 98.8702,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[5]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1192 | {<br>                        "recipe_order": 6,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "condition": "if necessary",<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[5] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |

## Source Mapping

KOMODO accession `1192`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1192' >1192</a></TD>
					<TD>BM MEDIUM</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1192.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
