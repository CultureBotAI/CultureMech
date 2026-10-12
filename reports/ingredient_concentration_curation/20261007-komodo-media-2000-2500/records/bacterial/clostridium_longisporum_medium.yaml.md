# KOMODO Concentration Review: CLOSTRIDIUM LONGISPORUM medium

- Record: data/normalized_yaml/bacterial/clostridium_longisporum_medium.yaml
- ID: CultureMech:006392
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `28a175cdf19b345d6797f76d0b7870f7029802f1e9303eb1d84913e31112ad88`
- Proposed/result SHA256: `28a175cdf19b345d6797f76d0b7870f7029802f1e9303eb1d84913e31112ad88`
- Source: https://mediadive.dsmz.de/rest/medium/741
- Source SHA256: b5c9493e66496fb2c5d5e64c4bcf9675dd01382531706e8697e6092dc99dd8f1
- Retrieved: 2026-10-08T02:54:44.459278+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Agar | {"unit": "G_PER_L", "value": "15.000000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/741 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "3.000000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/741 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[2].concentration` | Glucose | {"unit": "G_PER_L", "value": "5.000000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/741 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[3].concentration` | CO2 | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/741 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[4].concentration` | Sodium acetate | {"unit": "G_PER_L", "value": "3.000000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/741 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[5].concentration` | Cysteine hydrochloride | {"unit": "G_PER_L", "value": "0.500000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/741 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[6].concentration` | Lab-Lemco powder | {"unit": "G_PER_L", "value": "10.000000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/741 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[7].concentration` | Sodium chloride | {"unit": "G_PER_L", "value": "5.000000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/741 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[8].concentration` | Soluble starch | {"unit": "G_PER_L", "value": "1.000000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/741 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |
| `ingredients[9].concentration` | Peptone | {"unit": "G_PER_L", "value": "10.000000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/741 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |

## Source Mapping

KOMODO accession `741`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium741.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=741' >741</a></TD>
					<TD>CLOSTRIDIUM LONGISPORUM medium</TD>
					<TD> 6.8</TD>
					<TD>true</TD>
					<TD>true</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium741.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium741.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
