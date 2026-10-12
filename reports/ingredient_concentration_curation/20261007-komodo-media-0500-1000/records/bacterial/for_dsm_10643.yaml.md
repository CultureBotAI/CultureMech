# KOMODO Concentration Review: For DSM 10643

- Record: data/normalized_yaml/bacterial/for_dsm_10643.yaml
- ID: CultureMech:004422
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3a720f1cce57a49539009805f961dc6642f5e460043fdbbb70678e3f93106da4`
- Proposed/result SHA256: `3a720f1cce57a49539009805f961dc6642f5e460043fdbbb70678e3f93106da4`
- Source: https://mediadive.dsmz.de/rest/medium/215c
- Source SHA256: 119f34e2aed0499f38707f6223ad8bf14f02a61161371188b846c4c6fe3df7dc
- Retrieved: 2026-10-07T10:43:56.124751+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Brain heart infusion | {"unit": "G_PER_L", "value": "37"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215c | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[1].concentration` | Na2S x 9 H2O | {"unit": "G_PER_L", "value": "0.25"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215c | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[2].concentration` | glycerol | {"unit": "G_PER_L", "value": "8.70"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215c | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[3].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215c | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[4].concentration` | L-Cysteine HCl x H2O | {"unit": "G_PER_L", "value": "0.25"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215c | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[5].concentration` | N2 | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215c | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `parent_media` | KOMODO_215c_BHI_medium_FOR_STRICT_ANAEROBES | {"id": "CultureMech:004425", "name": "KOMODO_215c_BHI_medium_FOR_STRICT_ANAEROBES", "notes": "KOMODO Medium 215c is the parent BHI strict-anaerobe formulation.", "path": "data/normalized_yaml/bacterial/KOMODO_215c_BHI_medium_FOR_STRICT_ANAEROBES.yaml", "relationship": "STRAIN_SPECIFIC_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Brain heart infusion | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/215c | {<br>                        "recipe_order": 1,<br>                        "compound": "Brain heart infusion",<br>                        "compound_id": 186,<br>                        "attribute": "DIFCO",<br>                        "amount": 37,<br>                        "unit": "g",<br>                        "g_l": 37,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | L-Cysteine HCl x H2O | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/215c | {<br>                        "recipe_order": 2,<br>                        "compound": "L-Cysteine HCl x H2O",<br>                        "compound_id": 770,<br>                        "amount": 0.25,<br>                        "unit": "g",<br>                        "g_l": 0.25,<br>                        "mmol_l": 1.4234,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Na2S x 9 H2O | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/215c | {<br>                        "recipe_order": 3,<br>                        "compound": "Na2S x 9 H2O",<br>                        "compound_id": 54,<br>                        "amount": 0.25,<br>                        "unit": "g",<br>                        "g_l": 0.25,<br>                        "mmol_l": 1.04088,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/215c | {<br>                        "recipe_order": 4,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/215c | {<br>                        "step": "Prepare medium anoxically under 100% N2 gas atmosphere. Reducing agents are added after autoclaving from sterile anoxic solutions prepared under N2."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `215c.1`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=215c.1' >215c.1</a></TD>
					<TD> For DSM 10643</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>true</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
