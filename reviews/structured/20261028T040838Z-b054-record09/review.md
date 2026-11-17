# Fresh scientific review: Basal Salt Medium with biphenyl

- Review: 20261028T040838Z-b054-record09
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T04:00:34.588188Z
- Finished UTC: 2026-10-28T04:08:38.836059Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

NBRC1333 identity is sound, but six stocks/doses and seven water additions are flattened; liquid biphenyl concentration conflicts with the selected agar-vapour variant, stock pH/preparation is absent, and generated grounding is stale. Four fresh canonical checks pass.

## Scope And Provenance

Complete generated target and exact maintained owner; scoped dependencies expressly identified; current primary and ontology evidence separately captured.

Selection: Actual batch054 selection index09; fresh review after lost historical bundles, not reconstruction.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008625 | data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml | generated | basal_salt_medium_with_biphenyl |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:008625 | Actual exit 0; original full streams and times retained. |
| Canonical strict | passed | True | CultureMech:008625 | Actual exit 0; original full streams and times retained. |
| Canonical terms | passed | True | CultureMech:008625 | Actual exit 0; original full streams and times retained. |
| Canonical references | passed | True | CultureMech:008625 | Actual exit 0; original full streams and times retained. |

## Scientific And Domain Assessments

### NBRC1333/TOGO 2036 exact identity and variants

identity: supported. Targets: CultureMech:008625.

One maintained owner matches the source identity. The NBRC110670 catalog associates this medium with environmental Metapseudomonas furukawaii, but that separate catalog observation is not automatically added as universal growth evidence.

### Every local quantity and scoped source condition

quantity: concern. Targets: CultureMech:008625.

38 exact local concentration fields covered by 34 stage-specific decisions; unchanged source-matched masses are retained with their denominator limits.

