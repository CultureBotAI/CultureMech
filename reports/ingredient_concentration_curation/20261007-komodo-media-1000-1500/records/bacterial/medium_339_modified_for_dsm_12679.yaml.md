# KOMODO Concentration Review: MEDIUM 339 MODIFIED FOR DSM 12679

- Record: data/normalized_yaml/bacterial/medium_339_modified_for_dsm_12679.yaml
- ID: CultureMech:005036
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9262313455503807d25f24542178a84e557445e8fac5981c98b63e67c9543a6d`
- Proposed/result SHA256: `9262313455503807d25f24542178a84e557445e8fac5981c98b63e67c9543a6d`
- Source: https://mediadive.dsmz.de/rest/medium/339
- Source SHA256: 3ecc4181db2729301c191a97c57382749d7424fd167f7d8432051f0c3f43db42
- Retrieved: 2026-10-07T10:45:38.877354+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | dehydrated Wilkins-Chalgren medium | {"unit": "G_PER_L", "value": "33"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/339 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[1].concentration` | Sodium resazurin | {"unit": "G_PER_L", "value": "0.0005"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/339 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[2].concentration` | L-Cysteine HCl | {"unit": "G_PER_L", "value": "0.3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/339 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `parent_media` | wilkins_chalgren_anaerobe_broth_oxoid_cm_643 | {"id": "CultureMech:005046", "name": "wilkins_chalgren_anaerobe_broth_oxoid_cm_643", "notes": "KOMODO Medium 339 is the WILKINS-CHALGREN ANAEROBE BROTH (Oxoid CM 643) base.", "path": "data/normalized_yaml/bacterial/wilkins_chalgren_anaerobe_broth_oxoid_cm_643.yaml", "relationship": "STRAIN_SPECIFIC_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | dehydrated Wilkins-Chalgren medium | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/339 | {<br>                        "recipe_order": 1,<br>                        "compound": "dehydrated Wilkins-Chalgren medium",<br>                        "compound_id": 2095,<br>                        "attribute": "Oxoid CM0643",<br>                        "amount": 33,<br>                        "unit": "g",<br>                        "g_l": 33,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Sodium resazurin | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/339 | {<br>                        "recipe_order": 2,<br>                        "compound": "Sodium resazurin",<br>                        "compound_id": 1852,<br>                        "attribute": "0.1% w/v",<br>                        "amount": 0.5,<br>                        "unit": "ml",<br>                        "g_l": 0.0005,<br>                        "mmol_l": 0.00199068,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | L-Cysteine HCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/339 | {<br>                        "recipe_order": 3,<br>                        "compound": "L-Cysteine HCl",<br>                        "compound_id": 1157,<br>                        "amount": 0.3,<br>                        "unit": "g",<br>                        "g_l": 0.3,<br>                        "mmol_l": 1.90331,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/339 | {<br>                        "recipe_order": 4,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/339 | {<br>                        "step": "Dissolve 33.0 g/l dehydrated Wilkins-Chalgren medium (Oxoid CM0643) in distilled water and add 0.5 ml/l Na-resazurin solution (0.1% w/v), bring to the boil and cool to room temperature while sparging with 100% N2 gas. Add L-cysteine-HCL x H2O (0.3 g/l), dispense the medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After autoclaving check pH and adjust to pH 6.8 - 7.0, if necessary."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
| `source.data.solutions[0].steps[1]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/339 | {<br>                        "step": "Note: In case resazurin is not colourless addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution, freshly prepared under N2 and filter-sterilized) can be used to completely reduce the medium."<br>                    } | $.data.solutions[0].steps[1] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `339_12679`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium339.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=339_12679' >339_12679</a></TD>
					<TD>MEDIUM 339 MODIFIED FOR DSM 12679</TD>
					<TD>null</TD>
					<TD>false</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium339.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium339.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
