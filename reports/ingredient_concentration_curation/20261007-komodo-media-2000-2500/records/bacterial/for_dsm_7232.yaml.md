# KOMODO Concentration Review: For DSM 7232

- Record: data/normalized_yaml/bacterial/for_dsm_7232.yaml
- ID: CultureMech:006110
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b0569929dc9fcf5b05d44069ad5abcd91a5b4fe1467bfa0dea31f7bdfa1c5c99`
- Proposed/result SHA256: `b0569929dc9fcf5b05d44069ad5abcd91a5b4fe1467bfa0dea31f7bdfa1c5c99`
- Source: https://mediadive.dsmz.de/rest/medium/617a
- Source SHA256: bf573df1a3cff90349790aa490022fa21ca9a81b006fa840a9c9ccceb2d8e6c0
- Retrieved: 2026-10-07T12:16:29.533899+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Beef extract | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/617a | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[1].concentration` | Peptone | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/617a | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[2].concentration` | NaCl | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/617a | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[3].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/617a | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[4].concentration` | Tap water | {"unit": "G_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/617a | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `parent_media` | blood_agar_base_oxoid_cm55 | {"id": "CultureMech:001747", "name": "blood_agar_base_oxoid_cm55", "notes": "KOMODO Medium 617a.1 applies DSMZ Medium 617a to DSM 7232 after correcting the stale DSMZ 617 NaCl concentration.", "path": "data/normalized_yaml/bacterial/blood_agar_base_oxoid_cm55.yaml", "relationship": "STRAIN_SPECIFIC_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Beef extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/617a | {<br>                        "recipe_order": 1,<br>                        "compound": "Beef extract",<br>                        "compound_id": 85,<br>                        "attribute": "Lab Lemco",<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Peptone | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/617a | {<br>                        "recipe_order": 2,<br>                        "compound": "Peptone",<br>                        "compound_id": 1,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/617a | {<br>                        "recipe_order": 3,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "mmol_l": 85.5578,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/617a | {<br>                        "recipe_order": 4,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | Tap water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/617a | {<br>                        "recipe_order": 5,<br>                        "compound": "Tap water",<br>                        "compound_id": 322,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/617a | {<br>                        "step": "Final pH of the medium should be 7.3."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `617a.1`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium617a.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=617a.1' >617a.1</a></TD>
					<TD> For DSM 7232</TD>
					<TD> 7.3</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium617a.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium617a.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
