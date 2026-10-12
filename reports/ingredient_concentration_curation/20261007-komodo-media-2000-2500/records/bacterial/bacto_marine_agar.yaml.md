# KOMODO Concentration Review: BACTO MARINE AGAR

- Record: data/normalized_yaml/bacterial/bacto_marine_agar.yaml
- ID: CultureMech:006092
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b1415b4cbb30bedbc2b26bdd1b03096af51369b55f660fa4ec1c3706b37786f2`
- Proposed/result SHA256: `b1415b4cbb30bedbc2b26bdd1b03096af51369b55f660fa4ec1c3706b37786f2`
- Source: https://mediadive.dsmz.de/rest/medium/604
- Source SHA256: a25ea7c956aaaa789566158fc1dbcb3b5655e60dff6e71b8c25c9eb7222324be
- Retrieved: 2026-10-07T12:16:16.152652+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Marine agar 2216 (Difco 0979) | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/604 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Marine agar 2216, Marine agar 2216 (Difco 0979) | unchanged |
| `source.data.solutions[0].recipe[0]` | Marine agar 2216 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/604 | {<br>                        "recipe_order": 1,<br>                        "compound": "Marine agar 2216",<br>                        "compound_id": 1628,<br>                        "attribute": "Difco 0979",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/604 | {<br>                        "step": "MARINE AGAR 2216 (Difco 0979)."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `604`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium604.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=604' >604</a></TD>
					<TD>BACTO MARINE AGAR</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium604.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium604.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
