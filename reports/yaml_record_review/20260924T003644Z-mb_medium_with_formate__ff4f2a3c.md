# YAML Record Review: MB MEDIUM WITH FORMATE

- Repository: CultureMech
- Record: `data/merge_yaml/merged/mb_medium_with_formate__ff4f2a3c.yaml`
- Started UTC: 2026-09-24T00:35:25Z
- Finished UTC: 2026-09-24T00:36:43Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/mb_medium_with_formate__ff4f2a3c.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:003033`
- Name: `mb_medium_with_formate`
- Original name: `MB MEDIUM WITH FORMATE`
- Source accession: `mediadive.medium:J688`, labeled `MB MEDIUM WITH FORMATE`
- Maintained owner for future fixes: no normalized content edit is indicated before regeneration; the corrected owner is already `data/normalized_yaml/bacterial/mb_medium_with_formate.yaml`
- Generated status: stale generated canonical merge of one normalized record. The generated file was last merged on 2026-08-06 from the pre-repair `mb_medium_with_formate.yaml` content and does not include the owner repair event dated 2026-09-10.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mb_medium_with_formate__ff4f2a3c.yaml` exited 0 with no diagnostics. |
| Strict schema | Passed. `scripts/validate_strict.py data/merge_yaml/merged/mb_medium_with_formate__ff4f2a3c.yaml --out /private/tmp/mb_medium_with_formate__ff4f2a3c.strict.tsv --workers 1 --quiet` scanned 1 file with 0 error rows; the TSV was header-only. |
| References | Passed. `linkml-reference-validator validate data data/merge_yaml/merged/mb_medium_with_formate__ff4f2a3c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` exited 0 with 0 checks and no failures. |
| Terms | Passed. `linkml-term-validator validate-data data/merge_yaml/merged/mb_medium_with_formate__ff4f2a3c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. It emitted the expected `eutils` `pkg_resources` warning before reporting `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The generated record is intended to denote JCM/MediaDive J688, `MB MEDIUM WITH FORMATE`. The `media_term`, `kg_microbe_match`, original name, and MediaDive J688 REST payload all agree on that identity.

The formula content no longer denotes that full medium. MediaDive J688 describes the medium as Medium 687 with its methanol solution replaced by sodium formate solution, but the generated record contains only the 136 g/L sodium formate stock. It omits the Medium 687 Solution A salts, yeast extract, Trypticase peptone, bicarbonate, gas handling, trace minerals, selenite-tungstate solution, trace vitamins, and 5 percent cysteine and sulfide additions.

The direct normalized owner has already been repaired with a 2026-09-10 curation event, rich `ingredients:`, `solutions:`, `references:`, and an explanatory source note for TOGO M708/JCM 688. The generated file lacks all of that because it predates the repair.

## Evidence

### Supported

- MediaDive J688 supports the source identity and the source instruction to use Medium 687, replacing methanol solution with sodium formate solution.
- MediaDive J688 supports the sodium formate stock strength: 6.8 g sodium formate in 50 ml water, equivalent to 136 g/L.
- The live JCM 687 page supports the MB MEDIUM WITH METHANOL base formula that J688 modifies: Solution A contains NaCl, yeast extract, Trypticase peptone, NH4Cl, MgCl2 x 6 H2O, KCl, CaCl2 x 2 H2O, K2HPO4, resazurin, 10 ml trace minerals, 1 ml selenite-tungstate solution, 4 g NaHCO3, and 920 ml distilled water.
- The live JCM 151, 431, and 197 pages support the trace-minerals, selenite-tungstate, and trace-vitamin stock formulas referenced by Medium 687.

### Unsupported or over-scoped

- A one-ingredient root recipe with 136 `G_PER_L` sodium formate is not supported as the full J688 medium. That amount describes the sodium formate stock, not the final medium.
- The generated record's only preparation step, `Use Medium No. 687, replacing Methanol solution with Sodium formate solution (see below).`, cannot be executed from the generated YAML because the referenced Medium 687 base formula and the sodium formate stock boundary are absent.

## Completeness

- A gitignore-independent exact field scan of `data/merge_yaml/merged/mb_medium_with_formate__ff4f2a3c.yaml`, `data/normalized_yaml/bacterial/mb_medium_with_formate.yaml`, and `data/normalized_yaml/bacterial/TOGO_M708_MB_Medium_With_Formate.yaml` confirmed that the generated file has no top-level `solutions:`, `references:`, or `target_organisms:` slots, while the repaired direct owner does have `solutions:` and `references:`.
- Missing `solutions:` is a blocker in the generated record because sodium formate is a stock solution, and every supporting source defines J688 by substitution into a stock-rich Medium 687 formula.
- Missing `references:` is a staleness symptom in the generated record; the repaired direct owner now carries references for JCM 688 and TOGO M708/M142/M190/M431.
- Missing `target_organisms:` is acceptable. Neither the inspected MediaDive J688 JSON nor the related JCM stock pages asserted a specific growth outcome for a named organism.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The generated J688 record is stale and represents only the sodium formate stock, not MB MEDIUM WITH FORMATE. | The generated file has one root ingredient, `Sodium formate` at 136 `G_PER_L`, which MediaDive identifies as the 50 ml sodium formate stock for J688. The current normalized owner has been repaired with Solution A, stock additions, and references, but the generated merge predates that repair. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/bacterial/mb_medium_with_formate.yaml`; no direct normalized edit is indicated by this review. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/mb_medium_with_formate__ff4f2a3c.yaml` from the current `data/normalized_yaml/bacterial/mb_medium_with_formate.yaml`.
2. Verify that the regenerated record includes the repaired Solution A root ingredients, `solutions:` entries for trace minerals, selenite-tungstate solution, the 5 percent sulfide and cysteine additions, sodium formate solution, and trace vitamins, plus the 2026-09-10 `RESOLVED_JCM_688_MB_FORMATE_SCORE20` history entry.
3. If regeneration still emits a one-ingredient sodium-formate-only record, inspect the merge generator for stale source reads or filtering of repaired normalized fields before changing recipe content.

## Follow-up Checks

- Run the merge freshness check after regenerating and compare the generated J688 YAML against its normalized owner.
- Run open schema, strict schema, reference, and term validation on the regenerated J688 merged record.
- Manually spot-check the regenerated stock contents against JCM 687, JCM 151, JCM 431, JCM 197, and the MediaDive J688 sodium formate solution payload.

## Additional Notes

- The live JCM `GRMD=688` page returned `Nothing found`; the current J688 identity and sodium-formate stock were therefore checked through MediaDive. The related JCM `GRMD=687`, `151`, `431`, and `197` pages were live.
- The TOGO M708 normalized sibling was inspected as a same-source import, but it is not the generated record's owner and does not need to be merged into this canonical file to resolve the observed stale-output defect.
- This review did not patch generated YAML, normalized YAML, or GitHub state.
