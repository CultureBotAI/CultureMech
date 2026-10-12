# KOMODO Concentration Review: MEDIUM 453 MODIFIED FOR DSM 6349

- Record: data/normalized_yaml/bacterial/medium_453_modified_for_dsm_6349.yaml
- ID: CultureMech:005294
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `94d38c023a602327e1ab64fe25dbf589503f08abef682aacad8617748a96eba0`
- Proposed/result SHA256: `94d38c023a602327e1ab64fe25dbf589503f08abef682aacad8617748a96eba0`
- Source: https://mediadive.dsmz.de/rest/medium/453
- Source SHA256: ea99ebf9a45f357cb0f6e6ec8d9c8cc01dc1886866f5b2a98adafedf7eb7f953
- Retrieved: 2026-10-07T10:47:15.588539+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Meat peptone | {"unit": "G_PER_L", "value": "7.8"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/453 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[1].concentration` | Casein peptone | {"unit": "G_PER_L", "value": "7.8"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/453 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[2].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "2.8"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/453 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[3].concentration` | NaCl | {"unit": "G_PER_L", "value": "5.6"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/453 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[4].concentration` | D(+)-Glucose | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/453 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `parent_media` | standard_i_medium | {"id": "CultureMech:005303", "name": "standard_i_medium", "path": "data/normalized_yaml/bacterial/KOMODO_453_STANDARD_I_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Meat peptone | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/453 | {<br>                        "recipe_order": 1,<br>                        "compound": "Meat peptone",<br>                        "compound_id": 646,<br>                        "amount": 7.8,<br>                        "unit": "g",<br>                        "g_l": 7.8,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Casein peptone | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/453 | {<br>                        "recipe_order": 2,<br>                        "compound": "Casein peptone",<br>                        "compound_id": 21,<br>                        "amount": 7.8,<br>                        "unit": "g",<br>                        "g_l": 7.8,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/453 | {<br>                        "recipe_order": 3,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 2.8,<br>                        "unit": "g",<br>                        "g_l": 2.8,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/453 | {<br>                        "recipe_order": 4,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 5.6,<br>                        "unit": "g",<br>                        "g_l": 5.6,<br>                        "mmol_l": 95.8248,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | D(+)-Glucose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/453 | {<br>                        "recipe_order": 5,<br>                        "compound": "D(+)-Glucose",<br>                        "compound_id": 94,<br>                        "amount": 1,<br>                        "unit": "g",<br>                        "g_l": 1,<br>                        "mmol_l": 5.55062,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[5]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/453 | {<br>                        "recipe_order": 6,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[5] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/453 | {<br>                        "step": "Autoclave for 15 min at 121\u00b0C. pH of the final medium is 7.5. "<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `453_6349`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium453.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=453_6349' >453_6349</a></TD>
					<TD>MEDIUM 453 MODIFIED FOR DSM 6349</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium453.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium453.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
