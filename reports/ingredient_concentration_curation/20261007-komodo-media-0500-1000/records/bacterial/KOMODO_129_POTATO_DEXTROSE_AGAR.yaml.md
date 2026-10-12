# KOMODO Concentration Review: POTATO DEXTROSE AGAR

- Record: data/normalized_yaml/bacterial/KOMODO_129_POTATO_DEXTROSE_AGAR.yaml
- ID: CultureMech:004047
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e20a0c8e4d0ffe0537860a60458516ff1c2c870d26272f4879bcd8e456963f9b`
- Proposed/result SHA256: `e20a0c8e4d0ffe0537860a60458516ff1c2c870d26272f4879bcd8e456963f9b`
- Source: https://mediadive.dsmz.de/rest/medium/129
- Source SHA256: 5d1f36a91fce216d63d1d3447509fd753a402f48fad4a8b0e5d34db9415f31f1
- Retrieved: 2026-10-07T10:42:36.852628+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Glucose | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/129 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[1].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/129 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[2].concentration` | Potato | {"unit": "G_PER_L", "value": "200"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/129 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | potato_dextrose_agar | {"id": "CultureMech:010445", "name": "potato_dextrose_agar", "notes": "KOMODO record states DSMZ Medium 129 provenance and exactly matches the single DSMZ parent signature; parent is categorized fungal while the KOMODO source duplicate is categorized bacterial.", "path": "data/normalized_yaml/fungal/potato_dextrose_agar.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Potato infusion | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/129 | {<br>                        "recipe_order": 1,<br>                        "solution": "Potato infusion",<br>                        "solution_id": 227,<br>                        "attribute": "",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Glucose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/129 | {<br>                        "recipe_order": 2,<br>                        "compound": "Glucose",<br>                        "compound_id": 5,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 111.012,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/129 | {<br>                        "recipe_order": 3,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/129 | {<br>                        "step": "Adjust pH to 5.6. Sterilize at 121\u00b0C for 15 min"<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
| `source.data.solutions[1].recipe[0]` | Water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/129 | {<br>                        "recipe_order": 1,<br>                        "compound": "Water",<br>                        "compound_id": 754,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[1].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[1].recipe[1]` | Potato | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/129 | {<br>                        "recipe_order": 2,<br>                        "compound": "Potato",<br>                        "compound_id": 1606,<br>                        "amount": 200,<br>                        "unit": "g",<br>                        "g_l": 200,<br>                        "optional": 0<br>                    } | $.data.solutions[1].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[1].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/129 | {<br>                        "step": "Boil 200 g scrubbed and sliced potatoes in 1000 ml water for 1 hour. Pass through fine sieve. Avoid new potatoes."<br>                    } | $.data.solutions[1].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `129`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium129.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=129' >129</a></TD>
					<TD>POTATO DEXTROSE AGAR</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium129.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium129.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
