# KOMODO Concentration Review: LB (Luria-Bertani) medium

- Record: data/normalized_yaml/bacterial/KOMODO_381_LB_Luria-Bertani_medium.yaml
- ID: CultureMech:005128
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `af7bc0bb8d7303b063e10952283b53cb6e4be1271ff55b81f34d005cc6aeb390`
- Proposed/result SHA256: `af7bc0bb8d7303b063e10952283b53cb6e4be1271ff55b81f34d005cc6aeb390`
- Source: https://mediadive.dsmz.de/rest/medium/381
- Source SHA256: 278bab1c77dcbeb909d839e54a6fba27042daf112a642f25171d17c7e107d43e
- Retrieved: 2026-10-07T10:46:16.336083+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Peptone | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/381 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): NaCl, Peptone, Sea Salt, Tryptone | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/381 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): NaCl, Peptone, Sea Salt, Tryptone | unchanged |
| `ingredients[2].concentration` | Sea Salt | {"unit": "G_PER_L", "value": "25"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/381 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): NaCl, Peptone, Sea Salt, Tryptone | unchanged |
| `ingredients[3].concentration` | Agar | {"unit": "G_PER_L", "value": "12"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/381 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): NaCl, Peptone, Sea Salt, Tryptone | unchanged |
| `source.data.solutions[0].recipe[0]` | Tryptone | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/381 | {<br>                        "recipe_order": 1,<br>                        "compound": "Tryptone",<br>                        "compound_id": 71,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "mmol_l": 140.687,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/381 | {<br>                        "recipe_order": 2,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/381 | {<br>                        "recipe_order": 3,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "mmol_l": 171.116,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/381 | {<br>                        "recipe_order": 4,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 59.4654,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/381 | {<br>                        "recipe_order": 5,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/381 | {<br>                        "step": "Adjust pH to 7.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `381`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium381.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=381' >381</a></TD>
					<TD>LB (Luria-Bertani) medium</TD>
					<TD> 7.0</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium381.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium381.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
