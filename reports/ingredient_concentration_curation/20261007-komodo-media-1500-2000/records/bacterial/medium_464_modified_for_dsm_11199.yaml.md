# KOMODO Concentration Review: MEDIUM 464 MODIFIED FOR DSM 11199

- Record: data/normalized_yaml/bacterial/medium_464_modified_for_dsm_11199.yaml
- ID: CultureMech:005509
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f9b5aa7b468d92d4cdc1cee629222bc3d883eaeed2f1ade5cc26d3e081f6925a`
- Proposed/result SHA256: `f9b5aa7b468d92d4cdc1cee629222bc3d883eaeed2f1ade5cc26d3e081f6925a`
- Source: https://mediadive.dsmz.de/rest/medium/464
- Source SHA256: 1b1d6da7bcb91079093c4d151010201518587f76f2cadb4f85ee4b32d29bad98
- Retrieved: 2026-10-07T10:47:32.925755+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Tryptone | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/464 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "2.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/464 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[2].concentration` | Dextrose | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/464 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[3].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/464 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `parent_media` | plate_count_agar | {"id": "CultureMech:005519", "name": "plate_count_agar", "path": "data/normalized_yaml/bacterial/KOMODO_464_PLATE_COUNT_AGAR.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Tryptone | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/464 | {<br>                        "recipe_order": 1,<br>                        "compound": "Tryptone",<br>                        "compound_id": 71,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "mmol_l": 70.3433,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/464 | {<br>                        "recipe_order": 2,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 2.5,<br>                        "unit": "g",<br>                        "g_l": 2.5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Dextrose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/464 | {<br>                        "recipe_order": 3,<br>                        "compound": "Dextrose",<br>                        "compound_id": 60,<br>                        "amount": 1,<br>                        "unit": "g",<br>                        "g_l": 1,<br>                        "mmol_l": 5.04617,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/464 | {<br>                        "recipe_order": 4,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/464 | {<br>                        "recipe_order": 5,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/464 | {<br>                        "step": "Adjust pH to 7.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `464_11199`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium464.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=464_11199' >464_11199</a></TD>
					<TD>MEDIUM 464 MODIFIED FOR DSM 11199</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium464.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium464.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
