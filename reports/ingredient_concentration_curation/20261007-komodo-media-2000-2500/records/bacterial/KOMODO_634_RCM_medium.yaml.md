# KOMODO Concentration Review: RCM medium

- Record: data/normalized_yaml/bacterial/KOMODO_634_RCM_medium.yaml
- ID: CultureMech:006148
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `64b85252daf122431446a6fa1686e4e397ffb786e08dd8137a4a4123744faebc`
- Proposed/result SHA256: `64b85252daf122431446a6fa1686e4e397ffb786e08dd8137a4a4123744faebc`
- Source: https://mediadive.dsmz.de/rest/medium/634
- Source SHA256: 08d5145d37c11531b461cde2a1bc8c197290bb618ade5ace80ba24b21afea94e
- Retrieved: 2026-10-07T12:16:43.764449+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | dehydrated RCM medium | {"unit": "G_PER_L", "value": "38"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/634 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Sodium carbonate | unchanged |
| `ingredients[1].concentration` | Sodium resazurin | {"unit": "G_PER_L", "value": "0.0005"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/634 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Sodium carbonate | unchanged |
| `ingredients[2].concentration` | Sodium carbonate | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/634 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Sodium carbonate | unchanged |
| `variant_children[0]` | rcm_medium_halophilic_clostridia | {"id": "CultureMech:006150", "name": "rcm_medium_halophilic_clostridia", "notes": "Same ingredient and concentration signature; review as possible duplicate source record.", "path": "data/normalized_yaml/bacterial/rcm_medium_halophilic_clostridia.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `variant_children[1]` | rcm_medium_modified | {"id": "CultureMech:006149", "name": "rcm_medium_modified", "notes": "Same ingredient and concentration signature; review as possible duplicate source record.", "path": "data/normalized_yaml/bacterial/rcm_medium_modified.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `variant_children[2]` | rcm_medium_n2_co2 | {"id": "CultureMech:001768", "name": "rcm_medium_n2_co2", "notes": "Same ingredient and concentration signature; review as possible duplicate source record.", "path": "data/normalized_yaml/bacterial/rcm_medium_n2_co2.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | dehydrated RCM medium | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/634 | {<br>                        "recipe_order": 1,<br>                        "compound": "dehydrated RCM medium",<br>                        "compound_id": 2126,<br>                        "attribute": "dissolved in distilled water",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Sodium resazurin | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/634 | {<br>                        "recipe_order": 2,<br>                        "compound": "Sodium resazurin",<br>                        "compound_id": 1852,<br>                        "attribute": "0.1% w/v",<br>                        "amount": 0.5,<br>                        "unit": "ml",<br>                        "g_l": 0.0005,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/634 | {<br>                        "step": "Dissolve dehydrated RCM medium (available from BD-BBL, OXOID or MERCK) in distilled water and add 0.5 ml/l Na-resazurin solution (0.1% w/v), bring to the boil and cool to room temperature while sparging with 100% N2 gas. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `634`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium634.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=634' >634</a></TD>
					<TD>RCM medium</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium634.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium634.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
