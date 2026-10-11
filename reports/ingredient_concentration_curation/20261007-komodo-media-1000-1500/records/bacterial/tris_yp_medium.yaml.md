# KOMODO Concentration Review: TRIS - YP medium

- Record: data/normalized_yaml/bacterial/tris_yp_medium.yaml
- ID: CultureMech:004661
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `33809b7eca57b77125bf1cd4b91bbe842aa0f805d7ba49d99f5e643277b3f6a2`
- Proposed/result SHA256: `33809b7eca57b77125bf1cd4b91bbe842aa0f805d7ba49d99f5e643277b3f6a2`
- Source: https://mediadive.dsmz.de/rest/medium/257
- Source SHA256: 876fc8d97f5ec103e10ade341534cd3015eb4239ad2d8e630c77480f6289edaf
- Retrieved: 2026-10-07T10:44:29.515838+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/257 | {<br>                        "recipe_order": 1,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "attribute": "BD Bacto",<br>                        "amount": 3,<br>                        "unit": "g",<br>                        "g_l": 3,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[1].concentration` | Peptone | {"unit": "G_PER_L", "value": "0.6"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/257 | {<br>                        "recipe_order": 2,<br>                        "compound": "Peptone",<br>                        "compound_id": 1,<br>                        "attribute": "BD Bacto",<br>                        "amount": 0.6,<br>                        "unit": "g",<br>                        "g_l": 0.6,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[2].concentration` | Tris-HCl buffer | {"unit": "G_PER_L", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/257 | {<br>                        "recipe_order": 4,<br>                        "compound": "Tris-HCl buffer",<br>                        "compound_id": 285,<br>                        "attribute": "0.05 M, pH 7.5",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "mmol_l": 50,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `variant_children[0]` | bdellovibrio_yp_medium | {"id": "CultureMech:001356", "name": "bdellovibrio_yp_medium", "notes": "Same ingredient and concentration signature; review as possible duplicate source record.", "path": "data/normalized_yaml/bacterial/bdellovibrio_yp_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/257 | {<br>                        "step": "Preparation of double layered agar plates:<p>\r\n<b>Bottom layer:</b> Dissolve 12.0 g Bacto agar in 900 ml distilled water and autoclave. After cooling to 60\u00b0C add 100 ml of sterile YP medium (autoclaved at 121\u00b0C for 15 min) and pour plates. Dry plates at room temperature for 2 - 3 days .<p>\r\n<b>Top layer:</b> Grow prey bacterium on agar slants using medium 54. Prepare 5 ml aliquots of 0.6% Bacto agar in distilled water and autoclave in test tubes. After cooling to 45\u00b0C in a water bath add 0.5 ml sterile YP medium (autoclaved at 121\u00b0C for 15 min) and 0.5 ml cell suspension of host organism, mix and pour top layer. For the top layer of one plate use one 24 h old agar slant culture and wash off grown cells in 0.5 ml sterile water.<p>"<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
| `source.data.solutions[0].steps[1]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/257 | {<br>                        "step": "Inoculate double layer plates the same day when prepared."<br>                    } | $.data.solutions[0].steps[1] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `257`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium257.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=257' >257</a></TD>
					<TD>TRIS - YP medium</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium257.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium257.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
