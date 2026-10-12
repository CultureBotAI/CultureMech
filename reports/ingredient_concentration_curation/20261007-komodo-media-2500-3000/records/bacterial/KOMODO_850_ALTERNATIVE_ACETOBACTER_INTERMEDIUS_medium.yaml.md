# KOMODO Concentration Review: ALTERNATIVE ACETOBACTER INTERMEDIUS medium

- Record: data/normalized_yaml/bacterial/KOMODO_850_ALTERNATIVE_ACETOBACTER_INTERMEDIUS_medium.yaml
- ID: CultureMech:006658
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c1162ab0dcff33ebe233696fec51944c3efd698f7510272ebaffc01358aea50b`
- Proposed/result SHA256: `c1162ab0dcff33ebe233696fec51944c3efd698f7510272ebaffc01358aea50b`
- Source: https://mediadive.dsmz.de/rest/medium/850
- Source SHA256: 9a2a2a4f223d9f1860e557af0f957efb96dfbf30844caa99f6f2e423848fc292
- Retrieved: 2026-10-07T12:19:59.044460+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Glucose | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/850 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/850 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Agar | {"unit": "G_PER_L", "value": "12"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/850 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `parent_media` | alternative_acetobacter_intermedius_medium | {"id": "CultureMech:002008", "name": "alternative_acetobacter_intermedius_medium", "notes": "KOMODO record states DSMZ Medium 850 provenance and exactly matches the single same-category DSMZ parent signature.", "path": "data/normalized_yaml/bacterial/alternative_acetobacter_intermedius_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Glucose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/850 | {<br>                        "recipe_order": 1,<br>                        "compound": "Glucose",<br>                        "compound_id": 5,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "mmol_l": 27.7531,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/850 | {<br>                        "recipe_order": 2,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 3,<br>                        "unit": "g",<br>                        "g_l": 3,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/850 | {<br>                        "recipe_order": 3,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 12,<br>                        "unit": "g",<br>                        "g_l": 12,<br>                        "mmol_l": 35.6792,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/850 | {<br>                        "recipe_order": 4,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |

## Source Mapping

KOMODO accession `850`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium850.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=850' >850</a></TD>
					<TD>ALTERNATIVE ACETOBACTER INTERMEDIUS medium</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium850.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium850.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
