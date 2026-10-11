# KOMODO Concentration Review: FASTIDIOUS ANAEROBE AGAR

- Record: data/normalized_yaml/bacterial/KOMODO_1203_FASTIDIOUS_ANAEROBE_AGAR.yaml
- ID: CultureMech:003951
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2853248face159a16aaddc004e71932eb1fd83587a5625be21b134d24bcc6ac1`
- Proposed/result SHA256: `2853248face159a16aaddc004e71932eb1fd83587a5625be21b134d24bcc6ac1`
- Source: https://mediadive.dsmz.de/rest/medium/1203
- Source SHA256: d0659707de5efe353ab2bc2b26c7fb2dc2cb03567b6e71e78d1c8bd0b3ea51e4
- Retrieved: 2026-10-07T13:18:45.580830+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Fastidious Anaerobe Agar (Acumedia) | {"unit": "G_PER_L", "value": "45.7"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1203 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Fastidious Anaerobe Agar, Fastidious Anaerobe Agar (Acumedia), Horse blood, Sterile defibrinated horse blood | unchanged |
| `ingredients[1].concentration` | Deionized water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1203 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Fastidious Anaerobe Agar, Fastidious Anaerobe Agar (Acumedia), Horse blood, Sterile defibrinated horse blood | unchanged |
| `ingredients[2].concentration` | Sterile defibrinated horse blood | {"unit": "PERCENT_V_V", "value": "5-10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1203 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Fastidious Anaerobe Agar, Fastidious Anaerobe Agar (Acumedia), Horse blood, Sterile defibrinated horse blood | unchanged |
| `parent_media` | fastidious_anaerobe_agar | {"id": "CultureMech:000653", "name": "fastidious_anaerobe_agar", "notes": "Parent DSMZ Medium 1203 formula for this KOMODO source duplicate.", "path": "data/normalized_yaml/bacterial/fastidious_anaerobe_agar.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Fastidious Anaerobe Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1203 | {<br>                        "recipe_order": 1,<br>                        "compound": "Fastidious Anaerobe Agar",<br>                        "compound_id": 1077,<br>                        "attribute": "acumedia",<br>                        "amount": 45.7,<br>                        "unit": "g",<br>                        "g_l": 45.7,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Deionized water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1203 | {<br>                        "recipe_order": 2,<br>                        "compound": "Deionized water",<br>                        "compound_id": 418,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Horse blood | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1203 | {<br>                        "recipe_order": 3,<br>                        "compound": "Horse blood",<br>                        "compound_id": 724,<br>                        "condition": "adjust if required",<br>                        "amount": 10,<br>                        "unit": "%",<br>                        "g_l": 100,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1203 | {<br>                        "step": "Allow to soak for 10 minutes, swirl to mix then sterilize by autoclaving at 121\u00b0C for 15 minutes. Cool to 47\u00b0C then aseptically add 5-10% of sterile defibrinated horse blood, mix well and pour plates. pH: 7.2 \u00b1 0.2"<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `1203`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1203' >1203</a></TD>
					<TD>FASTIDIOUS ANAEROBE AGAR</TD>
					<TD> 7.0 - 7.4</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