{"schema":"fresh-b054-scoped-quantity-inventory-v1","target":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","quantity_field_count":38,"decisions":[{"quantity_id":"q1","label":"Distilled water","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1338.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1338.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The1338 G_PER_L sum combines 936 mL main water, two 1 L stock waters numerically treated as1, and four 100 mL stock waters. Restore all seven stage-local volumes; no density or universal denominator follows.","source_stage":"main water","source_amount":936,"source_unit":"mL","denominator":"main water input","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 26-28","quote":"Distilled water\n936\nml"}]},{"quantity_id":"q2","label":"biphenyl","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"Primary explicitly supports 1 g/L biphenyl for liquid medium, while agar plating receives vapour from crystals. Both local layers classify the record SOLID_AGAR yet carry a fixed 1 G_PER_L dose. Split or condition the variants; do not transfer the liquid dose to the plate.","source_stage":"liquid substrate / agar-vapour alternative","source_amount":1,"source_unit":"g/L","denominator":"explicit liquid-medium concentration only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 155-155","quote":"Substrate (biphenyl) was added at a concentration of 1g/liter. For agar plating medium, biphenyl was provided as a vapor by placing crystals on the lid of a petri dish. The dish was sealed with polyethylene tape."}]},{"quantity_id":"q3","label":"Agar (if needed)","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[2].concentration","stored":{"value":"15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[2].concentration","stored":{"value":"15","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"15 g agar is explicitly optional per listed batch. Preserve its conditionality and do not assert a measured final-volume denominator from the sum of input liquids.","source_stage":"optional agar","source_amount":15,"source_unit":"g","denominator":"optional source batch","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 64-66","quote":"Agar (if needed)\n15\ng"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[3].concentration","stored":{"value":"68.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[3].concentration","stored":{"value":"68.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact source mass belongs to the named stock batch, not to main ingredients. Preserve supplied chemical form, amount and stock water separately; no normalization from water alone or generic dilution multiplier is asserted.","source_stage":"20x phosphate stock","source_amount":"68.05","source_unit":"g","denominator":"stock batch with separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 76-81","quote":"KH\n2\nPO\n4\n68.05\ng"}]},{"quantity_id":"q5","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[4].concentration","stored":{"value":"87.09","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[4].concentration","stored":{"value":"87.09","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact source mass belongs to the named stock batch, not to main ingredients. Preserve supplied chemical form, amount and stock water separately; no normalization from water alone or generic dilution multiplier is asserted.","source_stage":"20x phosphate stock","source_amount":"87.09","source_unit":"g","denominator":"stock batch with separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 70-75","quote":"K\n2\nHPO\n4\n87.09\ng"}]},{"quantity_id":"q6","label":"KOH","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[5].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[5].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"The source supplies no numeric alkali amount. Retain an unquantified adjustment reagent, but move it to the identified stock pH7.0 step rather than a main-medium variable ingredient.","source_stage":"20x phosphate pH adjuster","source_amount":null,"source_unit":null,"denominator":"stock pH adjustment only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 86-86","quote":"Adjust pH to 7.0 with KOH."}]},{"quantity_id":"q7","label":"(NH4)2SO4","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[6].concentration","stored":{"value":"198.66","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[6].concentration","stored":{"value":"198.66","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact source mass belongs to the named stock batch, not to main ingredients. Preserve supplied chemical form, amount and stock water separately; no normalization from water alone or generic dilution multiplier is asserted.","source_stage":"100x ammonium sulfate stock","source_amount":"198.66","source_unit":"g","denominator":"stock batch with separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 93-100","quote":"(NH\n4\n)\n2\nSO\n4\n198.66\ng"}]},{"quantity_id":"q8","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[7].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[7].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"The source supplies no numeric alkali amount. Retain an unquantified adjustment reagent, but move it to the identified stock pH7.0 step rather than a main-medium variable ingredient.","source_stage":"100x ammonium sulfate pH adjuster","source_amount":null,"source_unit":null,"denominator":"stock pH adjustment only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 105-105","quote":"Adjust pH to 7.0 with NaOH."}]},{"quantity_id":"q9","label":"FeSO4","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.056","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.056","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact source mass belongs to the named stock batch, not to main ingredients. Preserve supplied chemical form, amount and stock water separately; no normalization from water alone or generic dilution multiplier is asserted.","source_stage":"1000x iron stock","source_amount":"0.056","source_unit":"g","denominator":"stock batch with separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 108-111","quote":"FeSO\n4\n0.056\ng"}]},{"quantity_id":"q10","label":"MgCl2","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[9].concentration","stored":{"value":"16.26","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[9].concentration","stored":{"value":"16.26","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact source mass belongs to the named stock batch, not to main ingredients. Preserve supplied chemical form, amount and stock water separately; no normalization from water alone or generic dilution multiplier is asserted.","source_stage":"1000x magnesium stock","source_amount":"16.26","source_unit":"g","denominator":"stock batch with separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 117-120","quote":"MgCl\n2\n16.26\ng"}]},{"quantity_id":"q11","label":"MnCl2·4H2O","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact source mass belongs to the named stock batch, not to main ingredients. Preserve supplied chemical form, amount and stock water separately; no normalization from water alone or generic dilution multiplier is asserted.","source_stage":"1000x trace stock","source_amount":"0.1","source_unit":"g","denominator":"stock batch with separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 129-135","quote":"MnCl\n2\n·4H\n2\nO\n0.1\ng"}]},{"quantity_id":"q12","label":"CaCl2","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.65","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.65","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact source mass belongs to the named stock batch, not to main ingredients. Preserve supplied chemical form, amount and stock water separately; no normalization from water alone or generic dilution multiplier is asserted.","source_stage":"1000x trace stock","source_amount":"2.65","source_unit":"g","denominator":"stock batch with separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 125-128","quote":"CaCl\n2\n2.65\ng"}]},{"quantity_id":"q13","label":"Na2MoO4·4H2O","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact source mass belongs to the named stock batch, not to main ingredients. Preserve supplied chemical form, amount and stock water separately; no normalization from water alone or generic dilution multiplier is asserted.","source_stage":"1000x molybdate stock","source_amount":"0.1","source_unit":"g","denominator":"stock batch with separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 143-151","quote":"Na\n2\nMoO\n4\n·4H\n2\nO\n0.1\ng"}]},{"quantity_id":"q14","label":"20 x PO4*","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"solutions[0].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"solutions[0].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source specifies a stock addition in mL, not G_PER_L. Preserve named stock identity, explicit dose and six separate compositions; the 1000 mL sum of listed inputs is not a measured final-volume instruction.","source_stage":"main receiving stock dose","source_amount":"50","source_unit":"mL","denominator":"one listed main batch","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 29-33","quote":"20 x PO\n4\n*\n50\nml"}]},{"quantity_id":"q15","label":"100 x (NH4)2SO4**","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source specifies a stock addition in mL, not G_PER_L. Preserve named stock identity, explicit dose and six separate compositions; the 1000 mL sum of listed inputs is not a measured final-volume instruction.","source_stage":"main receiving stock dose","source_amount":"10","source_unit":"mL","denominator":"one listed main batch","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 34-42","quote":"100 x (NH\n4\n)\n2\nSO\n4\n**\n10\nml"}]},{"quantity_id":"q16","label":"1000 x FeSO4***","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source specifies a stock addition in mL, not G_PER_L. Preserve named stock identity, explicit dose and six separate compositions; the 1000 mL sum of listed inputs is not a measured final-volume instruction.","source_stage":"main receiving stock dose","source_amount":"1","source_unit":"mL","denominator":"one listed main batch","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 43-47","quote":"1000 x FeSO\n4\n***\n1\nml"}]},{"quantity_id":"q17","label":"1000 x MgCl2****","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"solutions[3].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"solutions[3].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source specifies a stock addition in mL, not G_PER_L. Preserve named stock identity, explicit dose and six separate compositions; the 1000 mL sum of listed inputs is not a measured final-volume instruction.","source_stage":"main receiving stock dose","source_amount":"1","source_unit":"mL","denominator":"one listed main batch","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 48-52","quote":"1000 x MgCl\n2\n****\n1\nml"}]},{"quantity_id":"q18","label":"1000 x Trace elements*****","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"solutions[4].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"solutions[4].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source specifies a stock addition in mL, not G_PER_L. Preserve named stock identity, explicit dose and six separate compositions; the 1000 mL sum of listed inputs is not a measured final-volume instruction.","source_stage":"main receiving stock dose","source_amount":"1","source_unit":"mL","denominator":"one listed main batch","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 53-56","quote":"1000 x Trace elements\n*****\n1\nml"}]},{"quantity_id":"q19","label":"1000 x Na2MoO4******","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"solutions[5].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"solutions[5].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source specifies a stock addition in mL, not G_PER_L. Preserve named stock identity, explicit dose and six separate compositions; the 1000 mL sum of listed inputs is not a measured final-volume instruction.","source_stage":"main receiving stock dose","source_amount":"1","source_unit":"mL","denominator":"one listed main batch","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 57-63","quote":"1000 x Na\n2\nMoO\n4\n******\n1\nml"}]},{"quantity_id":"q20","label":"Phosphate stock water","local_fields":[],"decision":"add","rationale":"Restore this water addition inside its own stock. It does not enter the main batch in full and is not an explicit final-volume makeup statement.","source_stage":"Phosphate stock water","source_amount":1,"source_unit":"L","denominator":"stock batch water","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 82-84","quote":"Distilled water\n1\nL"}]},{"quantity_id":"q21","label":"Ammonium stock water","local_fields":[],"decision":"add","rationale":"Restore this water addition inside its own stock. It does not enter the main batch in full and is not an explicit final-volume makeup statement.","source_stage":"Ammonium stock water","source_amount":1,"source_unit":"L","denominator":"stock batch water","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 101-103","quote":"Distilled water\n1\nL"}]},{"quantity_id":"q22","label":"Iron stock water","local_fields":[],"decision":"add","rationale":"Restore this water addition inside its own stock. It does not enter the main batch in full and is not an explicit final-volume makeup statement.","source_stage":"Iron stock water","source_amount":100,"source_unit":"mL","denominator":"stock batch water","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 112-114","quote":"Distilled water\n100\nml"}]},{"quantity_id":"q23","label":"Magnesium stock water","local_fields":[],"decision":"add","rationale":"Restore this water addition inside its own stock. It does not enter the main batch in full and is not an explicit final-volume makeup statement.","source_stage":"Magnesium stock water","source_amount":100,"source_unit":"mL","denominator":"stock batch water","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 121-123","quote":"Distilled water\n100\nml"}]},{"quantity_id":"q24","label":"Trace stock water","local_fields":[],"decision":"add","rationale":"Restore this water addition inside its own stock. It does not enter the main batch in full and is not an explicit final-volume makeup statement.","source_stage":"Trace stock water","source_amount":100,"source_unit":"mL","denominator":"stock batch water","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 136-138","quote":"Distilled water\n100\nml"}]},{"quantity_id":"q25","label":"Molybdate stock water","local_fields":[],"decision":"add","rationale":"Restore this water addition inside its own stock. It does not enter the main batch in full and is not an explicit final-volume makeup statement.","source_stage":"Molybdate stock water","source_amount":100,"source_unit":"mL","denominator":"stock batch water","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 152-154","quote":"Distilled water\n100\nml"}]},{"quantity_id":"q26","label":"Separate sterilization and cooling","local_fields":[],"decision":"add","rationale":"Retain separate sterilization, cooling to65 °C and ordered aseptic addition. The source does not supply sterilization temperature or duration; do not invent them.","source_stage":"preparation","source_amount":65,"source_unit":"degC","denominator":"cooling only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 67-67","quote":"Sterilize separately and cool to 65°C. Aseptically add to the following medium in order."}]},{"quantity_id":"q27","label":"Phosphate stock pH","local_fields":[],"decision":"add","rationale":"pH7.0 with unquantified KOH applies to the phosphate stock, not automatically the finished medium.","source_stage":"phosphate stock pH","source_amount":7,"source_unit":"pH","denominator":null,"sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 85-86","quote":"pH 7.0\nAdjust pH to 7.0 with KOH."}]},{"quantity_id":"q28","label":"Ammonium stock pH","local_fields":[],"decision":"add","rationale":"pH7.0 with unquantified NaOH applies to the ammonium stock, not automatically the finished medium.","source_stage":"ammonium stock pH","source_amount":7,"source_unit":"pH","denominator":null,"sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 104-105","quote":"pH 7.0\nAdjust pH to 7.0 with NaOH."}]},{"quantity_id":"q29","label":"Source stock factor 20 x PO4*","local_fields":[],"decision":"evidence_only","rationale":"Retain this source stock name/factor as identity context. It does not establish a final receiving concentration for every component or authorize multiplication without a verified volume basis.","source_stage":"stock identity","source_amount":20,"source_unit":"x","denominator":"source stock label only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 29-33","quote":"20 x PO\n4\n*\n50\nml"}]},{"quantity_id":"q30","label":"Source stock factor 100 x (NH4)2SO4**","local_fields":[],"decision":"evidence_only","rationale":"Retain this source stock name/factor as identity context. It does not establish a final receiving concentration for every component or authorize multiplication without a verified volume basis.","source_stage":"stock identity","source_amount":100,"source_unit":"x","denominator":"source stock label only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 34-42","quote":"100 x (NH\n4\n)\n2\nSO\n4\n**\n10\nml"}]},{"quantity_id":"q31","label":"Source stock factor 1000 x FeSO4***","local_fields":[],"decision":"evidence_only","rationale":"Retain this source stock name/factor as identity context. It does not establish a final receiving concentration for every component or authorize multiplication without a verified volume basis.","source_stage":"stock identity","source_amount":1000,"source_unit":"x","denominator":"source stock label only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 43-47","quote":"1000 x FeSO\n4\n***\n1\nml"}]},{"quantity_id":"q32","label":"Source stock factor 1000 x MgCl2****","local_fields":[],"decision":"evidence_only","rationale":"Retain this source stock name/factor as identity context. It does not establish a final receiving concentration for every component or authorize multiplication without a verified volume basis.","source_stage":"stock identity","source_amount":1000,"source_unit":"x","denominator":"source stock label only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 48-52","quote":"1000 x MgCl\n2\n****\n1\nml"}]},{"quantity_id":"q33","label":"Source stock factor 1000 x Trace elements*****","local_fields":[],"decision":"evidence_only","rationale":"Retain this source stock name/factor as identity context. It does not establish a final receiving concentration for every component or authorize multiplication without a verified volume basis.","source_stage":"stock identity","source_amount":1000,"source_unit":"x","denominator":"source stock label only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 53-56","quote":"1000 x Trace elements\n*****\n1\nml"}]},{"quantity_id":"q34","label":"Source stock factor 1000 x Na2MoO4******","local_fields":[],"decision":"evidence_only","rationale":"Retain this source stock name/factor as identity context. It does not establish a final receiving concentration for every component or authorize multiplication without a verified volume basis.","source_stage":"stock identity","source_amount":1000,"source_unit":"x","denominator":"source stock label only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt lines 57-63","quote":"1000 x Na\n2\nMoO\n4\n******\n1\nml"}]}],"limits":["A listed water amount is not an explicit measured final volume. Stock-local amounts are not receiving-medium rates.","Source-only rows/conditions are explicit; no density assumptions or invented missing gas balance."]}

### Chemical identity, canonical labels and packaged MIM

grounding: supported. Targets: CultureMech:008625.

All asserted CHEBI objects were retrieved directly and exact labels compared; supplied-form exceptions are described individually. Packaged MIM membership or label agreement alone is not chemical verification.

### Category, composition and physical-state scope

representation: concern. Targets: CultureMech:008625.

Bacterial scope is supported. SOLID_AGAR represents only an optional variant and must be made conditional alongside the liquid alternative. Agar makes the solid formulation composition distinct; a future liquid defined/synthetic classification requires explicit variant curation rather than blindly retaining imported COMPLEX/UNDEFINED defaults.

### Current repairs and historical review limits

provenance: supported. Targets: CultureMech:008625.

Complete current target/owner history and selected September report were read. Existing repair credit is retained; current writer bodies describe current behavior only. No lost 451–520 bundle is reconstructed or backdated.

## Findings

### f1: Six stocks are flattened and their receiving doses have mass units

major / open / confirmed; issue key: b054-09-f1.

