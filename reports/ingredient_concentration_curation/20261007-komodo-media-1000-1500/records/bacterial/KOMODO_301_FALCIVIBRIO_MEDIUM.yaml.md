# KOMODO Concentration Review: FALCIVIBRIO MEDIUM

- Record: data/normalized_yaml/bacterial/KOMODO_301_FALCIVIBRIO_MEDIUM.yaml
- ID: CultureMech:004799
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `4b72b7a50fc75a9d93b83bd6099b45429d90a8df5e8691db01c5cfc4654c1812`
- Proposed/result SHA256: `4b72b7a50fc75a9d93b83bd6099b45429d90a8df5e8691db01c5cfc4654c1812`
- Source: https://mediadive.dsmz.de/rest/medium/301
- Source SHA256: e05eab934165218efd4f93094b4496b5429e3f1b7b3bb994943f201f64f22eb5
- Retrieved: 2026-10-07T10:45:02.824021+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Wilkins-Chalgren-Anaerobe-Broth | {"unit": "G_PER_L", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/301 | {<br>                        "recipe_order": 1,<br>                        "compound": "Wilkins-Chalgren-Anaerobe-Broth",<br>                        "compound_id": 2093,<br>                        "attribute": "Oxoid",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[1].concentration` | L-Cysteine | {"unit": "G_PER_L", "value": "0.3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/301 | {<br>                        "recipe_order": 2,<br>                        "compound": "L-Cysteine",<br>                        "compound_id": 671,<br>                        "amount": 0.3,<br>                        "unit": "g",<br>                        "g_l": 0.3,<br>                        "mmol_l": 2.47606,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source g_l disagrees with its amount/unit/provider-volume arithmetic. | unchanged |
| `ingredients[2].concentration` | Resazurin | {"unit": "G_PER_L", "value": "0.001"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/301 | {<br>                        "recipe_order": 3,<br>                        "compound": "Resazurin",<br>                        "compound_id": 25,<br>                        "amount": 1,<br>                        "unit": "mg",<br>                        "g_l": 0.001,<br>                        "mmol_l": 0.00436319,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source g_l disagrees with its amount/unit/provider-volume arithmetic. | unchanged |
| `ingredients[3].concentration` | Sterile serum | {"unit": "G_PER_L", "value": "50"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/301 | {<br>                        "recipe_order": 4,<br>                        "compound": "Sterile serum",<br>                        "compound_id": 2094,<br>                        "attribute": "horse, bovine or lamb",<br>                        "amount": 50,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `parent_media` | falcivibrio_medium | {"id": "CultureMech:001401", "name": "falcivibrio_medium", "notes": "KOMODO record explicitly cites DSMZ Medium 301; one unlinked DSMZ parent record exists and the local physical state, pH, ingredient, and concentration signatures match exactly.", "path": "data/normalized_yaml/bacterial/falcivibrio_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/301 | {<br>                        "step": "Wilkins-Chalgren-Anaerobe-Broth (Oxoid) is supplemented with 0.3 g/l of L-cysteine and 1.0 mg/l of resazurin. Prepare the medium under 100% nitrogen gas. To the autoclaved medium add 50 ml/l of sterile serum (horse, bovine or lamb)."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `301`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium301.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=301' >301</a></TD>
					<TD>FALCIVIBRIO MEDIUM</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>true</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium301.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium301.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
