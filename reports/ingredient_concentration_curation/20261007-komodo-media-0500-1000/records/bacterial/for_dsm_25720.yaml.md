# KOMODO Concentration Review: For DSM 25720

- Record: data/normalized_yaml/bacterial/for_dsm_25720.yaml
- ID: CultureMech:004215
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `aff3d714dc765d710779b7c1e84b41c9ada1a97c94ceedca392acc2c6a9b1446`
- Proposed/result SHA256: `aff3d714dc765d710779b7c1e84b41c9ada1a97c94ceedca392acc2c6a9b1446`
- Source: https://mediadive.dsmz.de/rest/medium/191
- Source SHA256: 026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87
- Retrieved: 2026-10-07T10:43:27.139611+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Corn meal | {"unit": "G_PER_L", "value": "50.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/191 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `ingredients[1].concentration` | Agar | {"unit": "G_PER_L", "value": "10.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/191 | unknown / not asserted | unknown / not asserted | KOMODO variant requires its own formulation evidence; a link to the base DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts. | unchanged |
| `parent_media` | corn_meal_agar | {"id": "CultureMech:001283", "name": "corn_meal_agar", "notes": "KOMODO Medium 191.2 preserves DSMZ Medium 191 components and concentrations but records pH 7.5 for DSM 25720.", "path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml", "relationship": "PH_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Corn meal | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/191 | {<br>                        "recipe_order": 1,<br>                        "compound": "Corn meal",<br>                        "compound_id": 2087,<br>                        "amount": 50,<br>                        "unit": "g",<br>                        "g_l": 50,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/191 | {<br>                        "recipe_order": 2,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/191 | {<br>                        "recipe_order": 3,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "mmol_l": 29.7327,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/191 | {<br>                        "step": "Blend 50.0 g corn meal in 800 ml of distilled water. Leave overnight in the refrigerator. Heat at 60\u00b0C for one hour. Filter and make up volume to 1 l. Add 10.0 g agar and heat to dissolve, then autoclave at 121\u00b0C for 15 minutes. pH 6.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `191.2`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=191.2' >191.2</a></TD>
					<TD> For DSM 25720</TD>
					<TD> 7.5, NaOH</TD>
					<TD>true</TD>
					<TD>true</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
