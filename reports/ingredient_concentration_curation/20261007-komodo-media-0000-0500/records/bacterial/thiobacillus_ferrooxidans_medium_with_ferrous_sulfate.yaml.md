# KOMODO Concentration Review: THIOBACILLUS FERROOXIDANS MEDIUM WITH FERROUS SULFATE

- Record: data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_ferrous_sulfate.yaml
- ID: CultureMech:006344
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `092f60c0f6aaf141fec23ca34385269f4f6bf57b7a15f3f561855f7cd89f5318`
- Proposed/result SHA256: `092f60c0f6aaf141fec23ca34385269f4f6bf57b7a15f3f561855f7cd89f5318`
- Source: https://mediadive.dsmz.de/rest/medium/70
- Source SHA256: b9b44e4e320f61690b17eda4518b1bc313e91117847a2f02085dadde2278eb20
- Retrieved: 2026-10-07T10:41:38.058597+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "0.4"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/70 | unknown / not asserted | unknown / not asserted | KOMODO and amount-source pH conditions differ; establish the exact formulation/version before supporting its concentrations. | unchanged |
| `ingredients[1].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "0.4"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/70 | unknown / not asserted | unknown / not asserted | KOMODO and amount-source pH conditions differ; establish the exact formulation/version before supporting its concentrations. | unchanged |
| `ingredients[2].concentration` | (NH4)2SO4 | {"unit": "G_PER_L", "value": "0.4"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/70 | unknown / not asserted | unknown / not asserted | KOMODO and amount-source pH conditions differ; establish the exact formulation/version before supporting its concentrations. | unchanged |
| `ingredients[3].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "33.3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/70 | unknown / not asserted | unknown / not asserted | KOMODO and amount-source pH conditions differ; establish the exact formulation/version before supporting its concentrations. | unchanged |
| `ingredients[4].concentration` | H2SO4 | {"unit": "G_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/70 | unknown / not asserted | unknown / not asserted | KOMODO and amount-source pH conditions differ; establish the exact formulation/version before supporting its concentrations. | unchanged |
| `source.data.solutions[0].recipe[0]` | KH2PO4 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/70 | {<br>                        "recipe_order": 1,<br>                        "compound": "KH2PO4",<br>                        "compound_id": 11,<br>                        "amount": 0.4,<br>                        "unit": "g",<br>                        "g_l": 0.4,<br>                        "mmol_l": 2.93932,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | MgSO4 x 7 H2O | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/70 | {<br>                        "recipe_order": 2,<br>                        "compound": "MgSO4 x 7 H2O",<br>                        "compound_id": 8,<br>                        "amount": 0.4,<br>                        "unit": "g",<br>                        "g_l": 0.4,<br>                        "mmol_l": 1.62288,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | (NH4)2SO4 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/70 | {<br>                        "recipe_order": 3,<br>                        "compound": "(NH4)2SO4",<br>                        "compound_id": 27,<br>                        "amount": 0.4,<br>                        "unit": "g",<br>                        "g_l": 0.4,<br>                        "mmol_l": 3.02709,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | FeSO4 x 7 H2O | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/70 | {<br>                        "recipe_order": 4,<br>                        "compound": "FeSO4 x 7 H2O",<br>                        "compound_id": 12,<br>                        "amount": 33.3,<br>                        "unit": "g",<br>                        "g_l": 33.3,<br>                        "mmol_l": 119.778,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | H2SO4 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/70 | {<br>                        "recipe_order": 5,<br>                        "compound": "H2SO4",<br>                        "compound_id": 122,<br>                        "attribute": "0.1 N",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/70 | {<br>                        "step": "Adjust pH to 1.8 with 2N sulfuric acid. Sterilize by autoclaving for 15 min at 121\u00b0C."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `70`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium70.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=70' >70</a></TD>
					<TD>THIOBACILLUS FERROOXIDANS MEDIUM WITH FERROUS SULFATE</TD>
					<TD> 1.4, H2SO4</TD>
					<TD>false</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium70.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium70.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
