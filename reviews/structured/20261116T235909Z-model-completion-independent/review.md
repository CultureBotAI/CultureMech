# Independent review of model-completion events and field-specific holds

- Review: 20261116T235909Z-model-completion-independent
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-11-16T23:59:09Z
- Finished UTC: 2026-11-16T23:59:09Z
- Reviewer: codex-bundle-independent-scientific-reviewer (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Gas phase, species/strain/alternative arms, literal batch and unspecified-percent bases, named stocks and negative mixture membership remain explicit. No whole-medium or successful-growth inference is approved.

## Scope And Provenance

31 original model-held rows plus six existing-event amount promotions, covering 27 recipe preimages and 37 dispositions.

Selection: Exact frozen proposal and source/recipe hash inventory.
Coverage: partial; 27 reviewed / 27 in the declared population.
Source: working_tree at Git base b2652f7c7197aef33162ac9a721d21a16d528249.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000025 | data/normalized_yaml/algae/Artificial_Seawater_Medium.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | artificial_seawater_medium |
| CultureMech:000170 | data/normalized_yaml/algae/F_2_Medium.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | f_2_medium |
| CultureMech:000233 | data/normalized_yaml/algae/TAP_Medium.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | tap_medium |
| CultureMech:015450 | data/normalized_yaml/algae/bg11.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | BG11 |
| CultureMech:009166 | data/normalized_yaml/archaea/ignicoccus_medium_for_dsm_18386.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | ignicoccus_medium_for_dsm_18386 |
| CultureMech:000643 | data/normalized_yaml/archaea/methanobacterium_medium.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | methanobacterium_medium |
| CultureMech:009226 | data/normalized_yaml/archaea/sulfolobus_medium_anaerobic_for_dsm_2162.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | sulfolobus_medium_anaerobic_for_dsm_2162 |
| CultureMech:004018 | data/normalized_yaml/bacterial/KOMODO_125_METHYLOBACTERIUM_MEDIUM.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | methylobacterium_medium |
| CultureMech:006403 | data/normalized_yaml/bacterial/KOMODO_751_SC_medium.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | sc_medium |
| CultureMech:006900 | data/normalized_yaml/bacterial/KOMODO_956_MEDIUM_FOR_DSM_14457_AND_14458.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | medium_for_dsm_14457_and_14458 |
| CultureMech:007843 | data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | methylotroph_medium |
| CultureMech:008906 | data/normalized_yaml/bacterial/bacto_marine_broth_difco_2216_for_dsm_11879.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | bacto_marine_broth_difco_2216_for_dsm_11879 |
| CultureMech:007092 | data/normalized_yaml/bacterial/cdm_teusink_et_al.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | cdm_teusink_et_al |
| CultureMech:006260 | data/normalized_yaml/bacterial/for_dsm_9463.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | for_dsm_9463 |
| CultureMech:006262 | data/normalized_yaml/bacterial/for_dsm_9466.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | for_dsm_9466 |
| CultureMech:006263 | data/normalized_yaml/bacterial/for_dsm_9467.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | for_dsm_9467 |
| CultureMech:006264 | data/normalized_yaml/bacterial/for_dsm_9468.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | for_dsm_9468 |
| CultureMech:002134 | data/normalized_yaml/bacterial/medium_for_dsm_14457_and_14458.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | medium_for_dsm_14457_and_14458 |
| CultureMech:000718 | data/normalized_yaml/bacterial/methylobacterium_medium.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | methylobacterium_medium |
| CultureMech:007202 | data/normalized_yaml/bacterial/minimal_medium_teusink_et_al.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | minimal_medium_teusink_et_al |
| CultureMech:007076 | data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_and_salt_stress_tang_et_al_2009.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | minimal_medium_w_amino_acids_and_salt_stress_tang_et_al_2009 |
| CultureMech:007075 | data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_tang_et_al_2009.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | minimal_medium_w_amino_acids_tang_et_al_2009 |
| CultureMech:007070 | data/normalized_yaml/bacterial/modified_m1_medium_with_18_mm_lactate_pinchuk_et_al.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | modified_m1_medium_with_18_mm_lactate_pinchuk_et_al |
| CultureMech:007069 | data/normalized_yaml/bacterial/modified_m1_medium_with_20_mm_lactate_pinchuk_et_al.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | modified_m1_medium_with_20_mm_lactate_pinchuk_et_al |
| CultureMech:007072 | data/normalized_yaml/bacterial/modified_m1_medium_with_acetate_pinchuk_et_al.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | modified_m1_medium_with_acetate_pinchuk_et_al |
| CultureMech:007071 | data/normalized_yaml/bacterial/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | modified_m1_medium_with_lactate_and_glycine_no_nh4cl |
| CultureMech:001884 | data/normalized_yaml/bacterial/sc_medium.yaml # Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal | maintained | sc_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Proposal, targets, sources and exact amount-only promotions | passed | True | CultureMech:000025, CultureMech:000170, CultureMech:000233, CultureMech:015450, CultureMech:009166, CultureMech:000643, CultureMech:009226, CultureMech:004018, CultureMech:006403, CultureMech:006900, CultureMech:007843, CultureMech:008906, CultureMech:007092, CultureMech:006260, CultureMech:006262, CultureMech:006263, CultureMech:006264, CultureMech:002134, CultureMech:000718, CultureMech:007202, CultureMech:007076, CultureMech:007075, CultureMech:007070, CultureMech:007069, CultureMech:007072, CultureMech:007071, CultureMech:001884 | All preimages/captures and source coordinates verified; six replacements add only amount, preserving existing identity, action, evidence and stage. |
| Independent source-family claim review | passed | True | CultureMech:000025, CultureMech:000170, CultureMech:000233, CultureMech:015450, CultureMech:009166, CultureMech:000643, CultureMech:009226, CultureMech:004018, CultureMech:006403, CultureMech:006900, CultureMech:007843, CultureMech:008906, CultureMech:007092, CultureMech:006260, CultureMech:006262, CultureMech:006263, CultureMech:006264, CultureMech:002134, CultureMech:000718, CultureMech:007202, CultureMech:007076, CultureMech:007075, CultureMech:007070, CultureMech:007069, CultureMech:007072, CultureMech:007071, CultureMech:001884 | Manual primary-source reading supports the bounded assertions and holds; gas supply is not liquid concentration, named mixture is not constituent identity, and alternative arms are not simultaneous. |

## Scientific And Domain Assessments

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:000025.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:000170.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:000233.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:015450.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:009166.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:000643.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:009226.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:004018.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:006403.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:006900.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:007843.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:008906.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:007092.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:006260.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:006262.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:006263.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:006264.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:002134.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:000718.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:007202.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:007076.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:007075.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:007070.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:007069.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:007072.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:007071.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

### Proposed model completion and quantity representation

scope: supported. Targets: CultureMech:001884.

The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 751 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium751.pdf; Page 1 liquid-medium instruction | supports | Official liquid-medium instruction supplies phosphate masses, not an explicit final litre. SET_AMOUNT correctly retains 1.5 g KH2PO4 and 0.5 g K2HPO4 per batch. |
| 670 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium670.pdf; Page 1 base table and strain preparations | supports | Current official base table supplies 950 mL water before separately described ferrous stock/strain amendments. This input is not a final-volume denominator or the older archive's one-litre input. |
| 125 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium125.pdf; Page 1 carbon alternatives | supports | Official instruction explicitly supplies 5 mL methanol or a methane-air atmosphere. The promoted amount preserves the methanol batch input without purity or final-volume assumptions. |
| 956 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium956.pdf; Page 1 post-sterilization alternatives | supports | Official post-sterilization alternatives specify final 0.5 percent methanol or 0.3 percent methylamine. Basis remains unspecified; no v/v or mass concentration is invented. |
| 119 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium119.pdf; Strain-specific post-inoculation gas instructions | supports | Official DSM2030/9575 instructions specify 2 bar overpressure and DSM25939/25945 specify 1 bar, after inoculation with 80:20 hydrogen/carbon dioxide. Events preserve strain, stage and gas context; no liquid dose is implied. |
| hemiaulus | PMID:33083143; Methods: naturally dissolved N2 | supports | Methods explicitly describe naturally dissolved nitrogen in fixed-N-free cultures. A held operation is appropriate: source presence does not establish deliberate nitrogen addition or a named fixed-nitrogen removal. |
| fertilizer | PMID:40484141; Primary abstract only | supports | The primary abstract supports a named water-soluble fertilizer replacing TAP trace/macroelements. The named mixture input is defensible while exact product composition, dose and displaced chemicals remain held. |
| teusink | doi:10.1128/AEM.71.11.7253-7262.2005; Table 1 headings and footnotes | supports | The source table's complete-formulation membership is not automatically converted into ingredient additions or removal operations. Existing discrete approved amounts are outside this follow-up assertion scope. |
| tang | doi:10.1002/btpr.227; Author manuscript page 4 | supports | Author manuscript page4 specifies the AA-S-18 supplement, 17 included amino acids at 25 micromolar each and three excluded amino acids. Named mixture input is supported. Exclusion from the supplement does not establish whole-culture absence or removal; exact DL forms are not inferred. |
| pinchuk | doi:10.1371/journal.pcbi.1000822; Methods: Bacterial Strains and Growth Media | supports | Methods explicitly name 10 mL each of two 10x stocks without a final-volume denominator. Literal inputs are retained, with stock-component correspondence to flattened parents held separately. |
| bg11 | PMID:34584038; Methods: phototrophic BG-11 gas supply | supports | Captured phototrophic Methods support alternative ambient-air/2-percent-CO2 supplies at 0.5 vvm for ABC-009 in BG-11. This is distinct from the heterotrophic YM experiment; no gas fraction is encoded as a dissolved concentration. |
| matsui | DOI:10.1104/pp.18.00453; Methods: culture conditions and transformation | supports | Culture Methods distinguish high-CO2 and ambient-air aeration arms. The gas identity/stage is represented without mixing alternative arms or inventing aqueous concentration. |
| kato | doi:10.1264/jsme2.ME19128; Methods: cultivation of methanotrophs | supports | Methods assign default 20 micromolar metal treatments to the specified strain arms and separately describe methane gas per tube or 20 mM methanol. The methane amount is a two-mL gas input into one tube batch; metal hydration, standard-state gas volume and simultaneous carbon supplies are not invented. |
| kosch | doi:10.5283/epub.34741; Printed pages27–28, sections2.2.2.1–2.2.2.2 | supports | Printed page28 distinguishes final 80:20 hydrogen/carbon-dioxide headspace exchange at 1.5 bar from the earlier nitrogen/carbon-dioxide purge and chamber gas. The proposed events preserve that final-headspace scope. |
| willard | doi:10.1128/mbio.01033-24; Materials and Methods: low-sulfate Brock salts and species-specific pH | supports | Culture Methods supports elemental sulfur at 10 g/L, separate species groups receiving 1 or 0.2 g/L yeast extract, and the sucrose/NZ-Amine arm. Vented bottles do not independently prove a removal of the local parent's sulfide or nitrogen. |
| tsuji | DOI:10.1007/s10126-021-10037-4; Primary abstract only | supports | The publisher abstract directly contrasts supplied 5-percent and 0.04-percent carbon-dioxide air under low sodium; the lower-CO2 arm did not support growth. Both inputs can be recorded without a positive growth claim or invented full Methods. Browser inspection; no local capture hash claimed. |
| marine | doi:10.1099/ijs.0.012724-0; Primary paper page 2730 | supports | The primary-paper author copy, printed2730, states dilution of marine medium to half strength with water. The named diluent input is supported; an absolute water volume or complete constituent expansion is not inferred. Browser inspection; no local capture hash claimed. |

## Limits And Additional Notes

- Agent scientific review, not human approval or release approval.
- No recipes were mutated; native writer/export/schema gates remain separate.
- Tsuji evidence is the publisher abstract only; marine-paper text was inspected in an author copy. Neither browser-only source is assigned a fabricated capture hash.
- This review does not establish exact forms of unresolved salts/stocks, correspondence to flattened parents, or unreported final volumes.
- Gas events retain headspace/aeration stages; no liquid dose or physiological success is inferred.
- No-op record/variant envelopes may be omitted by the separate merger without changing these scientific decisions or disposition accounting.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261116T235909Z-model-completion-independent
kind: batch
repository: CultureBotAI/CultureMech
title: Independent review of model-completion events and field-specific holds
started_at: '2026-11-16T23:59:09Z'
finished_at: '2026-11-16T23:59:09Z'
reviewer:
  identity: codex-bundle-independent-scientific-reviewer
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author this follow-up proposal or its six amount
    promotions. Reviewer authored earlier extraction and MIM intake code and a distinct
    earlier bacterial cohort; this review is limited to the new proposal.
skill: curate-yaml-record; review-ingredient-concentrations
completion: completed
verdict: pass_with_limitations
scientific_review: true
native_verdict: The proposed 47 appended events, 19 field-specific holds and six literal-amount
  promotions agree with inspected sources; no new material finding.
summary: Gas phase, species/strain/alternative arms, literal batch and unspecified-percent
  bases, named stocks and negative mixture membership remain explicit. No whole-medium
  or successful-growth inference is approved.
source:
  git_revision: b2652f7c7197aef33162ac9a721d21a16d528249
  state: working_tree
  inputs:
  - path: .temp/variant-completeness-683/independent-model-review-v1/119.pdf
    sha256: 65295918764de4ed5b73ce773ab4057a7183ecf8bfd7fff0d02393d901b41a2a
    role: context
  - path: .temp/variant-completeness-683/independent-model-review-v1/125.pdf
    sha256: e107edb0e43f303bc124e81ef0430f07fde07eb9efbcf1cea9c35e3a2190ad8f
    role: context
  - path: .temp/variant-completeness-683/independent-model-review-v1/670.pdf
    sha256: e21dbc3f7c16cf301001aaa5ca4ca7aa57fb486cbccba0995c46e094946917ab
    role: context
  - path: .temp/variant-completeness-683/independent-model-review-v1/751.pdf
    sha256: 721e0310d250ea6eab5d453f063b9452b48b8368ad53fa9384cb54434d2e59fb
    role: context
  - path: .temp/variant-completeness-683/independent-model-review-v1/956.pdf
    sha256: 156fe7f9a826c658bf690c9c892ba7d137848d397f55cf93568c4c3145374f39
    role: context
  - path: .temp/variant-completeness-683/independent-model-review-v1/fertilizer.json
    sha256: 3f738652b616e23152d9ce0740fc5f05ebabd63716e5a17cdc5482b56643d375
    role: context
  - path: .temp/variant-completeness-683/independent-model-review-v1/hemiaulus.xml
    sha256: b2b891255be3531171e9479c4d8744724632f3b4e3f89573664273774d4f47e9
    role: context
  - path: .temp/variant-completeness-683/independent-model-review-v1/pinchuk.xml
    sha256: 9fc877d8ff8e5822a2abf7e00ef5395d11cba3da89281ba3c2038e1c14de6d81
    role: context
  - path: .temp/variant-completeness-683/independent-model-review-v1/tang.pdf
    sha256: ebbab61739c7a8c63213c57e0258f20822d165ef8188e23455ff8495689eb4be
    role: context
  - path: .temp/variant-completeness-683/independent-model-review-v1/teusink.html
    sha256: 3b4288d316e061cdad56879cb8a30c2cccff1fe3361eb0be71778d49c9dbef91
    role: context
  - path: .temp/variant-completeness-683/independent-model-review-v1/willard.xml
    sha256: 7808bc365628f8d1a71ab0a20135f2f0619a19fc6db1d587961007e8c0ecaba3
    role: context
  - path: .temp/variant-completeness-683/sources/bg11-2021/source.xml
    sha256: 669d11703f04dc008905d7ac0b78c5963585ff556d92fb0229ae63323634a697
    role: context
  - path: .temp/variant-completeness-683/sources/koschnitzki-2017/source.pdf
    sha256: 21117464e1481e058031575f2bd668afd37677cd842636230adf54982111e8f9
    role: context
  - path: .temp/variant-completeness-683/sources/matsui-2018-html/source.html
    sha256: beecd6db87651dbf5f4119169a755249ba977070ee4a7046d26dff3bab3b5d43
    role: context
  - path: .temp/variant-completeness-683/sources/methylotroph-2020/source.xml
    sha256: 2ade9577ad927b568273334fa9b14d2da22d155f877535d317ad13a0977a224d
    role: context
  - path: conf/variant_ingredient_curation/completeness-model-683.json
    sha256: 548408377e4a75f000f779560647661533107b78199283df371ccda1680fde28
    role: context
  - path: data/normalized_yaml/algae/Artificial_Seawater_Medium.yaml
    sha256: b6636a9b18a477aaaa935531eea34a7a050a1859db0ea04c73054331e12dbaba
    role: target
  - path: data/normalized_yaml/algae/F_2_Medium.yaml
    sha256: 87cec46fd41e42ee7de2dd99b3ed5d0862ae970048f8a410458478f8e2caff37
    role: target
  - path: data/normalized_yaml/algae/TAP_Medium.yaml
    sha256: b44608e3c6ce42801cea59497c6bce8e5dd1be3c2e08ae43f55617bf789ccc77
    role: target
  - path: data/normalized_yaml/algae/bg11.yaml
    sha256: 50cf10be2d7e6c7eec48f0d9ad0911b27e4d6e52b8386cfe43924339a304c468
    role: target
  - path: data/normalized_yaml/archaea/ignicoccus_medium_for_dsm_18386.yaml
    sha256: c37b836f529b1cd7080fb17e9b9a837501712e78e6fb5afa98bf246501fd733b
    role: target
  - path: data/normalized_yaml/archaea/methanobacterium_medium.yaml
    sha256: b671cbbe466583591ab494a297e153dbb74a5d374144b8a1c7b558c7bfc264df
    role: target
  - path: data/normalized_yaml/archaea/sulfolobus_medium_anaerobic_for_dsm_2162.yaml
    sha256: bba397f1a053e773b29be15a57da4a60c4d5753827582e11c168525890b4c4f8
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_125_METHYLOBACTERIUM_MEDIUM.yaml
    sha256: de0a27c5f2553ac733ea5c894832649bf2e9df8f152c0b005e77ad4c4e2fd75b
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_751_SC_medium.yaml
    sha256: 7b82abae9ce5b26b7275ccc93142a5ae7fb64bc9183b8fb77a3b362390676be2
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_956_MEDIUM_FOR_DSM_14457_AND_14458.yaml
    sha256: 28178c1e9f4ee18312185a850956fa768139cd8f7d63bb17d57d30883eedeee3
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml
    sha256: 967394ea5131b424e8bdb02c7d5318d6d60b97cb8539abd8b49f995a3dcc8107
    role: target
  - path: data/normalized_yaml/bacterial/bacto_marine_broth_difco_2216_for_dsm_11879.yaml
    sha256: c3e997aa7c21b7d944f3846b9a5f3be32a0c875c6e2b8f5e502a06c438e5fbe2
    role: target
  - path: data/normalized_yaml/bacterial/cdm_teusink_et_al.yaml
    sha256: 56aaf4fd22a1592e455b432079cb1123888e3687241cfe1dca1799fd8b88b6c2
    role: target
  - path: data/normalized_yaml/bacterial/for_dsm_9463.yaml
    sha256: 48bdb6484a3a819111d59dd466d2f1d7a56ba8885e1be5bf5ec051f0ae7afb17
    role: target
  - path: data/normalized_yaml/bacterial/for_dsm_9466.yaml
    sha256: 4bbc3a0de4dfd7c77e335a3dd88f909a54b96f9a0074586ec43f3efefd8ffb68
    role: target
  - path: data/normalized_yaml/bacterial/for_dsm_9467.yaml
    sha256: c5576056dbb824038944c4e314ec46f683e143e99477d2f1bb57cc2ee4d2761c
    role: target
  - path: data/normalized_yaml/bacterial/for_dsm_9468.yaml
    sha256: a03592f45477a35dc9f386dcdea84372affb01e376578a46a28f3e4080d8244b
    role: target
  - path: data/normalized_yaml/bacterial/medium_for_dsm_14457_and_14458.yaml
    sha256: 961e732e30fe0227c8f821592fcbdbfdf5a4ce32530f5b87e53c09e4a28ab28b
    role: target
  - path: data/normalized_yaml/bacterial/methylobacterium_medium.yaml
    sha256: 63cded5b220afa3cf50a2600602b0ce9223fba7558090f0f671ea16fd0b671a4
    role: target
  - path: data/normalized_yaml/bacterial/minimal_medium_teusink_et_al.yaml
    sha256: d26aa32bdb693b07e740b72bcfd5b9735f9081b4b72ad5f2991fe089acba52fc
    role: target
  - path: data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_and_salt_stress_tang_et_al_2009.yaml
    sha256: 24894a0f2c8d08506236297f5ecef184e0b3d5a6f50891073da9f6e8cada6a3e
    role: target
  - path: data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_tang_et_al_2009.yaml
    sha256: cb231608c24a08626143cc56b344442b0fd20bd3e93583210cacd9b7959585c7
    role: target
  - path: data/normalized_yaml/bacterial/modified_m1_medium_with_18_mm_lactate_pinchuk_et_al.yaml
    sha256: 208093fb2ff607811c1bf4f861b01f51195fb7ef8f60381990be2e8ff5d247b6
    role: target
  - path: data/normalized_yaml/bacterial/modified_m1_medium_with_20_mm_lactate_pinchuk_et_al.yaml
    sha256: fea807f8ffc653ec2c739a2763e13b798cf57e4304abe98060416173dab8aeff
    role: target
  - path: data/normalized_yaml/bacterial/modified_m1_medium_with_acetate_pinchuk_et_al.yaml
    sha256: 376f15a9b13520aa85a4fd8e58ed1dda66eeeec2fa083fb63b838c4649f9a868
    role: target
  - path: data/normalized_yaml/bacterial/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml
    sha256: 2b20af3fb04b842674d3b4118a3701121241c8df985266e357d500d0d121e5a1
    role: target
  - path: data/normalized_yaml/bacterial/sc_medium.yaml
    sha256: a5571ed03f3198bdb4118a90282d2624af5c9b9caa98ed3f83cdd2bc76a242e5
    role: target
  - path: scripts/adhoc/review_model_completion_683.py
    sha256: 98da4c2c6f2373b0bfa80a5f87b5fc8b2d23d330e5581a32a6fbae0947da96fa
    role: context
scope:
  description: 31 original model-held rows plus six existing-event amount promotions,
    covering 27 recipe preimages and 37 dispositions.
  selection: Exact frozen proposal and source/recipe hash inventory.
  coverage: partial
  population_size: 27
  reviewed_target_ids:
  - CultureMech:000025
  - CultureMech:000170
  - CultureMech:000233
  - CultureMech:015450
  - CultureMech:009166
  - CultureMech:000643
  - CultureMech:009226
  - CultureMech:004018
  - CultureMech:006403
  - CultureMech:006900
  - CultureMech:007843
  - CultureMech:008906
  - CultureMech:007092
  - CultureMech:006260
  - CultureMech:006262
  - CultureMech:006263
  - CultureMech:006264
  - CultureMech:002134
  - CultureMech:000718
  - CultureMech:007202
  - CultureMech:007076
  - CultureMech:007075
  - CultureMech:007070
  - CultureMech:007069
  - CultureMech:007072
  - CultureMech:007071
  - CultureMech:001884
  exclusions:
  - target: Unrelated recipe assertions, full formulations and truth of unresolved
      held details
    reason: Only the enumerated proposal is assessed; held dimensions are retained
      rather than approved.
targets:
- target_id: CultureMech:000025
  path: data/normalized_yaml/algae/Artificial_Seawater_Medium.yaml
  label: artificial_seawater_medium
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/Artificial_Seawater_Medium.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:000170
  path: data/normalized_yaml/algae/F_2_Medium.yaml
  label: f_2_medium
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/F_2_Medium.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:000233
  path: data/normalized_yaml/algae/TAP_Medium.yaml
  label: tap_medium
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/TAP_Medium.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:015450
  path: data/normalized_yaml/algae/bg11.yaml
  label: BG11
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/bg11.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:009166
  path: data/normalized_yaml/archaea/ignicoccus_medium_for_dsm_18386.yaml
  label: ignicoccus_medium_for_dsm_18386
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/ignicoccus_medium_for_dsm_18386.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:000643
  path: data/normalized_yaml/archaea/methanobacterium_medium.yaml
  label: methanobacterium_medium
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/methanobacterium_medium.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:009226
  path: data/normalized_yaml/archaea/sulfolobus_medium_anaerobic_for_dsm_2162.yaml
  label: sulfolobus_medium_anaerobic_for_dsm_2162
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/sulfolobus_medium_anaerobic_for_dsm_2162.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:004018
  path: data/normalized_yaml/bacterial/KOMODO_125_METHYLOBACTERIUM_MEDIUM.yaml
  label: methylobacterium_medium
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_125_METHYLOBACTERIUM_MEDIUM.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:006403
  path: data/normalized_yaml/bacterial/KOMODO_751_SC_medium.yaml
  label: sc_medium
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_751_SC_medium.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:006900
  path: data/normalized_yaml/bacterial/KOMODO_956_MEDIUM_FOR_DSM_14457_AND_14458.yaml
  label: medium_for_dsm_14457_and_14458
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_956_MEDIUM_FOR_DSM_14457_AND_14458.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007843
  path: data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml
  label: methylotroph_medium
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:008906
  path: data/normalized_yaml/bacterial/bacto_marine_broth_difco_2216_for_dsm_11879.yaml
  label: bacto_marine_broth_difco_2216_for_dsm_11879
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacto_marine_broth_difco_2216_for_dsm_11879.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007092
  path: data/normalized_yaml/bacterial/cdm_teusink_et_al.yaml
  label: cdm_teusink_et_al
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_teusink_et_al.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:006260
  path: data/normalized_yaml/bacterial/for_dsm_9463.yaml
  label: for_dsm_9463
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_9463.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:006262
  path: data/normalized_yaml/bacterial/for_dsm_9466.yaml
  label: for_dsm_9466
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_9466.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:006263
  path: data/normalized_yaml/bacterial/for_dsm_9467.yaml
  label: for_dsm_9467
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_9467.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:006264
  path: data/normalized_yaml/bacterial/for_dsm_9468.yaml
  label: for_dsm_9468
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_9468.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:002134
  path: data/normalized_yaml/bacterial/medium_for_dsm_14457_and_14458.yaml
  label: medium_for_dsm_14457_and_14458
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_for_dsm_14457_and_14458.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:000718
  path: data/normalized_yaml/bacterial/methylobacterium_medium.yaml
  label: methylobacterium_medium
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/methylobacterium_medium.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007202
  path: data/normalized_yaml/bacterial/minimal_medium_teusink_et_al.yaml
  label: minimal_medium_teusink_et_al
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/minimal_medium_teusink_et_al.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007076
  path: data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_and_salt_stress_tang_et_al_2009.yaml
  label: minimal_medium_w_amino_acids_and_salt_stress_tang_et_al_2009
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_and_salt_stress_tang_et_al_2009.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007075
  path: data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_tang_et_al_2009.yaml
  label: minimal_medium_w_amino_acids_tang_et_al_2009
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_tang_et_al_2009.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007070
  path: data/normalized_yaml/bacterial/modified_m1_medium_with_18_mm_lactate_pinchuk_et_al.yaml
  label: modified_m1_medium_with_18_mm_lactate_pinchuk_et_al
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_m1_medium_with_18_mm_lactate_pinchuk_et_al.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007069
  path: data/normalized_yaml/bacterial/modified_m1_medium_with_20_mm_lactate_pinchuk_et_al.yaml
  label: modified_m1_medium_with_20_mm_lactate_pinchuk_et_al
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_m1_medium_with_20_mm_lactate_pinchuk_et_al.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007072
  path: data/normalized_yaml/bacterial/modified_m1_medium_with_acetate_pinchuk_et_al.yaml
  label: modified_m1_medium_with_acetate_pinchuk_et_al
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_m1_medium_with_acetate_pinchuk_et_al.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007071
  path: data/normalized_yaml/bacterial/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml
  label: modified_m1_medium_with_lactate_and_glycine_no_nh4cl
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:001884
  path: data/normalized_yaml/bacterial/sc_medium.yaml
  label: sc_medium
  kind: maintained
  record_class: MediaRecipe
  selector: Only model-completion events, held mentions and six literal-amount promotions
    in the pinned proposal
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/sc_medium.yaml
    role: authoritative normalized recipe
checks:
- check_id: frozen-inputs
  name: Proposal, targets, sources and exact amount-only promotions
  status: passed
  required: true
  summary: All preimages/captures and source coordinates verified; six replacements
    add only amount, preserving existing identity, action, evidence and stage.
  target_ids:
  - CultureMech:000025
  - CultureMech:000170
  - CultureMech:000233
  - CultureMech:015450
  - CultureMech:009166
  - CultureMech:000643
  - CultureMech:009226
  - CultureMech:004018
  - CultureMech:006403
  - CultureMech:006900
  - CultureMech:007843
  - CultureMech:008906
  - CultureMech:007092
  - CultureMech:006260
  - CultureMech:006262
  - CultureMech:006263
  - CultureMech:006264
  - CultureMech:002134
  - CultureMech:000718
  - CultureMech:007202
  - CultureMech:007076
  - CultureMech:007075
  - CultureMech:007070
  - CultureMech:007069
  - CultureMech:007072
  - CultureMech:007071
  - CultureMech:001884
- check_id: scientific-claims
  name: Independent source-family claim review
  status: passed
  required: true
  summary: Manual primary-source reading supports the bounded assertions and holds;
    gas supply is not liquid concentration, named mixture is not constituent identity,
    and alternative arms are not simultaneous.
  target_ids:
  - CultureMech:000025
  - CultureMech:000170
  - CultureMech:000233
  - CultureMech:015450
  - CultureMech:009166
  - CultureMech:000643
  - CultureMech:009226
  - CultureMech:004018
  - CultureMech:006403
  - CultureMech:006900
  - CultureMech:007843
  - CultureMech:008906
  - CultureMech:007092
  - CultureMech:006260
  - CultureMech:006262
  - CultureMech:006263
  - CultureMech:006264
  - CultureMech:002134
  - CultureMech:000718
  - CultureMech:007202
  - CultureMech:007076
  - CultureMech:007075
  - CultureMech:007070
  - CultureMech:007069
  - CultureMech:007072
  - CultureMech:007071
  - CultureMech:001884
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
evidence:
- evidence_id: '751'
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium751.pdf
  locator: Page 1 liquid-medium instruction
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: Official liquid-medium instruction supplies phosphate masses, not an explicit
    final litre. SET_AMOUNT correctly retains 1.5 g KH2PO4 and 0.5 g K2HPO4 per batch.
  snapshot_sha256: 721e0310d250ea6eab5d453f063b9452b48b8368ad53fa9384cb54434d2e59fb
- evidence_id: '670'
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium670.pdf
  locator: Page 1 base table and strain preparations
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: Current official base table supplies 950 mL water before separately described
    ferrous stock/strain amendments. This input is not a final-volume denominator
    or the older archive's one-litre input.
  snapshot_sha256: e21dbc3f7c16cf301001aaa5ca4ca7aa57fb486cbccba0995c46e094946917ab
- evidence_id: '125'
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium125.pdf
  locator: Page 1 carbon alternatives
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: Official instruction explicitly supplies 5 mL methanol or a methane-air
    atmosphere. The promoted amount preserves the methanol batch input without purity
    or final-volume assumptions.
  snapshot_sha256: e107edb0e43f303bc124e81ef0430f07fde07eb9efbcf1cea9c35e3a2190ad8f
- evidence_id: '956'
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium956.pdf
  locator: Page 1 post-sterilization alternatives
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: Official post-sterilization alternatives specify final 0.5 percent methanol
    or 0.3 percent methylamine. Basis remains unspecified; no v/v or mass concentration
    is invented.
  snapshot_sha256: 156fe7f9a826c658bf690c9c892ba7d137848d397f55cf93568c4c3145374f39
- evidence_id: '119'
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium119.pdf
  locator: Strain-specific post-inoculation gas instructions
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: Official DSM2030/9575 instructions specify 2 bar overpressure and DSM25939/25945
    specify 1 bar, after inoculation with 80:20 hydrogen/carbon dioxide. Events preserve
    strain, stage and gas context; no liquid dose is implied.
  snapshot_sha256: 65295918764de4ed5b73ce773ab4057a7183ecf8bfd7fff0d02393d901b41a2a
- evidence_id: hemiaulus
  kind: primary_source
  reference: PMID:33083143
  locator: 'Methods: naturally dissolved N2'
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: 'Methods explicitly describe naturally dissolved nitrogen in fixed-N-free
    cultures. A held operation is appropriate: source presence does not establish
    deliberate nitrogen addition or a named fixed-nitrogen removal.'
  snapshot_sha256: b2b891255be3531171e9479c4d8744724632f3b4e3f89573664273774d4f47e9
- evidence_id: fertilizer
  kind: primary_source
  reference: PMID:40484141
  locator: Primary abstract only
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: The primary abstract supports a named water-soluble fertilizer replacing
    TAP trace/macroelements. The named mixture input is defensible while exact product
    composition, dose and displaced chemicals remain held.
  snapshot_sha256: 3f738652b616e23152d9ce0740fc5f05ebabd63716e5a17cdc5482b56643d375
- evidence_id: teusink
  kind: primary_source
  reference: doi:10.1128/AEM.71.11.7253-7262.2005
  locator: Table 1 headings and footnotes
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: The source table's complete-formulation membership is not automatically
    converted into ingredient additions or removal operations. Existing discrete approved
    amounts are outside this follow-up assertion scope.
  snapshot_sha256: 3b4288d316e061cdad56879cb8a30c2cccff1fe3361eb0be71778d49c9dbef91
- evidence_id: tang
  kind: primary_source
  reference: doi:10.1002/btpr.227
  locator: Author manuscript page 4
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: Author manuscript page4 specifies the AA-S-18 supplement, 17 included amino
    acids at 25 micromolar each and three excluded amino acids. Named mixture input
    is supported. Exclusion from the supplement does not establish whole-culture absence
    or removal; exact DL forms are not inferred.
  snapshot_sha256: ebbab61739c7a8c63213c57e0258f20822d165ef8188e23455ff8495689eb4be
- evidence_id: pinchuk
  kind: primary_source
  reference: doi:10.1371/journal.pcbi.1000822
  locator: 'Methods: Bacterial Strains and Growth Media'
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: Methods explicitly name 10 mL each of two 10x stocks without a final-volume
    denominator. Literal inputs are retained, with stock-component correspondence
    to flattened parents held separately.
  snapshot_sha256: 9fc877d8ff8e5822a2abf7e00ef5395d11cba3da89281ba3c2038e1c14de6d81
- evidence_id: bg11
  kind: primary_source
  reference: PMID:34584038
  locator: 'Methods: phototrophic BG-11 gas supply'
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: Captured phototrophic Methods support alternative ambient-air/2-percent-CO2
    supplies at 0.5 vvm for ABC-009 in BG-11. This is distinct from the heterotrophic
    YM experiment; no gas fraction is encoded as a dissolved concentration.
  snapshot_sha256: 669d11703f04dc008905d7ac0b78c5963585ff556d92fb0229ae63323634a697
- evidence_id: matsui
  kind: primary_source
  reference: DOI:10.1104/pp.18.00453
  locator: 'Methods: culture conditions and transformation'
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: Culture Methods distinguish high-CO2 and ambient-air aeration arms. The
    gas identity/stage is represented without mixing alternative arms or inventing
    aqueous concentration.
  snapshot_sha256: beecd6db87651dbf5f4119169a755249ba977070ee4a7046d26dff3bab3b5d43
- evidence_id: kato
  kind: primary_source
  reference: doi:10.1264/jsme2.ME19128
  locator: 'Methods: cultivation of methanotrophs'
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: Methods assign default 20 micromolar metal treatments to the specified
    strain arms and separately describe methane gas per tube or 20 mM methanol. The
    methane amount is a two-mL gas input into one tube batch; metal hydration, standard-state
    gas volume and simultaneous carbon supplies are not invented.
  snapshot_sha256: 2ade9577ad927b568273334fa9b14d2da22d155f877535d317ad13a0977a224d
- evidence_id: kosch
  kind: primary_source
  reference: doi:10.5283/epub.34741
  locator: Printed pages27–28, sections2.2.2.1–2.2.2.2
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: Printed page28 distinguishes final 80:20 hydrogen/carbon-dioxide headspace
    exchange at 1.5 bar from the earlier nitrogen/carbon-dioxide purge and chamber
    gas. The proposed events preserve that final-headspace scope.
  snapshot_sha256: 21117464e1481e058031575f2bd668afd37677cd842636230adf54982111e8f9
- evidence_id: willard
  kind: primary_source
  reference: doi:10.1128/mbio.01033-24
  locator: 'Materials and Methods: low-sulfate Brock salts and species-specific pH'
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: Culture Methods supports elemental sulfur at 10 g/L, separate species groups
    receiving 1 or 0.2 g/L yeast extract, and the sucrose/NZ-Amine arm. Vented bottles
    do not independently prove a removal of the local parent's sulfide or nitrogen.
  snapshot_sha256: 7808bc365628f8d1a71ab0a20135f2f0619a19fc6db1d587961007e8c0ecaba3
- evidence_id: tsuji
  kind: primary_source
  reference: DOI:10.1007/s10126-021-10037-4
  locator: Primary abstract only
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: The publisher abstract directly contrasts supplied 5-percent and 0.04-percent
    carbon-dioxide air under low sodium; the lower-CO2 arm did not support growth.
    Both inputs can be recorded without a positive growth claim or invented full Methods.
    Browser inspection; no local capture hash claimed.
- evidence_id: marine
  kind: primary_source
  reference: doi:10.1099/ijs.0.012724-0
  locator: Primary paper page 2730
  accessed_at: '2026-11-16T23:59:09Z'
  support: supports
  summary: The primary-paper author copy, printed2730, states dilution of marine medium
    to half strength with water. The named diluent input is supported; an absolute
    water volume or complete constituent expansion is not inferred. Browser inspection;
    no local capture hash claimed.
assessments:
- assessment_id: model-CultureMech-000025
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:000025
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-000170
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:000170
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-000233
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:000233
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-015450
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:015450
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-009166
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:009166
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-000643
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:000643
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-009226
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:009226
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-004018
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:004018
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-006403
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:006403
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-006900
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:006900
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-007843
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:007843
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-008906
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:008906
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-007092
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:007092
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-006260
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:006260
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-006262
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:006262
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-006263
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:006263
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-006264
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:006264
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-002134
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:002134
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-000718
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:000718
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-007202
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:007202
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-007076
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:007076
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-007075
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:007075
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-007070
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:007070
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-007069
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:007069
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-007072
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:007072
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-007071
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:007071
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
- assessment_id: model-CultureMech-001884
  area: scope
  topic: Proposed model completion and quantity representation
  outcome: supported
  target_ids:
  - CultureMech:001884
  evidence_ids:
  - '751'
  - '670'
  - '125'
  - '956'
  - '119'
  - hemiaulus
  - fertilizer
  - teusink
  - tang
  - pinchuk
  - bg11
  - matsui
  - kato
  - kosch
  - willard
  - tsuji
  - marine
  summary: The enumerated proposal agrees with the source-family judgments and preserves
    uncertainty in separate held dimensions. Context-only dispositions add no invented
    ingredients.
findings: []
actions: []
limitations:
- Agent scientific review, not human approval or release approval.
- No recipes were mutated; native writer/export/schema gates remain separate.
- Tsuji evidence is the publisher abstract only; marine-paper text was inspected in
  an author copy. Neither browser-only source is assigned a fabricated capture hash.
- This review does not establish exact forms of unresolved salts/stocks, correspondence
  to flattened parents, or unreported final volumes.
- Gas events retain headspace/aeration stages; no liquid dose or physiological success
  is inferred.
- No-op record/variant envelopes may be omitted by the separate merger without changing
  these scientific decisions or disposition accounting.
links:
- https://github.com/CultureBotAI/CultureMech/issues/683
- https://github.com/CultureBotAI/CultureMech/issues/760
```
