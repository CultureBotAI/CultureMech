# Author source review of 98 Carini, Jensen, Pinchuk and Tang variant rows

- Review: 20261116T212534Z-four-variant-families-author
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-11-16T21:11:35Z
- Finished UTC: 2026-11-16T21:25:34Z
- Reviewer: codex-variant-family-author (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Reviewed primary Methods and table contexts for this exact 21-record proposal. Preserved 2013/2014 assay differences, isotope labels, source-stated hydrate forms, literal B-vitamin labels, stage boundaries and unsupported-conversion holds. No whole-medium equivalence, growth outcome or ontology identity is certified.

## Scope And Provenance

98 exact queue rows in Carini AMS1, Jensen BL, Pinchuk M1 and Tang tracer families; proposals only, no recipe application or whole-record certification.

Selection: Exact inventory membership of the four named planning groups; all 98 rows represented in proposal dispositions.
Coverage: partial; 21 reviewed / 21 in the declared population.
Source: working_tree at Git base 93d23e4415213bb92890db6f8330e18247ad2553.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007386 | data/normalized_yaml/bacterial/MEDIADB_479_AMS1_Pyruvate_Glycine.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Carini 2014 AMS1 phosphite utilization assay |
| CultureMech:007388 | data/normalized_yaml/bacterial/MEDIADB_480_AMS1_Pyruvate_Glycine.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Carini 2014 AMS1 glucose 6-phosphate utilization assay |
| CultureMech:007389 | data/normalized_yaml/bacterial/MEDIADB_481_AMS1_Pyruvate_Glycine.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Carini 2014 AMS1 ribose 5-phosphate utilization assay |
| CultureMech:007390 | data/normalized_yaml/bacterial/MEDIADB_482_AMS1_Pyruvate_Glycine.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Carini 2014 AMS1 methylphosphonic acid utilization assay |
| CultureMech:007391 | data/normalized_yaml/bacterial/MEDIADB_483_AMS1_Pyruvate_Glycine.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Carini 2014 AMS1 2-aminoethylphosphonic acid utilization assay |
| CultureMech:007392 | data/normalized_yaml/bacterial/MEDIADB_484_AMS1_Pyruvate_Glycine.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Carini 2014 AMS1 phosphoserine utilization assay |
| CultureMech:007382 | data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Carini 2013 AMS1 glycine substitution assay |
| CultureMech:007384 | data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Carini 2013 AMS1 serine substitution assay |
| CultureMech:007302 | data/normalized_yaml/bacterial/bl_medium.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Jensen 1993 BL Medium reported preparation |
| CultureMech:007303 | data/normalized_yaml/bacterial/bl_medium_arg.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Jensen 1993 BL Medium + Arg reported preparation |
| CultureMech:007306 | data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Jensen 1993 BL Medium + Arg + Ser + Trp reported preparation |
| CultureMech:007304 | data/normalized_yaml/bacterial/bl_medium_asp.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Jensen 1993 BL Medium + Asp reported preparation |
| CultureMech:007305 | data/normalized_yaml/bacterial/bl_medium_low_mops.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Jensen 1993 BL Medium, Low MOPS reported preparation |
| CultureMech:007070 | data/normalized_yaml/bacterial/modified_m1_medium_with_18_mm_lactate_pinchuk_et_al.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Pinchuk 2010 reported batch M1 with 18 mM lactate |
| CultureMech:007069 | data/normalized_yaml/bacterial/modified_m1_medium_with_20_mm_lactate_pinchuk_et_al.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Pinchuk 2010 reported batch M1 with 20 mM D,L-lactate |
| CultureMech:007072 | data/normalized_yaml/bacterial/modified_m1_medium_with_acetate_pinchuk_et_al.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Pinchuk 2010 reported batch M1 with acetate |
| CultureMech:007071 | data/normalized_yaml/bacterial/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Pinchuk 2010 reported batch M1 with lactate and glycine nitrogen |
| CultureMech:007073 | data/normalized_yaml/bacterial/minimal_medium_tang_et_al_2009.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Tang 2009 manuscript 20 mM PIPES tracer medium |
| CultureMech:007076 | data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_and_salt_stress_tang_et_al_2009.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Tang 2009 manuscript 20 mM PIPES tracer medium with salt and amino acids |
| CultureMech:007075 | data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_tang_et_al_2009.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Tang 2009 manuscript 20 mM PIPES tracer medium with amino acids |
| CultureMech:007074 | data/normalized_yaml/bacterial/minimal_medium_with_salt_stress_tang_et_al_2009.yaml # Existing inline variant modification rows and proposed ingredient_changes only | maintained | Tang 2009 manuscript 20 mM PIPES tracer medium with salt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native target/input inspection | passed | True | CultureMech:007386, CultureMech:007388, CultureMech:007389, CultureMech:007390, CultureMech:007391, CultureMech:007392, CultureMech:007382, CultureMech:007384, CultureMech:007302, CultureMech:007303, CultureMech:007306, CultureMech:007304, CultureMech:007305, CultureMech:007070, CultureMech:007069, CultureMech:007072, CultureMech:007071, CultureMech:007073, CultureMech:007076, CultureMech:007075, CultureMech:007074 | Native inspector captured exact recipe and proposal inputs; current recipe hashes still match proposal preimages. |
| Author reading of primary methods and source-form claims | passed | True | CultureMech:007386, CultureMech:007388, CultureMech:007389, CultureMech:007390, CultureMech:007391, CultureMech:007392, CultureMech:007382, CultureMech:007384, CultureMech:007302, CultureMech:007303, CultureMech:007306, CultureMech:007304, CultureMech:007305, CultureMech:007070, CultureMech:007069, CultureMech:007072, CultureMech:007071, CultureMech:007073, CultureMech:007076, CultureMech:007075, CultureMech:007074 | Read captured primary content; visually inspected Carini 2014 p.5 and Tang manuscript p.4. Jensen ASM PDF text inspected through browser; local hash unavailable. Exact source ambiguity is retained rather than resolved by inference. |
| Native guarded proposal preview | passed | True | CultureMech:007386, CultureMech:007388, CultureMech:007389, CultureMech:007390, CultureMech:007391, CultureMech:007392, CultureMech:007382, CultureMech:007384, CultureMech:007302, CultureMech:007303, CultureMech:007306, CultureMech:007304, CultureMech:007305, CultureMech:007070, CultureMech:007069, CultureMech:007072, CultureMech:007071, CultureMech:007073, CultureMech:007076, CultureMech:007075, CultureMech:007074 | 21 records planned without writes; exact source-text binding and native schema/semantic validation passed for the proposals. |

## Scientific And Domain Assessments

### CultureMech:007386 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007386.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: SET_CONCENTRATION Pyruvate 100 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Methionine 5 MICROMOLAR (old descriptor: DL-methionine); stage: 2014 alternate-phosphorus utilization assay &#124; SET_CONCENTRATION Glycine 5 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007386 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007386.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III) chloride); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007386 variants[0].modifications[2]

scope: supported. Targets: CultureMech:007386.

Partial: source-literal vitamin designations/doses structured; B7/biotin 4 nM already present and retained. Specific vitamers/salt forms remain unresolved; no B-number ontology identity assigned. Proposals: REPLACE B1 6 MICROMOLAR (old descriptor: Thiamine); stage: 2014 alternate-phosphorus utilization assay &#124; ADD B3 800 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B5 425 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B6 500 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B9 4 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B12 700 PICOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD Myo-inositol 6 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD 4-Aminobenzoic acid 60 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007386 variants[0].modifications[3]

scope: supported. Targets: CultureMech:007386.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium sulfate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Calcium chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride anhydrous); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Manganese chloride tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Zinc sulfate heptahydrate 800 PICOMOLAR (old descriptor: Zinc sulfate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Cobalt chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt chloride); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Sodium molybdate dihydrate 300 PICOMOLAR (old descriptor: Sodium molybdate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Nickel chloride hexahydrate 1 NANOMOLAR (old descriptor: Nickel chloride); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007386 variants[0].modifications[4]

scope: supported. Targets: CultureMech:007386.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REMOVE Sodium dihydrogen phosphate; stage: 2014 alternate-phosphorus assay base preparation

### CultureMech:007386 variants[0].modifications[5]

scope: concern. Targets: CultureMech:007386.

The source prints phosphite as NaPHO3.5H2O; its stoichiometry is unresolved. Literal formula and 1 µM dose remain in prose; no corrected salt identity is asserted. No new ingredient event proposed.

### CultureMech:007386 variants[0].modifications[6]

scope: supported. Targets: CultureMech:007386.

Preparation order, gas sparging and pH context retained as prose. No dissolved-gas dose or new positive ingredient is inferred. No new ingredient event proposed.

### CultureMech:007388 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007388.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: SET_CONCENTRATION Pyruvate 100 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Methionine 5 MICROMOLAR (old descriptor: DL-methionine); stage: 2014 alternate-phosphorus utilization assay &#124; SET_CONCENTRATION Glycine 5 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007388 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007388.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III) chloride); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007388 variants[0].modifications[2]

scope: supported. Targets: CultureMech:007388.

Partial: source-literal vitamin designations/doses structured; B7/biotin 4 nM already present and retained. Specific vitamers/salt forms remain unresolved; no B-number ontology identity assigned. Proposals: REPLACE B1 6 MICROMOLAR (old descriptor: Thiamine); stage: 2014 alternate-phosphorus utilization assay &#124; ADD B3 800 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B5 425 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B6 500 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B9 4 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B12 700 PICOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD Myo-inositol 6 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD 4-Aminobenzoic acid 60 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007388 variants[0].modifications[3]

scope: supported. Targets: CultureMech:007388.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium sulfate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Calcium chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride anhydrous); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Manganese chloride tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Zinc sulfate heptahydrate 800 PICOMOLAR (old descriptor: Zinc sulfate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Cobalt chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt chloride); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Sodium molybdate dihydrate 300 PICOMOLAR (old descriptor: Sodium molybdate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Nickel chloride hexahydrate 1 NANOMOLAR (old descriptor: Nickel chloride); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007388 variants[0].modifications[4]

scope: supported. Targets: CultureMech:007388.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REMOVE Sodium dihydrogen phosphate; stage: 2014 alternate-phosphorus assay base preparation

### CultureMech:007388 variants[0].modifications[5]

scope: supported. Targets: CultureMech:007388.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Glucose 6-phosphate 1.0 MICROMOLAR (old descriptor: D-Glucose 6-phosphate); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007388 variants[0].modifications[6]

scope: supported. Targets: CultureMech:007388.

Preparation order, gas sparging and pH context retained as prose. No dissolved-gas dose or new positive ingredient is inferred. No new ingredient event proposed.

### CultureMech:007389 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007389.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: SET_CONCENTRATION Pyruvate 100 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Methionine 5 MICROMOLAR (old descriptor: DL-methionine); stage: 2014 alternate-phosphorus utilization assay &#124; SET_CONCENTRATION Glycine 5 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007389 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007389.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III) chloride); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007389 variants[0].modifications[2]

scope: supported. Targets: CultureMech:007389.

Partial: source-literal vitamin designations/doses structured; B7/biotin 4 nM already present and retained. Specific vitamers/salt forms remain unresolved; no B-number ontology identity assigned. Proposals: REPLACE B1 6 MICROMOLAR (old descriptor: Thiamine); stage: 2014 alternate-phosphorus utilization assay &#124; ADD B3 800 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B5 425 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B6 500 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B9 4 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B12 700 PICOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD Myo-inositol 6 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD 4-Aminobenzoic acid 60 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007389 variants[0].modifications[3]

scope: supported. Targets: CultureMech:007389.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium sulfate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Calcium chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride anhydrous); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Manganese chloride tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Zinc sulfate heptahydrate 800 PICOMOLAR (old descriptor: Zinc sulfate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Cobalt chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt chloride); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Sodium molybdate dihydrate 300 PICOMOLAR (old descriptor: Sodium molybdate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Nickel chloride hexahydrate 1 NANOMOLAR (old descriptor: Nickel chloride); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007389 variants[0].modifications[4]

scope: supported. Targets: CultureMech:007389.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REMOVE Sodium dihydrogen phosphate; stage: 2014 alternate-phosphorus assay base preparation

### CultureMech:007389 variants[0].modifications[5]

scope: supported. Targets: CultureMech:007389.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Ribose 5-phosphate 1.0 MICROMOLAR (old descriptor: D-Ribose 5-phosphate); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007389 variants[0].modifications[6]

scope: supported. Targets: CultureMech:007389.

Preparation order, gas sparging and pH context retained as prose. No dissolved-gas dose or new positive ingredient is inferred. No new ingredient event proposed.

### CultureMech:007390 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007390.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: SET_CONCENTRATION Pyruvate 100 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Methionine 5 MICROMOLAR (old descriptor: DL-methionine); stage: 2014 alternate-phosphorus utilization assay &#124; SET_CONCENTRATION Glycine 5 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007390 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007390.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III) chloride); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007390 variants[0].modifications[2]

scope: supported. Targets: CultureMech:007390.

Partial: source-literal vitamin designations/doses structured; B7/biotin 4 nM already present and retained. Specific vitamers/salt forms remain unresolved; no B-number ontology identity assigned. Proposals: REPLACE B1 6 MICROMOLAR (old descriptor: Thiamine); stage: 2014 alternate-phosphorus utilization assay &#124; ADD B3 800 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B5 425 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B6 500 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B9 4 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B12 700 PICOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD Myo-inositol 6 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD 4-Aminobenzoic acid 60 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007390 variants[0].modifications[3]

scope: supported. Targets: CultureMech:007390.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium sulfate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Calcium chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride anhydrous); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Manganese chloride tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Zinc sulfate heptahydrate 800 PICOMOLAR (old descriptor: Zinc sulfate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Cobalt chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt chloride); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Sodium molybdate dihydrate 300 PICOMOLAR (old descriptor: Sodium molybdate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Nickel chloride hexahydrate 1 NANOMOLAR (old descriptor: Nickel chloride); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007390 variants[0].modifications[4]

scope: supported. Targets: CultureMech:007390.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REMOVE Sodium dihydrogen phosphate; stage: 2014 alternate-phosphorus assay base preparation

### CultureMech:007390 variants[0].modifications[5]

scope: supported. Targets: CultureMech:007390.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: SET_CONCENTRATION Methylphosphonic acid 1.0 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007390 variants[0].modifications[6]

scope: supported. Targets: CultureMech:007390.

Preparation order, gas sparging and pH context retained as prose. No dissolved-gas dose or new positive ingredient is inferred. No new ingredient event proposed.

### CultureMech:007391 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007391.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: SET_CONCENTRATION Pyruvate 100 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Methionine 5 MICROMOLAR (old descriptor: DL-methionine); stage: 2014 alternate-phosphorus utilization assay &#124; SET_CONCENTRATION Glycine 5 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007391 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007391.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III) chloride); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007391 variants[0].modifications[2]

scope: supported. Targets: CultureMech:007391.

Partial: source-literal vitamin designations/doses structured; B7/biotin 4 nM already present and retained. Specific vitamers/salt forms remain unresolved; no B-number ontology identity assigned. Proposals: REPLACE B1 6 MICROMOLAR (old descriptor: Thiamine); stage: 2014 alternate-phosphorus utilization assay &#124; ADD B3 800 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B5 425 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B6 500 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B9 4 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B12 700 PICOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD Myo-inositol 6 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD 4-Aminobenzoic acid 60 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007391 variants[0].modifications[3]

scope: supported. Targets: CultureMech:007391.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium sulfate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Calcium chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride anhydrous); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Manganese chloride tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Zinc sulfate heptahydrate 800 PICOMOLAR (old descriptor: Zinc sulfate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Cobalt chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt chloride); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Sodium molybdate dihydrate 300 PICOMOLAR (old descriptor: Sodium molybdate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Nickel chloride hexahydrate 1 NANOMOLAR (old descriptor: Nickel chloride); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007391 variants[0].modifications[4]

scope: supported. Targets: CultureMech:007391.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REMOVE Sodium dihydrogen phosphate; stage: 2014 alternate-phosphorus assay base preparation

### CultureMech:007391 variants[0].modifications[5]

scope: supported. Targets: CultureMech:007391.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE 2-aminoethylphosphonic acid 1.0 MICROMOLAR (old descriptor: 2-Aminoethylphosphonate); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007391 variants[0].modifications[6]

scope: supported. Targets: CultureMech:007391.

Preparation order, gas sparging and pH context retained as prose. No dissolved-gas dose or new positive ingredient is inferred. No new ingredient event proposed.

### CultureMech:007392 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007392.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: SET_CONCENTRATION Pyruvate 100 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Methionine 5 MICROMOLAR (old descriptor: DL-methionine); stage: 2014 alternate-phosphorus utilization assay &#124; SET_CONCENTRATION Glycine 5 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007392 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007392.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III) chloride); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007392 variants[0].modifications[2]

scope: supported. Targets: CultureMech:007392.

Partial: source-literal vitamin designations/doses structured; B7/biotin 4 nM already present and retained. Specific vitamers/salt forms remain unresolved; no B-number ontology identity assigned. Proposals: REPLACE B1 6 MICROMOLAR (old descriptor: Thiamine); stage: 2014 alternate-phosphorus utilization assay &#124; ADD B3 800 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B5 425 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B6 500 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B9 4 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD B12 700 PICOMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD Myo-inositol 6 MICROMOLAR; stage: 2014 alternate-phosphorus utilization assay &#124; ADD 4-Aminobenzoic acid 60 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007392 variants[0].modifications[3]

scope: supported. Targets: CultureMech:007392.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium sulfate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Calcium chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride anhydrous); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Manganese chloride tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Zinc sulfate heptahydrate 800 PICOMOLAR (old descriptor: Zinc sulfate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Cobalt chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt chloride); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Sodium molybdate dihydrate 300 PICOMOLAR (old descriptor: Sodium molybdate); stage: 2014 alternate-phosphorus utilization assay &#124; REPLACE Nickel chloride hexahydrate 1 NANOMOLAR (old descriptor: Nickel chloride); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007392 variants[0].modifications[4]

