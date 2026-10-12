# KOMODO Concentration Review: MEDIUM 662 MODIFIED FOR DSM 6699

- Record: data/normalized_yaml/bacterial/medium_662_modified_for_dsm_6699.yaml
- ID: CultureMech:006242
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `790bb0819bbb38f611001992d3926bcd0911e2272be7f1b7d6b8ca93a6c16769`
- Proposed/result SHA256: `790bb0819bbb38f611001992d3926bcd0911e2272be7f1b7d6b8ca93a6c16769`
- Source: https://mediadive.dsmz.de/rest/medium/662
- Source SHA256: 21eb95dbcd2db557b3023c3575120b67941f1c506f39e929e8a0f84af04b1127
- Retrieved: 2026-10-07T12:17:10.341282+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Glucose | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/662 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[1].concentration` | Polypeptone | {"unit": "G_PER_L", "value": "2"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/662 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[2].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.2"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/662 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[3].concentration` | NH4NO3 | {"unit": "G_PER_L", "value": "0.2"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/662 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `parent_media` | yepg_medium | {"id": "CultureMech:006244", "name": "yepg_medium", "path": "data/normalized_yaml/bacterial/KOMODO_662_YEPG_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Glucose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/662 | {<br>                        "recipe_order": 1,<br>                        "compound": "Glucose",<br>                        "compound_id": 5,<br>                        "amount": 1,<br>                        "unit": "g",<br>                        "g_l": 1,<br>                        "mmol_l": 5.55062,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Polypeptone | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/662 | {<br>                        "recipe_order": 2,<br>                        "compound": "Polypeptone",<br>                        "compound_id": 442,<br>                        "amount": 2,<br>                        "unit": "g",<br>                        "g_l": 2,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/662 | {<br>                        "recipe_order": 3,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 0.2,<br>                        "unit": "g",<br>                        "g_l": 0.2,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | NH4NO3 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/662 | {<br>                        "recipe_order": 4,<br>                        "compound": "NH4NO3",<br>                        "compound_id": 178,<br>                        "amount": 0.2,<br>                        "unit": "g",<br>                        "g_l": 0.2,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/662 | {<br>                        "recipe_order": 5,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/662 | {<br>                        "step": "Adjust pH to 7.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `662_6699`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium662.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=662_6699' >662_6699</a></TD>
					<TD>MEDIUM 662 MODIFIED FOR DSM 6699</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium662.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium662.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
