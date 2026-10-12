# KOMODO Concentration Review: RCM medium (halophilic clostridia)

- Record: data/normalized_yaml/bacterial/rcm_medium_halophilic_clostridia.yaml
- ID: CultureMech:006150
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `db12f6ad33fbb3859339781bc110c03104b566f544856c65736bcdc1f9837256`
- Proposed/result SHA256: `db12f6ad33fbb3859339781bc110c03104b566f544856c65736bcdc1f9837256`
- Source: https://mediadive.dsmz.de/rest/medium/634b
- Source SHA256: a8bfd580a484d3f3b87ec00b5619c43439573112c537f8ff682cb868349ac003
- Retrieved: 2026-10-07T12:16:45.312244+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | dehydrated RCM medium | {"unit": "G_PER_L", "value": "38"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/634b | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Sea salts, Sodium carbonate | unchanged |
| `ingredients[1].concentration` | Sodium resazurin | {"unit": "G_PER_L", "value": "0.0005"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/634b | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Sea salts, Sodium carbonate | unchanged |
| `ingredients[2].concentration` | Sodium carbonate | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/634b | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Sea salts, Sodium carbonate | unchanged |
| `parent_media` | rcm_medium | {"id": "CultureMech:006148", "name": "rcm_medium", "path": "data/normalized_yaml/bacterial/KOMODO_634_RCM_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | dehydrated RCM medium | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/634b | {<br>                        "recipe_order": 1,<br>                        "compound": "dehydrated RCM medium",<br>                        "compound_id": 2126,<br>                        "attribute": "",<br>                        "amount": 38,<br>                        "unit": "g",<br>                        "g_l": 38,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Sea salts | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/634b | {<br>                        "recipe_order": 2,<br>                        "compound": "Sea salts",<br>                        "compound_id": 2367,<br>                        "attribute": "SIGMA",<br>                        "amount": 30,<br>                        "unit": "g",<br>                        "g_l": 30,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Sodium resazurin | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/634b | {<br>                        "recipe_order": 3,<br>                        "compound": "Sodium resazurin",<br>                        "compound_id": 1852,<br>                        "attribute": "0.1% w/v",<br>                        "amount": 0.5,<br>                        "unit": "ml",<br>                        "g_l": 0.0005,<br>                        "mmol_l": 0.00199068,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/634b | {<br>                        "recipe_order": 4,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/634b | {<br>                        "step": "Dissolve dehydrated RCM medium (available from BD BBL, OXOID, or MERCK) and SIGMA Sea Salts (30.0 g/l) in distilled water and add 0.5 ml/l Na-resazurin solution (0.1% w/v). Bring to a boil and cool to room temperature while sparging with 100% N2 gas. Dispense the medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave for 15 min at 121\u00b0C. Adjust the pH of the complete medium to 6.8."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `634b`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium634b.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=634b' >634b</a></TD>
					<TD>RCM medium (halophilic clostridia)</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium634b.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium634b.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