scope: supported. Targets: CultureMech:007392.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REMOVE Sodium dihydrogen phosphate; stage: 2014 alternate-phosphorus assay base preparation

### CultureMech:007392 variants[0].modifications[5]

scope: supported. Targets: CultureMech:007392.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Phosphoserine 1.0 MICROMOLAR (old descriptor: O-Phospho-L-serine); stage: 2014 alternate-phosphorus utilization assay

### CultureMech:007392 variants[0].modifications[6]

scope: supported. Targets: CultureMech:007392.

Preparation order, gas sparging and pH context retained as prose. No dissolved-gas dose or new positive ingredient is inferred. No new ingredient event proposed.

### CultureMech:007382 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007382.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: SET_CONCENTRATION Pyruvate 50 MICROMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; REPLACE Methionine 10 MICROMOLAR (old descriptor: DL-methionine); stage: 2013 Table 3 glycine-substitution assay

### CultureMech:007382 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007382.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: SET_CONCENTRATION Glycine 25 MICROMOLAR; stage: 2013 Table 3 glycine-substitution assay

### CultureMech:007382 variants[0].modifications[2]

scope: supported. Targets: CultureMech:007382.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium sulfate); stage: 2013 Table 3 glycine-substitution assay

### CultureMech:007382 variants[0].modifications[3]

scope: supported. Targets: CultureMech:007382.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Calcium chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride anhydrous); stage: 2013 Table 3 glycine-substitution assay &#124; REPLACE Manganese chloride tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage: 2013 Table 3 glycine-substitution assay &#124; REPLACE Zinc sulfate heptahydrate 800 PICOMOLAR (old descriptor: Zinc sulfate); stage: 2013 Table 3 glycine-substitution assay &#124; REPLACE Cobalt chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt chloride); stage: 2013 Table 3 glycine-substitution assay &#124; REPLACE Sodium molybdate dihydrate 300 PICOMOLAR (old descriptor: Sodium molybdate); stage: 2013 Table 3 glycine-substitution assay &#124; REPLACE Nickel chloride hexahydrate 1 NANOMOLAR (old descriptor: Nickel chloride); stage: 2013 Table 3 glycine-substitution assay

### CultureMech:007382 variants[0].modifications[4]

scope: supported. Targets: CultureMech:007382.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III) chloride); stage: 2013 Table 3 glycine-substitution assay

### CultureMech:007382 variants[0].modifications[5]

scope: supported. Targets: CultureMech:007382.

Partial: source-literal vitamin designations/doses structured; B7/biotin 4 nM already present and retained. Specific vitamers/salt forms remain unresolved; no B-number ontology identity assigned. Proposals: ADD B1 6 MICROMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; ADD B3 800 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; ADD B5 425 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; ADD B6 500 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; ADD B9 4 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; ADD B12 700 PICOMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; ADD Myo-inositol 6 MICROMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; ADD 4-Aminobenzoic acid 60 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; REMOVE 4-Amino-5-hydroxymethyl-2-methylpyrimidine; stage: 2013 Table 3 glycine-substitution assay

### CultureMech:007382 variants[0].modifications[6]

scope: supported. Targets: CultureMech:007382.

Preparation order, gas sparging and pH context retained as prose. No dissolved-gas dose or new positive ingredient is inferred. No new ingredient event proposed.

### CultureMech:007384 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007384.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: SET_CONCENTRATION Pyruvate 50 MICROMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; REPLACE Methionine 10 MICROMOLAR (old descriptor: DL-methionine); stage: 2013 Table 3 glycine-substitution assay

### CultureMech:007384 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007384.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Serine 25 MICROMOLAR (old descriptor: L-Serine); stage: 2013 Table 3 glycine-substitution assay

### CultureMech:007384 variants[0].modifications[2]

scope: supported. Targets: CultureMech:007384.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium sulfate); stage: 2013 Table 3 glycine-substitution assay

### CultureMech:007384 variants[0].modifications[3]

scope: supported. Targets: CultureMech:007384.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Calcium chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride anhydrous); stage: 2013 Table 3 glycine-substitution assay &#124; REPLACE Manganese chloride tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage: 2013 Table 3 glycine-substitution assay &#124; REPLACE Zinc sulfate heptahydrate 800 PICOMOLAR (old descriptor: Zinc sulfate); stage: 2013 Table 3 glycine-substitution assay &#124; REPLACE Cobalt chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt chloride); stage: 2013 Table 3 glycine-substitution assay &#124; REPLACE Sodium molybdate dihydrate 300 PICOMOLAR (old descriptor: Sodium molybdate); stage: 2013 Table 3 glycine-substitution assay &#124; REPLACE Nickel chloride hexahydrate 1 NANOMOLAR (old descriptor: Nickel chloride); stage: 2013 Table 3 glycine-substitution assay

### CultureMech:007384 variants[0].modifications[4]

scope: supported. Targets: CultureMech:007384.

Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment. Proposals: REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III) chloride); stage: 2013 Table 3 glycine-substitution assay

### CultureMech:007384 variants[0].modifications[5]

scope: supported. Targets: CultureMech:007384.

Partial: source-literal vitamin designations/doses structured; B7/biotin 4 nM already present and retained. Specific vitamers/salt forms remain unresolved; no B-number ontology identity assigned. Proposals: ADD B1 6 MICROMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; ADD B3 800 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; ADD B5 425 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; ADD B6 500 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; ADD B9 4 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; ADD B12 700 PICOMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; ADD Myo-inositol 6 MICROMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; ADD 4-Aminobenzoic acid 60 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay &#124; REMOVE 4-Amino-5-hydroxymethyl-2-methylpyrimidine; stage: 2013 Table 3 glycine-substitution assay

### CultureMech:007384 variants[0].modifications[6]

scope: supported. Targets: CultureMech:007384.

Preparation order, gas sparging and pH context retained as prose. No dissolved-gas dose or new positive ingredient is inferred. No new ingredient event proposed.

### CultureMech:007302 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007302.

Stock filtration pore size/order is preparation context, not an ingredient occurrence. No new ingredient event proposed.

### CultureMech:007302 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007302.

Calcium salt identity retained without converting pantothenate-basis amount to salt molarity. Proposals: REPLACE Calcium pantothenate (old descriptor: Pantothenate); stage: BL medium vitamin-stock preparation

### CultureMech:007302 variants[0].modifications[2]

scope: concern. Targets: CultureMech:007302.

Nominal formulation retained; MgCl2 hydration and molybdate formula/hydration remain unresolved. No imported hydrate is certified. No new ingredient event proposed.

### CultureMech:007302 variants[0].modifications[3]

scope: supported. Targets: CultureMech:007302.

Existing treatment ingredient/dose retained; this row adds Table 3 context rather than a new variant ingredient. No growth claim revalidated. No new ingredient event proposed.

### CultureMech:007303 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007303.

Stock filtration pore size/order is preparation context, not an ingredient occurrence. No new ingredient event proposed.

### CultureMech:007303 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007303.

Calcium salt identity retained without converting pantothenate-basis amount to salt molarity. Proposals: REPLACE Calcium pantothenate (old descriptor: Pantothenate); stage: BL medium vitamin-stock preparation

### CultureMech:007303 variants[0].modifications[2]

scope: concern. Targets: CultureMech:007303.

Nominal formulation retained; MgCl2 hydration and molybdate formula/hydration remain unresolved. No imported hydrate is certified. No new ingredient event proposed.

