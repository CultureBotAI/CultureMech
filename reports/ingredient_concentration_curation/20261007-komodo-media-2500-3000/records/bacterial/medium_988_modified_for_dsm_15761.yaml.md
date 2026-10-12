# KOMODO Concentration Review: MEDIUM 988 MODIFIED FOR DSM 15761

- Record: data/normalized_yaml/bacterial/medium_988_modified_for_dsm_15761.yaml
- ID: CultureMech:006957
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `29e78015afa377ffe6bbd0d46faf6aa242aaf8d8eaa8ef245ea2371db0b9e70b`
- Proposed/result SHA256: `29e78015afa377ffe6bbd0d46faf6aa242aaf8d8eaa8ef245ea2371db0b9e70b`
- Source: https://mediadive.dsmz.de/rest/medium/988
- Source SHA256: 186558f33f4783a97154ad65e49d254377d37b7a9b7b3ea9ce7ec2b61fa78277
- Retrieved: 2026-10-07T13:15:31.269545+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/988 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[1].concentration` | Peptone | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/988 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[2].concentration` | Sodium succinate | {"unit": "G_PER_L", "value": "2.3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/988 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[3].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/988 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `parent_media` | yeast_peptone_succinate_medium | {"id": "CultureMech:006959", "name": "yeast_peptone_succinate_medium", "notes": "Manual review found matching DSMZ/KOMODO Medium 988 source, solid-agar state, pH, ingredient identity, and concentration signature.", "path": "data/normalized_yaml/bacterial/yeast_peptone_succinate_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/988 | {<br>                        "recipe_order": 1,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 3,<br>                        "unit": "g",<br>                        "g_l": 3,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Peptone | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/988 | {<br>                        "recipe_order": 2,<br>                        "compound": "Peptone",<br>                        "compound_id": 1,<br>                        "amount": 3,<br>                        "unit": "g",<br>                        "g_l": 3,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Sodium succinate | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/988 | {<br>                        "recipe_order": 3,<br>                        "compound": "Sodium succinate",<br>                        "compound_id": 730,<br>                        "amount": 2.3,<br>                        "unit": "g",<br>                        "g_l": 2.3,<br>                        "mmol_l": 14.1932,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/988 | {<br>                        "recipe_order": 4,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/988 | {<br>                        "recipe_order": 5,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "condition": "for solid medium",<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/988 | {<br>                        "step": "Final pH 7.2. The medium may be solidified by adding 15 g/l agar."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `988_15761`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium988.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=988_15761' >988_15761</a></TD>
					<TD>MEDIUM 988 MODIFIED FOR DSM 15761</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium988.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium988.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
