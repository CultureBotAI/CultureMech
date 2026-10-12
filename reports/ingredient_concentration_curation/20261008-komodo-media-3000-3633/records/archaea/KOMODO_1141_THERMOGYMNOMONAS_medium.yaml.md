# KOMODO Concentration Review: THERMOGYMNOMONAS medium

- Record: data/normalized_yaml/archaea/KOMODO_1141_THERMOGYMNOMONAS_medium.yaml
- ID: CultureMech:003851
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `82802ca06afddb8b3a4eadb542a7eeed992108ae782090d5a63c5293f5951588`
- Proposed/result SHA256: `82802ca06afddb8b3a4eadb542a7eeed992108ae782090d5a63c5293f5951588`
- Source: https://mediadive.dsmz.de/rest/medium/1141
- Source SHA256: f478ca42c11ca3fbc9bdfc78100e06bae24152a4fafc3a85f680618eaf1b97d4
- Retrieved: 2026-10-07T13:17:52.423252+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | (NH4)2SO4 | {"unit": "G_PER_L", "value": "0.2"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1141 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): H2SO4 | unchanged |
| `ingredients[1].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1141 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): H2SO4 | unchanged |
| `ingredients[2].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1141 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): H2SO4 | unchanged |
| `ingredients[3].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "0.25"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1141 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): H2SO4 | unchanged |
| `ingredients[4].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1141 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): H2SO4 | unchanged |
| `ingredients[5].concentration` | Glucose | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1141 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): H2SO4 | unchanged |
| `ingredients[6].concentration` | H2SO4 | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1141 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): H2SO4 | unchanged |
| `source.data.solutions[0].recipe[0]` | (NH4)2SO4 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1141 | {<br>                        "recipe_order": 1,<br>                        "compound": "(NH4)2SO4",<br>                        "compound_id": 27,<br>                        "amount": 0.2,<br>                        "unit": "g",<br>                        "g_l": 0.2,<br>                        "mmol_l": 1.51355,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | KH2PO4 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1141 | {<br>                        "recipe_order": 2,<br>                        "compound": "KH2PO4",<br>                        "compound_id": 11,<br>                        "amount": 3,<br>                        "unit": "g",<br>                        "g_l": 3,<br>                        "mmol_l": 22.045,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | MgSO4 x 7 H2O | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1141 | {<br>                        "recipe_order": 3,<br>                        "compound": "MgSO4 x 7 H2O",<br>                        "compound_id": 8,<br>                        "amount": 0.5,<br>                        "unit": "g",<br>                        "g_l": 0.5,<br>                        "mmol_l": 2.02859,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | CaCl2 x 2 H2O | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1141 | {<br>                        "recipe_order": 4,<br>                        "compound": "CaCl2 x 2 H2O",<br>                        "compound_id": 7,<br>                        "amount": 0.25,<br>                        "unit": "g",<br>                        "g_l": 0.25,<br>                        "mmol_l": 1.70051,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1141 | {<br>                        "recipe_order": 5,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "attribute": "Difco",<br>                        "amount": 1,<br>                        "unit": "g",<br>                        "g_l": 1,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[5]` | Glucose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1141 | {<br>                        "recipe_order": 6,<br>                        "compound": "Glucose",<br>                        "compound_id": 5,<br>                        "attribute": "",<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "mmol_l": 55.5062,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[5] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[6]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1141 | {<br>                        "recipe_order": 7,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[6] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1141 | {<br>                        "step": "Adjust pH to 3.0 with 10 N H2SO4. Separately autoclave yeast extract and glucose as 10% solutions, and add aseptically to the medium."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `1141`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1141.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1141' >1141</a></TD>
					<TD>THERMOGYMNOMONAS medium</TD>
					<TD> 3.0, H2SO4</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1141.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1141.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