### CultureMech:007303 variants[0].modifications[3]

scope: supported. Targets: CultureMech:007303.

Existing treatment ingredient/dose retained; this row adds Table 3 context rather than a new variant ingredient. No growth claim revalidated. No new ingredient event proposed.

### CultureMech:007306 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007306.

Stock filtration pore size/order is preparation context, not an ingredient occurrence. No new ingredient event proposed.

### CultureMech:007306 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007306.

Calcium salt identity retained without converting pantothenate-basis amount to salt molarity. Proposals: REPLACE Calcium pantothenate (old descriptor: Pantothenate); stage: BL medium vitamin-stock preparation

### CultureMech:007306 variants[0].modifications[2]

scope: concern. Targets: CultureMech:007306.

Nominal formulation retained; MgCl2 hydration and molybdate formula/hydration remain unresolved. No imported hydrate is certified. No new ingredient event proposed.

### CultureMech:007306 variants[0].modifications[3]

scope: supported. Targets: CultureMech:007306.

Existing treatment ingredient/dose retained; this row adds Table 3 context rather than a new variant ingredient. No growth claim revalidated. No new ingredient event proposed.

### CultureMech:007304 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007304.

Stock filtration pore size/order is preparation context, not an ingredient occurrence. No new ingredient event proposed.

### CultureMech:007304 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007304.

Calcium salt identity retained without converting pantothenate-basis amount to salt molarity. Proposals: REPLACE Calcium pantothenate (old descriptor: Pantothenate); stage: BL medium vitamin-stock preparation

### CultureMech:007304 variants[0].modifications[2]

scope: concern. Targets: CultureMech:007304.

Nominal formulation retained; MgCl2 hydration and molybdate formula/hydration remain unresolved. No imported hydrate is certified. No new ingredient event proposed.

### CultureMech:007304 variants[0].modifications[3]

scope: supported. Targets: CultureMech:007304.

Existing treatment ingredient/dose retained; this row adds Table 3 context rather than a new variant ingredient. No growth claim revalidated. No new ingredient event proposed.

### CultureMech:007305 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007305.

Stock filtration pore size/order is preparation context, not an ingredient occurrence. No new ingredient event proposed.

### CultureMech:007305 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007305.

Calcium salt identity retained without converting pantothenate-basis amount to salt molarity. Proposals: REPLACE Calcium pantothenate (old descriptor: Pantothenate); stage: BL medium vitamin-stock preparation

### CultureMech:007305 variants[0].modifications[2]

scope: concern. Targets: CultureMech:007305.

Nominal formulation retained; MgCl2 hydration and molybdate formula/hydration remain unresolved. No imported hydrate is certified. No new ingredient event proposed.

### CultureMech:007305 variants[0].modifications[3]

scope: supported. Targets: CultureMech:007305.

Existing treatment ingredient/dose retained; this row adds Table 3 context rather than a new variant ingredient. No growth claim revalidated. No new ingredient event proposed.

### CultureMech:007073 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007073.

Literal study buffer concentration; no base mutation. Proposals: SET_CONCENTRATION PIPES 20 MILLIMOLAR; stage: isotope-tracer growth assay

### CultureMech:007073 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007073.

Labeled substrate kept distinct from imported unlabeled sodium L-lactate. Proposals: REPLACE [3-13C] sodium L-lactate 30 MILLIMOLAR (old descriptor: Sodium L-lactate); stage: isotope-tracer growth assay

### CultureMech:007076 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007076.

Literal study buffer concentration; no base mutation. Proposals: SET_CONCENTRATION PIPES 20 MILLIMOLAR; stage: isotope-tracer growth assay

### CultureMech:007076 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007076.

Labeled substrate kept distinct from imported unlabeled sodium L-lactate. Proposals: REPLACE [3-13C] sodium L-lactate 30 MILLIMOLAR (old descriptor: Sodium L-lactate); stage: isotope-tracer growth assay

### CultureMech:007076 variants[0].modifications[2]

scope: concern. Targets: CultureMech:007076.

AA-S-18 is a 17-component mixture at 25 µM each, not 25 µM mixture. Exact correspondence to flattened imported amino acids (including DL forms) remains unresolved; no duplicate mixture/individual presence or unsupported stereochemistry is asserted. No new ingredient event proposed.

### CultureMech:007075 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007075.

Literal study buffer concentration; no base mutation. Proposals: SET_CONCENTRATION PIPES 20 MILLIMOLAR; stage: isotope-tracer growth assay

### CultureMech:007075 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007075.

Labeled substrate kept distinct from imported unlabeled sodium L-lactate. Proposals: REPLACE [3-13C] sodium L-lactate 30 MILLIMOLAR (old descriptor: Sodium L-lactate); stage: isotope-tracer growth assay

### CultureMech:007075 variants[0].modifications[2]

scope: concern. Targets: CultureMech:007075.

AA-S-18 is a 17-component mixture at 25 µM each, not 25 µM mixture. Exact correspondence to flattened imported amino acids (including DL forms) remains unresolved; no duplicate mixture/individual presence or unsupported stereochemistry is asserted. No new ingredient event proposed.

### CultureMech:007074 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007074.

Literal study buffer concentration; no base mutation. Proposals: SET_CONCENTRATION PIPES 20 MILLIMOLAR; stage: isotope-tracer growth assay

### CultureMech:007074 variants[0].modifications[1]

scope: supported. Targets: CultureMech:007074.

Labeled substrate kept distinct from imported unlabeled sodium L-lactate. Proposals: REPLACE [3-13C] sodium L-lactate 30 MILLIMOLAR (old descriptor: Sodium L-lactate); stage: isotope-tracer growth assay

### CultureMech:007070 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007070.

Explicit phosphate-form replacement; no parent recipe equivalence inferred. Proposals: REPLACE Sodium dihydrogen phosphate monohydrate 4.35 MILLIMOLAR (old descriptor: Dibasic sodium phosphate); stage: modified M1 batch culture

### CultureMech:007070 variants[0].modifications[1]

scope: concern. Targets: CultureMech:007070.

Source names 10× Wolfe vitamin/mineral stock additions; correspondence to the parent's flattened stock components and final-volume basis are unresolved. Do not add stock components twice or invent individual replacements. No new ingredient event proposed.

### CultureMech:007070 variants[0].modifications[2]

scope: supported. Targets: CultureMech:007070.

Batch PIPES 30 mM already present; pH and exclusion of chemostat/anaerobic treatments remain context. No chemostat Fe(III)-NTA or fumarate added. No new ingredient event proposed.

### CultureMech:007069 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007069.

Explicit phosphate-form replacement; no parent recipe equivalence inferred. Proposals: REPLACE Sodium dihydrogen phosphate monohydrate 4.35 MILLIMOLAR (old descriptor: Dibasic sodium phosphate); stage: modified M1 batch culture

### CultureMech:007069 variants[0].modifications[1]

scope: concern. Targets: CultureMech:007069.

Source names 10× Wolfe vitamin/mineral stock additions; correspondence to the parent's flattened stock components and final-volume basis are unresolved. Do not add stock components twice or invent individual replacements. No new ingredient event proposed.

### CultureMech:007069 variants[0].modifications[2]

scope: supported. Targets: CultureMech:007069.

Batch PIPES 30 mM already present; pH and exclusion of chemostat/anaerobic treatments remain context. No chemostat Fe(III)-NTA or fumarate added. No new ingredient event proposed.

### CultureMech:007072 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007072.

Explicit phosphate-form replacement; no parent recipe equivalence inferred. Proposals: REPLACE Sodium dihydrogen phosphate monohydrate 4.35 MILLIMOLAR (old descriptor: Dibasic sodium phosphate); stage: modified M1 batch culture

### CultureMech:007072 variants[0].modifications[1]

scope: concern. Targets: CultureMech:007072.

Source names 10× Wolfe vitamin/mineral stock additions; correspondence to the parent's flattened stock components and final-volume basis are unresolved. Do not add stock components twice or invent individual replacements. No new ingredient event proposed.

### CultureMech:007072 variants[0].modifications[2]

scope: supported. Targets: CultureMech:007072.

Batch PIPES 30 mM already present; pH and exclusion of chemostat/anaerobic treatments remain context. No chemostat Fe(III)-NTA or fumarate added. No new ingredient event proposed.

### CultureMech:007071 variants[0].modifications[0]

scope: supported. Targets: CultureMech:007071.

Explicit phosphate-form replacement; no parent recipe equivalence inferred. Proposals: REPLACE Sodium dihydrogen phosphate monohydrate 4.35 MILLIMOLAR (old descriptor: Dibasic sodium phosphate); stage: modified M1 batch culture

### CultureMech:007071 variants[0].modifications[1]

scope: concern. Targets: CultureMech:007071.

Source names 10× Wolfe vitamin/mineral stock additions; correspondence to the parent's flattened stock components and final-volume basis are unresolved. Do not add stock components twice or invent individual replacements. No new ingredient event proposed.

### CultureMech:007071 variants[0].modifications[2]

scope: supported. Targets: CultureMech:007071.

Batch PIPES 30 mM already present; pH and exclusion of chemostat/anaerobic treatments remain context. No chemostat Fe(III)-NTA or fumarate added. No new ingredient event proposed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| proposal | conf/variant_ingredient_curation/carini-jensen-pinchuk-tang-683.json; records ingredient_changes and all 98 dispositions | supports | Exact source-bound proposals with per-event names, actions, concentration units/basis, stage, old descriptors and source evidence; unresolved rows explicitly held. |
| primary-1 | doi:10.1038/ismej.2012.122; Methods and explicitly cited formulation tables; per-event evidence locators in proposal | supports | Primary content read for the explicit variant-only claims. Capture bytes and extraction receipt retained; chemical identities are not established by retrieval. |
| primary-2 | doi:10.1038/ncomms5346; Methods and explicitly cited formulation tables; per-event evidence locators in proposal | supports | Primary content read for the explicit variant-only claims. Capture bytes and extraction receipt retained; chemical identities are not established by retrieval. |
| primary-3 | doi:10.1371/journal.pcbi.1000822; Methods and explicitly cited formulation tables; per-event evidence locators in proposal | supports | Primary content read for the explicit variant-only claims. Capture bytes and extraction receipt retained; chemical identities are not established by retrieval. |
| primary-4 | doi:10.1002/btpr.227; Methods and explicitly cited formulation tables; per-event evidence locators in proposal | supports | Primary content read for the explicit variant-only claims. Capture bytes and extraction receipt retained; chemical identities are not established by retrieval. |
| primary-5 | doi:10.1128/aem.59.12.4363-4366.1993; pp.4363–4364, formulation paragraph, Table 1 footnote b, Table 3 | supports | Primary content read for the explicit variant-only claims. Primary PDF text inspected with browser tool; anonymous local downloads failed (403/500). No local source hash available. |

## Limits And Additional Notes

- Author review is not independent or human approval. No recipe was changed by this agent.
- B-number vitamins remain source-level labels with molecular/salt forms unresolved; generic methionine, serine and P-substrate labels do not certify imported stereoisomers.
- Held rows preserve uncertain phosphite stoichiometry, Jensen hydration/form questions, Wolfe stock correspondence and Tang 17-amino-acid mixture correspondence. These are not claims of absent ingredients.
- Jensen primary PDF has no retained local byte hash because anonymous downloads failed; browser text was inspected. Tang evidence is the OSTI-hosted manuscript version, whose page includes author edits.
- The source-specific negative phosphate event refers to original AMS1 Table 1 phosphate, not a claim that each imported parent contains phosphate or that residual phosphate is zero.
- Independent proposal review, central guarded application, post-application export accounting and release gates remain separate.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261116T212534Z-four-variant-families-author
kind: batch
repository: CultureBotAI/CultureMech
title: Author source review of 98 Carini, Jensen, Pinchuk and Tang variant rows
started_at: '2026-11-16T21:11:35Z'
finished_at: '2026-11-16T21:25:34Z'
reviewer:
  identity: codex-variant-family-author
  kind: agent
  independence: self_review
  independence_basis: The reviewer authored these proposals and the schema extension.
    This is an explicitly non-independent scientific author check; a separate reviewer
    must clear application.
skill: curate-yaml-record; review-ingredient-concentrations
completion: completed
verdict: needs_curation
native_verdict: 182 supported source-scoped events proposed; 98 row dispositions complete,
  with unresolved stock/mixture/form gaps retained. Independent review and application
  remain pending.
scientific_review: true
summary: Reviewed primary Methods and table contexts for this exact 21-record proposal.
  Preserved 2013/2014 assay differences, isotope labels, source-stated hydrate forms,
  literal B-vitamin labels, stage boundaries and unsupported-conversion holds. No
  whole-medium equivalence, growth outcome or ontology identity is certified.
