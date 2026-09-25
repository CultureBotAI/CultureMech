# YAML Record Review: LB + Streptomycin, Rifampicin medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_streptomycin_rifampicin_medium.yaml
- Started UTC: 2026-09-23T19:17:28Z
- Finished UTC: 2026-09-23T19:18:50Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008554 |
| Name | lb_streptomycin_rifampicin_medium |
| Original name | LB + Streptomycin, Rifampicin medium |
| Category | bacterial |
| Physical state | SOLID_AGAR |
| Media grounding | TOGO:M1972 |
| Source provenance | Togo M1972 imported from NBRC_M1250 |
| Generated file | data/merge_yaml/merged/lb_streptomycin_rifampicin_medium.yaml |
| Maintained canonical owner | data/normalized_yaml/bacterial/lb_streptomycin_rifampicin_medium.yaml |
| Merge fingerprint | 99e3b177df198fce534b889fa8b5168357f0b85ef91ad229d32c60485c0c9f7d |

The reviewed target is a generated merge that collapsed nine different NBRC LB antibiotic recipes. Its maintained canonical owner was repaired in September 2026, so the next correction is regeneration rather than a direct generated-YAML edit.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lb_streptomycin_rifampicin_medium.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/lb_streptomycin_rifampicin_medium.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

Togo M1972 and NBRC Medium 1250 identify `LB + Streptomycin, Rifampicin medium`: an LB base with 10 g Bacto Tryptone (Difco), 5 g yeast extract, 5 g NaCl, 985 ml distilled water, 15 g agar if needed, 10 ml Streptomycin solution at 50 mg/ml, 5 ml Rifampicin solution at 50 mg/ml, pH 7.0, and separate filtration for the antibiotic stocks.

The generated record keeps the M1972 identity but merges eight other NBRC antibiotic recipes as synonyms: ampicilin/hygromycin, ampicillin/cefpodoxime/kanamycin, ampicillin/kanamycin, chloramphenicol, kanamycin/hygromycin, nalidixic acid/ciprofloxacin, rifampicin-only, and streptomycin-only. The maintained owners for these nine source IDs now have distinct `original_name` values, media terms, and antibiotic CHEBI mappings, so they are supplemented variants of NBRC LB rather than duplicates of each other.

An ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:008554`, all nine generated Togo IDs, `NBRC_M1250`, `NO=1250`, and the merge fingerprint found the reviewed generated merge, the nine maintained owners, indexes, and archived validation rows.

## Evidence

Supported in the inspected M1972 sources:

- The `TOGO:M1972` identity and `LB + Streptomycin, Rifampicin medium` label are supported by Togo M1972 and NBRC Medium 1250.
- The basal LB components are supported: 10 g/L Bacto Tryptone (Difco), 5 g/L yeast extract, 5 g/L NaCl, 985 ml/L distilled water, and 15 g/L agar if needed.
- The antibiotic stocks are supported as 10 ml/L Streptomycin solution at 50 mg/ml and 5 ml/L Rifampicin solution at 50 mg/ml, both sterilized separately by filtration.
- pH 7.0 is supported.

Unsupported or stale in the generated record:

- `Distilled water` is represented as `1 G_PER_L`; NBRC M1250 lists 985 ml because antibiotic stocks supply the remaining 15 ml per liter.
- The two antibiotic additions are represented as empty solutions at `10 G_PER_L` and `5 G_PER_L`; the source gives them as 10 ml/L and 5 ml/L stock-solution additions with 50 mg/ml stock strength.
- The generated record omits pH 7.0, the separate filter-sterilization instruction, the antibiotic stock compositions, and the structured NBRC/Togo references.
- The generated `synonyms` and `merged_from` arrays conflate eight other antibiotic variants with this M1972 streptomycin/rifampicin formulation.

## Completeness

The generated record is not complete enough for safe use. It has the correct canonical identity but the old stock-solution representation loses dimensions, stock concentrations, final stock-addition volumes, pH, and preparation boundaries.

The maintained `lb_streptomycin_rifampicin_medium.yaml` owner now restores 985 ml/L water, 10.0 ml/L streptomycin stock, 5.0 ml/L rifampicin stock, 50 mg/ml nested stock compositions, pH 7.0, filter-sterilization and addition steps, parent-media metadata, data-quality flags, and structured references. The other eight maintained antibiotic owners also now name distinct Togo media and antibiotic combinations.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Blocker | The generated merge conflates nine non-duplicate antibiotic LB variants. | The generated synonyms span mutually exclusive media such as LB + Chloramphenicol, LB + Rifampicin, LB + Streptomycin, and LB + Streptomycin, Rifampicin. Their maintained owners now carry distinct Togo IDs and antibiotic CHEBI mappings. | `data/merge_yaml/merged/` regeneration from the repaired normalized owners |
| Major | The generated M1972 record has stale water and antibiotic stock units. | NBRC Medium 1250 lists 985 ml distilled water, 10 ml Streptomycin solution at 50 mg/ml, and 5 ml Rifampicin solution at 50 mg/ml; the generated record has 1 g/L water and 10 g/L and 5 g/L empty solution rows. | `data/merge_yaml/merged/` regeneration from `data/normalized_yaml/bacterial/lb_streptomycin_rifampicin_medium.yaml` |
| Major | The generated record omits pH 7.0 and separate filter sterilization for the stock solutions. | Togo M1972 and NBRC Medium 1250 both carry pH 7.0 and the footnote to sterilize the antibiotic stocks separately by filtration. | `data/merge_yaml/merged/` regeneration from `data/normalized_yaml/bacterial/lb_streptomycin_rifampicin_medium.yaml` |
| Minor | The generated record lacks structured references. | The maintained owner now carries Togo M1972 and NBRC 1250 references, while the generated reference validator performed zero checks. | `data/merge_yaml/merged/` regeneration from the repaired normalized owner |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` from the repaired normalized corpus so the nine NBRC LB antibiotic variants no longer share one generated record.
2. Ensure merge fingerprinting distinguishes supplemented variants by antibiotic identity, stock strength, and addition volume.
3. Regenerate downstream pages and indexes so NBRC M1250 publishes 985 ml/L water and the two separately filter-sterilized antibiotic stocks with ml/L additions and nested 50 mg/ml stock concentrations.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated `lb_streptomycin_rifampicin_medium` output.
- Manually verify that the regenerated M1972 record contains only streptomycin and rifampicin stock additions, not the eight other antibiotic variant names.
- Manually compare the regenerated M1972 YAML against Togo M1972 and NBRC 1250 for 985 ml/L distilled water, 10 ml/L Streptomycin solution, 5 ml/L Rifampicin solution, pH 7.0, and separate filter sterilization.
- Re-run an ignored-inclusive search for `TOGO:M1936`, `TOGO:M2012`, `TOGO:M2050`, `TOGO:M1899`, `TOGO:M1935`, `TOGO:M2013`, `TOGO:M1971`, `TOGO:M1970`, and `TOGO:M1972` to confirm they no longer share fingerprint `99e3b177df198fce534b889fa8b5168357f0b85ef91ad229d32c60485c0c9f7d`.

## Additional Notes

The validator suite accepts the stale generated record because empty stock solutions with numeric concentrations are schema-valid. The failure is semantic: the old merge lost antibiotic identities and stock-solution dimensionality.
