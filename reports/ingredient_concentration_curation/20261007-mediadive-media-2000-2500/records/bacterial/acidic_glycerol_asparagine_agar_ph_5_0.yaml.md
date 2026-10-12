# Medium Concentration Review: ACIDIC GLYCEROL-ASPARAGINE AGAR (pH 5.0)

- Record: data/normalized_yaml/bacterial/acidic_glycerol_asparagine_agar_ph_5_0.yaml
- ID: CultureMech:002775
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `8c1d32fe4afc8819ea93d7fdfd10ff3473d685f2b1f453f2485c0ecd2e90a234`
- Proposed/result SHA256: `8c1d32fe4afc8819ea93d7fdfd10ff3473d685f2b1f453f2485c0ecd2e90a234`
- Source: https://mediadive.dsmz.de/rest/medium/J422
- Source SHA256: dc320fd448613738db47081497fbd68e77450a7c2960ca3ed62cf39948ab7cb7
- Retrieved: 2026-10-07T14:06:24.224946+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | L-Asparagine | {"unit": "G_PER_L", "value": "0.999001"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J422 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[1].concentration` | Glycerol | {"unit": "G_PER_L", "value": "9.99001"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J422 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[2].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "0.999001"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J422 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[3].concentration` | Agar | {"unit": "G_PER_L", "value": "14.985"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J422 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].concentration` | Trace salt solution | {"unit": "ML_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J422 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].composition[0].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J422 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].composition[1].concentration` | MnCl2 x 4 H2O | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J422 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].composition[2].concentration` | ZnSO4 x 7 H2O | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J422 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J422 | {<br>                        "step": "Prepare Glycerol-asparagine agar (ISP-5) (see Medium No. 60) and adjust pH to 5.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