The13 main ingredient rows include six distinct stock formulations, while all six solutions are Unknown solution stubs with empty composition and G_PER_L doses. Primary NBRC1333 specifies 50 mL, 10 mL and four 1 mL additions. Rebuild stage-local stocks/doses before regeneration; current importer already has stage-preserving paths and must not be described as historically unchanged.

### f2: Main and stock water additions were summed across units and containers

major / open / confirmed; issue key: b054-09-f2.

The1338 G_PER_L row joins unrelated main/stock volumes and treats each 1 L stock water numerically as1. Restore 936 mL main water, two 1 L stock waters and four 100 mL stock waters separately. The receiving liquid inputs sum 1000 mL, but no explicit final-volume statement is given.

### f3: Liquid biphenyl rate and agar-vapour formulation are conflated

major / open / confirmed; issue key: b054-09-f3.

NBRC gives 1 g/L for substrate in liquid medium and a vapour-delivery alternative for agar plating. The selected SOLID_AGAR representation has a fixed 1 G_PER_L biphenyl row and optional agar. Preserve explicit liquid versus plate variants and do not certify the plate dose from the liquid rate.

### f4: Stock pH and ordered preparation are omitted

major / open / confirmed; issue key: b054-09-f4.

KOH and NaOH are unquantified stock-local pH7.0 adjusters, not generic final-medium ingredients. Separate sterilization, cooling to65 °C and ordered aseptic addition are absent. Preserve these source limits; no sterilization time/temperature or final-medium pH is supplied.

### f5: The generated target omits the owner biphenyl repair

major / open / confirmed; issue key: b054-09-f5.

The maintained owner has the August 20 MIM grounding event and CHEBI:17097; the target retains the earlier ungrounded row. Credit the current writer and owner repair, then regenerate without claiming the present merger accepts incompatible formulations.

### f6: Source evidence and remaining grounding scope need explicit placement

minor / open / confirmed; issue key: b054-09-f6.

Primary and TOGO links are notes only. Attach stage-specific claim evidence. The exact source tetrahydrate name for sodium molybdate is retained without an asserted CHEBI; the packaged CSV has no exact supplied-label match. This is a scoped unresolved mapping, not evidence that the source should be changed to the common dihydrate. Agar and biphenyl missing secondary links are distinct from confirmed wrong IDs.

## Recommended Actions And Acceptance Checks

### a1

Correct the maintained source for: Six stocks are flattened and their receiving doses have mass units. The13 main ingredient rows include six distinct stock formulations, while all six solutions are Unknown solution stubs with empty composition and G_PER_L doses. Primary NBRC1333 specifies 50 mL, 10 mL and four 1 mL additions. Rebuild stage-local stocks/doses before regeneration; current importer already has stage-preserving paths and must not be described as historically unchanged.

- Preserve exact source version, claim scope, original history and new curation event; do not edit generated YAML directly.
- Re-run schema/strict/term/reference checks on corrected owner and regenerated target; compare every affected source row and preserve unsupported denominators as unresolved.

### a2

Correct the maintained source for: Main and stock water additions were summed across units and containers. The1338 G_PER_L row joins unrelated main/stock volumes and treats each 1 L stock water numerically as1. Restore 936 mL main water, two 1 L stock waters and four 100 mL stock waters separately. The receiving liquid inputs sum 1000 mL, but no explicit final-volume statement is given.

- Preserve exact source version, claim scope, original history and new curation event; do not edit generated YAML directly.
- Re-run schema/strict/term/reference checks on corrected owner and regenerated target; compare every affected source row and preserve unsupported denominators as unresolved.

### a3

Correct the maintained source for: Liquid biphenyl rate and agar-vapour formulation are conflated. NBRC gives 1 g/L for substrate in liquid medium and a vapour-delivery alternative for agar plating. The selected SOLID_AGAR representation has a fixed 1 G_PER_L biphenyl row and optional agar. Preserve explicit liquid versus plate variants and do not certify the plate dose from the liquid rate.

- Preserve exact source version, claim scope, original history and new curation event; do not edit generated YAML directly.
- Re-run schema/strict/term/reference checks on corrected owner and regenerated target; compare every affected source row and preserve unsupported denominators as unresolved.

### a4

Correct the maintained source for: Stock pH and ordered preparation are omitted. KOH and NaOH are unquantified stock-local pH7.0 adjusters, not generic final-medium ingredients. Separate sterilization, cooling to65 °C and ordered aseptic addition are absent. Preserve these source limits; no sterilization time/temperature or final-medium pH is supplied.

- Preserve exact source version, claim scope, original history and new curation event; do not edit generated YAML directly.
- Re-run schema/strict/term/reference checks on corrected owner and regenerated target; compare every affected source row and preserve unsupported denominators as unresolved.

### a5

Correct the maintained source for: The generated target omits the owner biphenyl repair. The maintained owner has the August 20 MIM grounding event and CHEBI:17097; the target retains the earlier ungrounded row. Credit the current writer and owner repair, then regenerate without claiming the present merger accepts incompatible formulations.

- Preserve exact source version, claim scope, original history and new curation event; do not edit generated YAML directly.
- Re-run schema/strict/term/reference checks on corrected owner and regenerated target; compare every affected source row and preserve unsupported denominators as unresolved.

### a6

Correct the maintained source for: Source evidence and remaining grounding scope need explicit placement. Primary and TOGO links are notes only. Attach stage-specific claim evidence. The exact source tetrahydrate name for sodium molybdate is retained without an asserted CHEBI; the packaged CSV has no exact supplied-label match. This is a scoped unresolved mapping, not evidence that the source should be changed to the common dihydrate. Agar and biphenyl missing secondary links are distinct from confirmed wrong IDs.

- Preserve exact source version, claim scope, original history and new curation event; do not edit generated YAML directly.
- Re-run schema/strict/term/reference checks on corrected owner and regenerated target; compare every affected source row and preserve unsupported denominators as unresolved.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; Exact raw and derivative text at sources/chebi15377.raw and .txt; metadata chebi15377.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi75832 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75832; Exact raw and derivative text at sources/chebi75832.raw and .txt; metadata chebi75832.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi17097 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17097; Exact raw and derivative text at sources/chebi17097.raw and .txt; metadata chebi17097.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527; Exact raw and derivative text at sources/chebi131527.raw and .txt; metadata chebi131527.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; Exact raw and derivative text at sources/chebi86368.raw and .txt; metadata chebi86368.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi32035 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32035; Exact raw and derivative text at sources/chebi32035.raw and .txt; metadata chebi32035.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; Exact raw and derivative text at sources/chebi63036.raw and .txt; metadata chebi63036.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi3312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:3312; Exact raw and derivative text at sources/chebi3312.raw and .txt; metadata chebi3312.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145; Exact raw and derivative text at sources/chebi32145.raw and .txt; metadata chebi32145.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:62946; Exact raw and derivative text at sources/chebi62946.raw and .txt; metadata chebi62946.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| togo2036 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2036; Exact raw and derivative text at sources/togo2036.raw and .txt; metadata togo2036.json | context_only | Exact linked TOGO provider transcription, not automatic override of primary |
| nbrc1333 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333; Exact raw and derivative text at sources/nbrc1333.raw and .txt; metadata nbrc1333.json | context_only | Full primary six-stock recipe; liquid substrate rate distinct from agar-vapour variant |
| nbrc110670 | https://www.nite.go.jp/nbrc/dbrp/dataview?dataId=STNB0000000110670; Exact raw and derivative text at sources/nbrc110670.raw and .txt; metadata nbrc110670.json | context_only | Environmental strain identity and catalog association only |
| chebi6636 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:6636; Exact raw and derivative text at sources/chebi6636.raw and .txt; metadata chebi6636.json | context_only | Exact ontology object identity/label/definition/formula; not formulation or preparation evidence |
| current | data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml; full target and owner; exact byte hashes in native source.inputs | context_only | Current target and exact maintained owner, including complete history and evidence. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; all9077rows; source commit/hash in adjacent metadata | context_only | Packaged MIM CSV only, exact row and key joins; MAPPED and REJECTED entries distinguished. No assertion about current remote release. |
| importer | src/culturemech/import/togo_importer.py; _ingredient_from_item; _extract_primary_components; _solution_from_item; _parse_unit; _convert_to_culturemech | context_only | Current TOGO importer preserves recognized primary sections and separate stocks, but bare g/ml values still map to per-litre enums and fallback/default paths exist. Current code is not proof of historical execution. |
| merger | src/culturemech/merge/formulation.py; formulation_content and merge_formulation_evidence; inspected merger.merge_group | context_only | Current formulation comparison requires exact scientific-field equality and merger rejects incompatible multi-source formulations; singleton publication still needs regeneration after owner changes. |
| prior | reports/yaml_record_review/20260921T184214Z-Basal_Salt_Medium_with_biphenyl.md; full report; exact target path in header | context_only | Fully read September narrative review of this exact target; derivative historical opinion only. Its command successes are not reused and its final-volume/merge inferences are independently reassessed. |
| mim-writer | scripts/apply_mim_groundings.py; target_slot, groundable, apply_to_record | context_only | Current MIM grounding writer fills only ungrounded slots from exact accepted mappings with no corpus conflict; it preserves existing source IDs and does not repair quantities or stock stages. |
| stock-migration | scripts/migrate_solutions_from_ingredients.py; _resolve_solution and _migrate_media_file | context_only | Current solution migrator matches names against a single-ID dictionary, copies existing concentration unchanged and can leave empty stubs. This is current code, not an authenticated replay of the old execution. |
| quantity-sidecar | REVIEW_WORK/batch054/record09/quantity-inventory.json; All decisions and exact local/source locators | supports | Complete scoped quantity decisions, including unchanged and unsupported claims. |
| grounding-sidecar | REVIEW_WORK/batch054/record09/grounding-inventory.json; slots, ontology_objects and exact CSV row pool | supports | Exact returned OLS objects and all asserted chemical slots, with literal label correspondence separate from supplied-form decisions. |
| check-schema | REVIEW_WORK/batch054/record09/schema-result.json; argv/start/finish/exit and SHA-bound original stdout/stderr | supports | Actual fresh schema canonical check; reference check reports zero snippets, and terms does not certify chemical supplied-form identity. |
| check-strict | REVIEW_WORK/batch054/record09/strict-result.json; argv/start/finish/exit and SHA-bound original stdout/stderr | supports | Actual fresh strict canonical check; reference check reports zero snippets, and terms does not certify chemical supplied-form identity. |
| check-terms | REVIEW_WORK/batch054/record09/terms-result.json; argv/start/finish/exit and SHA-bound original stdout/stderr | supports | Actual fresh terms canonical check; reference check reports zero snippets, and terms does not certify chemical supplied-form identity. |
| check-references | REVIEW_WORK/batch054/record09/references-result.json; argv/start/finish/exit and SHA-bound original stdout/stderr | supports | Actual fresh references canonical check; reference check reports zero snippets, and terms does not certify chemical supplied-form identity. |

