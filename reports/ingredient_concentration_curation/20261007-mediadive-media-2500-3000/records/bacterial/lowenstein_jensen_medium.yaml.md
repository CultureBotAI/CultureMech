# Medium Concentration Review: LOWENSTEIN-JENSEN MEDIUM

- Record: data/normalized_yaml/bacterial/lowenstein_jensen_medium.yaml
- ID: CultureMech:003059
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6acdffe7363c7ed6e59546b2ff3a0ba031806c03e3e7c87ac0ba70f008131417`
- Proposed/result SHA256: `6acdffe7363c7ed6e59546b2ff3a0ba031806c03e3e7c87ac0ba70f008131417`
- Source: https://mediadive.dsmz.de/rest/medium/J712
- Source SHA256: c5e03f6555c0c21f7436f57e0677be85bbff826751fc5a28e85881ea168b462d
- Retrieved: 2026-10-07T14:38:31.670574+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | L-asparagine | {"unit": "G_PER_L", "value": "3.6"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J712 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Monopotassium phosphate | {"unit": "G_PER_L", "value": "2.4"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J712 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Magnesium sulfate | {"unit": "G_PER_L", "value": "0.24"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J712 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Magnesium citrate | {"unit": "G_PER_L", "value": "0.6"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J712 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | Potato flour | {"unit": "G_PER_L", "value": "30.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J712 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | Glycerol | {"unit": "ML_PER_L", "value": "12.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J712 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | Malachite green | {"unit": "G_PER_L", "value": "0.025"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J712 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | Whole eggs | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J712 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `variant_children[0]` | lowenstein_jensen_medium | {"id": "CultureMech:010144", "name": "lowenstein_jensen_medium", "notes": "Source-equivalent TOGO M735 duplicate of JCM Medium 712, which uses commercial BD 220908 Lowenstein-Jensen medium slants.", "path": "data/normalized_yaml/bacterial/TOGO_M735_Lowenstein-Jensen_Medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J712 | {<br>                        "step": "Use commercially available Lowenstein-Jensen medium slants (BD 220908)."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
