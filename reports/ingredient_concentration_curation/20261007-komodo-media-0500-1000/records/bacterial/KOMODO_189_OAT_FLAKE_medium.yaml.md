# KOMODO Concentration Review: OAT FLAKE medium

- Record: data/normalized_yaml/bacterial/KOMODO_189_OAT_FLAKE_medium.yaml
- ID: CultureMech:004213
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `703f3bffcb2b6b58848e40c043040a43c9f48aef1ee956ef19901c208e9b0fb2`
- Proposed/result SHA256: `703f3bffcb2b6b58848e40c043040a43c9f48aef1ee956ef19901c208e9b0fb2`
- Source: https://mediadive.dsmz.de/rest/medium/189
- Source SHA256: 5f9a3c04ab01c39d3a249d81a5327ee074141354070941060433704b179cd74e
- Retrieved: 2026-10-07T10:43:25.566116+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Oat flakes | {"unit": "G_PER_L", "value": "30.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/189 | {<br>                        "recipe_order": 1,<br>                        "compound": "Oat flakes",<br>                        "compound_id": 292,<br>                        "amount": 30,<br>                        "unit": "g",<br>                        "g_l": 30,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[1].concentration` | Agar | {"unit": "G_PER_L", "value": "15.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/189 | {<br>                        "recipe_order": 2,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/189 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `parent_media` | oat_flake_medium | {"id": "CultureMech:001281", "name": "oat_flake_medium", "notes": "KOMODO record explicitly cites DSMZ Medium 189; the DSMZ parent has matching physical state, ingredient, and concentration signatures.", "path": "data/normalized_yaml/bacterial/oat_flake_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/189 | {<br>                        "step": "Boil oat flakes in water for 10 min; fill up to 1 l and add agar. Autoclave 20 min at 121\u00b0C. Shake before pouring. pH 6.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `189`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium189.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=189' >189</a></TD>
					<TD>OAT FLAKE medium</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium189.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium189.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