## Limits And Additional Notes

- Source FeSO4/MgCl2/CaCl2 omit hydrate qualifiers; retain the literal formulas without choosing common hydrates from mass intuition. Na2MoO4·4H2O is explicitly tetrahydrate and remains ungrounded rather than substituted.
- The six stock factors are labels, not independently measured stock potency. Optional agar and vapour delivery are distinct from the explicit liquid biphenyl rate.
- The September report is derivative historical context; its old validations and source access times are not used as current verification.
- Packaged MIM CSV observations apply only to commit 6643131b0f12ab40b66f98135245fca04027e0e9; no global absence or live MIM claim.
- No experiment, growth optimization or universal strain applicability is inferred; catalog identity examples are not automatically inserted as target_organisms.
- Canonical reference validation inspected zero references in the generated target; scientific source authentication is supplied separately here.
- Source recipes list batch amounts unless an explicit concentration/final-volume statement is quoted. No silent normalization based solely on listed water.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T040838Z-b054-record09
kind: record
repository: CultureBotAI/CultureMech
title: 'Fresh scientific review: Basal Salt Medium with biphenyl'
started_at: '2026-10-28T04:00:34.588188Z'
finished_at: '2026-10-28T04:08:38.836059Z'
reviewer:
  identity: Codex tsb_source_check
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Fresh review of maintained records not authored or modified
    by this reviewer; old narrative reports treated only as derivative context.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: NBRC1333 identity is sound, but six stocks/doses and seven water additions
  are flattened; liquid biphenyl concentration conflicts with the selected agar-vapour
  variant, stock pH/preparation is absent, and generated grounding is stale. Four
  fresh canonical checks pass.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
  - path: .claude/skills/review-ingredient-concentrations/references/evidence-contract.md
    sha256: 5eb4783f02a0567b45b462dfb5e8c0393fb34daf842a3ce23ff7946652f157d1
    role: context
  - path: .claude/skills/review-recipes/reference/linkage-and-duplicates.md
    sha256: e792d47f2b9e169d2306ac920f87aa1ced9b9d07c7650dd7d2feb7aee48c2234
    role: context
  - path: .claude/skills/review-recipes/reference/validation-rules.md
    sha256: 3b8666d58fc0c9deb02981053a50760a937675e6e22a6ecd53e92678e8d422f0
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: e3f1aeccd3d249f78739c902ea8d95052fec26fc5db752b5ca732d96ab37e466
    role: context
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/oak_config.yaml
    sha256: c0ef0808662f57dc2f57ce9b405485830503653aceee1451c9e1dae42f9e7021
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml
    sha256: 1528229578fc0f9602a1b1b03ebdaaea1ebcee2efb2e63016832f5a8201a9a6a
    role: target
  - path: data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml
    sha256: 79f86af25a012fef950b7648588010e62144abc5d835812e906e230da1a133e8
    role: context
  - path: docs/DATA_LAYERS.md
    sha256: 381cbb9ad2ba80f2a849507c4ce8b10839546ae4ce2757dad065e86fe381d236
    role: context
  - path: docs/record-review-profile.md
    sha256: 99eebe27f0079cb816c974f58ee457148da5a3c346ec9c30ff853b95dade9127
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 552166976136ed158a253773f0b763e670d2484e7354b48ec0f9b77b4250da77
    role: context
  - path: project.justfile
    sha256: 8cb892e67e1d94bc93c77f3a03d8d4ced32d8d31aa8e5b0346853cbc05077d6f
    role: context
  - path: reports/yaml_record_review/20260921T184214Z-Basal_Salt_Medium_with_biphenyl.md
    sha256: c9c7c32a81373e4ca69cab0263767c08ddbe5e73ffde1dcb9ea87027f02e6fde
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
    role: context
  - path: src/culturemech/merge/formulation.py
    sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
    role: context
  - path: src/culturemech/merge/matcher.py
    sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
    role: context
scope:
  description: Complete generated target and exact maintained owner; scoped dependencies
    expressly identified; current primary and ontology evidence separately captured.
  selection: Actual batch054 selection index09; fresh review after lost historical
    bundles, not reconstruction.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008625
targets:
- target_id: CultureMech:008625
  path: data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml
  label: basal_salt_medium_with_biphenyl
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml
    role: maintained source
  ownership_note: Exact single maintained owner from current identity and merged_from;
    generated target must be regenerated after owner curation.
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; original full streams and times retained.
  target_ids:
  - CultureMech:008625
  command: just validate-schema data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-schema
- check_id: strict
  name: Canonical strict
  status: passed
  required: true
  summary: Actual exit 0; original full streams and times retained.
  target_ids:
  - CultureMech:008625
  command: just validate-strict data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml
    --out REVIEW_WORK/batch054/record09/strict.tsv --workers 1 --quiet
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-strict
- check_id: terms
  name: Canonical terms
  status: passed
  required: true
  summary: Actual exit 0; original full streams and times retained.
  target_ids:
  - CultureMech:008625
  command: just validate-terms data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-terms
- check_id: references
  name: Canonical references
  status: passed
  required: true
  summary: Actual exit 0; original full streams and times retained.
  target_ids:
  - CultureMech:008625
  command: just validate-references data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  locator: Exact raw and derivative text at sources/chebi15377.raw and .txt; metadata
    chebi15377.json
  accessed_at: '2026-10-28T04:01:32.692041Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: chebi75832
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75832
  locator: Exact raw and derivative text at sources/chebi75832.raw and .txt; metadata
    chebi75832.json
  accessed_at: '2026-10-28T04:01:34.613211Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: 1ff12c151d1c7e56432f87c6980d66ae2083959a316f88529c8a3149781760c5
- evidence_id: chebi17097
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17097
  locator: Exact raw and derivative text at sources/chebi17097.raw and .txt; metadata
    chebi17097.json
  accessed_at: '2026-10-28T04:01:33.080967Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: 921ffb7241d39409a0996f430bf08b9916893da6151228fd7f52d7a7ca744903
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527
  locator: Exact raw and derivative text at sources/chebi131527.raw and .txt; metadata
    chebi131527.json
  accessed_at: '2026-10-28T04:01:32.479727Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: 0a5297c84ea9dd82508960482211f6b3c993fd8e2b83fe755dd2b23316cc4068
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  locator: Exact raw and derivative text at sources/chebi86368.raw and .txt; metadata
    chebi86368.json
  accessed_at: '2026-10-28T04:01:34.948072Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi32035
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32035
  locator: Exact raw and derivative text at sources/chebi32035.raw and .txt; metadata
    chebi32035.json
  accessed_at: '2026-10-28T04:01:33.197838Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: d0537d7c65cf63693a87f126d0f0f13501f6519f98fe7ca64fb07d469079571c
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  locator: Exact raw and derivative text at sources/chebi63036.raw and .txt; metadata
    chebi63036.json
  accessed_at: '2026-10-28T04:01:34.281359Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi3312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:3312
  locator: Exact raw and derivative text at sources/chebi3312.raw and .txt; metadata
    chebi3312.json
  accessed_at: '2026-10-28T04:01:33.825711Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: c468d22946b95659970843fef50c7cce0f87796940350baacca568c52aa5744e
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145
  locator: Exact raw and derivative text at sources/chebi32145.raw and .txt; metadata
    chebi32145.json
  accessed_at: '2026-10-28T04:01:33.412675Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: 089212e8c86e2d4a4b145366c8bc67e0056565ef6970dcdc3df63ad20dac234d
