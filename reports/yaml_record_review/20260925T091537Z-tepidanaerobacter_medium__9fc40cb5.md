# YAML Record Review: tepidanaerobacter_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/tepidanaerobacter_medium__9fc40cb5.yaml`
- Started UTC: 2026-09-25T09:14:06Z
- Finished UTC: 2026-09-25T09:15:37Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:009745` for `tepidanaerobacter_medium`, the TOGO M364 import of JCM Medium 370 merged with `TOGO_M434_Anaerolinea_Medium.yaml` on fingerprint `9fc40cb5f20f5b038964944fcaaddb2ea7e14d0048359eb5675fa067bfbedfc9`.

## Validation

- LinkML schema validation: Passed with `No issues found`.
- Strict validation: Passed; 1 file scanned and 0 error rows written to `/private/tmp/tepidanaerobacter_medium__9fc40cb5.strict.tsv`.
- Reference validation: Passed; 1 file validated, 0 external checks.
- Term validation: Passed.
- Embedded `curation_history`: Not checked; `just validate-history` validates standalone `history/`, not merged `MediaRecipe.curation_history`.

## Identity and Grounding

The generated target is grounded to `TOGO:M364`, which correctly traces back to JCM Medium 370, TEPIDANAEROBACTER MEDIUM. JCM 370 is a reference recipe: it says to use Medium 284, supplement Solution A with a final 2.3 g yeast extract per 900 mL, and use 2.2 g sucrose in Solution B per 100 mL instead of sodium pyruvate.

The generated merge also absorbed `TOGO:M434`, JCM Medium 434 ANAEROLINEA MEDIUM. That is a related JCM 284 modification but not a source duplicate: JCM 434 says to supplement Solution A with 1.0 mL trace vitamins and use 7.2 g sucrose in Solution B.

## Evidence

TOGO M364 preserves the JCM 370 source URL and expands the JCM 284 base into Solution A, Solution B, post-autoclave 3% L-cysteine HCl x H2O / Na2S x 9 H2O additions, and trace solutions. The top-level medium should retain Solution A as 900 mL, Solution B as 100 mL, and 0.01-volume additions of both 3% reducing stocks.

JCM Medium 284 defines the trace vitamins, trace elements, and Se/W stocks locally under SI MEDIUM. TOGO M364 imported those three local `see below` rows as `see Medium [M278]`, but live JCM Medium 278 is NAM AGAR and does not define those trace solutions.

## Completeness

The generated M364 target keeps most of the expected JCM 370 ingredient identities, but it no longer preserves the two-solution structure or the trace-stock compositions. The reducing-agent additions are also incomplete: `L--cysteine-HCl-H2O` is flattened as `10 G_PER_L`, while the matching Na2S x 9 H2O 3% solution remains only as an unresolved `Unknown solution`.

The target is not a valid representation of M434 after the merge. M434 should carry 0.1 g yeast extract in Solution A and 7.2 g sucrose in Solution B, while the generated target uses the M364 values of 2.3 g yeast extract and 2.2 g sucrose.

## Findings

- TOGO M364 and TOGO M434 were incorrectly merged as source duplicates even though their JCM source pages define different yeast-extract and sucrose modifications.
- `Solution A` and `Solution B` are stored as unresolved `solutions` rows with `900 G_PER_L` and `100 G_PER_L`, not as the 900 mL and 100 mL subsolutions in the source.
- The source 3% L-cysteine HCl x H2O reducing-stock addition is flattened to a top-level `10 G_PER_L` ingredient, while the paired 3% Na2S x 9 H2O addition is only an unresolved solution row.
- The JCM 284 local stock rows were imported as cross-references to `M278`; JCM 278 is NAM AGAR, so `Trace vitamins solution (see Medium [M278])`, `Trace element solution (see Medium [M278])`, and `Se/W solution (see Medium [M278])` are wrong.
- Imported gas rows are duplicated (`N2` plus `Nitrogen gas`) and still carry non-ASCII GMO gas-property labels.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M364_Tepidanaerobacter_Medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M434_Anaerolinea_Medium.yaml`, then regenerate merged YAML; do not hand-edit generated merge YAML.
- Keep JCM 370 / TOGO M364 separate from JCM 434 / TOGO M434 because they are concentration variants, not source duplicates.
- Represent Solution A, Solution B, the 3% L-cysteine HCl x H2O stock, and the 3% Na2S x 9 H2O stock as structured additions with source volumes, or expand them into final concentrations consistently.
- Resolve the trace vitamin, trace element, and Se/W rows from the local JCM Medium 284 tables instead of pointing them to JCM Medium 278.
- De-duplicate N2/Nitrogen gas and sanitize imported gas-property notes to ASCII.

## Follow-up Checks

- Revalidate regenerated M364 and M434 records with schema, strict, reference, and term validators.
- Search exact `TOGO:M364`, `TOGO:M434`, and `mediadive.medium:J370`, including ignored files, to confirm JCM Medium 370 and JCM Medium 434 no longer collapse into one generated record.
- Search exact `M278` in the repaired M364 and M434 normalized YAML, including ignored files, to confirm the false JCM 278 trace-solution links are gone.

## Additional Notes

Exact source-identity searches used `rg --no-ignore --hidden`, so ignored files were included. DSMZ/KOMODO Medium 1051 uses the same snake-case `tepidanaerobacter_medium` name, but it is a separate DSMZ medium and was not used as evidence for the TOGO M364 review.
