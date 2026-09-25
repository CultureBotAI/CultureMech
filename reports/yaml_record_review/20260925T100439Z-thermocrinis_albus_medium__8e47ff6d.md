# YAML Record Review: THERMOCRINIS ALBUS MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermocrinis_albus_medium__8e47ff6d.yaml`
- Started UTC: 2026-09-25T10:02:00Z
- Finished UTC: 2026-09-25T10:04:39Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002674`
- Merge fingerprint: `8e47ff6dae126a44f671c1753000d9e96ffb83a011715cc48668cda74f7b3b73`
- Merged source: `thermocrinis_albus_medium`
- Media term: `mediadive.medium:J316`
- Source medium: JCM J316, "THERMOCRINIS ALBUS MEDIUM"

## Validation

- LinkML schema validation: Passed with `No issues found`.
- Strict schema validation: Passed; 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed. The only stderr output was the expected `eutils` warning about `pkg_resources`.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not the embedded `MediaRecipe.curation_history` array in this merged YAML.

## Identity and Grounding

- The record is a direct MediaDive/JCM import of JCM 316 and keeps the JCM source, pH 7.0, and base main-solution amounts scaled by MediaDive's 1010 ml final volume.
- MediaDive represents `Trace minerals` as a 10 ml stock addition, but the import flattened that stock into top-level final-medium ingredients at stock concentrations.
- Flattening over-counted stock components that also occur in the main solution: NaCl is stored as 1.253465 g/L after summing 0.253465 g/L main NaCl and 1.0 g/L stock NaCl, and MnSO4 x n H2O is stored as 0.50000594059 g/L after summing 0.00000594059 g/L main MnSO4 and 0.5 g/L stock MnSO4.
- The target still carries legacy `mediaingredientmech_term` links for `NaNO3` and `Na2SeO4` despite both ingredients having CHEBI terms.

## Evidence

- JCM 316 lists a 10 ml Trace minerals row linked to JCM Medium 151, not individual trace stock salts at final-medium concentrations.
- MediaDive REST `J316` preserves the `Trace minerals` row as a 10 ml solution reference and includes the Trace minerals stock as a nested solution with 1000 ml stock volume.
- The generated target promotes Trace minerals stock-only ingredients such as nitrilotriacetic acid, MgSO4 x 7 H2O, CoSO4 x 7 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2, and Na2MoO4 x 2 H2O to top-level final-medium ingredients.
- Exact ignored-file search found an unmerged TOGO M311/JCM 316 branch in `data/merge_yaml/merged/THERMOCRINIS_ALBUS_MEDIUM.yaml`; that TOGO branch has its own mg-to-g import errors and should be reconciled only after the stock scaling issue is fixed.

## Completeness

- Required scalar fields, ingredient concentrations, the MediaDive J316 media term, JCM preparation text, curation history, and `merged_from` are present.
- No organisms or strain links are expected for this medium-level import.
- The Trace minerals stock relationship is absent because nested solution contents were flattened.

## Findings

- High - The 10 ml Trace minerals stock is flattened into top-level ingredients without scaling by the 10 ml stock addition, inflating trace-solution salts by roughly two orders of magnitude.
- High - Duplicate main and trace-stock salts are summed, corrupting final NaCl, CaCl2 x 2 H2O, H3BO3, and MnSO4 x n H2O concentrations.
- Medium - MediaDive reports the final gas pressure as 300 kPa while the original JCM 316 HTML says 200 kPa; the generated preparation text currently carries 300 kPa.
- Low - `NaNO3` and `Na2SeO4` retain legacy MediaIngredientMech links that should be refreshed to CHEBI-keyed links.

## Recommended Edits

- Fix the direct MediaDive import or stock-flattening path so `Trace minerals` remains a 10 ml nested solution reference or is scaled before flattening.
- Prevent data-quality cleanup from summing main-solution and stock-solution rows that belong to different solution scopes.
- Compare JCM 316 directly before deciding whether to override the MediaDive 300 kPa pressure with JCM's 200 kPa source value.
- Reconcile the direct MediaDive/JCM branch with TOGO M311 only after the TOGO mg-to-g and gas-note issues have been corrected in normalized YAML.
- Refresh `NaNO3` and `Na2SeO4` legacy MediaIngredientMech links from their existing CHEBI primary terms.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated J316 branch.
- Re-run exact ignored-file search for `thermocrinis_albus_medium`, `mediadive.medium:J316`, `TOGO_M311_Thermocrinis_Albus_Medium`, and `GRMD=316` after duplicate reconciliation.
- Compare the regenerated Trace minerals representation against MediaDive REST `J316` and JCM 316.

## Additional Notes

None found.