- evidence_id: chebi62946
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:62946
  locator: Exact raw and derivative text at sources/chebi62946.raw and .txt; metadata
    chebi62946.json
  accessed_at: '2026-10-28T04:01:33.968671Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: e035a92736c0b968363e9db17da9a4a81390ab174a65e689f6ae45c326324b44
- evidence_id: togo2036
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2036
  locator: Exact raw and derivative text at sources/togo2036.raw and .txt; metadata
    togo2036.json
  accessed_at: '2026-10-28T04:01:23.382574Z'
  support: context_only
  summary: Exact linked TOGO provider transcription, not automatic override of primary
  snapshot_sha256: a370b482013d2610dc59c9481bb8eb6f3b1e803fc4054d9d8cf3f507575aeca4
- evidence_id: nbrc1333
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333
  locator: Exact raw and derivative text at sources/nbrc1333.raw and .txt; metadata
    nbrc1333.json
  accessed_at: '2026-10-28T04:01:25.514594Z'
  support: context_only
  summary: Full primary six-stock recipe; liquid substrate rate distinct from agar-vapour
    variant
  snapshot_sha256: 3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631
- evidence_id: nbrc110670
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/dbrp/dataview?dataId=STNB0000000110670
  locator: Exact raw and derivative text at sources/nbrc110670.raw and .txt; metadata
    nbrc110670.json
  accessed_at: '2026-10-28T04:01:25.566769Z'
  support: context_only
  summary: Environmental strain identity and catalog association only
  snapshot_sha256: cf86a05126a71753654d24a757321c367264de8bc3efbe3c82c1b6317eaa9656
- evidence_id: chebi6636
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:6636
  locator: Exact raw and derivative text at sources/chebi6636.raw and .txt; metadata
    chebi6636.json
  accessed_at: '2026-10-28T04:01:34.552535Z'
  support: context_only
  summary: Exact ontology object identity/label/definition/formula; not formulation
    or preparation evidence
  snapshot_sha256: e5d9f5965bff11398a3b4fd443bbf98be3a50042f65de5861033b0304c9d0bdf
- evidence_id: current
  kind: record_content
  reference: data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml
  locator: full target and owner; exact byte hashes in native source.inputs
  accessed_at: '2026-10-28T04:08:38.763704Z'
  support: context_only
  summary: Current target and exact maintained owner, including complete history and
    evidence.
  snapshot_sha256: 1528229578fc0f9602a1b1b03ebdaaea1ebcee2efb2e63016832f5a8201a9a6a
- evidence_id: mim
  kind: database
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: all9077rows; source commit/hash in adjacent metadata
  accessed_at: '2026-10-28T04:08:38.763880Z'
  support: context_only
  summary: Packaged MIM CSV only, exact row and key joins; MAPPED and REJECTED entries
    distinguished. No assertion about current remote release.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item; _extract_primary_components; _solution_from_item;
    _parse_unit; _convert_to_culturemech
  accessed_at: '2026-10-28T04:08:38.764257Z'
  support: context_only
  summary: Current TOGO importer preserves recognized primary sections and separate
    stocks, but bare g/ml values still map to per-litre enums and fallback/default
    paths exist. Current code is not proof of historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: merger
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content and merge_formulation_evidence; inspected merger.merge_group
  accessed_at: '2026-10-28T04:08:38.764304Z'
  support: context_only
  summary: Current formulation comparison requires exact scientific-field equality
    and merger rejects incompatible multi-source formulations; singleton publication
    still needs regeneration after owner changes.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: prior
  kind: prior_review
  reference: reports/yaml_record_review/20260921T184214Z-Basal_Salt_Medium_with_biphenyl.md
  locator: full report; exact target path in header
  accessed_at: '2026-10-28T04:08:38.764337Z'
  support: context_only
  summary: Fully read September narrative review of this exact target; derivative
    historical opinion only. Its command successes are not reused and its final-volume/merge
    inferences are independently reassessed.
  snapshot_sha256: c9c7c32a81373e4ca69cab0263767c08ddbe5e73ffde1dcb9ea87027f02e6fde
- evidence_id: mim-writer
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: target_slot, groundable, apply_to_record
  accessed_at: '2026-10-28T04:08:38.764669Z'
  support: context_only
  summary: Current MIM grounding writer fills only ungrounded slots from exact accepted
    mappings with no corpus conflict; it preserves existing source IDs and does not
    repair quantities or stock stages.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: stock-migration
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: _resolve_solution and _migrate_media_file
  accessed_at: '2026-10-28T04:08:38.764839Z'
  support: context_only
  summary: Current solution migrator matches names against a single-ID dictionary,
    copies existing concentration unchanged and can leave empty stubs. This is current
    code, not an authenticated replay of the old execution.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: quantity-sidecar
  kind: record_content
  reference: REVIEW_WORK/batch054/record09/quantity-inventory.json
  locator: All decisions and exact local/source locators
  accessed_at: '2026-10-28T04:08:38.835017Z'
  support: supports
  summary: Complete scoped quantity decisions, including unchanged and unsupported
    claims.
  snapshot_sha256: 4e16a59cf11a604a331c98636740515770f2cc4152571494d1c5e92eee726a2a
- evidence_id: grounding-sidecar
  kind: authority
  reference: REVIEW_WORK/batch054/record09/grounding-inventory.json
  locator: slots, ontology_objects and exact CSV row pool
  accessed_at: '2026-10-28T04:08:38.835079Z'
  support: supports
  summary: Exact returned OLS objects and all asserted chemical slots, with literal
    label correspondence separate from supplied-form decisions.
  snapshot_sha256: f92e44e9d9752a6a579ccd7954b3087ffcdfcdccec214e7df10058fafab6cb25
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch054/record09/schema-result.json
  locator: argv/start/finish/exit and SHA-bound original stdout/stderr
  accessed_at: '2026-10-28T04:00:35.884410Z'
  support: supports
  summary: Actual fresh schema canonical check; reference check reports zero snippets,
    and terms does not certify chemical supplied-form identity.
  snapshot_sha256: 2641d4106ef6ffe7cb3ccd170982255c5b658b5347d0e686561774937e6f2ccb
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch054/record09/strict-result.json
  locator: argv/start/finish/exit and SHA-bound original stdout/stderr
  accessed_at: '2026-10-28T04:00:37.021631Z'
  support: supports
  summary: Actual fresh strict canonical check; reference check reports zero snippets,
    and terms does not certify chemical supplied-form identity.
  snapshot_sha256: 4a37fd2ad664b7e25dbecb85d61536f2e58e2e7ff6e1f4ae45b1e84848dcfc73
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch054/record09/terms-result.json
  locator: argv/start/finish/exit and SHA-bound original stdout/stderr
  accessed_at: '2026-10-28T04:00:38.428614Z'
  support: supports
  summary: Actual fresh terms canonical check; reference check reports zero snippets,
    and terms does not certify chemical supplied-form identity.
  snapshot_sha256: 1aa702b59ae67282a655fb61a06a5833a8520b71affbf53225faacf6b2e83635
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch054/record09/references-result.json
  locator: argv/start/finish/exit and SHA-bound original stdout/stderr
  accessed_at: '2026-10-28T04:00:39.284870Z'
  support: supports
  summary: Actual fresh references canonical check; reference check reports zero snippets,
    and terms does not certify chemical supplied-form identity.
  snapshot_sha256: 8480d76a0a642bb6890fda60916c286fa2e8789a3edfaa5deccec3ba09035245
assessments:
- assessment_id: identity
  area: identity
  topic: NBRC1333/TOGO 2036 exact identity and variants
  outcome: supported
  summary: One maintained owner matches the source identity. The NBRC110670 catalog
    associates this medium with environmental Metapseudomonas furukawaii, but that
    separate catalog observation is not automatically added as universal growth evidence.
  target_ids:
  - CultureMech:008625
  evidence_ids:
  - nbrc1333
  - togo2036
  - nbrc110670
  - current
