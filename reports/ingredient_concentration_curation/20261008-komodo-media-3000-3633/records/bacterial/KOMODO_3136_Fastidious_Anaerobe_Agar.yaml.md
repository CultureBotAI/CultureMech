# KOMODO Concentration Review: Fastidious Anaerobe Agar

- Record: data/normalized_yaml/bacterial/KOMODO_3136_Fastidious_Anaerobe_Agar.yaml
- ID: CultureMech:004984
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c5eab3dc4fcaeae5ac4668b48d4b73390b2a4197dfa50574e518d520a5ab13ea`
- Proposed/result SHA256: `c5eab3dc4fcaeae5ac4668b48d4b73390b2a4197dfa50574e518d520a5ab13ea`
- Source: https://mediadive.dsmz.de/rest/medium/3136
- Source SHA256: b5c9493e66496fb2c5d5e64c4bcf9675dd01382531706e8697e6092dc99dd8f1
- Retrieved: 2026-10-08T08:00:46.803045+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Fastidious Anaerobe Agar (Acumedia) | {"unit": "G_PER_L", "value": "45.7"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/3136 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[1].concentration` | Deionized water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/3136 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[2].concentration` | Sterile defibrinated horse blood | {"unit": "PERCENT_V_V", "value": "5-10"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/3136 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `parent_media` | fastidious_anaerobe_agar | {"id": "CultureMech:000653", "name": "fastidious_anaerobe_agar", "notes": "Parent DSMZ Medium 1203 formula for this KOMODO source duplicate.", "path": "data/normalized_yaml/bacterial/fastidious_anaerobe_agar.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/3136 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |

## Source Mapping

KOMODO accession `3136`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3136.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=3136' >3136</a></TD>
					<TD>Fastidious Anaerobe Agar</TD>
					<TD> 7.0 - 7.4</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>true</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3136.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3136.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
