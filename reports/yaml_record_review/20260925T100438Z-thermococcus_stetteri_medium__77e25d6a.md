# YAML Record Review: Thermococcus Stetteri Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermococcus_stetteri_medium__77e25d6a.yaml`
- Started UTC: 2026-09-25T10:02:00Z
- Finished UTC: 2026-09-25T10:04:38Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:008065`
- Merge fingerprint: `77e25d6aff0065cd132daac40e70b15a0cb7d49bc3257a8902c7e89490252194`
- Merged sources: `TOGO_M151_Thermococcus_Stetteri_Medium`, `TOGO_M152_Thermococcus_Litoralis_Medium`, `TOGO_M233_Thermococcus_Fumicolans_Medium`
- Media term: `TOGO:M151`
- Source medium: JCM M160, "THERMOCOCCUS STETTERI MEDIUM"

## Validation

- LinkML schema validation: Passed with `No issues found`.
- Strict schema validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 reference checks and no errors.
- Term validation: Passed. The only stderr output was the expected `eutils` warning about `pkg_resources`.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not the embedded `MediaRecipe.curation_history` array in this merged YAML.

## Identity and Grounding

- TOGO M151, M152, and M233 are related JCM recipes, but they are not exact source duplicates. JCM 161 derives from JCM 160 with 1.0 g/L final yeast extract, 5.0 g/L final peptone, and pH 7.2; JCM 241 derives from JCM 160 with 0.5 g/L final yeast extract, 2.0 g/L final peptone, and pH 7.5.
- The generated merge keeps M151's 3 g/L yeast extract and 0.5 g/L Bacto peptone as canonical while storing M152 and M233 only as synonyms, losing their variant-specific peptide/yeast and pH values.
- The imported `Resazurin` amount is 1000x too high: TOGO M151/M152/M233 and JCM 160 all specify 1 mg, while the generated record stores 1 `G_PER_L`.
- The 1 L `Modified Brock's salt base solution` cross-reference to TOGO M156/JCM 165 is stored as an empty `Unknown solution` at 1 g/L.

## Evidence

- TOGO API `M151` links JCM 160 and pH 6.5; JCM 160 lists 1 L Modified Brock's salt base, 25 g NaCl, 3 g yeast extract, 0.5 g Bacto peptone, 10 g sulfur powder, and 1 mg resazurin.
- TOGO API `M152` links JCM 161 and pH 7.2; JCM 161 says to use JCM 160 with 1.0 g/L final yeast extract and 5.0 g/L final peptone.
- TOGO API `M233` links JCM 241; JCM 241 says to use JCM 160 with 0.5 g/L final yeast extract, 2.0 g/L final peptone, and pH 7.5.
- Exact ignored-file search found direct JCM-derived normalized records for JCM 160, JCM 161, and JCM 241 that are split from this TOGO merge. A first `JCM_M239`/`GRMD=239` hit set was discarded because M233 actually cites `JCM_M241`/`GRMD=241`.

## Completeness

- Required scalar fields, ingredient concentrations, the TOGO M151 media term, curation history, synonyms, and `merged_from` are present.
- No organisms or strain links are expected for this medium-level import.
- The generated merge does not represent M152 and M233 as parameterized variants of M151.
- The Modified Brock's salt base composition and the JCM 160 anaerobic preparation instructions are absent.

## Findings

- High - Three JCM variant media were merged as source duplicates, dropping M152 and M233 variant-specific yeast, peptone, and pH values.
- High - `Resazurin` was imported as 1 g/L even though the source uses 1 mg/L.
- High - The 1 L Modified Brock's salt base cross-reference was migrated to an empty 1 g/L solution instead of being expanded from TOGO M156/JCM 165.
- Medium - JCM 160's anaerobic N2 preparation, separate yeast/peptone stock handling, sulfur steaming, and Na2S x 9 H2O addition are missing from the TOGO branch.
- Medium - The generated M151 canonical record has no `ph_value` even though TOGO M151 reports pH 6.5.

## Recommended Edits

- Fix `data/normalized_yaml/archaea/TOGO_M151_Thermococcus_Stetteri_Medium.yaml`, `TOGO_M152_Thermococcus_Litoralis_Medium.yaml`, and `TOGO_M233_Thermococcus_Fumicolans_Medium.yaml`, not the generated merge YAML, to normalize resazurin as 0.001 g/L and expand or structurally reference the M156 base.
- Model M152 and M233 as variants of M151 with their yeast, peptone, and pH changes instead of exact duplicate synonyms.
- Preserve JCM 160 preparation text on the M151 base and inherit it for M152/M233 variants unless their original JCM pages override it.
- Reconcile the TOGO and direct MediaDive/JCM branches after M151/M152/M233 variant structure is explicit.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated M151/M152/M233 family.
- Re-run exact ignored-file search for `TOGO_M151_Thermococcus_Stetteri_Medium`, `TOGO_M152_Thermococcus_Litoralis_Medium`, `TOGO_M233_Thermococcus_Fumicolans_Medium`, `GRMD=160`, `GRMD=161`, and `GRMD=241` after variant reconciliation.
- Compare regenerated base solution and preparation text against JCM 160, 161, and 241 before merging the TOGO and direct JCM families.

## Additional Notes

None found.
