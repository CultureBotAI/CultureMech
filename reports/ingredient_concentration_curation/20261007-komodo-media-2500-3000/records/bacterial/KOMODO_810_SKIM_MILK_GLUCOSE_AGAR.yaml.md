# KOMODO Concentration Review: SKIM MILK/GLUCOSE AGAR

- Record: data/normalized_yaml/bacterial/KOMODO_810_SKIM_MILK_GLUCOSE_AGAR.yaml
- ID: CultureMech:006533
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9e2fd685ff6ae6a3c56c14738f6c4dc73cc3eac535b1d88f646aab3399866dff`
- Proposed/result SHA256: `9e2fd685ff6ae6a3c56c14738f6c4dc73cc3eac535b1d88f646aab3399866dff`
- Source: https://mediadive.dsmz.de/rest/medium/810
- Source SHA256: ede9ce39d332c01cbfc5767901d36dc1c923bdedacae95be7451e372243543fb
- Retrieved: 2026-10-07T12:19:15.458546+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Skim milk | {"unit": "G_PER_L", "value": "80"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/810 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[1].concentration` | Glucose | {"unit": "G_PER_L", "value": "40"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/810 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[2].concentration` | Agar | {"unit": "G_PER_L", "value": "40"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/810 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | skim_milk_glucose_agar | {"id": "CultureMech:001955", "name": "skim_milk_glucose_agar", "notes": "KOMODO record states DSMZ Medium 810 provenance and exactly matches the single same-category DSMZ parent signature.", "path": "data/normalized_yaml/bacterial/skim_milk_glucose_agar.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Solution A | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/810 | {<br>                        "recipe_order": 1,<br>                        "solution": "Solution A",<br>                        "solution_id": 1645,<br>                        "amount": 500,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Solution B | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/810 | {<br>                        "recipe_order": 2,<br>                        "solution": "Solution B",<br>                        "solution_id": 1646,<br>                        "amount": 500,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/810 | {<br>                        "step": "Autoclave separately, mix and adjust pH to 6.8"<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
| `source.data.solutions[1].recipe[0]` | Skim milk | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/810 | {<br>                        "recipe_order": 1,<br>                        "compound": "Skim milk",<br>                        "compound_id": 262,<br>                        "amount": 40,<br>                        "unit": "g",<br>                        "g_l": 80,<br>                        "optional": 0<br>                    } | $.data.solutions[1].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[1].recipe[1]` | Water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/810 | {<br>                        "recipe_order": 2,<br>                        "compound": "Water",<br>                        "compound_id": 754,<br>                        "amount": 500,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[1].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[2].recipe[0]` | Glucose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/810 | {<br>                        "recipe_order": 1,<br>                        "compound": "Glucose",<br>                        "compound_id": 5,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 40,<br>                        "mmol_l": 222.025,<br>                        "optional": 0<br>                    } | $.data.solutions[2].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[2].recipe[1]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/810 | {<br>                        "recipe_order": 2,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 40,<br>                        "mmol_l": 118.931,<br>                        "optional": 0<br>                    } | $.data.solutions[2].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[2].recipe[2]` | Water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/810 | {<br>                        "recipe_order": 3,<br>                        "compound": "Water",<br>                        "compound_id": 754,<br>                        "amount": 500,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[2].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |

## Source Mapping

KOMODO accession `810`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium810.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=810' >810</a></TD>
					<TD>SKIM MILK/GLUCOSE AGAR</TD>
					<TD> 6.8</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium810.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium810.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
