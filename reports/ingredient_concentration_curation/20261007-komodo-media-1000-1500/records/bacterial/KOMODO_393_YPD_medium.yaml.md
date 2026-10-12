# KOMODO Concentration Review: YPD medium

- Record: data/normalized_yaml/bacterial/KOMODO_393_YPD_medium.yaml
- ID: CultureMech:005177
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f5c418f62e7e5e29b313f767f59043b3ca544d52816fdf7d608d6bf5bc9c2b5b`
- Proposed/result SHA256: `f5c418f62e7e5e29b313f767f59043b3ca544d52816fdf7d608d6bf5bc9c2b5b`
- Source: https://mediadive.dsmz.de/rest/medium/393
- Source SHA256: 57ff32b4634974d9f35ab6fca4eb5217704c6f24e424ab59e28494cc9e811d6c
- Retrieved: 2026-10-07T10:46:27.609725+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/393 | Adjust pH to 5.6. Sterilize at 121°C for 15 min. | $.data.solutions[0].steps[0].step | Manual source review withheld support: The API preparation says pH 5.6, while local and API metadata and the original DSMZ PDF specify pH 6.5. Preserve the source disagreement and reconcile the exact recipe version; do not treat matching concentration rows as a fully reconciled formulation. | unchanged |
| `ingredients[1].concentration` | Peptone | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/393 | Adjust pH to 5.6. Sterilize at 121°C for 15 min. | $.data.solutions[0].steps[0].step | Manual source review withheld support: The API preparation says pH 5.6, while local and API metadata and the original DSMZ PDF specify pH 6.5. Preserve the source disagreement and reconcile the exact recipe version; do not treat matching concentration rows as a fully reconciled formulation. | unchanged |
| `ingredients[2].concentration` | Glucose | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/393 | Adjust pH to 5.6. Sterilize at 121°C for 15 min. | $.data.solutions[0].steps[0].step | Manual source review withheld support: The API preparation says pH 5.6, while local and API metadata and the original DSMZ PDF specify pH 6.5. Preserve the source disagreement and reconcile the exact recipe version; do not treat matching concentration rows as a fully reconciled formulation. | unchanged |
| `parent_media` | ypd_medium | {"id": "CultureMech:001500", "name": "ypd_medium", "notes": "KOMODO record explicitly cites DSMZ Medium 393; one unlinked DSMZ parent record exists and the local physical state, pH, ingredient, and concentration signatures match exactly.", "path": "data/normalized_yaml/bacterial/ypd_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/393 | {<br>                        "recipe_order": 1,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Peptone | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/393 | {<br>                        "recipe_order": 2,<br>                        "compound": "Peptone",<br>                        "compound_id": 1,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Glucose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/393 | {<br>                        "recipe_order": 3,<br>                        "compound": "Glucose",<br>                        "compound_id": 5,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 111.012,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/393 | {<br>                        "recipe_order": 4,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/393 | {<br>                        "step": "Adjust pH to 5.6. Sterilize at 121\u00b0C for 15 min."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `393`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium393.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=393' >393</a></TD>
					<TD>YPD medium</TD>
					<TD> 6.5</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium393.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium393.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
