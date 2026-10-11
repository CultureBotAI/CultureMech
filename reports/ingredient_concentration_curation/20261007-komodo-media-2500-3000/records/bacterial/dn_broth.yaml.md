# KOMODO Concentration Review: DN BROTH

- Record: data/normalized_yaml/bacterial/dn_broth.yaml
- ID: CultureMech:003523
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b03ebac31d54d84e5146e3bb9eaec271ae742c631812c77eef3c8d8e6b1eb5a7`
- Proposed/result SHA256: `b03ebac31d54d84e5146e3bb9eaec271ae742c631812c77eef3c8d8e6b1eb5a7`
- Source: https://mediadive.dsmz.de/rest/medium/1012
- Source SHA256: 9a169a067333d9a17d6c382538cc0d7d48add501efabe5dc4527c97b54f2a4ea
- Retrieved: 2026-10-07T13:15:57.737104+00:00
- Source type: official DSMZ dataset; discovery: verified KOMODO cross-reference; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | HEPES buffer | {"unit": "G_PER_L", "value": "6"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1012 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Casamino acids, HEPES buffer, NaOH, Nutrient broth, Yeast extract | unchanged |
| `ingredients[1].concentration` | MgCl2 x 6 H2O | {"unit": "G_PER_L", "value": "0.6"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1012 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Casamino acids, HEPES buffer, NaOH, Nutrient broth, Yeast extract | unchanged |
| `ingredients[2].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "0.3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1012 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Casamino acids, HEPES buffer, NaOH, Nutrient broth, Yeast extract | unchanged |
| `ingredients[3].concentration` | NaOH | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1012 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Casamino acids, HEPES buffer, NaOH, Nutrient broth, Yeast extract | unchanged |
| `source.data.solutions[0].recipe[0]` | Nutrient broth | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1012 | {<br>                        "recipe_order": 1,<br>                        "compound": "Nutrient broth",<br>                        "compound_id": 269,<br>                        "attribute": "BD Difco",<br>                        "amount": 0.8,<br>                        "unit": "g",<br>                        "g_l": 0.8,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Casamino acids | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1012 | {<br>                        "recipe_order": 2,<br>                        "compound": "Casamino acids",<br>                        "compound_id": 101,<br>                        "attribute": "BD Bacto",<br>                        "amount": 0.5,<br>                        "unit": "g",<br>                        "g_l": 0.5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1012 | {<br>                        "recipe_order": 3,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "attribute": "OXOID",<br>                        "amount": 0.1,<br>                        "unit": "g",<br>                        "g_l": 0.1,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | CaCl2 x 2 H2O | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1012 | {<br>                        "recipe_order": 4,<br>                        "compound": "CaCl2 x 2 H2O",<br>                        "compound_id": 7,<br>                        "amount": 0.3,<br>                        "unit": "g",<br>                        "g_l": 0.3,<br>                        "mmol_l": 2.04061,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[4]` | MgCl2 x 6 H2O | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1012 | {<br>                        "recipe_order": 5,<br>                        "compound": "MgCl2 x 6 H2O",<br>                        "compound_id": 79,<br>                        "amount": 0.6,<br>                        "unit": "g",<br>                        "g_l": 0.6,<br>                        "mmol_l": 2.95126,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[4] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[5]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1012 | {<br>                        "recipe_order": 6,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[5] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1012 | {<br>                        "step": "Dissolve ingredients except calcium and magnesium chloride and adjust pH of the medium to 7.2 with NaOH. After autoclaving add calcium and magnesium from sterile stock solutions."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
| `source.data.solutions[0].steps[1]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1012 | {<br>                        "step": "Before inoculation prepare a suspension of prey cells in 30-40 ml medium using a 250 ml flask. Usually the resuspension of two overnight cultures of the prey strain on agar slants of DSMZ medium 54 will yield a final concentration of 10<sup>8</sup> to 10<sup>9</sup> cells per ml culture broth."<br>                    } | $.data.solutions[0].steps[1] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Source Mapping

KOMODO accession `1012`; original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1012.pdf.

Mapping source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; SHA256 `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a`; retrieved 2026-10-07T13:01:23.350274+00:00. Exact captured row:

```html
<TR>
					<TD width="50"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1012' >1012</a></TD>
					<TD>DN BROTH</TD>
					<TD> 7.2, NaOH</TD>
					<TD>true</TD>
					<TD>false</TD>
					<TD>false</TD>
<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1012.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1012.pdf</a></TD>
				</TR>
```

This is identity evidence only. A variant's link to a base recipe does not support the variant's quantities. The complete claim table above includes unchanged and unresolved results; a report is not scientific completion.
