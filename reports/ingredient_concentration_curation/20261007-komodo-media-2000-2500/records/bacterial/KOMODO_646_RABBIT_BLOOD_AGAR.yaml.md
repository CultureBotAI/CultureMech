# KOMODO Concentration Review: RABBIT BLOOD AGAR

- Record: data/normalized_yaml/bacterial/KOMODO_646_RABBIT_BLOOD_AGAR.yaml
- ID: CultureMech:006192
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0543ad3c22f2d895bd8324f97a74933111674f07c3a533792eaad7dc2a7aa4bf`
- Proposed/result SHA256: `0543ad3c22f2d895bd8324f97a74933111674f07c3a533792eaad7dc2a7aa4bf`
- Source: https://mediadive.dsmz.de/rest/medium/646
- Source SHA256: fc6f9b5dcf1a1f149b058adb72ac0f096356b36d3ac2293edc2262f5b26aa806
- Retrieved: 2026-10-07T12:16:56.823785+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Blood Agar Base from Difco 0045 | {"unit": "G_PER_L", "value": "40.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/646 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Blood Agar Base, Blood Agar Base from Difco 0045, Rabbit blood, Sterile defibrinated rabbit blood | unchanged |
| `ingredients[1].concentration` | Sterile defibrinated rabbit blood | {"unit": "PERCENT_V_V", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/646 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Blood Agar Base, Blood Agar Base from Difco 0045, Rabbit blood, Sterile defibrinated rabbit blood | unchanged |
| `parent_media` | rabbit_blood_agar | {"id": "CultureMech:001784", "name": "rabbit_blood_agar", "notes": "KOMODO record states DSMZ Medium 646 provenance and mirrors the same rabbit blood agar formulation.", "path": "data/normalized_yaml/bacterial/rabbit_blood_agar.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Blood Agar Base | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/646 | {<br>                        "recipe_order": 2,<br>                        "compound": "Blood Agar Base",<br>                        "compound_id": 2130,<br>                        "attribute": "Difco 0045",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Rabbit blood | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/646 | {<br>                        "recipe_order": 3,<br>                        "compound": "Rabbit blood",<br>                        "compound_id": 1927,<br>                        "attribute": "sterile, defibrinated",<br>                        "amount": 5,<br>                        "unit": "%",<br>                        "g_l": 50,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/646 | {<br>                        "step": "Prepare Blood Agar Base from Difco 0045 according to directions on the bottle (40.0 g/l). Sterilize and cool to 45\u00b0C. Aseptically add 5% sterile defibrinated rabbit blood or sheep blood, mix well."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `646`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium646.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=646' >646</a></TD>
					<TD>RABBIT BLOOD AGAR</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium646.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium646.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