source:
  git_revision: 93d23e4415213bb92890db6f8330e18247ad2553
  state: working_tree
  inputs:
  - path: data/normalized_yaml/bacterial/MEDIADB_479_AMS1_Pyruvate_Glycine.yaml
    sha256: da931f52a98d91ce90d5e81fd7ab5c68b0429278aa54f5631a5cf0cc87ea2ffd
    role: target
  - path: data/normalized_yaml/bacterial/MEDIADB_480_AMS1_Pyruvate_Glycine.yaml
    sha256: ea2b2acbd4c5d5549d930245ba0cb2c545bf53554228ba94b4464bef3b84aa0b
    role: target
  - path: data/normalized_yaml/bacterial/MEDIADB_481_AMS1_Pyruvate_Glycine.yaml
    sha256: aac6fa08f14b416af16cb2cf810830d7446581c01639b826baa15928b1eb621f
    role: target
  - path: data/normalized_yaml/bacterial/MEDIADB_482_AMS1_Pyruvate_Glycine.yaml
    sha256: f04fe7a26b3483185ef244d7a24c15ed72fe462bbd7a5024daac020d36822798
    role: target
  - path: data/normalized_yaml/bacterial/MEDIADB_483_AMS1_Pyruvate_Glycine.yaml
    sha256: 829718162c5f7f6129504c441c77d2afc3a8803a9cdba98256be669fac12f785
    role: target
  - path: data/normalized_yaml/bacterial/MEDIADB_484_AMS1_Pyruvate_Glycine.yaml
    sha256: 6f4f90d434df33b85f84ad80f13ee35921c3dd1be9ded5bc88696af1ef730969
    role: target
  - path: data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml
    sha256: 2f3755a57cf3a1daa6ff1adb12467300d5149beec89cc04f93f50bfc9d796fdb
    role: target
  - path: data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml
    sha256: 1033a43ff2f5dc484bdc5f8592a6baffb401bb68e317e2d1b09da88e55834833
    role: target
  - path: data/normalized_yaml/bacterial/bl_medium.yaml
    sha256: e6c916970fe767115371333f5bc6e991b0f9d3b8e87cd6b99fbfb7155ebab71f
    role: target
  - path: data/normalized_yaml/bacterial/bl_medium_arg.yaml
    sha256: 7f25e7cb2791204fa39e95d5b8aebf81e07e8325e157f877e7026aa2f4a87808
    role: target
  - path: data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml
    sha256: 5383545a363dac9dc71abe20ca9a72b21bc206dbc73482cd32dead149efeb9f1
    role: target
  - path: data/normalized_yaml/bacterial/bl_medium_asp.yaml
    sha256: bf326dd778e325fa6f4da70fc6ca77b5810bd1cda09bfedfca2f8d24fb647d50
    role: target
  - path: data/normalized_yaml/bacterial/bl_medium_low_mops.yaml
    sha256: c234e3095aa45e99b3f921352b46e01f1091df9c574b53f45b8e5279f6ded863
    role: target
  - path: data/normalized_yaml/bacterial/modified_m1_medium_with_18_mm_lactate_pinchuk_et_al.yaml
    sha256: 337e8e001897e6c07ee61195728641cae74af4be7d7047e151b92236ca888030
    role: target
  - path: data/normalized_yaml/bacterial/modified_m1_medium_with_20_mm_lactate_pinchuk_et_al.yaml
    sha256: cb5594d8ff5643116cc9af48087ae48fc0d2ce3724b0a44eb0707ecff0405990
    role: target
  - path: data/normalized_yaml/bacterial/modified_m1_medium_with_acetate_pinchuk_et_al.yaml
    sha256: 43bbe710acde1f13649466e138ddede7095ed1ab6b82ac28ea45dfdaea1c9732
    role: target
  - path: data/normalized_yaml/bacterial/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml
    sha256: 3aa1f6350de52f946239892c4cc133cd61ed8c147ef04f59c10138b6b4b39de7
    role: target
  - path: data/normalized_yaml/bacterial/minimal_medium_tang_et_al_2009.yaml
    sha256: e237bf46588511f92c3d2be2936a339cbebe8ff637e9b8090b1ea33cb7a30181
    role: target
  - path: data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_and_salt_stress_tang_et_al_2009.yaml
    sha256: 525b234085271da5df8e15c5100c9d06fa9f69b86481841b7a235e5c715fc7cf
    role: target
  - path: data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_tang_et_al_2009.yaml
    sha256: d34a088fc64f1ee54530be887d8624819ba19d0f38c85cdb31dc26db0c5e2a28
    role: target
  - path: data/normalized_yaml/bacterial/minimal_medium_with_salt_stress_tang_et_al_2009.yaml
    sha256: 965e35a934eb1c8146481a51974f0294024d5176dbeab66bc4e7d328e8b834e1
    role: target
  - path: conf/variant_ingredient_curation/carini-jensen-pinchuk-tang-683.json
    sha256: 786ae063209accd3c3ad1e67bd2043e0ff0a4e94703e6b5d8a55b0d073d1b32c
    role: author proposal
  - path: .temp/variant-683/family-sources/native-inspection-postcheckpoint.json
    sha256: c89539760c33c14678d50e503759b92e8ac1c99d32108b89748cd33fd15d554d
    role: native target inspection
  - path: .temp/variant-683/family-sources/four-families-preview-v1.json
    sha256: 9980f1fec6943b94ac4ee509f54f519de0a68282d2bb44074d91a6f0957845eb
    role: native guarded preview
  - path: .temp/variant-683/family-sources/carini-2013-html/source.html
    sha256: b9fa5f44ed26edc1d3323374ba097fbc17c10510893d36703f9328983c77c2d1
    role: primary source
  - path: .temp/variant-683/family-sources/carini-2014/source.pdf
    sha256: f20160ac5dc3840b1fb757178b876f0bd41f34fe6cb2be1aec2928d28dbf667e
    role: primary source
  - path: .temp/variant-683/family-sources/pinchuk-2010/source.xml
    sha256: 9fc877d8ff8e5822a2abf7e00ef5395d11cba3da89281ba3c2038e1c14de6d81
    role: primary source
  - path: .temp/variant-683/family-sources/tang-2009/source.pdf
    sha256: ebbab61739c7a8c63213c57e0258f20822d165ef8188e23455ff8495689eb4be
    role: primary source
scope:
  description: 98 exact queue rows in Carini AMS1, Jensen BL, Pinchuk M1 and Tang
    tracer families; proposals only, no recipe application or whole-record certification.
  selection: Exact inventory membership of the four named planning groups; all 98
    rows represented in proposal dispositions.
  coverage: partial
  population_size: 21
  reviewed_target_ids:
  - CultureMech:007386
  - CultureMech:007388
  - CultureMech:007389
  - CultureMech:007390
  - CultureMech:007391
  - CultureMech:007392
  - CultureMech:007382
  - CultureMech:007384
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007306
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007070
  - CultureMech:007069
  - CultureMech:007072
  - CultureMech:007071
  - CultureMech:007073
  - CultureMech:007076
  - CultureMech:007075
  - CultureMech:007074
  exclusions:
  - target: Base ingredients, global growth/taxonomy and unrelated record content
    reason: Read as context; not comprehensively revalidated or scientifically recertified.
  - target: Remaining queue families and MIM/KGM mapping release
    reason: Outside this source-family review.
targets:
- target_id: CultureMech:007386
  path: data/normalized_yaml/bacterial/MEDIADB_479_AMS1_Pyruvate_Glycine.yaml
  label: Carini 2014 AMS1 phosphite utilization assay
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/MEDIADB_479_AMS1_Pyruvate_Glycine.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007388
  path: data/normalized_yaml/bacterial/MEDIADB_480_AMS1_Pyruvate_Glycine.yaml
  label: Carini 2014 AMS1 glucose 6-phosphate utilization assay
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/MEDIADB_480_AMS1_Pyruvate_Glycine.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007389
  path: data/normalized_yaml/bacterial/MEDIADB_481_AMS1_Pyruvate_Glycine.yaml
  label: Carini 2014 AMS1 ribose 5-phosphate utilization assay
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/MEDIADB_481_AMS1_Pyruvate_Glycine.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007390
  path: data/normalized_yaml/bacterial/MEDIADB_482_AMS1_Pyruvate_Glycine.yaml
  label: Carini 2014 AMS1 methylphosphonic acid utilization assay
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/MEDIADB_482_AMS1_Pyruvate_Glycine.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007391
  path: data/normalized_yaml/bacterial/MEDIADB_483_AMS1_Pyruvate_Glycine.yaml
  label: Carini 2014 AMS1 2-aminoethylphosphonic acid utilization assay
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/MEDIADB_483_AMS1_Pyruvate_Glycine.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007392
  path: data/normalized_yaml/bacterial/MEDIADB_484_AMS1_Pyruvate_Glycine.yaml
  label: Carini 2014 AMS1 phosphoserine utilization assay
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/MEDIADB_484_AMS1_Pyruvate_Glycine.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007382
  path: data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml
  label: Carini 2013 AMS1 glycine substitution assay
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007384
  path: data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml
  label: Carini 2013 AMS1 serine substitution assay
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007302
  path: data/normalized_yaml/bacterial/bl_medium.yaml
  label: Jensen 1993 BL Medium reported preparation
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bl_medium.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007303
  path: data/normalized_yaml/bacterial/bl_medium_arg.yaml
  label: Jensen 1993 BL Medium + Arg reported preparation
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bl_medium_arg.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007306
  path: data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml
  label: Jensen 1993 BL Medium + Arg + Ser + Trp reported preparation
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007304
  path: data/normalized_yaml/bacterial/bl_medium_asp.yaml
  label: Jensen 1993 BL Medium + Asp reported preparation
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bl_medium_asp.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007305
  path: data/normalized_yaml/bacterial/bl_medium_low_mops.yaml
  label: Jensen 1993 BL Medium, Low MOPS reported preparation
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bl_medium_low_mops.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007070
  path: data/normalized_yaml/bacterial/modified_m1_medium_with_18_mm_lactate_pinchuk_et_al.yaml
  label: Pinchuk 2010 reported batch M1 with 18 mM lactate
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_m1_medium_with_18_mm_lactate_pinchuk_et_al.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007069
  path: data/normalized_yaml/bacterial/modified_m1_medium_with_20_mm_lactate_pinchuk_et_al.yaml
  label: Pinchuk 2010 reported batch M1 with 20 mM D,L-lactate
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_m1_medium_with_20_mm_lactate_pinchuk_et_al.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007072
  path: data/normalized_yaml/bacterial/modified_m1_medium_with_acetate_pinchuk_et_al.yaml
  label: Pinchuk 2010 reported batch M1 with acetate
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_m1_medium_with_acetate_pinchuk_et_al.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007071
  path: data/normalized_yaml/bacterial/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml
  label: Pinchuk 2010 reported batch M1 with lactate and glycine nitrogen
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007073
  path: data/normalized_yaml/bacterial/minimal_medium_tang_et_al_2009.yaml
  label: Tang 2009 manuscript 20 mM PIPES tracer medium
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/minimal_medium_tang_et_al_2009.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007076
  path: data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_and_salt_stress_tang_et_al_2009.yaml
  label: Tang 2009 manuscript 20 mM PIPES tracer medium with salt and amino acids
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_and_salt_stress_tang_et_al_2009.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007075
  path: data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_tang_et_al_2009.yaml
  label: Tang 2009 manuscript 20 mM PIPES tracer medium with amino acids
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/minimal_medium_w_amino_acids_tang_et_al_2009.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007074
  path: data/normalized_yaml/bacterial/minimal_medium_with_salt_stress_tang_et_al_2009.yaml
  label: Tang 2009 manuscript 20 mM PIPES tracer medium with salt
  kind: maintained
  record_class: MediaRecipe
  selector: Existing inline variant modification rows and proposed ingredient_changes
    only
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/minimal_medium_with_salt_stress_tang_et_al_2009.yaml
    role: authoritative normalized recipe
checks:
- check_id: native-inspect
  name: Native target/input inspection
  status: passed
  required: true
  summary: Native inspector captured exact recipe and proposal inputs; current recipe
    hashes still match proposal preimages.
  target_ids:
  - CultureMech:007386
  - CultureMech:007388
  - CultureMech:007389
  - CultureMech:007390
  - CultureMech:007391
  - CultureMech:007392
  - CultureMech:007382
  - CultureMech:007384
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007306
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007070
  - CultureMech:007069
  - CultureMech:007072
  - CultureMech:007071
  - CultureMech:007073
  - CultureMech:007076
  - CultureMech:007075
  - CultureMech:007074
  evidence_ids:
  - proposal
