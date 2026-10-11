# KOMODO Concentration Review: SPIROCHAETA ISOVALERICA medium

- Record: data/normalized_yaml/bacterial/spirochaeta_isovalerica_medium.yaml
- ID: CultureMech:004701
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9ba9b7e0cc62670da4016da35ee7f51db2bb3d9c271196c3a5b34796d85b6411`
- Proposed/result SHA256: `9ba9b7e0cc62670da4016da35ee7f51db2bb3d9c271196c3a5b34796d85b6411`
- Source: https://mediadive.dsmz.de/rest/medium/273
- Source SHA256: b5c9493e66496fb2c5d5e64c4bcf9675dd01382531706e8697e6092dc99dd8f1
- Retrieved: 2026-10-07T22:41:42.788029+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Glucose | {"unit": "G_PER_L", "value": "2"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/273 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[1].concentration` | Trypticase (BBL) | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/273 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[2].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/273 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[3].concentration` | Tris-HCl-buffer (0.2 M; pH 7.5) | {"unit": "ML_PER_L", "value": "250"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/273 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[4].concentration` | Sea water | {"unit": "ML_PER_L", "value": "750"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/273 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[5].concentration` | Cysteine-HCl x H2O | {"unit": "G_PER_L", "value": "0.05"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/273 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[6].concentration` | Resazurin | {"unit": "G_PER_L", "value": "0.001"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/273 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |

## Source Mapping

KOMODO accession `273`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium273.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=273' >273</a></TD>
					<TD>SPIROCHAETA ISOVALERICA medium</TD>
					<TD> 7.5</TD>
					<TD>true</TD>
					<TD>true</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium273.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium273.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
