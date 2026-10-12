# KOMODO Concentration Review: BOSEA medium

- Record: data/normalized_yaml/bacterial/KOMODO_1052_BOSEA_medium.yaml
- ID: CultureMech:003627
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `aa4b410e10649e7b73eb27d74fac7a8019fb4e9d179aa8ca2cb1e552508f6410`
- Proposed/result SHA256: `aa4b410e10649e7b73eb27d74fac7a8019fb4e9d179aa8ca2cb1e552508f6410`
- Source: https://mediadive.dsmz.de/rest/medium/1052
- Source SHA256: cbde2f1a092e198b82a23d9ff7e0696d8cb451291da1b9c228ba6b485cadc872
- Retrieved: 2026-10-07T13:16:33.338912+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1052 | Same as solutions A and B of medium 585, CYE-ACES agar. | $.data.solutions[0].steps[1].step | Manual source review withheld support: The source refers to solutions A and B of DSMZ 585, which are separately sterilized preparations containing 490 ml water each, while the local/API flat recipe lists 1000 ml water. Resolve the intended BOSEA preparation and water allocation without importing the distinct C/D supplements of 585 or assuming a measured final litre. | unchanged |
| `ingredients[1].concentration` | ACES | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1052 | Same as solutions A and B of medium 585, CYE-ACES agar. | $.data.solutions[0].steps[1].step | Manual source review withheld support: The source refers to solutions A and B of DSMZ 585, which are separately sterilized preparations containing 490 ml water each, while the local/API flat recipe lists 1000 ml water. Resolve the intended BOSEA preparation and water allocation without importing the distinct C/D supplements of 585 or assuming a measured final litre. | unchanged |
| `ingredients[2].concentration` | Activated charcoal | {"unit": "G_PER_L", "value": "2"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1052 | Same as solutions A and B of medium 585, CYE-ACES agar. | $.data.solutions[0].steps[1].step | Manual source review withheld support: The source refers to solutions A and B of DSMZ 585, which are separately sterilized preparations containing 490 ml water each, while the local/API flat recipe lists 1000 ml water. Resolve the intended BOSEA preparation and water allocation without importing the distinct C/D supplements of 585 or assuming a measured final litre. | unchanged |
| `ingredients[3].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1052 | Same as solutions A and B of medium 585, CYE-ACES agar. | $.data.solutions[0].steps[1].step | Manual source review withheld support: The source refers to solutions A and B of DSMZ 585, which are separately sterilized preparations containing 490 ml water each, while the local/API flat recipe lists 1000 ml water. Resolve the intended BOSEA preparation and water allocation without importing the distinct C/D supplements of 585 or assuming a measured final litre. | unchanged |
| `parent_media` | bosea_medium | {"id": "CultureMech:000480", "name": "bosea_medium", "notes": "Exact DSMZ/KOMODO medium-number match with matching ingredient and concentration signature.", "path": "data/normalized_yaml/bacterial/bosea_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1052 | {<br>                        "recipe_order": 1,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | ACES | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1052 | {<br>                        "recipe_order": 2,<br>                        "compound": "ACES",<br>                        "compound_id": 581,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "mmol_l": 54.8847,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Activated charcoal | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1052 | {<br>                        "recipe_order": 3,<br>                        "compound": "Activated charcoal",<br>                        "compound_id": 582,<br>                        "amount": 2,<br>                        "unit": "g",<br>                        "g_l": 2,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1052 | {<br>                        "recipe_order": 4,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1052 | {<br>                        "recipe_order": 5,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1052 | {<br>                        "step": "Adjust pH to 6.9 prior to addition of agar."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
| `source.data.solutions[0].steps[1]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1052 | {<br>                        "step": "Same as solutions A and B of medium 585, CYE-ACES agar."<br>                    } | $.data.solutions[0].steps[1] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `1052`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1052.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1052' >1052</a></TD>
					<TD>BOSEA medium</TD>
					<TD> 6.9</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1052.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1052.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