- check_id: primary-claims
  name: Author reading of primary methods and source-form claims
  status: passed
  required: true
  summary: Read captured primary content; visually inspected Carini 2014 p.5 and Tang
    manuscript p.4. Jensen ASM PDF text inspected through browser; local hash unavailable.
    Exact source ambiguity is retained rather than resolved by inference.
  target_ids:
  - CultureMech:007386
  - CultureMech:007388
  - CultureMech:007389
  - CultureMech:007390
  - CultureMech:007391
  - CultureMech:007392
  - CultureMech:007382
  - CultureMech:007384
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007306
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007070
  - CultureMech:007069
  - CultureMech:007072
  - CultureMech:007071
  - CultureMech:007073
  - CultureMech:007076
  - CultureMech:007075
  - CultureMech:007074
  evidence_ids:
  - primary-1
  - primary-2
  - primary-3
  - primary-4
  - primary-5
- check_id: guarded-preview
  name: Native guarded proposal preview
  status: passed
  required: true
  summary: 21 records planned without writes; exact source-text binding and native
    schema/semantic validation passed for the proposals.
  target_ids:
  - CultureMech:007386
  - CultureMech:007388
  - CultureMech:007389
  - CultureMech:007390
  - CultureMech:007391
  - CultureMech:007392
  - CultureMech:007382
  - CultureMech:007384
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007306
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007070
  - CultureMech:007069
  - CultureMech:007072
  - CultureMech:007071
  - CultureMech:007073
  - CultureMech:007076
  - CultureMech:007075
  - CultureMech:007074
  command: .venv/bin/python scripts/curate_variant_ingredients.py conf/variant_ingredient_curation/carini-jensen-pinchuk-tang-683.json
    --receipt .temp/variant-683/family-sources/four-families-preview-v1.json
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - proposal
evidence:
- evidence_id: proposal
  kind: record_content
  reference: conf/variant_ingredient_curation/carini-jensen-pinchuk-tang-683.json
  locator: records ingredient_changes and all 98 dispositions
  accessed_at: '2026-11-16T21:25:34Z'
  support: supports
  summary: Exact source-bound proposals with per-event names, actions, concentration
    units/basis, stage, old descriptors and source evidence; unresolved rows explicitly
    held.
  snapshot_sha256: 786ae063209accd3c3ad1e67bd2043e0ff0a4e94703e6b5d8a55b0d073d1b32c
- evidence_id: primary-1
  kind: primary_source
  reference: doi:10.1038/ismej.2012.122
  locator: Methods and explicitly cited formulation tables; per-event evidence locators
    in proposal
  accessed_at: '2026-11-16T21:14:10.894520Z'
  support: supports
  summary: Primary content read for the explicit variant-only claims. Capture bytes
    and extraction receipt retained; chemical identities are not established by retrieval.
  snapshot_sha256: b9fa5f44ed26edc1d3323374ba097fbc17c10510893d36703f9328983c77c2d1
- evidence_id: primary-2
  kind: primary_source
  reference: doi:10.1038/ncomms5346
  locator: Methods and explicitly cited formulation tables; per-event evidence locators
    in proposal
  accessed_at: '2026-11-16T21:12:33.547333Z'
  support: supports
  summary: Primary content read for the explicit variant-only claims. Capture bytes
    and extraction receipt retained; chemical identities are not established by retrieval.
  snapshot_sha256: f20160ac5dc3840b1fb757178b876f0bd41f34fe6cb2be1aec2928d28dbf667e
- evidence_id: primary-3
  kind: primary_source
  reference: doi:10.1371/journal.pcbi.1000822
  locator: Methods and explicitly cited formulation tables; per-event evidence locators
    in proposal
  accessed_at: '2026-11-16T21:11:35.871596Z'
  support: supports
  summary: Primary content read for the explicit variant-only claims. Capture bytes
    and extraction receipt retained; chemical identities are not established by retrieval.
  snapshot_sha256: 9fc877d8ff8e5822a2abf7e00ef5395d11cba3da89281ba3c2038e1c14de6d81
- evidence_id: primary-4
  kind: primary_source
  reference: doi:10.1002/btpr.227
  locator: Methods and explicitly cited formulation tables; per-event evidence locators
    in proposal
  accessed_at: '2026-11-16T21:12:00.724377Z'
  support: supports
  summary: Primary content read for the explicit variant-only claims. Capture bytes
    and extraction receipt retained; chemical identities are not established by retrieval.
  snapshot_sha256: ebbab61739c7a8c63213c57e0258f20822d165ef8188e23455ff8495689eb4be
- evidence_id: primary-5
  kind: primary_source
  reference: doi:10.1128/aem.59.12.4363-4366.1993
  locator: pp.4363–4364, formulation paragraph, Table 1 footnote b, Table 3
  accessed_at: '2026-11-16T21:25:34Z'
  support: supports
  summary: Primary content read for the explicit variant-only claims. Primary PDF
    text inspected with browser tool; anonymous local downloads failed (403/500).
    No local source hash available.
