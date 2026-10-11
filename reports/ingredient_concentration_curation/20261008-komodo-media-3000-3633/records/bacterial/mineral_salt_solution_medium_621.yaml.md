# KOMODO Concentration Review: Mineral salt solution (medium 621)

- Record: data/normalized_yaml/bacterial/mineral_salt_solution_medium_621.yaml
- ID: CultureMech:004808
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `71600310f801e2bde787cff2bc2d01918cbc5efd38d2fd9d146602247589f629`
- Proposed/result SHA256: `71600310f801e2bde787cff2bc2d01918cbc5efd38d2fd9d146602247589f629`
- Source: https://mediadive.dsmz.de/rest/medium/3029
- Source SHA256: b5c9493e66496fb2c5d5e64c4bcf9675dd01382531706e8697e6092dc99dd8f1
- Retrieved: 2026-10-08T07:59:20.048385+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | KOH | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/3029 | unknown / not asserted | unknown / not asserted | Mapped DSMZ amount source returned HTTP 404. No ingredient evidence was available from this endpoint; the mapping alone cannot support a quantity. Original recipe retrieval remains an explicit follow-up. | unchanged |

## Source Mapping

KOMODO accession `3029`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3029.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=3029' >3029</a></TD>
					<TD>Mineral salt solution (medium 621)</TD>
					<TD> 7.2, KOH, H2SO4</TD>
					<TD>false</TD>
					<TD>false</TD>
					<TD>true</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3029.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3029.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
