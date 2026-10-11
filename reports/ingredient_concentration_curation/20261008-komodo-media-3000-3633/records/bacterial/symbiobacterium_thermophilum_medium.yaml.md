# KOMODO Concentration Review: SYMBIOBACTERIUM THERMOPHILUM medium

- Record: data/normalized_yaml/bacterial/symbiobacterium_thermophilum_medium.yaml
- ID: CultureMech:004043
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `694cc61ae41e8118c59caafd6af20820225ed82deca18cfed10f1cd88c6944b5`
- Proposed/result SHA256: `694cc61ae41e8118c59caafd6af20820225ed82deca18cfed10f1cd88c6944b5`
- Source: https://mediadive.dsmz.de/rest/medium/1293
- Source SHA256: 2bfcd49f86d402605b6d6479d2a6c3579d09c2ebbbc10dc44f66e710fcc2fbb1
- Retrieved: 2026-10-07T13:20:06.632871+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1293 | unknown / not asserted | unknown / not asserted | Explicit stock-to-medium mixing ratio requires preparation-stage review; table concentrations cannot automatically establish both base and complete-medium amounts. | unchanged |
| `ingredients[1].concentration` | NaNO3 | {"unit": "G_PER_L", "value": "1.7"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1293 | unknown / not asserted | unknown / not asserted | Explicit stock-to-medium mixing ratio requires preparation-stage review; table concentrations cannot automatically establish both base and complete-medium amounts. | unchanged |
| `ingredients[2].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1293 | unknown / not asserted | unknown / not asserted | Explicit stock-to-medium mixing ratio requires preparation-stage review; table concentrations cannot automatically establish both base and complete-medium amounts. | unchanged |
| `ingredients[3].concentration` | Tryptone | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1293 | unknown / not asserted | unknown / not asserted | Explicit stock-to-medium mixing ratio requires preparation-stage review; table concentrations cannot automatically establish both base and complete-medium amounts. | unchanged |
| `ingredients[4].concentration` | NH4HCO3 | {"unit": "G_PER_L", "value": "3.2"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1293 | unknown / not asserted | unknown / not asserted | Explicit stock-to-medium mixing ratio requires preparation-stage review; table concentrations cannot automatically establish both base and complete-medium amounts. | unchanged |
| `source.data.solutions[0].recipe[0]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1293 | {<br>                        "recipe_order": 1,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "mmol_l": 85.5578,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | NaNO3 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1293 | {<br>                        "recipe_order": 2,<br>                        "compound": "NaNO3",<br>                        "compound_id": 187,<br>                        "amount": 1.7,<br>                        "unit": "g",<br>                        "g_l": 1.7,<br>                        "mmol_l": 20.0012,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1293 | {<br>                        "recipe_order": 3,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "attribute": "OXOID",<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Tryptone | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1293 | {<br>                        "recipe_order": 4,<br>                        "compound": "Tryptone",<br>                        "compound_id": 71,<br>                        "attribute": "BD Bacto",<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | NH4HCO3 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1293 | {<br>                        "recipe_order": 5,<br>                        "compound": "NH4HCO3",<br>                        "compound_id": 855,<br>                        "amount": 3.2,<br>                        "unit": "g",<br>                        "g_l": 3.2,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[5]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1293 | {<br>                        "recipe_order": 6,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[5] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1293 | {<br>                        "step": "Dissolve ingredients (except bicarbonate) and adjust pH to 8.0, sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add bicarbonate from a sterile anoxic 3.2% (w/v) stock solution prepared under 80% N2 and 20% CO2 gas mixture (e.g., add 1 ml stock solution per 9 ml medium). Adjust pH of the complete medium to 7.5 - 7.8, if necessary."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
| `source.data.solutions[0].steps[1]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1293 | {<br>                        "step": "After inoculation add sterile 100% H2 gas to an overpressure of 0.5 bar."<br>                    } | $.data.solutions[0].steps[1] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `1293`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1293.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1293' >1293</a></TD>
					<TD>SYMBIOBACTERIUM THERMOPHILUM medium</TD>
					<TD> 7.5 - 7.8</TD>
					<TD>true</TD>
					<TD>true</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1293.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1293.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