assessments:
- assessment_id: queue-row-146
  area: scope
  topic: CultureMech:007386 variants[0].modifications[0]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    SET_CONCENTRATION Pyruvate 100 MICROMOLAR; stage: 2014 alternate-phosphorus utilization
    assay | REPLACE Methionine 5 MICROMOLAR (old descriptor: DL-methionine); stage:
    2014 alternate-phosphorus utilization assay | SET_CONCENTRATION Glycine 5 MICROMOLAR;
    stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007386
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-147
  area: scope
  topic: CultureMech:007386 variants[0].modifications[1]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III)
    chloride); stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007386
  evidence_ids:
  - proposal
  - primary-1
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-148
  area: scope
  topic: CultureMech:007386 variants[0].modifications[2]
  outcome: supported
  summary: 'Partial: source-literal vitamin designations/doses structured; B7/biotin
    4 nM already present and retained. Specific vitamers/salt forms remain unresolved;
    no B-number ontology identity assigned. Proposals: REPLACE B1 6 MICROMOLAR (old
    descriptor: Thiamine); stage: 2014 alternate-phosphorus utilization assay | ADD
    B3 800 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B5
    425 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B6 500
    NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B9 4 NANOMOLAR;
    stage: 2014 alternate-phosphorus utilization assay | ADD B12 700 PICOMOLAR; stage:
    2014 alternate-phosphorus utilization assay | ADD Myo-inositol 6 MICROMOLAR; stage:
    2014 alternate-phosphorus utilization assay | ADD 4-Aminobenzoic acid 60 NANOMOLAR;
    stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007386
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-149
  area: scope
  topic: CultureMech:007386 variants[0].modifications[3]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium
    sulfate); stage: 2014 alternate-phosphorus utilization assay | REPLACE Calcium
    chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride anhydrous);
    stage: 2014 alternate-phosphorus utilization assay | REPLACE Manganese chloride
    tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage: 2014 alternate-phosphorus
    utilization assay | REPLACE Zinc sulfate heptahydrate 800 PICOMOLAR (old descriptor:
    Zinc sulfate); stage: 2014 alternate-phosphorus utilization assay | REPLACE Cobalt
    chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt chloride); stage: 2014
    alternate-phosphorus utilization assay | REPLACE Sodium molybdate dihydrate 300
    PICOMOLAR (old descriptor: Sodium molybdate); stage: 2014 alternate-phosphorus
    utilization assay | REPLACE Nickel chloride hexahydrate 1 NANOMOLAR (old descriptor:
    Nickel chloride); stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007386
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-150
  area: scope
  topic: CultureMech:007386 variants[0].modifications[4]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REMOVE Sodium dihydrogen phosphate; stage: 2014 alternate-phosphorus assay base
    preparation'
  target_ids:
  - CultureMech:007386
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-151
  area: scope
  topic: CultureMech:007386 variants[0].modifications[5]
  outcome: concern
  summary: The source prints phosphite as NaPHO3.5H2O; its stoichiometry is unresolved.
    Literal formula and 1 µM dose remain in prose; no corrected salt identity is asserted.
    No new ingredient event proposed.
  target_ids:
  - CultureMech:007386
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: unsupported
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: HELD_EVIDENCE
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-152
  area: scope
  topic: CultureMech:007386 variants[0].modifications[6]
  outcome: supported
  summary: Preparation order, gas sparging and pH context retained as prose. No dissolved-gas
    dose or new positive ingredient is inferred. No new ingredient event proposed.
  target_ids:
  - CultureMech:007386
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: CONDITION_ONLY
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-153
  area: scope
  topic: CultureMech:007388 variants[0].modifications[0]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    SET_CONCENTRATION Pyruvate 100 MICROMOLAR; stage: 2014 alternate-phosphorus utilization
    assay | REPLACE Methionine 5 MICROMOLAR (old descriptor: DL-methionine); stage:
    2014 alternate-phosphorus utilization assay | SET_CONCENTRATION Glycine 5 MICROMOLAR;
    stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007388
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-154
  area: scope
  topic: CultureMech:007388 variants[0].modifications[1]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III)
    chloride); stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007388
  evidence_ids:
  - proposal
  - primary-1
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-155
  area: scope
  topic: CultureMech:007388 variants[0].modifications[2]
  outcome: supported
  summary: 'Partial: source-literal vitamin designations/doses structured; B7/biotin
    4 nM already present and retained. Specific vitamers/salt forms remain unresolved;
    no B-number ontology identity assigned. Proposals: REPLACE B1 6 MICROMOLAR (old
    descriptor: Thiamine); stage: 2014 alternate-phosphorus utilization assay | ADD
    B3 800 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B5
    425 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B6 500
    NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B9 4 NANOMOLAR;
    stage: 2014 alternate-phosphorus utilization assay | ADD B12 700 PICOMOLAR; stage:
    2014 alternate-phosphorus utilization assay | ADD Myo-inositol 6 MICROMOLAR; stage:
    2014 alternate-phosphorus utilization assay | ADD 4-Aminobenzoic acid 60 NANOMOLAR;
    stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007388
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-156
  area: scope
  topic: CultureMech:007388 variants[0].modifications[3]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium
    sulfate); stage: 2014 alternate-phosphorus utilization assay | REPLACE Calcium
    chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride anhydrous);
    stage: 2014 alternate-phosphorus utilization assay | REPLACE Manganese chloride
    tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage: 2014 alternate-phosphorus
    utilization assay | REPLACE Zinc sulfate heptahydrate 800 PICOMOLAR (old descriptor:
    Zinc sulfate); stage: 2014 alternate-phosphorus utilization assay | REPLACE Cobalt
    chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt chloride); stage: 2014
    alternate-phosphorus utilization assay | REPLACE Sodium molybdate dihydrate 300
    PICOMOLAR (old descriptor: Sodium molybdate); stage: 2014 alternate-phosphorus
    utilization assay | REPLACE Nickel chloride hexahydrate 1 NANOMOLAR (old descriptor:
    Nickel chloride); stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007388
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-157
  area: scope
  topic: CultureMech:007388 variants[0].modifications[4]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REMOVE Sodium dihydrogen phosphate; stage: 2014 alternate-phosphorus assay base
    preparation'
  target_ids:
  - CultureMech:007388
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-158
  area: scope
  topic: CultureMech:007388 variants[0].modifications[5]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Glucose 6-phosphate 1.0 MICROMOLAR (old descriptor: D-Glucose 6-phosphate);
    stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007388
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-159
  area: scope
  topic: CultureMech:007388 variants[0].modifications[6]
  outcome: supported
  summary: Preparation order, gas sparging and pH context retained as prose. No dissolved-gas
    dose or new positive ingredient is inferred. No new ingredient event proposed.
  target_ids:
  - CultureMech:007388
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: CONDITION_ONLY
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-160
  area: scope
  topic: CultureMech:007389 variants[0].modifications[0]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    SET_CONCENTRATION Pyruvate 100 MICROMOLAR; stage: 2014 alternate-phosphorus utilization
    assay | REPLACE Methionine 5 MICROMOLAR (old descriptor: DL-methionine); stage:
    2014 alternate-phosphorus utilization assay | SET_CONCENTRATION Glycine 5 MICROMOLAR;
    stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007389
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-161
  area: scope
  topic: CultureMech:007389 variants[0].modifications[1]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III)
    chloride); stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007389
  evidence_ids:
  - proposal
  - primary-1
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-162
  area: scope
  topic: CultureMech:007389 variants[0].modifications[2]
  outcome: supported
  summary: 'Partial: source-literal vitamin designations/doses structured; B7/biotin
    4 nM already present and retained. Specific vitamers/salt forms remain unresolved;
    no B-number ontology identity assigned. Proposals: REPLACE B1 6 MICROMOLAR (old
    descriptor: Thiamine); stage: 2014 alternate-phosphorus utilization assay | ADD
    B3 800 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B5
    425 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B6 500
    NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B9 4 NANOMOLAR;
    stage: 2014 alternate-phosphorus utilization assay | ADD B12 700 PICOMOLAR; stage:
    2014 alternate-phosphorus utilization assay | ADD Myo-inositol 6 MICROMOLAR; stage:
    2014 alternate-phosphorus utilization assay | ADD 4-Aminobenzoic acid 60 NANOMOLAR;
    stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007389
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-163
  area: scope
  topic: CultureMech:007389 variants[0].modifications[3]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium
    sulfate); stage: 2014 alternate-phosphorus utilization assay | REPLACE Calcium
    chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride anhydrous);
    stage: 2014 alternate-phosphorus utilization assay | REPLACE Manganese chloride
    tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage: 2014 alternate-phosphorus
    utilization assay | REPLACE Zinc sulfate heptahydrate 800 PICOMOLAR (old descriptor:
    Zinc sulfate); stage: 2014 alternate-phosphorus utilization assay | REPLACE Cobalt
    chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt chloride); stage: 2014
    alternate-phosphorus utilization assay | REPLACE Sodium molybdate dihydrate 300
    PICOMOLAR (old descriptor: Sodium molybdate); stage: 2014 alternate-phosphorus
    utilization assay | REPLACE Nickel chloride hexahydrate 1 NANOMOLAR (old descriptor:
    Nickel chloride); stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007389
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-164
  area: scope
  topic: CultureMech:007389 variants[0].modifications[4]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REMOVE Sodium dihydrogen phosphate; stage: 2014 alternate-phosphorus assay base
    preparation'
  target_ids:
  - CultureMech:007389
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-165
  area: scope
  topic: CultureMech:007389 variants[0].modifications[5]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Ribose 5-phosphate 1.0 MICROMOLAR (old descriptor: D-Ribose 5-phosphate);
    stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007389
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-166
  area: scope
  topic: CultureMech:007389 variants[0].modifications[6]
  outcome: supported
  summary: Preparation order, gas sparging and pH context retained as prose. No dissolved-gas
    dose or new positive ingredient is inferred. No new ingredient event proposed.
  target_ids:
  - CultureMech:007389
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: CONDITION_ONLY
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-167
  area: scope
  topic: CultureMech:007390 variants[0].modifications[0]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    SET_CONCENTRATION Pyruvate 100 MICROMOLAR; stage: 2014 alternate-phosphorus utilization
    assay | REPLACE Methionine 5 MICROMOLAR (old descriptor: DL-methionine); stage:
    2014 alternate-phosphorus utilization assay | SET_CONCENTRATION Glycine 5 MICROMOLAR;
    stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007390
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-168
  area: scope
  topic: CultureMech:007390 variants[0].modifications[1]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III)
    chloride); stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007390
  evidence_ids:
  - proposal
  - primary-1
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-169
  area: scope
  topic: CultureMech:007390 variants[0].modifications[2]
  outcome: supported
  summary: 'Partial: source-literal vitamin designations/doses structured; B7/biotin
    4 nM already present and retained. Specific vitamers/salt forms remain unresolved;
    no B-number ontology identity assigned. Proposals: REPLACE B1 6 MICROMOLAR (old
    descriptor: Thiamine); stage: 2014 alternate-phosphorus utilization assay | ADD
    B3 800 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B5
    425 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B6 500
    NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B9 4 NANOMOLAR;
    stage: 2014 alternate-phosphorus utilization assay | ADD B12 700 PICOMOLAR; stage:
    2014 alternate-phosphorus utilization assay | ADD Myo-inositol 6 MICROMOLAR; stage:
    2014 alternate-phosphorus utilization assay | ADD 4-Aminobenzoic acid 60 NANOMOLAR;
    stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007390
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-170
  area: scope
  topic: CultureMech:007390 variants[0].modifications[3]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium
    sulfate); stage: 2014 alternate-phosphorus utilization assay | REPLACE Calcium
    chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride anhydrous);
    stage: 2014 alternate-phosphorus utilization assay | REPLACE Manganese chloride
    tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage: 2014 alternate-phosphorus
    utilization assay | REPLACE Zinc sulfate heptahydrate 800 PICOMOLAR (old descriptor:
    Zinc sulfate); stage: 2014 alternate-phosphorus utilization assay | REPLACE Cobalt
    chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt chloride); stage: 2014
    alternate-phosphorus utilization assay | REPLACE Sodium molybdate dihydrate 300
    PICOMOLAR (old descriptor: Sodium molybdate); stage: 2014 alternate-phosphorus
    utilization assay | REPLACE Nickel chloride hexahydrate 1 NANOMOLAR (old descriptor:
    Nickel chloride); stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007390
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-171
  area: scope
  topic: CultureMech:007390 variants[0].modifications[4]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REMOVE Sodium dihydrogen phosphate; stage: 2014 alternate-phosphorus assay base
    preparation'
  target_ids:
  - CultureMech:007390
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-172
  area: scope
  topic: CultureMech:007390 variants[0].modifications[5]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    SET_CONCENTRATION Methylphosphonic acid 1.0 MICROMOLAR; stage: 2014 alternate-phosphorus
    utilization assay'
  target_ids:
  - CultureMech:007390
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-173
  area: scope
  topic: CultureMech:007390 variants[0].modifications[6]
  outcome: supported
  summary: Preparation order, gas sparging and pH context retained as prose. No dissolved-gas
    dose or new positive ingredient is inferred. No new ingredient event proposed.
  target_ids:
  - CultureMech:007390
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: CONDITION_ONLY
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-174
  area: scope
  topic: CultureMech:007391 variants[0].modifications[0]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    SET_CONCENTRATION Pyruvate 100 MICROMOLAR; stage: 2014 alternate-phosphorus utilization
    assay | REPLACE Methionine 5 MICROMOLAR (old descriptor: DL-methionine); stage:
    2014 alternate-phosphorus utilization assay | SET_CONCENTRATION Glycine 5 MICROMOLAR;
    stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007391
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-175
  area: scope
  topic: CultureMech:007391 variants[0].modifications[1]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III)
    chloride); stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007391
  evidence_ids:
  - proposal
  - primary-1
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-176
  area: scope
  topic: CultureMech:007391 variants[0].modifications[2]
  outcome: supported
  summary: 'Partial: source-literal vitamin designations/doses structured; B7/biotin
    4 nM already present and retained. Specific vitamers/salt forms remain unresolved;
    no B-number ontology identity assigned. Proposals: REPLACE B1 6 MICROMOLAR (old
    descriptor: Thiamine); stage: 2014 alternate-phosphorus utilization assay | ADD
    B3 800 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B5
    425 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B6 500
    NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B9 4 NANOMOLAR;
    stage: 2014 alternate-phosphorus utilization assay | ADD B12 700 PICOMOLAR; stage:
    2014 alternate-phosphorus utilization assay | ADD Myo-inositol 6 MICROMOLAR; stage:
    2014 alternate-phosphorus utilization assay | ADD 4-Aminobenzoic acid 60 NANOMOLAR;
    stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007391
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-177
  area: scope
  topic: CultureMech:007391 variants[0].modifications[3]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium
    sulfate); stage: 2014 alternate-phosphorus utilization assay | REPLACE Calcium
    chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride anhydrous);
    stage: 2014 alternate-phosphorus utilization assay | REPLACE Manganese chloride
    tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage: 2014 alternate-phosphorus
    utilization assay | REPLACE Zinc sulfate heptahydrate 800 PICOMOLAR (old descriptor:
    Zinc sulfate); stage: 2014 alternate-phosphorus utilization assay | REPLACE Cobalt
    chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt chloride); stage: 2014
    alternate-phosphorus utilization assay | REPLACE Sodium molybdate dihydrate 300
    PICOMOLAR (old descriptor: Sodium molybdate); stage: 2014 alternate-phosphorus
    utilization assay | REPLACE Nickel chloride hexahydrate 1 NANOMOLAR (old descriptor:
    Nickel chloride); stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007391
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-178
  area: scope
  topic: CultureMech:007391 variants[0].modifications[4]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REMOVE Sodium dihydrogen phosphate; stage: 2014 alternate-phosphorus assay base
    preparation'
  target_ids:
  - CultureMech:007391
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-179
  area: scope
  topic: CultureMech:007391 variants[0].modifications[5]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE 2-aminoethylphosphonic acid 1.0 MICROMOLAR (old descriptor: 2-Aminoethylphosphonate);
    stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007391
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-180
  area: scope
  topic: CultureMech:007391 variants[0].modifications[6]
  outcome: supported
  summary: Preparation order, gas sparging and pH context retained as prose. No dissolved-gas
    dose or new positive ingredient is inferred. No new ingredient event proposed.
  target_ids:
  - CultureMech:007391
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: CONDITION_ONLY
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-181
  area: scope
  topic: CultureMech:007392 variants[0].modifications[0]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    SET_CONCENTRATION Pyruvate 100 MICROMOLAR; stage: 2014 alternate-phosphorus utilization
    assay | REPLACE Methionine 5 MICROMOLAR (old descriptor: DL-methionine); stage:
    2014 alternate-phosphorus utilization assay | SET_CONCENTRATION Glycine 5 MICROMOLAR;
    stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007392
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-182
  area: scope
  topic: CultureMech:007392 variants[0].modifications[1]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III)
    chloride); stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007392
  evidence_ids:
  - proposal
  - primary-1
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-183
  area: scope
  topic: CultureMech:007392 variants[0].modifications[2]
  outcome: supported
  summary: 'Partial: source-literal vitamin designations/doses structured; B7/biotin
    4 nM already present and retained. Specific vitamers/salt forms remain unresolved;
    no B-number ontology identity assigned. Proposals: REPLACE B1 6 MICROMOLAR (old
    descriptor: Thiamine); stage: 2014 alternate-phosphorus utilization assay | ADD
    B3 800 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B5
    425 NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B6 500
    NANOMOLAR; stage: 2014 alternate-phosphorus utilization assay | ADD B9 4 NANOMOLAR;
    stage: 2014 alternate-phosphorus utilization assay | ADD B12 700 PICOMOLAR; stage:
    2014 alternate-phosphorus utilization assay | ADD Myo-inositol 6 MICROMOLAR; stage:
    2014 alternate-phosphorus utilization assay | ADD 4-Aminobenzoic acid 60 NANOMOLAR;
    stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007392
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-184
  area: scope
  topic: CultureMech:007392 variants[0].modifications[3]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium
    sulfate); stage: 2014 alternate-phosphorus utilization assay | REPLACE Calcium
    chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride anhydrous);
    stage: 2014 alternate-phosphorus utilization assay | REPLACE Manganese chloride
    tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage: 2014 alternate-phosphorus
    utilization assay | REPLACE Zinc sulfate heptahydrate 800 PICOMOLAR (old descriptor:
    Zinc sulfate); stage: 2014 alternate-phosphorus utilization assay | REPLACE Cobalt
    chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt chloride); stage: 2014
    alternate-phosphorus utilization assay | REPLACE Sodium molybdate dihydrate 300
    PICOMOLAR (old descriptor: Sodium molybdate); stage: 2014 alternate-phosphorus
    utilization assay | REPLACE Nickel chloride hexahydrate 1 NANOMOLAR (old descriptor:
    Nickel chloride); stage: 2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007392
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-185
  area: scope
  topic: CultureMech:007392 variants[0].modifications[4]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REMOVE Sodium dihydrogen phosphate; stage: 2014 alternate-phosphorus assay base
    preparation'
  target_ids:
  - CultureMech:007392
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-186
  area: scope
  topic: CultureMech:007392 variants[0].modifications[5]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Phosphoserine 1.0 MICROMOLAR (old descriptor: O-Phospho-L-serine); stage:
    2014 alternate-phosphorus utilization assay'
  target_ids:
  - CultureMech:007392
  evidence_ids:
  - proposal
  - primary-2
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-2
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-187
  area: scope
  topic: CultureMech:007392 variants[0].modifications[6]
  outcome: supported
  summary: Preparation order, gas sparging and pH context retained as prose. No dissolved-gas
    dose or new positive ingredient is inferred. No new ingredient event proposed.
  target_ids:
  - CultureMech:007392
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: CONDITION_ONLY
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-204
  area: scope
  topic: CultureMech:007382 variants[0].modifications[0]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    SET_CONCENTRATION Pyruvate 50 MICROMOLAR; stage: 2013 Table 3 glycine-substitution
    assay | REPLACE Methionine 10 MICROMOLAR (old descriptor: DL-methionine); stage:
    2013 Table 3 glycine-substitution assay'
  target_ids:
  - CultureMech:007382
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-205
  area: scope
  topic: CultureMech:007382 variants[0].modifications[1]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    SET_CONCENTRATION Glycine 25 MICROMOLAR; stage: 2013 Table 3 glycine-substitution
    assay'
  target_ids:
  - CultureMech:007382
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-206
  area: scope
  topic: CultureMech:007382 variants[0].modifications[2]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium
    sulfate); stage: 2013 Table 3 glycine-substitution assay'
  target_ids:
  - CultureMech:007382
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-207
  area: scope
  topic: CultureMech:007382 variants[0].modifications[3]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Calcium chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride
    anhydrous); stage: 2013 Table 3 glycine-substitution assay | REPLACE Manganese
    chloride tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage:
    2013 Table 3 glycine-substitution assay | REPLACE Zinc sulfate heptahydrate 800
    PICOMOLAR (old descriptor: Zinc sulfate); stage: 2013 Table 3 glycine-substitution
    assay | REPLACE Cobalt chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt
    chloride); stage: 2013 Table 3 glycine-substitution assay | REPLACE Sodium molybdate
    dihydrate 300 PICOMOLAR (old descriptor: Sodium molybdate); stage: 2013 Table
    3 glycine-substitution assay | REPLACE Nickel chloride hexahydrate 1 NANOMOLAR
    (old descriptor: Nickel chloride); stage: 2013 Table 3 glycine-substitution assay'
  target_ids:
  - CultureMech:007382
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-208
  area: scope
  topic: CultureMech:007382 variants[0].modifications[4]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III)
    chloride); stage: 2013 Table 3 glycine-substitution assay'
  target_ids:
  - CultureMech:007382
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-209
  area: scope
  topic: CultureMech:007382 variants[0].modifications[5]
  outcome: supported
  summary: 'Partial: source-literal vitamin designations/doses structured; B7/biotin
    4 nM already present and retained. Specific vitamers/salt forms remain unresolved;
    no B-number ontology identity assigned. Proposals: ADD B1 6 MICROMOLAR; stage:
    2013 Table 3 glycine-substitution assay | ADD B3 800 NANOMOLAR; stage: 2013 Table
    3 glycine-substitution assay | ADD B5 425 NANOMOLAR; stage: 2013 Table 3 glycine-substitution
    assay | ADD B6 500 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay |
    ADD B9 4 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay | ADD B12 700
    PICOMOLAR; stage: 2013 Table 3 glycine-substitution assay | ADD Myo-inositol 6
    MICROMOLAR; stage: 2013 Table 3 glycine-substitution assay | ADD 4-Aminobenzoic
    acid 60 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay | REMOVE 4-Amino-5-hydroxymethyl-2-methylpyrimidine;
    stage: 2013 Table 3 glycine-substitution assay'
  target_ids:
  - CultureMech:007382
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-210
  area: scope
  topic: CultureMech:007382 variants[0].modifications[6]
  outcome: supported
  summary: Preparation order, gas sparging and pH context retained as prose. No dissolved-gas
    dose or new positive ingredient is inferred. No new ingredient event proposed.
  target_ids:
  - CultureMech:007382
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: CONDITION_ONLY
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-211
  area: scope
  topic: CultureMech:007384 variants[0].modifications[0]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    SET_CONCENTRATION Pyruvate 50 MICROMOLAR; stage: 2013 Table 3 glycine-substitution
    assay | REPLACE Methionine 10 MICROMOLAR (old descriptor: DL-methionine); stage:
    2013 Table 3 glycine-substitution assay'
  target_ids:
  - CultureMech:007384
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-212
  area: scope
  topic: CultureMech:007384 variants[0].modifications[1]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Serine 25 MICROMOLAR (old descriptor: L-Serine); stage: 2013 Table 3 glycine-substitution
    assay'
  target_ids:
  - CultureMech:007384
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-213
  area: scope
  topic: CultureMech:007384 variants[0].modifications[2]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Magnesium sulfate heptahydrate 2.8 MILLIMOLAR (old descriptor: Magnesium
    sulfate); stage: 2013 Table 3 glycine-substitution assay'
  target_ids:
  - CultureMech:007384
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-214
  area: scope
  topic: CultureMech:007384 variants[0].modifications[3]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Calcium chloride dihydrate 10 MILLIMOLAR (old descriptor: Calcium chloride
    anhydrous); stage: 2013 Table 3 glycine-substitution assay | REPLACE Manganese
    chloride tetrahydrate 9 NANOMOLAR (old descriptor: Manganese chloride); stage:
    2013 Table 3 glycine-substitution assay | REPLACE Zinc sulfate heptahydrate 800
    PICOMOLAR (old descriptor: Zinc sulfate); stage: 2013 Table 3 glycine-substitution
    assay | REPLACE Cobalt chloride hexahydrate 500 PICOMOLAR (old descriptor: Cobalt
    chloride); stage: 2013 Table 3 glycine-substitution assay | REPLACE Sodium molybdate
    dihydrate 300 PICOMOLAR (old descriptor: Sodium molybdate); stage: 2013 Table
    3 glycine-substitution assay | REPLACE Nickel chloride hexahydrate 1 NANOMOLAR
    (old descriptor: Nickel chloride); stage: 2013 Table 3 glycine-substitution assay'
  target_ids:
  - CultureMech:007384
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-215
  area: scope
  topic: CultureMech:007384 variants[0].modifications[4]
  outcome: supported
  summary: 'Source-supported variant event(s); base ingredients/prose unchanged. Unspecified
    stereochemistry is retained explicitly without ontology assignment. Proposals:
    REPLACE Iron(III) chloride hexahydrate 1 MICROMOLAR (old descriptor: Iron(III)
    chloride); stage: 2013 Table 3 glycine-substitution assay'
  target_ids:
  - CultureMech:007384
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-216
  area: scope
  topic: CultureMech:007384 variants[0].modifications[5]
  outcome: supported
  summary: 'Partial: source-literal vitamin designations/doses structured; B7/biotin
    4 nM already present and retained. Specific vitamers/salt forms remain unresolved;
    no B-number ontology identity assigned. Proposals: ADD B1 6 MICROMOLAR; stage:
    2013 Table 3 glycine-substitution assay | ADD B3 800 NANOMOLAR; stage: 2013 Table
    3 glycine-substitution assay | ADD B5 425 NANOMOLAR; stage: 2013 Table 3 glycine-substitution
    assay | ADD B6 500 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay |
    ADD B9 4 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay | ADD B12 700
    PICOMOLAR; stage: 2013 Table 3 glycine-substitution assay | ADD Myo-inositol 6
    MICROMOLAR; stage: 2013 Table 3 glycine-substitution assay | ADD 4-Aminobenzoic
    acid 60 NANOMOLAR; stage: 2013 Table 3 glycine-substitution assay | REMOVE 4-Amino-5-hydroxymethyl-2-methylpyrimidine;
    stage: 2013 Table 3 glycine-substitution assay'
  target_ids:
  - CultureMech:007384
  evidence_ids:
  - proposal
  - primary-1
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-1
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-217
  area: scope
  topic: CultureMech:007384 variants[0].modifications[6]
  outcome: supported
  summary: Preparation order, gas sparging and pH context retained as prose. No dissolved-gas
    dose or new positive ingredient is inferred. No new ingredient event proposed.
  target_ids:
  - CultureMech:007384
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: CONDITION_ONLY
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-237
  area: scope
  topic: CultureMech:007302 variants[0].modifications[0]
  outcome: supported
  summary: Stock filtration pore size/order is preparation context, not an ingredient
    occurrence. No new ingredient event proposed.
  target_ids:
  - CultureMech:007302
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: CONDITION_ONLY
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-238
  area: scope
  topic: CultureMech:007302 variants[0].modifications[1]
  outcome: supported
  summary: 'Calcium salt identity retained without converting pantothenate-basis amount
    to salt molarity. Proposals: REPLACE Calcium pantothenate (old descriptor: Pantothenate);
    stage: BL medium vitamin-stock preparation'
  target_ids:
  - CultureMech:007302
  evidence_ids:
  - proposal
  - primary-5
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-5
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-239
  area: scope
  topic: CultureMech:007302 variants[0].modifications[2]
  outcome: concern
  summary: Nominal formulation retained; MgCl2 hydration and molybdate formula/hydration
    remain unresolved. No imported hydrate is certified. No new ingredient event proposed.
  target_ids:
  - CultureMech:007302
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: unsupported
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: HELD_EVIDENCE
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-240
  area: scope
  topic: CultureMech:007302 variants[0].modifications[3]
  outcome: supported
  summary: Existing treatment ingredient/dose retained; this row adds Table 3 context
    rather than a new variant ingredient. No growth claim revalidated. No new ingredient
    event proposed.
  target_ids:
  - CultureMech:007302
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: ALREADY_STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-241
  area: scope
  topic: CultureMech:007303 variants[0].modifications[0]
  outcome: supported
  summary: Stock filtration pore size/order is preparation context, not an ingredient
    occurrence. No new ingredient event proposed.
  target_ids:
  - CultureMech:007303
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: CONDITION_ONLY
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-242
  area: scope
  topic: CultureMech:007303 variants[0].modifications[1]
  outcome: supported
  summary: 'Calcium salt identity retained without converting pantothenate-basis amount
    to salt molarity. Proposals: REPLACE Calcium pantothenate (old descriptor: Pantothenate);
    stage: BL medium vitamin-stock preparation'
  target_ids:
  - CultureMech:007303
  evidence_ids:
  - proposal
  - primary-5
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-5
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-243
  area: scope
  topic: CultureMech:007303 variants[0].modifications[2]
  outcome: concern
  summary: Nominal formulation retained; MgCl2 hydration and molybdate formula/hydration
    remain unresolved. No imported hydrate is certified. No new ingredient event proposed.
  target_ids:
  - CultureMech:007303
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: unsupported
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: HELD_EVIDENCE
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-244
  area: scope
  topic: CultureMech:007303 variants[0].modifications[3]
  outcome: supported
  summary: Existing treatment ingredient/dose retained; this row adds Table 3 context
    rather than a new variant ingredient. No growth claim revalidated. No new ingredient
    event proposed.
  target_ids:
  - CultureMech:007303
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: ALREADY_STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-245
  area: scope
  topic: CultureMech:007306 variants[0].modifications[0]
  outcome: supported
  summary: Stock filtration pore size/order is preparation context, not an ingredient
    occurrence. No new ingredient event proposed.
  target_ids:
  - CultureMech:007306
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: CONDITION_ONLY
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-246
  area: scope
  topic: CultureMech:007306 variants[0].modifications[1]
  outcome: supported
  summary: 'Calcium salt identity retained without converting pantothenate-basis amount
    to salt molarity. Proposals: REPLACE Calcium pantothenate (old descriptor: Pantothenate);
    stage: BL medium vitamin-stock preparation'
  target_ids:
  - CultureMech:007306
  evidence_ids:
  - proposal
  - primary-5
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-5
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-247
  area: scope
  topic: CultureMech:007306 variants[0].modifications[2]
  outcome: concern
  summary: Nominal formulation retained; MgCl2 hydration and molybdate formula/hydration
    remain unresolved. No imported hydrate is certified. No new ingredient event proposed.
  target_ids:
  - CultureMech:007306
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: unsupported
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: HELD_EVIDENCE
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-248
  area: scope
  topic: CultureMech:007306 variants[0].modifications[3]
  outcome: supported
  summary: Existing treatment ingredient/dose retained; this row adds Table 3 context
    rather than a new variant ingredient. No growth claim revalidated. No new ingredient
    event proposed.
  target_ids:
  - CultureMech:007306
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: ALREADY_STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-249
  area: scope
  topic: CultureMech:007304 variants[0].modifications[0]
  outcome: supported
  summary: Stock filtration pore size/order is preparation context, not an ingredient
    occurrence. No new ingredient event proposed.
  target_ids:
  - CultureMech:007304
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: CONDITION_ONLY
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-250
  area: scope
  topic: CultureMech:007304 variants[0].modifications[1]
  outcome: supported
  summary: 'Calcium salt identity retained without converting pantothenate-basis amount
    to salt molarity. Proposals: REPLACE Calcium pantothenate (old descriptor: Pantothenate);
    stage: BL medium vitamin-stock preparation'
  target_ids:
  - CultureMech:007304
  evidence_ids:
  - proposal
  - primary-5
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-5
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-251
  area: scope
  topic: CultureMech:007304 variants[0].modifications[2]
  outcome: concern
  summary: Nominal formulation retained; MgCl2 hydration and molybdate formula/hydration
    remain unresolved. No imported hydrate is certified. No new ingredient event proposed.
  target_ids:
  - CultureMech:007304
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: unsupported
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: HELD_EVIDENCE
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-252
  area: scope
  topic: CultureMech:007304 variants[0].modifications[3]
  outcome: supported
  summary: Existing treatment ingredient/dose retained; this row adds Table 3 context
    rather than a new variant ingredient. No growth claim revalidated. No new ingredient
    event proposed.
  target_ids:
  - CultureMech:007304
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: ALREADY_STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-253
  area: scope
  topic: CultureMech:007305 variants[0].modifications[0]
  outcome: supported
  summary: Stock filtration pore size/order is preparation context, not an ingredient
    occurrence. No new ingredient event proposed.
  target_ids:
  - CultureMech:007305
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: CONDITION_ONLY
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-254
  area: scope
  topic: CultureMech:007305 variants[0].modifications[1]
  outcome: supported
  summary: 'Calcium salt identity retained without converting pantothenate-basis amount
    to salt molarity. Proposals: REPLACE Calcium pantothenate (old descriptor: Pantothenate);
    stage: BL medium vitamin-stock preparation'
  target_ids:
  - CultureMech:007305
  evidence_ids:
  - proposal
  - primary-5
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-5
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-255
  area: scope
  topic: CultureMech:007305 variants[0].modifications[2]
  outcome: concern
  summary: Nominal formulation retained; MgCl2 hydration and molybdate formula/hydration
    remain unresolved. No imported hydrate is certified. No new ingredient event proposed.
  target_ids:
  - CultureMech:007305
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: unsupported
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: HELD_EVIDENCE
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-256
  area: scope
  topic: CultureMech:007305 variants[0].modifications[3]
  outcome: supported
  summary: Existing treatment ingredient/dose retained; this row adds Table 3 context
    rather than a new variant ingredient. No growth claim revalidated. No new ingredient
    event proposed.
  target_ids:
  - CultureMech:007305
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: ALREADY_STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-337
  area: scope
  topic: CultureMech:007073 variants[0].modifications[0]
  outcome: supported
  summary: 'Literal study buffer concentration; no base mutation. Proposals: SET_CONCENTRATION
    PIPES 20 MILLIMOLAR; stage: isotope-tracer growth assay'
  target_ids:
  - CultureMech:007073
  evidence_ids:
  - proposal
  - primary-4
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-4
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-338
  area: scope
  topic: CultureMech:007073 variants[0].modifications[1]
  outcome: supported
  summary: 'Labeled substrate kept distinct from imported unlabeled sodium L-lactate.
    Proposals: REPLACE [3-13C] sodium L-lactate 30 MILLIMOLAR (old descriptor: Sodium
    L-lactate); stage: isotope-tracer growth assay'
  target_ids:
  - CultureMech:007073
  evidence_ids:
  - proposal
  - primary-4
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-4
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-342
  area: scope
  topic: CultureMech:007076 variants[0].modifications[0]
  outcome: supported
  summary: 'Literal study buffer concentration; no base mutation. Proposals: SET_CONCENTRATION
    PIPES 20 MILLIMOLAR; stage: isotope-tracer growth assay'
  target_ids:
  - CultureMech:007076
  evidence_ids:
  - proposal
  - primary-4
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-4
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-343
  area: scope
  topic: CultureMech:007076 variants[0].modifications[1]
  outcome: supported
  summary: 'Labeled substrate kept distinct from imported unlabeled sodium L-lactate.
    Proposals: REPLACE [3-13C] sodium L-lactate 30 MILLIMOLAR (old descriptor: Sodium
    L-lactate); stage: isotope-tracer growth assay'
  target_ids:
  - CultureMech:007076
  evidence_ids:
  - proposal
  - primary-4
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-4
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-344
  area: scope
  topic: CultureMech:007076 variants[0].modifications[2]
  outcome: concern
  summary: AA-S-18 is a 17-component mixture at 25 µM each, not 25 µM mixture. Exact
    correspondence to flattened imported amino acids (including DL forms) remains
    unresolved; no duplicate mixture/individual presence or unsupported stereochemistry
    is asserted. No new ingredient event proposed.
  target_ids:
  - CultureMech:007076
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: schema_gap
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: HELD_MODEL
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-345
  area: scope
  topic: CultureMech:007075 variants[0].modifications[0]
  outcome: supported
  summary: 'Literal study buffer concentration; no base mutation. Proposals: SET_CONCENTRATION
    PIPES 20 MILLIMOLAR; stage: isotope-tracer growth assay'
  target_ids:
  - CultureMech:007075
  evidence_ids:
  - proposal
  - primary-4
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-4
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-346
  area: scope
  topic: CultureMech:007075 variants[0].modifications[1]
  outcome: supported
  summary: 'Labeled substrate kept distinct from imported unlabeled sodium L-lactate.
    Proposals: REPLACE [3-13C] sodium L-lactate 30 MILLIMOLAR (old descriptor: Sodium
    L-lactate); stage: isotope-tracer growth assay'
  target_ids:
  - CultureMech:007075
  evidence_ids:
  - proposal
  - primary-4
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-4
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-347
  area: scope
  topic: CultureMech:007075 variants[0].modifications[2]
  outcome: concern
  summary: AA-S-18 is a 17-component mixture at 25 µM each, not 25 µM mixture. Exact
    correspondence to flattened imported amino acids (including DL forms) remains
    unresolved; no duplicate mixture/individual presence or unsupported stereochemistry
    is asserted. No new ingredient event proposed.
  target_ids:
  - CultureMech:007075
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: schema_gap
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: HELD_MODEL
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-348
  area: scope
  topic: CultureMech:007074 variants[0].modifications[0]
  outcome: supported
  summary: 'Literal study buffer concentration; no base mutation. Proposals: SET_CONCENTRATION
    PIPES 20 MILLIMOLAR; stage: isotope-tracer growth assay'
  target_ids:
  - CultureMech:007074
  evidence_ids:
  - proposal
  - primary-4
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-4
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-349
  area: scope
  topic: CultureMech:007074 variants[0].modifications[1]
  outcome: supported
  summary: 'Labeled substrate kept distinct from imported unlabeled sodium L-lactate.
    Proposals: REPLACE [3-13C] sodium L-lactate 30 MILLIMOLAR (old descriptor: Sodium
    L-lactate); stage: isotope-tracer growth assay'
  target_ids:
  - CultureMech:007074
  evidence_ids:
  - proposal
  - primary-4
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-4
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-360
  area: scope
  topic: CultureMech:007070 variants[0].modifications[0]
  outcome: supported
  summary: 'Explicit phosphate-form replacement; no parent recipe equivalence inferred.
    Proposals: REPLACE Sodium dihydrogen phosphate monohydrate 4.35 MILLIMOLAR (old
    descriptor: Dibasic sodium phosphate); stage: modified M1 batch culture'
  target_ids:
  - CultureMech:007070
  evidence_ids:
  - proposal
  - primary-3
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-3
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-361
  area: scope
  topic: CultureMech:007070 variants[0].modifications[1]
  outcome: concern
  summary: Source names 10× Wolfe vitamin/mineral stock additions; correspondence
    to the parent's flattened stock components and final-volume basis are unresolved.
    Do not add stock components twice or invent individual replacements. No new ingredient
    event proposed.
  target_ids:
  - CultureMech:007070
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: schema_gap
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: HELD_MODEL
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-362
  area: scope
  topic: CultureMech:007070 variants[0].modifications[2]
  outcome: supported
  summary: Batch PIPES 30 mM already present; pH and exclusion of chemostat/anaerobic
    treatments remain context. No chemostat Fe(III)-NTA or fumarate added. No new
    ingredient event proposed.
  target_ids:
  - CultureMech:007070
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: ALREADY_STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-363
  area: scope
  topic: CultureMech:007069 variants[0].modifications[0]
  outcome: supported
  summary: 'Explicit phosphate-form replacement; no parent recipe equivalence inferred.
    Proposals: REPLACE Sodium dihydrogen phosphate monohydrate 4.35 MILLIMOLAR (old
    descriptor: Dibasic sodium phosphate); stage: modified M1 batch culture'
  target_ids:
  - CultureMech:007069
  evidence_ids:
  - proposal
  - primary-3
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-3
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-364
  area: scope
  topic: CultureMech:007069 variants[0].modifications[1]
  outcome: concern
  summary: Source names 10× Wolfe vitamin/mineral stock additions; correspondence
    to the parent's flattened stock components and final-volume basis are unresolved.
    Do not add stock components twice or invent individual replacements. No new ingredient
    event proposed.
  target_ids:
  - CultureMech:007069
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: schema_gap
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: HELD_MODEL
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-365
  area: scope
  topic: CultureMech:007069 variants[0].modifications[2]
  outcome: supported
  summary: Batch PIPES 30 mM already present; pH and exclusion of chemostat/anaerobic
    treatments remain context. No chemostat Fe(III)-NTA or fumarate added. No new
    ingredient event proposed.
  target_ids:
  - CultureMech:007069
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: ALREADY_STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-366
  area: scope
  topic: CultureMech:007072 variants[0].modifications[0]
  outcome: supported
  summary: 'Explicit phosphate-form replacement; no parent recipe equivalence inferred.
    Proposals: REPLACE Sodium dihydrogen phosphate monohydrate 4.35 MILLIMOLAR (old
    descriptor: Dibasic sodium phosphate); stage: modified M1 batch culture'
  target_ids:
  - CultureMech:007072
  evidence_ids:
  - proposal
  - primary-3
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-3
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-367
  area: scope
  topic: CultureMech:007072 variants[0].modifications[1]
  outcome: concern
  summary: Source names 10× Wolfe vitamin/mineral stock additions; correspondence
    to the parent's flattened stock components and final-volume basis are unresolved.
    Do not add stock components twice or invent individual replacements. No new ingredient
    event proposed.
  target_ids:
  - CultureMech:007072
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: schema_gap
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: HELD_MODEL
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-368
  area: scope
  topic: CultureMech:007072 variants[0].modifications[2]
  outcome: supported
  summary: Batch PIPES 30 mM already present; pH and exclusion of chemostat/anaerobic
    treatments remain context. No chemostat Fe(III)-NTA or fumarate added. No new
    ingredient event proposed.
  target_ids:
  - CultureMech:007072
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: ALREADY_STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-369
  area: scope
  topic: CultureMech:007071 variants[0].modifications[0]
  outcome: supported
  summary: 'Explicit phosphate-form replacement; no parent recipe equivalence inferred.
    Proposals: REPLACE Sodium dihydrogen phosphate monohydrate 4.35 MILLIMOLAR (old
    descriptor: Dibasic sodium phosphate); stage: modified M1 batch culture'
  target_ids:
  - CultureMech:007071
  evidence_ids:
  - proposal
  - primary-3
  dimensions:
  - name: native_concentration_decision
    value: add
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
    - primary-3
  - name: queue_disposition
    value: STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-370
  area: scope
  topic: CultureMech:007071 variants[0].modifications[1]
  outcome: concern
  summary: Source names 10× Wolfe vitamin/mineral stock additions; correspondence
    to the parent's flattened stock components and final-volume basis are unresolved.
    Do not add stock components twice or invent individual replacements. No new ingredient
    event proposed.
  target_ids:
  - CultureMech:007071
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: schema_gap
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: HELD_MODEL
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
- assessment_id: queue-row-371
  area: scope
  topic: CultureMech:007071 variants[0].modifications[2]
  outcome: supported
  summary: Batch PIPES 30 mM already present; pH and exclusion of chemostat/anaerobic
    treatments remain context. No chemostat Fe(III)-NTA or fumarate added. No new
    ingredient event proposed.
  target_ids:
  - CultureMech:007071
  evidence_ids:
  - proposal
  dimensions:
  - name: native_concentration_decision
    value: evidence_only
    definition: Decision for new structured variant events only; existing base doses
      and whole-record scientific status are not certified.
    evidence_ids:
    - proposal
  - name: queue_disposition
    value: ALREADY_STRUCTURED
    definition: Disposition of this exact assigned queue row; STRUCTURED may retain
      explicitly stated identity/form limitations.
    evidence_ids:
    - proposal
findings: []
actions: []
limitations:
- Author review is not independent or human approval. No recipe was changed by this
  agent.
- B-number vitamins remain source-level labels with molecular/salt forms unresolved;
  generic methionine, serine and P-substrate labels do not certify imported stereoisomers.
- Held rows preserve uncertain phosphite stoichiometry, Jensen hydration/form questions,
  Wolfe stock correspondence and Tang 17-amino-acid mixture correspondence. These
  are not claims of absent ingredients.
- Jensen primary PDF has no retained local byte hash because anonymous downloads failed;
  browser text was inspected. Tang evidence is the OSTI-hosted manuscript version,
  whose page includes author edits.
- The source-specific negative phosphate event refers to original AMS1 Table 1 phosphate,
  not a claim that each imported parent contains phosphate or that residual phosphate
  is zero.
- Independent proposal review, central guarded application, post-application export
  accounting and release gates remain separate.
links:
- https://github.com/CultureBotAI/CultureMech/issues/683
```
