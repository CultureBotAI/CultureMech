# YAML Record Review: thiomonas_cuprina_medium__c5dba07d

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thiomonas_cuprina_medium__c5dba07d.yaml`
- Started UTC: 2026-09-25T13:08:31Z
- Finished UTC: 2026-09-25T13:08:31Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009546`
- Name: `thiomonas_cuprina_medium`
- Source grounding: TOGO Medium M3034, original source NBRC_M929-1

## Validation

- Schema validation: passed with no issues.
- Strict validation: passed with zero errors; `/private/tmp/thiomonas_cuprina_medium__c5dba07d.strict.tsv` was header-only.
- Reference validation: passed; exited 0 with no diagnostics.
- Term validation: passed after the known EUtils warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The `media_term` points to `TOGO:M3034`, the sulfur-powder NBRC 929 variant.
- NBRC 929 is a single base medium with post-autoclave alternatives; M3034 corresponds to sterile sulfur powder 0.05%.
- The scoped source search found the related NBRC 929 sibling variants, including TOGO M3035 and M3036, but did not find a second M3034 record. The search included ignored and hidden files.

## Evidence

- NBRC 929 lists KCl 0.33 g, MgCl2 x 6 H2O 2.75 g, MgSO4 x 7 H2O 3.45 g, NH4Cl 1.25 g, CaCl2 x 2 H2O 0.14 g, K2HPO4 0.18 g, KH2PO4 0.14 g, NaCl 0.5 g, 1 ml trace element solution, and 1 L distilled water for the parent recipe.
- The pH is adjusted to 3.5 with sulfuric acid before autoclaving.
- The trace solution is a 1 L stock dosed at 1 ml/L, not a collection of final 30 g/L MgSO4 x 7 H2O, 5 g/L MnSO4 x H2O, 10 g/L NaCl, 1.8 g/L CoCl2 x 6 H2O, and similar stock-strength rows.
- M3034 adds sterile sulfur powder as the 0.05% NBRC 929 post-autoclave variant.

## Completeness

- The generated record carries the source main salts, the sulfur-powder alternative, the sulfuric acid pH adjustment, and all trace-stock components.
- The generated record has no `target_organisms`; there are no growth claims to verify.

## Findings

- The 1 ml/L trace element stock is flattened into final ingredients at stock concentration.
- Duplicate cleanup summed stock MgSO4 x 7 H2O, NaCl, and CaCl2 x 2 H2O into the parent main salts, producing the same 1000x trace-stock inflation seen in the M3036 sibling.
- Stock water was added to the parent solvent row as `2.0` `G_PER_L`.
- `Trace element solution*` is retained as a separate solution at `1` `G_PER_L` with no stock topology.
- Sulfur powder is marked `VARIABLE` even though NBRC gives the M3034 addition as 0.05%.

## Recommended Edits

- Restore the NBRC trace element solution as a nested 1 L stock dosed at 1 ml/L.
- Keep main-recipe MgSO4 x 7 H2O, NaCl, and CaCl2 x 2 H2O distinct from trace-stock components until final concentrations are intentionally calculated.
- Convert or explicitly model the 0.05% sulfur-powder addition.
- Link the M3034, M3035, and M3036 records as variants of the shared NBRC 929 base.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after stock reconstruction.
- Verify the corrected variant does not reintroduce unitless water or `G_PER_L` rows for ml stock additions.

## Additional Notes

- Empty optional fields were not treated as defects.
