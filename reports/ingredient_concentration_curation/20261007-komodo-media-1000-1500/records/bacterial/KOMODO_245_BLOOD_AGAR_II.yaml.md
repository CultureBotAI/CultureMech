# KOMODO Concentration Review: BLOOD AGAR II

- Record: data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml
- ID: CultureMech:004616
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `64efad30588c9f1e9b70c7ba1512b7bda95274f46f55a1dbc72aff16ee39935a`
- Proposed/result SHA256: `64efad30588c9f1e9b70c7ba1512b7bda95274f46f55a1dbc72aff16ee39935a`
- Source: https://mediadive.dsmz.de/rest/medium/245
- Source SHA256: 79e3bafc9fdea26e0e22a44761168b39a03688350f0e6af5f1e1aeb798f7c869
- Retrieved: 2026-10-07T10:44:19.755358+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Defibrinated sheep blood | {"unit": "PERCENT_W_V", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/245 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[1].concentration` | Casein peptone | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/245 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[2].concentration` | Soy peptone | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/245 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[3].concentration` | NaCl | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/245 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[4].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/245 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | blood_agar_ii | {"id": "CultureMech:001345", "name": "blood_agar_ii", "notes": "KOMODO record explicitly cites DSMZ Medium 245; one unlinked DSMZ parent record exists and the local physical state, pH, ingredient, and concentration signatures match exactly.", "path": "data/normalized_yaml/bacterial/blood_agar_ii.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Main sol. 220 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/245 | {<br>                        "recipe_order": 1,<br>                        "solution": "Main sol. 220",<br>                        "solution_id": 477,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Defibrinated sheep blood | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/245 | {<br>                        "recipe_order": 2,<br>                        "compound": "Defibrinated sheep blood",<br>                        "compound_id": 1717,<br>                        "amount": 5,<br>                        "unit": "%",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[1].recipe[0]` | Casein peptone | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/245 | {<br>                        "recipe_order": 1,<br>                        "compound": "Casein peptone",<br>                        "compound_id": 21,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[1].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[1].recipe[1]` | Soy peptone | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/245 | {<br>                        "recipe_order": 2,<br>                        "compound": "Soy peptone",<br>                        "compound_id": 75,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[1].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[1].recipe[2]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/245 | {<br>                        "recipe_order": 3,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[1].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[1].recipe[3]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/245 | {<br>                        "recipe_order": 4,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[1].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[1].recipe[4]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/245 | {<br>                        "recipe_order": 5,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[1].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[1].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/245 | {<br>                        "step": "Adjust pH to 7.3. Medium is identical with Tryptone Soya Agar (Oxoid CM 131)."<br>                    } | $.data.solutions[1].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `245`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium245.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=245' >245</a></TD>
					<TD>BLOOD AGAR II</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium245.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium245.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
