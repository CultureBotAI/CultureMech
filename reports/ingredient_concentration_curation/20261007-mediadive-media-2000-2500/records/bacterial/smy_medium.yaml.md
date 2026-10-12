# Medium Concentration Review: SMY MEDIUM

- Record: data/normalized_yaml/bacterial/smy_medium.yaml
- ID: CultureMech:003297
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e71a273572fde2bf2a55007d289c6aa0ada1f3ebafdc7358c411a9a547ea7661`
- Proposed/result SHA256: `e71a273572fde2bf2a55007d289c6aa0ada1f3ebafdc7358c411a9a547ea7661`
- Source: https://mediadive.dsmz.de/rest/medium/J94
- Source SHA256: 6735e487d0a83d4f4c92ebcb995fb1b4174e3990a000539711d8779095638de6
- Retrieved: 2026-10-07T14:01:56.762796+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "900"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J94 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[1].concentration` | MgSO4・7H2O | {"unit": "G_PER_L", "value": "0.1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J94 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[2].concentration` | yeast extract | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J94 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[3].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "1.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J94 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[4].concentration` | NH4Cl | {"unit": "G_PER_L", "value": "0.3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J94 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[5].concentration` | Na2HPO4 | {"unit": "G_PER_L", "value": "4.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J94 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].concentration` | 10% Na2S2O3 solution | {"unit": "ML_PER_L", "value": "50"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J94 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[1].concentration` | Trace metal solution (see Medium [M80]) | {"unit": "ML_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J94 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J94 | {<br>                        "step": "Use SM medium (see Medium No. 89) with 50.0 ml/L (final) of 10% Na2S2O3 solution and 1.0 g/L yeast extract."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
