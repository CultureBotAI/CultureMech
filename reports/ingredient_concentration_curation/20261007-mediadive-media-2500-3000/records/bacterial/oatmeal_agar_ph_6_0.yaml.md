# Medium Concentration Review: OATMEAL AGAR (pH 6.0)

- Record: data/normalized_yaml/bacterial/oatmeal_agar_ph_6_0.yaml
- ID: CultureMech:003034
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7549725937010ba488e581cab1812f1ab71f2ddb83b3f776ba14cc924fa8670b`
- Proposed/result SHA256: `7549725937010ba488e581cab1812f1ab71f2ddb83b3f776ba14cc924fa8670b`
- Source: https://mediadive.dsmz.de/rest/medium/J689
- Source SHA256: cc156a5102a040c68a46ec5d4df6e205ec642fe6179d258c0072cc111b66b6fc
- Retrieved: 2026-10-07T14:38:13.323046+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Oatmeal | {"unit": "G_PER_L", "value": "19.98"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J689 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `ingredients[1].concentration` | Agar | {"unit": "G_PER_L", "value": "17.982"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J689 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].concentration` | Trace salt solution | {"unit": "ML_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J689 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].composition[0].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J689 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].composition[1].concentration` | MnCl2 x 4 H2O | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J689 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].composition[2].concentration` | ZnSO4 x 7 H2O | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J689 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J689 | {<br>                        "step": "Prepare Oatmeal agar (ISP-3) (see Medium No. 50) and adjust pH to 6.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
