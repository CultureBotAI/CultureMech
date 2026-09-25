# YAML Record Review: THERMOCRINIS JAMIESONII  MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermocrinis_jamiesonii_medium__a34d6543.yaml`
- Started UTC: 2026-09-25T10:05:20Z
- Finished UTC: 2026-09-25T10:07:09Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:003327`
- Merge fingerprint: `a34d6543116afa273b2a68a8a2c52436c3be437828c8b47d990aa899e13036c7`
- Merged source: `thermocrinis_jamiesonii_medium`
- Media term: `mediadive.medium:J978`
- Source medium: JCM J978, "THERMOCRINIS JAMIESONII  MEDIUM"

## Validation

- LinkML schema validation: Passed with `No issues found`.
- Strict schema validation: Passed; 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: Passed; 0 reference checks and no errors.
- Term validation: Passed. The only stderr output was the expected `eutils` warning about `pkg_resources`.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not the embedded `MediaRecipe.curation_history` array in this merged YAML.

## Identity and Grounding

- The record is a direct MediaDive/JCM import of JCM 978 and scales base-salt concentrations over MediaDive's 1035 ml total volume.
- MediaDive stores the 5 ml Mineral solution row as `Mineral solution (see Medium No. 976`, but the generated record migrates it to an empty `Unknown solution` at 5 g/L.
- MediaDive also stores the 10 ml acetate, thiosulfate, and bicarbonate stock additions as milliliter rows with attributes; the generated record converts them to 10 g/L top-level `Sodium acetate`, `Sodium Thiosulfate`, and `NaHCO3` ingredients.
- The direct MediaDive branch and TOGO M1031 branch remain split even though both cite JCM 978.

## Evidence

- MediaDive REST `J978` reports 1035 ml final volume, 1000 ml water, 5 ml Mineral solution, 10 ml 0.2 M Sodium acetate, 10 ml 0.2 M Sodium Thiosulfate, and 10 ml 8.0% NaHCO3.
- JCM 978 shows the same Mineral solution row linked to JCM Medium 976 and the same three per-liter stock additions after autoclaving.
- JCM 976 contains the Mineral solution stock formula below the main Thermoflexus hungenholtzii Medium table.
- Exact ignored-file search found the separate TOGO M1031 branch for the same JCM 978 source; the two branches are not merged.

## Completeness

- Required scalar fields, base ingredient concentrations, the MediaDive J978 term, JCM preparation steps, curation history, and `merged_from` are present.
- No organisms or strain links are expected for this medium-level import.
- The Mineral solution composition is absent.
- The acetate, thiosulfate, and bicarbonate stock additions lose their volume and stock-concentration semantics.

## Findings

- High - The three 10 ml post-autoclave stock additions are represented as 10 g/L top-level ingredients instead of stock solutions with 10 ml addition volumes.
- High - The 5 ml Mineral solution cross-reference to JCM 976 is an empty 5 g/L solution.
- Medium - The direct MediaDive J978 and TOGO M1031 branches are not reconciled.
- Low - `Mineral solution (see Medium No. 976` is missing a closing parenthesis in the imported preferred term.

## Recommended Edits

- Fix the direct MediaDive import or solution migration path so milliliter stock additions are not promoted to mass concentrations.
- Preserve the Mineral solution row as a 5 ml JCM 976 cross-reference or expand JCM 976's Mineral solution stock.
- Preserve the 0.2 M and 8.0% attributes as stock-solution concentration metadata rather than as text-only name fragments.
- Reconcile this branch with TOGO M1031 after both paths preserve the JCM 978 solution structure.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated MediaDive J978 branch.
- Re-run exact ignored-file search for `thermocrinis_jamiesonii_medium`, `mediadive.medium:J978`, `TOGO_M1031_Thermocrinis_Jamiesonii_Medium`, `GRMD=978`, and `GRMD=976` after duplicate reconciliation.
- Compare the regenerated solution rows against MediaDive REST `J978`, JCM 978, and JCM 976.

## Additional Notes

None found.
