# Medium Concentration Review: ACIDIC YEAST-STARCH AGAR (pH 5.0)

- Record: data/normalized_yaml/fungal/acidic_yeast_starch_agar_ph_5_0.yaml
- ID: CultureMech:010549
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `cbf4f0f29d6723002f1dd20a1ec37c6dfec5bb6437d0fc3b8305700d9793436b`
- Proposed/result SHA256: `cbf4f0f29d6723002f1dd20a1ec37c6dfec5bb6437d0fc3b8305700d9793436b`
- Source: https://mediadive.dsmz.de/rest/medium/J800
- Source SHA256: 4788a0d4a835677f38180f8ee8e0241ca37bbadcfa94ff8c690ffc69eebecb74
- Retrieved: 2026-10-07T14:39:43.800384+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "2"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J800 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Starch | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J800 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J800 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J800 | {<br>                        "step": "Prepare Yeast-starch agar (A) (see Medium No. 42) and adjust pH to 5.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
