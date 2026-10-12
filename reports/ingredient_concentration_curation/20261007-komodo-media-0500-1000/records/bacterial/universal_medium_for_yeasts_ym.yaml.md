# KOMODO Concentration Review: UNIVERSAL medium FOR YEASTS (YM)

- Record: data/normalized_yaml/bacterial/universal_medium_for_yeasts_ym.yaml
- ID: CultureMech:004210
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e4a6878a3a4dfb21f0293118983d555c0953a01fa9e8738f6d3ef76f240cb1bc`
- Proposed/result SHA256: `e4a6878a3a4dfb21f0293118983d555c0953a01fa9e8738f6d3ef76f240cb1bc`
- Source: https://mediadive.dsmz.de/rest/medium/186
- Source SHA256: e5cd7acae270fad684ed7448b2ee0167aa49e0c47ee40068af36bc33656b057f
- Retrieved: 2026-10-07T10:43:23.221380+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "3.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/186 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Malt extract | {"unit": "G_PER_L", "value": "3.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/186 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Soy peptone | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/186 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Glucose | {"unit": "G_PER_L", "value": "10.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/186 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | Agar | {"unit": "G_PER_L", "value": "15.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/186 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/186 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `parent_media` | universal_medium_for_yeasts_ym | {"id": "CultureMech:010463", "name": "universal_medium_for_yeasts_ym", "notes": "KOMODO record explicitly cites DSMZ Medium 186; the DSMZ parent has matching physical state, ingredient, and concentration signatures.", "path": "data/normalized_yaml/fungal/universal_medium_for_yeasts_ym.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/186 | {<br>                        "recipe_order": 1,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 3,<br>                        "unit": "g",<br>                        "g_l": 3,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Malt extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/186 | {<br>                        "recipe_order": 2,<br>                        "compound": "Malt extract",<br>                        "compound_id": 116,<br>                        "amount": 3,<br>                        "unit": "g",<br>                        "g_l": 3,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Soy peptone | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/186 | {<br>                        "recipe_order": 3,<br>                        "compound": "Soy peptone",<br>                        "compound_id": 75,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Glucose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/186 | {<br>                        "recipe_order": 4,<br>                        "compound": "Glucose",<br>                        "compound_id": 5,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "mmol_l": 55.5062,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/186 | {<br>                        "recipe_order": 5,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[5]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/186 | {<br>                        "recipe_order": 6,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[5] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |

## Source Mapping

KOMODO accession `186`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium186.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=186' >186</a></TD>
					<TD>UNIVERSAL medium FOR YEASTS (YM)</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium186.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium186.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
