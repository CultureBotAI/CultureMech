# Medium Concentration Review: HEMIN MEDIUM FOR MYCOBACTERIUM

- Record: data/normalized_yaml/bacterial/JCM_J714_HEMIN_MEDIUM_FOR_MYCOBACTERIUM.yaml
- ID: CultureMech:003061
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c5e9f35cc71349e809a675d003ac1427d568b4e220232349515f9bb4e06f1e2d`
- Proposed/result SHA256: `c5e9f35cc71349e809a675d003ac1427d568b4e220232349515f9bb4e06f1e2d`
- Source: https://mediadive.dsmz.de/rest/medium/J714
- Source SHA256: b91e7ca8123462cc2ca5899c0af1a4f363953760f567a8243c5ab90d532d11cf
- Retrieved: 2026-10-07T14:38:33.426480+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Middlebrook 7H10 agar (BD-Difco) | {"unit": "G_PER_L", "value": "19"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J714 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Glycerol | {"unit": "ML_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J714 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "895"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J714 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Middlebrook OADC Enrichment (BD-BBL) | {"unit": "ML_PER_L", "value": "100"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J714 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | Hemin | {"unit": "MICROMOLAR", "value": "60"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J714 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `parent_media` | middlebrook_7h10_agar_with_oadc_enrichment | {"id": "CultureMech:002743", "name": "middlebrook_7h10_agar_with_oadc_enrichment", "notes": "Parent JCM Medium 386 for the hemin-supplemented JCM Medium 714 recipe.", "path": "data/normalized_yaml/bacterial/middlebrook_7h10_agar_with_oadc_enrichment.yaml", "relationship": "SUPPLEMENTED_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J714 | {<br>                        "step": "Middlebrook 7H10 agar with OADC enrichment (see Medium No. 386) with 60 \u00ef\u00bf\u00bdmol/L of hemin. Hemin is solubilized with 1 N NaOH."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