- assessment_id: quantities
  area: quantity
  topic: Every local quantity and scoped source condition
  outcome: concern
  summary: 38 exact local concentration fields covered by 34 stage-specific decisions;
    unchanged source-matched masses are retained with their denominator limits.
  target_ids:
  - CultureMech:008625
  evidence_ids:
  - quantity-sidecar
  details: '{"schema":"fresh-b054-scoped-quantity-inventory-v1","target":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","quantity_field_count":38,"decisions":[{"quantity_id":"q1","label":"Distilled
    water","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1338.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1338.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The1338
    G_PER_L sum combines 936 mL main water, two 1 L stock waters numerically treated
    as1, and four 100 mL stock waters. Restore all seven stage-local volumes; no density
    or universal denominator follows.","source_stage":"main water","source_amount":936,"source_unit":"mL","denominator":"main
    water input","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 26-28","quote":"Distilled water\n936\nml"}]},{"quantity_id":"q2","label":"biphenyl","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"Primary
    explicitly supports 1 g/L biphenyl for liquid medium, while agar plating receives
    vapour from crystals. Both local layers classify the record SOLID_AGAR yet carry
    a fixed 1 G_PER_L dose. Split or condition the variants; do not transfer the liquid
    dose to the plate.","source_stage":"liquid substrate / agar-vapour alternative","source_amount":1,"source_unit":"g/L","denominator":"explicit
    liquid-medium concentration only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 155-155","quote":"Substrate (biphenyl) was added at a concentration of 1g/liter.
    For agar plating medium, biphenyl was provided as a vapor by placing crystals
    on the lid of a petri dish. The dish was sealed with polyethylene tape."}]},{"quantity_id":"q3","label":"Agar
    (if needed)","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[2].concentration","stored":{"value":"15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[2].concentration","stored":{"value":"15","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"15
    g agar is explicitly optional per listed batch. Preserve its conditionality and
    do not assert a measured final-volume denominator from the sum of input liquids.","source_stage":"optional
    agar","source_amount":15,"source_unit":"g","denominator":"optional source batch","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 64-66","quote":"Agar (if needed)\n15\ng"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[3].concentration","stored":{"value":"68.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[3].concentration","stored":{"value":"68.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact
    source mass belongs to the named stock batch, not to main ingredients. Preserve
    supplied chemical form, amount and stock water separately; no normalization from
    water alone or generic dilution multiplier is asserted.","source_stage":"20x phosphate
    stock","source_amount":"68.05","source_unit":"g","denominator":"stock batch with
    separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 76-81","quote":"KH\n2\nPO\n4\n68.05\ng"}]},{"quantity_id":"q5","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[4].concentration","stored":{"value":"87.09","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[4].concentration","stored":{"value":"87.09","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact
    source mass belongs to the named stock batch, not to main ingredients. Preserve
    supplied chemical form, amount and stock water separately; no normalization from
    water alone or generic dilution multiplier is asserted.","source_stage":"20x phosphate
    stock","source_amount":"87.09","source_unit":"g","denominator":"stock batch with
    separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 70-75","quote":"K\n2\nHPO\n4\n87.09\ng"}]},{"quantity_id":"q6","label":"KOH","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[5].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[5].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"The
    source supplies no numeric alkali amount. Retain an unquantified adjustment reagent,
    but move it to the identified stock pH7.0 step rather than a main-medium variable
    ingredient.","source_stage":"20x phosphate pH adjuster","source_amount":null,"source_unit":null,"denominator":"stock
    pH adjustment only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 86-86","quote":"Adjust pH to 7.0 with KOH."}]},{"quantity_id":"q7","label":"(NH4)2SO4","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[6].concentration","stored":{"value":"198.66","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[6].concentration","stored":{"value":"198.66","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact
    source mass belongs to the named stock batch, not to main ingredients. Preserve
    supplied chemical form, amount and stock water separately; no normalization from
    water alone or generic dilution multiplier is asserted.","source_stage":"100x
    ammonium sulfate stock","source_amount":"198.66","source_unit":"g","denominator":"stock
    batch with separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 93-100","quote":"(NH\n4\n)\n2\nSO\n4\n198.66\ng"}]},{"quantity_id":"q8","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[7].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[7].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"The
    source supplies no numeric alkali amount. Retain an unquantified adjustment reagent,
    but move it to the identified stock pH7.0 step rather than a main-medium variable
    ingredient.","source_stage":"100x ammonium sulfate pH adjuster","source_amount":null,"source_unit":null,"denominator":"stock
    pH adjustment only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 105-105","quote":"Adjust pH to 7.0 with NaOH."}]},{"quantity_id":"q9","label":"FeSO4","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.056","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.056","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact
    source mass belongs to the named stock batch, not to main ingredients. Preserve
    supplied chemical form, amount and stock water separately; no normalization from
    water alone or generic dilution multiplier is asserted.","source_stage":"1000x
    iron stock","source_amount":"0.056","source_unit":"g","denominator":"stock batch
    with separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 108-111","quote":"FeSO\n4\n0.056\ng"}]},{"quantity_id":"q10","label":"MgCl2","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[9].concentration","stored":{"value":"16.26","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[9].concentration","stored":{"value":"16.26","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact
    source mass belongs to the named stock batch, not to main ingredients. Preserve
    supplied chemical form, amount and stock water separately; no normalization from
    water alone or generic dilution multiplier is asserted.","source_stage":"1000x
    magnesium stock","source_amount":"16.26","source_unit":"g","denominator":"stock
    batch with separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 117-120","quote":"MgCl\n2\n16.26\ng"}]},{"quantity_id":"q11","label":"MnCl2·4H2O","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact
    source mass belongs to the named stock batch, not to main ingredients. Preserve
    supplied chemical form, amount and stock water separately; no normalization from
    water alone or generic dilution multiplier is asserted.","source_stage":"1000x
    trace stock","source_amount":"0.1","source_unit":"g","denominator":"stock batch
    with separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 129-135","quote":"MnCl\n2\n·4H\n2\nO\n0.1\ng"}]},{"quantity_id":"q12","label":"CaCl2","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.65","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.65","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact
    source mass belongs to the named stock batch, not to main ingredients. Preserve
    supplied chemical form, amount and stock water separately; no normalization from
    water alone or generic dilution multiplier is asserted.","source_stage":"1000x
    trace stock","source_amount":"2.65","source_unit":"g","denominator":"stock batch
    with separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 125-128","quote":"CaCl\n2\n2.65\ng"}]},{"quantity_id":"q13","label":"Na2MoO4·4H2O","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Exact
    source mass belongs to the named stock batch, not to main ingredients. Preserve
    supplied chemical form, amount and stock water separately; no normalization from
    water alone or generic dilution multiplier is asserted.","source_stage":"1000x
    molybdate stock","source_amount":"0.1","source_unit":"g","denominator":"stock
    batch with separately listed water; no explicit final makeup","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 143-151","quote":"Na\n2\nMoO\n4\n·4H\n2\nO\n0.1\ng"}]},{"quantity_id":"q14","label":"20
    x PO4*","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"solutions[0].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"solutions[0].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    specifies a stock addition in mL, not G_PER_L. Preserve named stock identity,
    explicit dose and six separate compositions; the 1000 mL sum of listed inputs
    is not a measured final-volume instruction.","source_stage":"main receiving stock
    dose","source_amount":"50","source_unit":"mL","denominator":"one listed main batch","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 29-33","quote":"20 x PO\n4\n*\n50\nml"}]},{"quantity_id":"q15","label":"100
    x (NH4)2SO4**","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    specifies a stock addition in mL, not G_PER_L. Preserve named stock identity,
    explicit dose and six separate compositions; the 1000 mL sum of listed inputs
    is not a measured final-volume instruction.","source_stage":"main receiving stock
    dose","source_amount":"10","source_unit":"mL","denominator":"one listed main batch","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 34-42","quote":"100 x (NH\n4\n)\n2\nSO\n4\n**\n10\nml"}]},{"quantity_id":"q16","label":"1000
    x FeSO4***","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    specifies a stock addition in mL, not G_PER_L. Preserve named stock identity,
    explicit dose and six separate compositions; the 1000 mL sum of listed inputs
    is not a measured final-volume instruction.","source_stage":"main receiving stock
    dose","source_amount":"1","source_unit":"mL","denominator":"one listed main batch","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 43-47","quote":"1000 x FeSO\n4\n***\n1\nml"}]},{"quantity_id":"q17","label":"1000
    x MgCl2****","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"solutions[3].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"solutions[3].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    specifies a stock addition in mL, not G_PER_L. Preserve named stock identity,
    explicit dose and six separate compositions; the 1000 mL sum of listed inputs
    is not a measured final-volume instruction.","source_stage":"main receiving stock
    dose","source_amount":"1","source_unit":"mL","denominator":"one listed main batch","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 48-52","quote":"1000 x MgCl\n2\n****\n1\nml"}]},{"quantity_id":"q18","label":"1000
    x Trace elements*****","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"solutions[4].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"solutions[4].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    specifies a stock addition in mL, not G_PER_L. Preserve named stock identity,
    explicit dose and six separate compositions; the 1000 mL sum of listed inputs
    is not a measured final-volume instruction.","source_stage":"main receiving stock
    dose","source_amount":"1","source_unit":"mL","denominator":"one listed main batch","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 53-56","quote":"1000 x Trace elements\n*****\n1\nml"}]},{"quantity_id":"q19","label":"1000
    x Na2MoO4******","local_fields":[{"path":"data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml","field_path":"solutions[5].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml","field_path":"solutions[5].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    specifies a stock addition in mL, not G_PER_L. Preserve named stock identity,
    explicit dose and six separate compositions; the 1000 mL sum of listed inputs
    is not a measured final-volume instruction.","source_stage":"main receiving stock
    dose","source_amount":"1","source_unit":"mL","denominator":"one listed main batch","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 57-63","quote":"1000 x Na\n2\nMoO\n4\n******\n1\nml"}]},{"quantity_id":"q20","label":"Phosphate
    stock water","local_fields":[],"decision":"add","rationale":"Restore this water
    addition inside its own stock. It does not enter the main batch in full and is
    not an explicit final-volume makeup statement.","source_stage":"Phosphate stock
    water","source_amount":1,"source_unit":"L","denominator":"stock batch water","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 82-84","quote":"Distilled water\n1\nL"}]},{"quantity_id":"q21","label":"Ammonium
    stock water","local_fields":[],"decision":"add","rationale":"Restore this water
    addition inside its own stock. It does not enter the main batch in full and is
    not an explicit final-volume makeup statement.","source_stage":"Ammonium stock
    water","source_amount":1,"source_unit":"L","denominator":"stock batch water","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 101-103","quote":"Distilled water\n1\nL"}]},{"quantity_id":"q22","label":"Iron
    stock water","local_fields":[],"decision":"add","rationale":"Restore this water
    addition inside its own stock. It does not enter the main batch in full and is
    not an explicit final-volume makeup statement.","source_stage":"Iron stock water","source_amount":100,"source_unit":"mL","denominator":"stock
    batch water","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 112-114","quote":"Distilled water\n100\nml"}]},{"quantity_id":"q23","label":"Magnesium
    stock water","local_fields":[],"decision":"add","rationale":"Restore this water
    addition inside its own stock. It does not enter the main batch in full and is
    not an explicit final-volume makeup statement.","source_stage":"Magnesium stock
    water","source_amount":100,"source_unit":"mL","denominator":"stock batch water","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 121-123","quote":"Distilled water\n100\nml"}]},{"quantity_id":"q24","label":"Trace
    stock water","local_fields":[],"decision":"add","rationale":"Restore this water
    addition inside its own stock. It does not enter the main batch in full and is
    not an explicit final-volume makeup statement.","source_stage":"Trace stock water","source_amount":100,"source_unit":"mL","denominator":"stock
    batch water","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 136-138","quote":"Distilled water\n100\nml"}]},{"quantity_id":"q25","label":"Molybdate
    stock water","local_fields":[],"decision":"add","rationale":"Restore this water
    addition inside its own stock. It does not enter the main batch in full and is
    not an explicit final-volume makeup statement.","source_stage":"Molybdate stock
    water","source_amount":100,"source_unit":"mL","denominator":"stock batch water","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 152-154","quote":"Distilled water\n100\nml"}]},{"quantity_id":"q26","label":"Separate
    sterilization and cooling","local_fields":[],"decision":"add","rationale":"Retain
    separate sterilization, cooling to65 °C and ordered aseptic addition. The source
    does not supply sterilization temperature or duration; do not invent them.","source_stage":"preparation","source_amount":65,"source_unit":"degC","denominator":"cooling
    only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 67-67","quote":"Sterilize separately and cool to 65°C. Aseptically add to
    the following medium in order."}]},{"quantity_id":"q27","label":"Phosphate stock
    pH","local_fields":[],"decision":"add","rationale":"pH7.0 with unquantified KOH
    applies to the phosphate stock, not automatically the finished medium.","source_stage":"phosphate
    stock pH","source_amount":7,"source_unit":"pH","denominator":null,"sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 85-86","quote":"pH 7.0\nAdjust pH to 7.0 with KOH."}]},{"quantity_id":"q28","label":"Ammonium
    stock pH","local_fields":[],"decision":"add","rationale":"pH7.0 with unquantified
    NaOH applies to the ammonium stock, not automatically the finished medium.","source_stage":"ammonium
    stock pH","source_amount":7,"source_unit":"pH","denominator":null,"sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 104-105","quote":"pH 7.0\nAdjust pH to 7.0 with NaOH."}]},{"quantity_id":"q29","label":"Source
    stock factor 20 x PO4*","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this source stock name/factor as identity context. It does not establish a final
    receiving concentration for every component or authorize multiplication without
    a verified volume basis.","source_stage":"stock identity","source_amount":20,"source_unit":"x","denominator":"source
    stock label only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 29-33","quote":"20 x PO\n4\n*\n50\nml"}]},{"quantity_id":"q30","label":"Source
    stock factor 100 x (NH4)2SO4**","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this source stock name/factor as identity context. It does not establish a final
    receiving concentration for every component or authorize multiplication without
    a verified volume basis.","source_stage":"stock identity","source_amount":100,"source_unit":"x","denominator":"source
    stock label only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 34-42","quote":"100 x (NH\n4\n)\n2\nSO\n4\n**\n10\nml"}]},{"quantity_id":"q31","label":"Source
    stock factor 1000 x FeSO4***","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this source stock name/factor as identity context. It does not establish a final
    receiving concentration for every component or authorize multiplication without
    a verified volume basis.","source_stage":"stock identity","source_amount":1000,"source_unit":"x","denominator":"source
    stock label only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 43-47","quote":"1000 x FeSO\n4\n***\n1\nml"}]},{"quantity_id":"q32","label":"Source
    stock factor 1000 x MgCl2****","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this source stock name/factor as identity context. It does not establish a final
    receiving concentration for every component or authorize multiplication without
    a verified volume basis.","source_stage":"stock identity","source_amount":1000,"source_unit":"x","denominator":"source
    stock label only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 48-52","quote":"1000 x MgCl\n2\n****\n1\nml"}]},{"quantity_id":"q33","label":"Source
    stock factor 1000 x Trace elements*****","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this source stock name/factor as identity context. It does not establish a final
    receiving concentration for every component or authorize multiplication without
    a verified volume basis.","source_stage":"stock identity","source_amount":1000,"source_unit":"x","denominator":"source
    stock label only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 53-56","quote":"1000 x Trace elements\n*****\n1\nml"}]},{"quantity_id":"q34","label":"Source
    stock factor 1000 x Na2MoO4******","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this source stock name/factor as identity context. It does not establish a final
    receiving concentration for every component or authorize multiplication without
    a verified volume basis.","source_stage":"stock identity","source_amount":1000,"source_unit":"x","denominator":"source
    stock label only","sources":[{"evidence_id":"nbrc1333","source_url":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1333","raw_sha256":"3c45e7ea0d2415d41dc55966456ea862df5c86e3ea93bf703c221bacb15d6631","text_sha256":"33b3971ac37e72fcfea4d338d867220a5d198d59585bbfafc6a046fa73f64ddf","locator":"nbrc1333.txt
    lines 57-63","quote":"1000 x Na\n2\nMoO\n4\n******\n1\nml"}]}],"limits":["A listed
    water amount is not an explicit measured final volume. Stock-local amounts are
    not receiving-medium rates.","Source-only rows/conditions are explicit; no density
    assumptions or invented missing gas balance."]}'
- assessment_id: grounding
  area: grounding
  topic: Chemical identity, canonical labels and packaged MIM
  outcome: supported
  summary: All asserted CHEBI objects were retrieved directly and exact labels compared;
    supplied-form exceptions are described individually. Packaged MIM membership or
    label agreement alone is not chemical verification.
  target_ids:
  - CultureMech:008625
  evidence_ids:
  - grounding-sidecar
  - mim
- assessment_id: classification
  area: representation
  topic: Category, composition and physical-state scope
  outcome: concern
  summary: Bacterial scope is supported. SOLID_AGAR represents only an optional variant
    and must be made conditional alongside the liquid alternative. Agar makes the
    solid formulation composition distinct; a future liquid defined/synthetic classification
    requires explicit variant curation rather than blindly retaining imported COMPLEX/UNDEFINED
    defaults.
  target_ids:
  - CultureMech:008625
  evidence_ids:
  - current
  - nbrc1333
- assessment_id: history
  area: provenance
  topic: Current repairs and historical review limits
  outcome: supported
  summary: Complete current target/owner history and selected September report were
    read. Existing repair credit is retained; current writer bodies describe current
    behavior only. No lost 451–520 bundle is reconstructed or backdated.
  target_ids:
  - CultureMech:008625
  evidence_ids:
  - prior
  - current
  - importer
  - merger
findings:
- finding_id: f1
  issue_key: b054-09-f1
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Six stocks are flattened and their receiving doses have mass units
  description: The13 main ingredient rows include six distinct stock formulations,
    while all six solutions are Unknown solution stubs with empty composition and
    G_PER_L doses. Primary NBRC1333 specifies 50 mL, 10 mL and four 1 mL additions.
    Rebuild stage-local stocks/doses before regeneration; current importer already
    has stage-preserving paths and must not be described as historically unchanged.
  target_ids:
  - CultureMech:008625
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - nbrc1333
  - togo2036
  - stock-migration
  - importer
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material source/form/quantity mismatch needs curator correction;
    no claimed schema blocker.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml
    role: maintained source
- finding_id: f2
  issue_key: b054-09-f2
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Main and stock water additions were summed across units and containers
  description: The1338 G_PER_L row joins unrelated main/stock volumes and treats each
    1 L stock water numerically as1. Restore 936 mL main water, two 1 L stock waters
    and four 100 mL stock waters separately. The receiving liquid inputs sum 1000
    mL, but no explicit final-volume statement is given.
  target_ids:
  - CultureMech:008625
  field_paths:
  - ingredients[0]
  evidence_ids:
  - nbrc1333
  - togo2036
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material source/form/quantity mismatch needs curator correction;
    no claimed schema blocker.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml
    role: maintained source
- finding_id: f3
  issue_key: b054-09-f3
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Liquid biphenyl rate and agar-vapour formulation are conflated
  description: NBRC gives 1 g/L for substrate in liquid medium and a vapour-delivery
    alternative for agar plating. The selected SOLID_AGAR representation has a fixed
    1 G_PER_L biphenyl row and optional agar. Preserve explicit liquid versus plate
    variants and do not certify the plate dose from the liquid rate.
  target_ids:
  - CultureMech:008625
  field_paths:
  - ingredients[1]
  - ingredients[2]
  - physical_state
  evidence_ids:
  - nbrc1333
  - togo2036
  rule_id: review-yaml-record/stage-and-variant-scope
  native_severity: P2
  normalization_reason: Material source/form/quantity mismatch needs curator correction;
    no claimed schema blocker.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml
    role: maintained source
- finding_id: f4
  issue_key: b054-09-f4
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Stock pH and ordered preparation are omitted
  description: KOH and NaOH are unquantified stock-local pH7.0 adjusters, not generic
    final-medium ingredients. Separate sterilization, cooling to65 °C and ordered
    aseptic addition are absent. Preserve these source limits; no sterilization time/temperature
    or final-medium pH is supplied.
  target_ids:
  - CultureMech:008625
  field_paths:
  - ingredients[5]
  - ingredients[7]
  - preparation_steps
  evidence_ids:
  - nbrc1333
  - togo2036
  rule_id: review-yaml-record/source-supported-completeness
  native_severity: P2
  normalization_reason: Material source/form/quantity mismatch needs curator correction;
    no claimed schema blocker.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml
    role: maintained source
- finding_id: f5
  issue_key: b054-09-f5
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: The generated target omits the owner biphenyl repair
  description: The maintained owner has the August 20 MIM grounding event and CHEBI:17097;
    the target retains the earlier ungrounded row. Credit the current writer and owner
    repair, then regenerate without claiming the present merger accepts incompatible
    formulations.
  target_ids:
  - CultureMech:008625
  field_paths:
  - ingredients[1].term
  - curation_history
  evidence_ids:
  - current
  - chebi17097
  - mim-writer
  - merger
  rule_id: review-yaml-record/maintained-owner-and-freshness
  native_severity: P2
  normalization_reason: Material source/form/quantity mismatch needs curator correction;
    no claimed schema blocker.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml
    role: maintained source
- finding_id: f6
  issue_key: b054-09-f6
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source evidence and remaining grounding scope need explicit placement
  description: Primary and TOGO links are notes only. Attach stage-specific claim
    evidence. The exact source tetrahydrate name for sodium molybdate is retained
    without an asserted CHEBI; the packaged CSV has no exact supplied-label match.
    This is a scoped unresolved mapping, not evidence that the source should be changed
    to the common dihydrate. Agar and biphenyl missing secondary links are distinct
    from confirmed wrong IDs.
  target_ids:
  - CultureMech:008625
  field_paths:
  - notes
  - ingredients[12]
  - ingredients[2]
  - ingredients[1]
  evidence_ids:
  - nbrc1333
  - togo2036
  - mim
  rule_id: review-yaml-record/claim-level-evidence
  native_severity: P3
  normalization_reason: Provenance or representational completeness issue with bounded
    impact.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml
    role: maintained source
actions:
- action_id: a1
  description: 'Correct the maintained source for: Six stocks are flattened and their
    receiving doses have mass units. The13 main ingredient rows include six distinct
    stock formulations, while all six solutions are Unknown solution stubs with empty
    composition and G_PER_L doses. Primary NBRC1333 specifies 50 mL, 10 mL and four
    1 mL additions. Rebuild stage-local stocks/doses before regeneration; current
    importer already has stage-preserving paths and must not be described as historically
    unchanged.'
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008625
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml
    role: maintained source
  acceptance_checks:
  - Preserve exact source version, claim scope, original history and new curation
    event; do not edit generated YAML directly.
  - Re-run schema/strict/term/reference checks on corrected owner and regenerated
    target; compare every affected source row and preserve unsupported denominators
    as unresolved.
  generator: Maintained owner curation then repository merge regeneration and freshness
    check
- action_id: a2
  description: 'Correct the maintained source for: Main and stock water additions
    were summed across units and containers. The1338 G_PER_L row joins unrelated main/stock
    volumes and treats each 1 L stock water numerically as1. Restore 936 mL main water,
    two 1 L stock waters and four 100 mL stock waters separately. The receiving liquid
    inputs sum 1000 mL, but no explicit final-volume statement is given.'
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008625
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml
    role: maintained source
  acceptance_checks:
  - Preserve exact source version, claim scope, original history and new curation
    event; do not edit generated YAML directly.
  - Re-run schema/strict/term/reference checks on corrected owner and regenerated
    target; compare every affected source row and preserve unsupported denominators
    as unresolved.
  generator: Maintained owner curation then repository merge regeneration and freshness
    check
- action_id: a3
  description: 'Correct the maintained source for: Liquid biphenyl rate and agar-vapour
    formulation are conflated. NBRC gives 1 g/L for substrate in liquid medium and
    a vapour-delivery alternative for agar plating. The selected SOLID_AGAR representation
    has a fixed 1 G_PER_L biphenyl row and optional agar. Preserve explicit liquid
    versus plate variants and do not certify the plate dose from the liquid rate.'
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008625
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml
    role: maintained source
  acceptance_checks:
  - Preserve exact source version, claim scope, original history and new curation
    event; do not edit generated YAML directly.
  - Re-run schema/strict/term/reference checks on corrected owner and regenerated
    target; compare every affected source row and preserve unsupported denominators
    as unresolved.
  generator: Maintained owner curation then repository merge regeneration and freshness
    check
- action_id: a4
  description: 'Correct the maintained source for: Stock pH and ordered preparation
    are omitted. KOH and NaOH are unquantified stock-local pH7.0 adjusters, not generic
    final-medium ingredients. Separate sterilization, cooling to65 °C and ordered
    aseptic addition are absent. Preserve these source limits; no sterilization time/temperature
    or final-medium pH is supplied.'
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008625
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml
    role: maintained source
  acceptance_checks:
  - Preserve exact source version, claim scope, original history and new curation
    event; do not edit generated YAML directly.
  - Re-run schema/strict/term/reference checks on corrected owner and regenerated
    target; compare every affected source row and preserve unsupported denominators
    as unresolved.
  generator: Maintained owner curation then repository merge regeneration and freshness
    check
- action_id: a5
  description: 'Correct the maintained source for: The generated target omits the
    owner biphenyl repair. The maintained owner has the August 20 MIM grounding event
    and CHEBI:17097; the target retains the earlier ungrounded row. Credit the current
    writer and owner repair, then regenerate without claiming the present merger accepts
    incompatible formulations.'
  finding_ids:
  - f5
  target_ids:
  - CultureMech:008625
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml
    role: maintained source
  acceptance_checks:
  - Preserve exact source version, claim scope, original history and new curation
    event; do not edit generated YAML directly.
  - Re-run schema/strict/term/reference checks on corrected owner and regenerated
    target; compare every affected source row and preserve unsupported denominators
    as unresolved.
  generator: Maintained owner curation then repository merge regeneration and freshness
    check
- action_id: a6
  description: 'Correct the maintained source for: Source evidence and remaining grounding
    scope need explicit placement. Primary and TOGO links are notes only. Attach stage-specific
    claim evidence. The exact source tetrahydrate name for sodium molybdate is retained
    without an asserted CHEBI; the packaged CSV has no exact supplied-label match.
    This is a scoped unresolved mapping, not evidence that the source should be changed
    to the common dihydrate. Agar and biphenyl missing secondary links are distinct
    from confirmed wrong IDs.'
  finding_ids:
  - f6
  target_ids:
  - CultureMech:008625
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml
    role: maintained source
  acceptance_checks:
  - Preserve exact source version, claim scope, original history and new curation
    event; do not edit generated YAML directly.
  - Re-run schema/strict/term/reference checks on corrected owner and regenerated
    target; compare every affected source row and preserve unsupported denominators
    as unresolved.
  generator: Maintained owner curation then repository merge regeneration and freshness
    check
limitations:
- Source FeSO4/MgCl2/CaCl2 omit hydrate qualifiers; retain the literal formulas without
  choosing common hydrates from mass intuition. Na2MoO4·4H2O is explicitly tetrahydrate
  and remains ungrounded rather than substituted.
- The six stock factors are labels, not independently measured stock potency. Optional
  agar and vapour delivery are distinct from the explicit liquid biphenyl rate.
- The September report is derivative historical context; its old validations and source
  access times are not used as current verification.
- Packaged MIM CSV observations apply only to commit 6643131b0f12ab40b66f98135245fca04027e0e9;
  no global absence or live MIM claim.
- No experiment, growth optimization or universal strain applicability is inferred;
  catalog identity examples are not automatically inserted as target_organisms.
- Canonical reference validation inspected zero references in the generated target;
  scientific source authentication is supplied separately here.
- Source recipes list batch amounts unless an explicit concentration/final-volume
  statement is quoted. No silent normalization based solely on listed water.
```
