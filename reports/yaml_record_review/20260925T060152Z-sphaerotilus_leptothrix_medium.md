# YAML Record Review: sphaerotilus_leptothrix_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/sphaerotilus_leptothrix_medium.yaml
- Started UTC: 2026-09-25T06:00:10Z
- Finished UTC: 2026-09-25T06:01:53Z
- Verdict: needs curation

## Target

Generated merged YAML for DSMZ 803 / KOMODO 803 plus TOGO M1923 / NBRC 1188 Sphaerotilus-Leptothrix Medium.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/sphaerotilus_leptothrix_medium.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The DSMZ and KOMODO source-duplicate relationship is valid: KOMODO 803 explicitly points to DSMZ 803 and copied the same ingredient signature.

TOGO M1923 points to NBRC 1188, not DSMZ. NBRC 1188 has the same pH and non-water masses as DSMZ 803, but it specifies distilled water while DSMZ specifies tap water. The generated three-way merge collapses that source-specific water distinction.

## Evidence

DSMZ 803 and MediaDive 803 list 1 g yeast extract, 1.5 g peptone, 0.2 g MgSO4 x 7 H2O, 0.05 g CaCl2, 0.5 g ferric ammonium citrate, 0.05 g MnSO4 x H2O, 0.01 g FeCl3 x 6 H2O, 20 g agar, and 1000 ml tap water at pH 7.1.

TOGO M1923 and NBRC 1188 list the same non-water masses and pH 7.1, but the final water row is 1 L distilled water.

## Completeness

The generated record preserves pH 7.1, the solid agar state, and all non-water source masses. The source water row is represented as `Tap water` at 1000 g/L, which is the wrong unit and hides the TOGO/NBRC distilled-water wording.

## Findings

- Critical: `Tap water` is modeled as 1000 `G_PER_L`; DSMZ specifies 1000 ml tap water and NBRC specifies 1 L distilled water.
- Major: the merge fingerprint treated DSMZ tap water and NBRC distilled water as equivalent. That may be acceptable for a loose duplicate, but the generated record should preserve the source-specific water wording or keep NBRC M1188 as a separate variant.
- Minor: the TOGO/NBRC source identity is present only in `merged_from`; the canonical identity and parent-media structure describe only the KOMODO to DSMZ source duplicate.

## Recommended Edits

- Repair the DSMZ/KOMODO normalized records to represent `Tap water` as 1000 ml/L instead of 1000 g/L.
- Repair the TOGO M1923 normalized record to represent `Distilled water` as 1000 ml/L instead of 1 g/L.
- Adjust duplicate merging so DSMZ 803 and NBRC 1188 either stay separate or preserve the tap-water versus distilled-water source distinction in the merged output.
- Regenerate `data/merge_yaml/merged/sphaerotilus_leptothrix_medium.yaml` from the repaired normalized records.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated record.
- Confirm no Sphaerotilus-Leptothrix generated record still has water as `G_PER_L`.
- Confirm the regenerated output preserves both DSMZ/KOMODO and TOGO/NBRC provenance.

## Additional Notes

None found.
