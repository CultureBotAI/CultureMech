# KOMODO Concentration Review: MEDIUM 105 MODIFIED FOR DSM 15972

- Record: data/normalized_yaml/bacterial/medium_105_modified_for_dsm_15972.yaml
- ID: CultureMech:003623
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3f273a514bcdca738701dc4281107132c7542dbcdacbcd48cd24ed6a7ddacad1`
- Proposed/result SHA256: `3f273a514bcdca738701dc4281107132c7542dbcdacbcd48cd24ed6a7ddacad1`
- Source: https://mediadive.dsmz.de/rest/medium/105
- Source SHA256: 441ab4bbd2962c44a71fb8592d9e516744dcb930fb2384c790f352ce68e4de86
- Retrieved: 2026-10-07T10:42:13.034849+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Glucose | {"unit": "G_PER_L", "value": "100"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/105 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/105 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[2].concentration` | CaCO3 | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/105 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[3].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/105 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `source.data.solutions[0].recipe[0]` | Glucose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/105 | {<br>                        "recipe_order": 1,<br>                        "compound": "Glucose",<br>                        "compound_id": 5,<br>                        "amount": 100,<br>                        "unit": "g",<br>                        "g_l": 100,<br>                        "mmol_l": 555.062,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/105 | {<br>                        "recipe_order": 2,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | CaCO3 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/105 | {<br>                        "recipe_order": 3,<br>                        "compound": "CaCO3",<br>                        "compound_id": 13,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 199.82,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/105 | {<br>                        "recipe_order": 4,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/105 | {<br>                        "recipe_order": 5,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "condition": "for solid medium",<br>                        "amount": 15,<br>                        "unit": "g/l",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/105 | {<br>                        "step": "Adjust pH to 6.8."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
| `source.data.solutions[0].steps[1]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/105 | {<br>                        "step": "Autoclave at 121 \u00b0C for 15 min."<br>                    } | $.data.solutions[0].steps[1] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
| `source.data.solutions[0].steps[2]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/105 | {<br>                        "step": "Note: 20 g calcium carbonate in the medium serves as a buffer. The calcium carbonate will settle in agar plates before the agar has set, producing an opaque layer in the bottom. As the strain grows and acid is produced this will react with the calcium carbonate, causing it to dissolve and form zones of clearing immediately below the colonies. In liquid culture the calcium carbonate also forms a sediment that clears as acid is produced."<br>                    } | $.data.solutions[0].steps[2] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `105_15972`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium105.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=105_15972' >105_15972</a></TD>
					<TD>MEDIUM 105 MODIFIED FOR DSM 15972</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium105.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium105.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
