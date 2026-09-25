# YAML Record Review: gab_medium_for_strain_egb

- Repository: CultureMech
- Record: data/merge_yaml/merged/gab_medium_for_strain_egb__0f264cf8.yaml
- Started UTC: 2026-09-23T05:06:46Z
- Finished UTC: 2026-09-23T05:07:45Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:002300` / `gab_medium_for_strain_egb`, the direct MediaDive/JCM Medium J1128 import.
- Compared it with maintained source `data/normalized_yaml/bacterial/gab_medium_for_strain_egb.yaml`.
- Cross-checked the MediaDive REST payload for JCM J1128 and the TOGO M1208 snapshot of the same retired JCM record.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass with 0 error rows.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- `mediadive.medium:J1128` correctly identifies MediaDive's JCM Medium 1128 snapshot for GAB MEDIUM FOR STRAIN EGB; the live JCM GRMD=1128 endpoint now returns "Nothing found".
- Exact ignored-inclusive lookup for `mediadive.medium:J1128`, `CultureMech:002300`, and `gab_medium_for_strain_egb` covered normalized and generated YAML; it found this maintained MediaDive owner, the TOGO M1208/JCM 1128 snapshot, index entries, and the suffixed generated file.
- The direct MediaDive owner and TOGO M1208 are source-equivalent JCM 1128 snapshots but remain separate records.
- Grounding for the six defined salts is appropriate.

## Evidence

- MediaDive J1128 lists a 1 L main solution containing 1 g NH4Cl, 0.3 g KH2PO4, 0.6 g K2HPO4, 0.5 g MgCl2 x 6 H2O, 0.1 g CaCl2 x 2 H2O, 2 g NaCl, and 956 ml Distilled water; the generated record preserves all six salt amounts.
- JCM 1128 then adds 20 ml 10% Na2CO3 solution, 4 ml 10% Yeast extract solution, and 20 ml 1 M Ammonium ferric citrate solution per liter after autoclaving under N2.
- The generated Na2CO3, Yeast extract, and Ammonium ferric citrate rows convert those stock-addition volumes into 20, 4, and 20 g/L top-level ingredients.
- The pH 8.0-8.2 completion check is present.

## Completeness

- The three post-autoclave stock additions are not represented structurally.
- Stock concentration attributes for 10% Na2CO3, 10% Yeast extract, and 1 M Ammonium ferric citrate are missing.
- The 956 ml source water row is not represented.
- The source-equivalent TOGO M1208 snapshot is not linked or merged with this direct MediaDive owner.

## Findings

- Major: 20 ml 10% Na2CO3, 4 ml 10% Yeast extract, and 20 ml 1 M Ammonium ferric citrate additions are imported as gram-per-liter final-medium rows.
- Minor: the 956 ml Distilled water source row is absent.
- Minor: MediaDive J1128 and TOGO M1208 are unlinked source-equivalent snapshots.

## Recommended Edits

- Rebuild the maintained JCM J1128 record with explicit Na2CO3, Yeast extract, and Ammonium ferric citrate stock additions.
- Preserve the source stock concentrations and 20 ml, 4 ml, and 20 ml per-liter addition volumes.
- Link or merge the direct MediaDive J1128 owner with the TOGO M1208 snapshot after both records normalize to the same stock-aware formula.
- Regenerate `data/merge_yaml/merged/gab_medium_for_strain_egb__0f264cf8.yaml` after normalized/import curation.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated JCM J1128 YAML.
- Confirm no 20 g/L Na2CO3, 4 g/L Yeast extract, or 20 g/L Ammonium ferric citrate top-level rows remain.
- Confirm the generated MediaDive and TOGO JCM 1128 snapshots do not remain divergent solely because one preserves gas rows or stock-addition text differently.

## Additional Notes

- The generated file is derived data and is a one-source merge. The same JCM J1128 stock-addition flattening is present in maintained normalized YAML.
