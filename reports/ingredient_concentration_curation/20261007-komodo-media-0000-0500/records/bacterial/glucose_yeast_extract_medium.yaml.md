# KOMODO Concentration Review: GLUCOSE Yeast extract medium

- Record: data/normalized_yaml/bacterial/glucose_yeast_extract_medium.yaml
- ID: CultureMech:005997
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f6ca2c8718ed9e695c44d825700d249d868f4c23d051044ef35df9b553ffc2b6`
- Proposed/result SHA256: `f6ca2c8718ed9e695c44d825700d249d868f4c23d051044ef35df9b553ffc2b6`
- Source: https://mediadive.dsmz.de/rest/medium/54
- Source SHA256: d471cc47a744485b528bccd26be3453def3e07c5cdc870eda5e122732eb6eaad
- Retrieved: 2026-10-07T10:41:23.980373+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Glucose | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/54 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/54 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | CaCO3 | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/54 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Agar | {"unit": "G_PER_L", "value": "17"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/54 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | Glucose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/54 | {<br>                        "recipe_order": 1,<br>                        "compound": "Glucose",<br>                        "compound_id": 5,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 111.012,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/54 | {<br>                        "recipe_order": 2,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | CaCO3 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/54 | {<br>                        "recipe_order": 3,<br>                        "compound": "CaCO3",<br>                        "compound_id": 13,<br>                        "attribute": "light precipitate",<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 199.82,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/54 | {<br>                        "recipe_order": 4,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/54 | {<br>                        "recipe_order": 5,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "condition": "if required",<br>                        "amount": 17,<br>                        "unit": "g",<br>                        "g_l": 17,<br>                        "mmol_l": 50.5456,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |

## Source Mapping

KOMODO accession `54`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium54.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=54' >54</a></TD>
					<TD>GLUCOSE Yeast extract medium</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>true</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium54.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium54.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
