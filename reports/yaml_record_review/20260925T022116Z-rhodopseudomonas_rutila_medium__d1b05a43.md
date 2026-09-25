# YAML Record Review: rhodopseudomonas_rutila_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rhodopseudomonas_rutila_medium__d1b05a43.yaml`
- Started UTC: 2026-09-25T02:21:15Z
- Finished UTC: 2026-09-25T02:21:25Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:001764` for DSMZ Medium 633 / `mediadive.medium:633`, generated from `data/normalized_yaml/bacterial/rhodopseudomonas_rutila_medium.yaml`.

## Validation

- Open schema validation: passed with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The target ID, label, category, and `mediadive.medium:633` grounding match DSMZ Medium 633. An exact ignored-inclusive search for `TOGO:M87`, `mediadive.medium:J95`, `mediadive.medium:633`, `JCM_M95`, `GRMD=95`, and `DSMZ_Medium633` found the expected DSMZ, TOGO, and JCM Rhodopseudomonas rutila owners and generated records under the relevant data trees.

DSMZ 633 should stay distinct from JCM 95: they share most of the recipe, but DSMZ 633 lists MnSO4 x H2O, thiamine-HCl x 2H2O, and 1 mg/L biotin, while JCM 95 lists MnSO4 x n H2O, thiamine HCl, and 0.01 mg/L biotin.

## Evidence

The DSMZ 633 PDF and MediaDive 633 list 2 g yeast extract, 2 g Na-L-malate, 2 g Na glutamate, 1 g KH2PO4, 0.5 g NaHCO3, 0.2 g MgSO4 x 7H2O, 0.1 g CaCl2 x 2H2O, 2 mg MnSO4 x H2O, 0.5 mg FeSO4 x 7H2O, 0.5 mg CoCl2 x 6H2O, 1 mg thiamine-HCl x 2H2O, 1 mg nicotinic acid, 1 mg biotin, and 1000 ml distilled water.

The generated target preserves the 13 non-water ingredient amounts and hydrate labels from DSMZ 633, but omits the final 1000 ml distilled-water row.

## Completeness

The source water row is missing. The JCM 95 recipe has a separate generated target with the same label and no curated relationship to DSMZ 633, so users cannot tell that the two Rhodopseudomonas rutila recipes are near variants rather than exact duplicates.

Empty optional pH, literature, and organism fields are not defects; DSMZ 633 does not provide them.

## Findings

- Major: `data/normalized_yaml/bacterial/rhodopseudomonas_rutila_medium.yaml` omits the 1000 ml distilled-water row that DSMZ 633 and MediaDive 633 list.
- Major: the generated corpus leaves DSMZ 633, JCM J95, and TOGO M87 as three unconnected Rhodopseudomonas rutila targets. JCM J95 and TOGO M87 need source-deduplication, and DSMZ 633 needs a separate curated relationship that preserves its different biotin concentration and hydrate forms.

## Recommended Edits

- Add the 1000 ml/L distilled-water row to `data/normalized_yaml/bacterial/rhodopseudomonas_rutila_medium.yaml`.
- Curate an explicit relationship from DSMZ 633 to the JCM 95 duplicate set, such as a concentration or provider variant, without merging DSMZ 633 as a source duplicate.
- Regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation for regenerated DSMZ 633.
- Confirm the regenerated DSMZ 633 target has 14 recipe rows, including distilled water.
- Confirm DSMZ 633 remains separate from JCM 95 but records a curated relationship to it.

## Additional Notes

No additional issues.
