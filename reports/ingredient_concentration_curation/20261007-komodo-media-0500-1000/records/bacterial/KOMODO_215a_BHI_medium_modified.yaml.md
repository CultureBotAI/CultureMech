# KOMODO Concentration Review: BHI medium (modified)

- Record: data/normalized_yaml/bacterial/KOMODO_215a_BHI_medium_modified.yaml
- ID: CultureMech:004419
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `16bd86d38334b0d67c5cdf289effc07f48ea171e6f602c5b0e4d44b9523875b3`
- Proposed/result SHA256: `16bd86d38334b0d67c5cdf289effc07f48ea171e6f602c5b0e4d44b9523875b3`
- Source: https://mediadive.dsmz.de/rest/medium/215a
- Source SHA256: 0f7e9ffd16c03233276ace6b54efa338be0927081953c372483668b0d395a769
- Retrieved: 2026-10-07T10:43:54.556376+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Calf brains | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215a | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Beef heart | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215a | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Proteose peptone | {"unit": "G_PER_L", "value": "10.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215a | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Dextrose | {"unit": "G_PER_L", "value": "2.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215a | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | Sodium chloride | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215a | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | Disodium phosphate | {"unit": "G_PER_L", "value": "2.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215a | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | Brain heart infusion | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/215a | {<br>                        "recipe_order": 1,<br>                        "compound": "Brain heart infusion",<br>                        "compound_id": 186,<br>                        "amount": 37,<br>                        "unit": "g",<br>                        "g_l": 37,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Erythromycin | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/215a | {<br>                        "recipe_order": 2,<br>                        "compound": "Erythromycin",<br>                        "compound_id": 315,<br>                        "amount": 10,<br>                        "unit": "mg",<br>                        "g_l": 0.01,<br>                        "mmol_l": 0.0136253,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/215a | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |

## Source Mapping

KOMODO accession `215a`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215a.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=215a' >215a</a></TD>
					<TD>BHI medium (modified)</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215a.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215a.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
