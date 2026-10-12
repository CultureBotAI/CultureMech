# Medium Concentration Review: ACIDIC OATMEAL AGAR (pH 5.0)

- Record: data/normalized_yaml/bacterial/acidic_oatmeal_agar_ph_5_0.yaml
- ID: CultureMech:002754
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `4f39ebcb4f2ddf7c57e2a89fed15bcb0e5d6cb508d277691c77b16787bdc992c`
- Proposed/result SHA256: `4f39ebcb4f2ddf7c57e2a89fed15bcb0e5d6cb508d277691c77b16787bdc992c`
- Source: https://mediadive.dsmz.de/rest/medium/J398
- Source SHA256: 017c5f158dd77b25b0c98ee3ded906bbe4b2edc5cf7d7a80f09a84e8671999d9
- Retrieved: 2026-10-07T14:06:02.004542+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Oatmeal | {"unit": "G_PER_L", "value": "19.98"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J398 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[1].concentration` | Agar | {"unit": "G_PER_L", "value": "17.982"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J398 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].concentration` | Trace salt solution | {"unit": "ML_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J398 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].composition[0].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J398 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].composition[1].concentration` | MnCl2 x 4 H2O | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J398 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].composition[2].concentration` | ZnSO4 x 7 H2O | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J398 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J398 | {<br>                        "step": "Prepare Oatmeal agar (ISP-3) (see Medium No. 50) and adjust pH to 5.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
