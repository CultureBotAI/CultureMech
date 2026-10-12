# KOMODO Concentration Review: medium FOR OSMOPHILIC FUNGI (M 40 Y)

- Record: data/normalized_yaml/bacterial/KOMODO_187_medium_FOR_OSMOPHILIC_FUNGI_M_40_Y.yaml
- ID: CultureMech:004211
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `74064c6a8c46274acbe7bde1ea3c8c15a84680a5693ce88b156741fa275dfd37`
- Proposed/result SHA256: `74064c6a8c46274acbe7bde1ea3c8c15a84680a5693ce88b156741fa275dfd37`
- Source: https://mediadive.dsmz.de/rest/medium/187
- Source SHA256: 07625361f0d69ed4448c7db3385b713adc4e36e147923c59f5975a572023f583
- Retrieved: 2026-10-07T10:43:24.007559+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Sucrose | {"unit": "G_PER_L", "value": "400"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/187 | Adjust pH to 5.6. Sterilize at 121°C for 15 min | $.data.solutions[0].steps[0].step | Manual source review withheld support: Source metadata and the local record state pH 5.4, while the source preparation says adjust pH to 5.6. The original linked PDF inspected in this review gives no pH statement. The preparation-stage or source-version distinction remains unresolved; no pH or concentration replacement is selected. | unchanged |
| `ingredients[1].concentration` | Malt extract | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/187 | Adjust pH to 5.6. Sterilize at 121°C for 15 min | $.data.solutions[0].steps[0].step | Manual source review withheld support: Source metadata and the local record state pH 5.4, while the source preparation says adjust pH to 5.6. The original linked PDF inspected in this review gives no pH statement. The preparation-stage or source-version distinction remains unresolved; no pH or concentration replacement is selected. | unchanged |
| `ingredients[2].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/187 | Adjust pH to 5.6. Sterilize at 121°C for 15 min | $.data.solutions[0].steps[0].step | Manual source review withheld support: Source metadata and the local record state pH 5.4, while the source preparation says adjust pH to 5.6. The original linked PDF inspected in this review gives no pH statement. The preparation-stage or source-version distinction remains unresolved; no pH or concentration replacement is selected. | unchanged |
| `ingredients[3].concentration` | Agar | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/187 | Adjust pH to 5.6. Sterilize at 121°C for 15 min | $.data.solutions[0].steps[0].step | Manual source review withheld support: Source metadata and the local record state pH 5.4, while the source preparation says adjust pH to 5.6. The original linked PDF inspected in this review gives no pH statement. The preparation-stage or source-version distinction remains unresolved; no pH or concentration replacement is selected. | unchanged |
| `variant_children[0]` | m40y_agar | {"id": "CultureMech:002699", "name": "m40y_agar", "notes": "Same ingredient and concentration signature; review as possible duplicate source record.", "path": "data/normalized_yaml/bacterial/m40y_agar.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `parent_media` | medium_for_osmophilic_fungi_m_40_y | {"id": "CultureMech:001279", "name": "medium_for_osmophilic_fungi_m_40_y", "notes": "KOMODO record explicitly cites DSMZ Medium 187; one unlinked DSMZ parent record exists and the local physical state, pH, ingredient, and concentration signatures match exactly.", "path": "data/normalized_yaml/bacterial/medium_for_osmophilic_fungi_m_40_y.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Sucrose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/187 | {<br>                        "recipe_order": 1,<br>                        "compound": "Sucrose",<br>                        "compound_id": 108,<br>                        "amount": 400,<br>                        "unit": "g",<br>                        "g_l": 400,<br>                        "mmol_l": 1168.57,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Malt extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/187 | {<br>                        "recipe_order": 2,<br>                        "compound": "Malt extract",<br>                        "compound_id": 116,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/187 | {<br>                        "recipe_order": 3,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/187 | {<br>                        "recipe_order": 4,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 59.4654,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/187 | {<br>                        "recipe_order": 5,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/187 | {<br>                        "step": "Adjust pH to 5.6. Sterilize at 121\u00b0C for 15 min"<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `187`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium187.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=187' >187</a></TD>
					<TD>medium FOR OSMOPHILIC FUNGI (M 40 Y)</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium187.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium187.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
