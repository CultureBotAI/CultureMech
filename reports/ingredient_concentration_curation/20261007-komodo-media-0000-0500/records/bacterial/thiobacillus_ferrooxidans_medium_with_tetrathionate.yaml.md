# KOMODO Concentration Review: THIOBACILLUS FERROOXIDANS MEDIUM WITH TETRATHIONATE

- Record: data/normalized_yaml/bacterial/thiobacillus_ferrooxidans_medium_with_tetrathionate.yaml
- ID: CultureMech:006372
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d94b441e346041c15a46e583d58c6ac35b533f87377cf3fd5b719e77a6606cea`
- Proposed/result SHA256: `d94b441e346041c15a46e583d58c6ac35b533f87377cf3fd5b719e77a6606cea`
- Source: https://mediadive.dsmz.de/rest/medium/72
- Source SHA256: b5c9493e66496fb2c5d5e64c4bcf9675dd01382531706e8697e6092dc99dd8f1
- Retrieved: 2026-10-07T20:27:18.870180+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "3.000000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/72 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[1].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "0.500000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/72 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[2].concentration` | (NH4)2SO4 | {"unit": "G_PER_L", "value": "3.000000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/72 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[3].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "0.250000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/72 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[4].concentration` | K2S4O6 | {"unit": "G_PER_L", "value": "5.000000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/72 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[5].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000.000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/72 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |

## Source Mapping

KOMODO accession `72`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium72.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=72' >72</a></TD>
					<TD>THIOBACILLUS FERROOXIDANS MEDIUM WITH TETRATHIONATE</TD>
					<TD>null</TD>
					<TD>false</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium72.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium72.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
