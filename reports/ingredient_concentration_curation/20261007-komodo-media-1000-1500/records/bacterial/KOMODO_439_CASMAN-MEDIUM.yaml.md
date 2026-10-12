# KOMODO Concentration Review: CASMAN-MEDIUM

- Record: data/normalized_yaml/bacterial/KOMODO_439_CASMAN-MEDIUM.yaml
- ID: CultureMech:005287
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `82f492761b35804283da6833858e2b7ca1575e4d96c7ef39143ca945e0319de6`
- Proposed/result SHA256: `82f492761b35804283da6833858e2b7ca1575e4d96c7ef39143ca945e0319de6`
- Source: https://mediadive.dsmz.de/rest/medium/439
- Source SHA256: 68e2d8d5a6de027ba6d97b57188d4898ba7fd7759909165b9d6ee6befbdd0f52
- Retrieved: 2026-10-07T10:47:04.459875+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Casman-Agar-Base (Difco) | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/439 | unknown / not asserted | unknown / not asserted | Duplicate ingredient labels require row-specific identity review. | unchanged |
| `ingredients[1].concentration` | Sheep blood | {"unit": "PERCENT_V_V", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/439 | unknown / not asserted | unknown / not asserted | Duplicate ingredient labels require row-specific identity review. | unchanged |
| `ingredients[2].concentration` | Water-lysed sheep blood | {"unit": "PERCENT_V_V", "value": "0.15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/439 | unknown / not asserted | unknown / not asserted | Duplicate ingredient labels require row-specific identity review. | unchanged |
| `parent_media` | casman_medium | {"id": "CultureMech:001547", "name": "casman_medium", "notes": "KOMODO record states DSMZ Medium 439 provenance and mirrors the same Casman-Agar-Base plus sheep-blood formulation.", "path": "data/normalized_yaml/bacterial/casman_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Casman-Agar-Base | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/439 | {<br>                        "recipe_order": 1,<br>                        "compound": "Casman-Agar-Base",<br>                        "compound_id": 2099,<br>                        "attribute": "Difco",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Sheep blood | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/439 | {<br>                        "recipe_order": 2,<br>                        "compound": "Sheep blood",<br>                        "compound_id": 2047,<br>                        "amount": 5,<br>                        "unit": "%",<br>                        "g_l": 50,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Sheep blood | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/439 | {<br>                        "recipe_order": 3,<br>                        "compound": "Sheep blood",<br>                        "compound_id": 2047,<br>                        "attribute": "water-lysed",<br>                        "amount": 0.15,<br>                        "unit": "%",<br>                        "g_l": 1.5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/439 | {<br>                        "step": "Casman-Agar-Base (Difco) supplemented with 5% sheep blood and 0.15% water-lysed sheep blood."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `439`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium439.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=439' >439</a></TD>
					<TD>CASMAN-MEDIUM</TD>
					<TD>null</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium439.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium439.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
