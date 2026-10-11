# KOMODO Concentration Review: SOUR DOUGH medium

- Record: data/normalized_yaml/bacterial/KOMODO_225_SOUR_DOUGH_medium.yaml
- ID: CultureMech:004579
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `21ef4af48562889dd7a1d8071c190c9e4137bd8b4efe3318305373f545247fef`
- Proposed/result SHA256: `21ef4af48562889dd7a1d8071c190c9e4137bd8b4efe3318305373f545247fef`
- Source: https://mediadive.dsmz.de/rest/medium/225
- Source SHA256: 0bc7ff32175041c3dd679e0b49ebe6c4e2ae85907e4adeaac9bc343cb2ea1f05
- Retrieved: 2026-10-07T10:44:04.738546+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Maltose | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/225 | unknown / not asserted | unknown / not asserted | Duplicate ingredient labels require row-specific identity review. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "18.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/225 | unknown / not asserted | unknown / not asserted | Duplicate ingredient labels require row-specific identity review. | unchanged |
| `ingredients[2].concentration` | Tween 80 | {"unit": "G_PER_L", "value": "0.3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/225 | unknown / not asserted | unknown / not asserted | Duplicate ingredient labels require row-specific identity review. | unchanged |
| `ingredients[3].concentration` | Casein peptone | {"unit": "G_PER_L", "value": "6"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/225 | unknown / not asserted | unknown / not asserted | Duplicate ingredient labels require row-specific identity review. | unchanged |
| `ingredients[4].concentration` | HCl | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/225 | unknown / not asserted | unknown / not asserted | Duplicate ingredient labels require row-specific identity review. | unchanged |
| `source.data.solutions[0].recipe[0]` | Maltose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/225 | {<br>                        "recipe_order": 1,<br>                        "compound": "Maltose",<br>                        "compound_id": 171,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 58.4283,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/225 | {<br>                        "recipe_order": 2,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 3,<br>                        "unit": "g",<br>                        "g_l": 3,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/225 | {<br>                        "recipe_order": 3,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "attribute": "fresh",<br>                        "amount": 15,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Tween 80 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/225 | {<br>                        "recipe_order": 4,<br>                        "compound": "Tween 80",<br>                        "compound_id": 22,<br>                        "amount": 0.3,<br>                        "unit": "g",<br>                        "g_l": 0.3,<br>                        "mmol_l": 0.229211,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | Casein peptone | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/225 | {<br>                        "recipe_order": 5,<br>                        "compound": "Casein peptone",<br>                        "compound_id": 21,<br>                        "condition": "",<br>                        "attribute": "tryptic digest",<br>                        "amount": 6,<br>                        "unit": "g",<br>                        "g_l": 6,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[5]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/225 | {<br>                        "recipe_order": 6,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[5] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/225 | {<br>                        "step": "Adjust pH to 5.6 with 20% lactic acid or HCl. Fresh yeast extract is prepared by autoclaving a 20% suspension of commercial baker's yeast in distilled water for 30 minutes at 121\u00b0C, allowing the suspension to settle overnight at 2 to 8\u00b0C, decanting and further clarifying the supernatant by centrifugation. The extract prepared in this manner contains 1.5% solids and if not to be used within a few days, should be frozen or freeze-dried immediately."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `225`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium225.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=225' >225</a></TD>
					<TD>SOUR DOUGH medium</TD>
					<TD> 5.6,HCl</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium225.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium225.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
