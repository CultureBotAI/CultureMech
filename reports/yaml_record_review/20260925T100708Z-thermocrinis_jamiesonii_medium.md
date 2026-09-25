# YAML Record Review: Thermocrinis Jamiesonii  Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermocrinis_jamiesonii_medium.yaml`
- Started UTC: 2026-09-25T10:05:20Z
- Finished UTC: 2026-09-25T10:07:08Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:007546`
- Merge fingerprint: `3f23b5eba9b1857cd9c4627b8eb38789395977a4ca75bb70996219a5ec79448d`
- Merged source: `TOGO_M1031_Thermocrinis_Jamiesonii_Medium`
- Media term: `TOGO:M1031`
- Source medium: JCM M978, "THERMOCRINIS JAMIESONII  MEDIUM"

## Validation

- LinkML schema validation: Passed with `No issues found`.
- Strict schema validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 reference checks and no errors.
- Term validation: Passed. The only stderr output was the expected `eutils` warning about `pkg_resources`.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not the embedded `MediaRecipe.curation_history` array in this merged YAML.

## Identity and Grounding

- TOGO M1031 and the direct MediaDive `mediadive.medium:J978` record are split generated branches of the same JCM 978 source.
- The imported main salts match the TOGO API amounts before final-volume scaling, but `Distilled water` is stored as 1 g/L even though the source row is 1 L.
- The 5 ml `Mineral solution` parent from TOGO M1029/JCM 976 is stored as an empty `Unknown solution` at 5 g/L.
- Three post-autoclave stock additions, 10 ml 8.0% NaHCO3, 10 ml 0.2 M sodium acetate, and 10 ml 0.2 M sodium thiosulfate, are stored as empty 10 g/L solutions with their concentration metadata only in the preferred term string.
- O2 is represented as an ungrounded variable ingredient; JCM 978 specifies 2% O2 in the gas phase before inoculation.

## Evidence

- TOGO API `M1031` links JCM 978 and preserves two solution groups: the base salts plus 5 ml Mineral solution `M1029`, then the three 10 ml bicarbonate, acetate, and thiosulfate solution additions plus O2.
- JCM 978 links the Mineral solution row to JCM Medium 976 and instructs aseptic per-liter addition of the three anaerobically stored solutions after cooling.
- JCM 976 defines the actual Mineral solution stock under Thermoflexus hungenholtzii Medium; the exact ignored-file search found it as TOGO M1029 / JCM M976.
- Exact ignored-file search found both the TOGO M1031 and direct MediaDive J978 normalized and generated records; they remain separate generated branches for one JCM 978 source.

## Completeness

- Required scalar fields, base ingredient concentrations, the TOGO media term, curation history, and `merged_from` are present.
- No organisms or strain links are expected for this medium-level import.
- Mineral solution and post-autoclave stock compositions are absent.
- JCM 978 preparation steps are absent.

## Findings

- High - Four solution rows were migrated to empty g/L solutions, including the 5 ml M1029 Mineral solution and three 10 ml post-autoclave stock additions.
- High - The 0.2 M and 8.0% concentration metadata for acetate, thiosulfate, and bicarbonate was not represented structurally.
- High - `Distilled water` is stored as 1 g/L even though the source row is a 1 L solvent volume.
- Medium - The O2 gas row lacks a CHEBI grounding and loses the explicit 2% gas-phase concentration.
- Medium - The TOGO M1031 and direct MediaDive J978 branches are not reconciled.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/TOGO_M1031_Thermocrinis_Jamiesonii_Medium.yaml`, not the generated merge YAML, so M1029 remains a 5 ml parent-solution addition and the three post-autoclave stocks retain their concentration metadata and 10 ml addition volumes.
- Expand or structurally reference TOGO M1029/JCM 976 for the Mineral solution.
- Preserve JCM 978 preparation steps during TOGO import.
- Ground O2 to CHEBI dioxigen and retain the 2% final gas-phase instruction.
- Reconcile TOGO M1031 with direct MediaDive J978 once both branches preserve the same stock-addition structure.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated TOGO M1031 branch.
- Re-run exact ignored-file search for `TOGO_M1031_Thermocrinis_Jamiesonii_Medium`, `mediadive.medium:J978`, `GRMD=978`, `TOGO_M1029`, and `GRMD=976` after duplicate reconciliation.
- Compare the regenerated solution rows against TOGO M1031, JCM 978, and JCM 976.

## Additional Notes

None found.
