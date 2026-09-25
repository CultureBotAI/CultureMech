# YAML Record Review: Lowenstein-Jensen Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/lowenstein_jensen_medium.yaml`
- Started UTC: `2026-09-23T20:26:03Z`
- Finished UTC: `2026-09-23T20:27:27Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:010144`
- `name`: `lowenstein_jensen_medium`
- `original_name`: `Lowenstein-Jensen Medium`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `TOGO:M735`
- `merge_fingerprint`: `77db060a9e49664ac71846ed899aaa8fd86f26241dd6c3c2911fe0cb405d807b`
- `merged_from`: `TOGO_M735_Lowenstein-Jensen_Medium`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/lowenstein_jensen_medium.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:010144`, `TOGO:M735`, `JCM_M712`, `GRMD=712`, `lowenstein_jensen_medium`, `Lowenstein-Jensen_Medium`, and the merge fingerprint found the maintained TOGO M735 owner, this generated TOGO M735 record, the maintained MediaDive J712 owner, and a generated MediaDive J712 sibling.
- TOGO M735 identifies the reviewed medium as Lowenstein-Jensen Medium, original media ID `JCM_M712`, and JCM GRMD 712.
- JCM 712 identifies the same `LOWENSTEIN-JENSEN MEDIUM` source and says to use commercially available Lowenstein-Jensen medium slants, BD 220908.
- MediaDive REST resolves JCM J712 to the same JCM source link and carries the same single instruction to use BD 220908 Lowenstein-Jensen medium slants.
- The maintained TOGO M735 owner already resolves the wrapper as a `1000` `ML_PER_L` solution linked to `CultureMech:003059`, but this generated record still emits `Lowenstein--Jensen medium slants (BD 220908)` as a `1` `G_PER_L` ingredient.

## Evidence

- TOGO M735 has one component named `Lowenstein--Jensen medium slants (BD 220908)` with volume 1 L and a comment to use the commercially available BD 220908 slants.
- JCM 712 has no ingredient weights; it directly instructs users to use the commercially available BD 220908 Lowenstein-Jensen medium slants.
- MediaDive J712 has no ingredient rows; its main solution has a single step, `Use commercially available Lowenstein-Jensen medium slants (BD 220908).`
- `data/normalized_yaml/bacterial/TOGO_M735_Lowenstein-Jensen_Medium.yaml` represents that wrapper as a typed solution with concentration `1000` `ML_PER_L`, a `MIX` preparation step, source references, and a `SOURCE_DUPLICATE` parent link to `data/normalized_yaml/bacterial/lowenstein_jensen_medium.yaml`.

## Completeness

- The generated record retains the right CultureMech ID, TOGO ID, JCM ID, and JCM source URL.
- The generated ingredient row has the source label but the wrong slot and dimensionality.
- The generated record is missing the normalized prepared-parent `solutions` entry.
- The generated record is missing the maintained owner preparation step and structured `references`.
- The generated record is missing the reciprocal source-duplicate relationship to the MediaDive J712 `CultureMech:003059` record.

## Findings

1. The commercial slant wrapper is modeled as a 1 g/L ingredient.
   - Evidence: TOGO M735, JCM 712, and MediaDive J712 all describe BD 220908 Lowenstein-Jensen medium slants as a commercial prepared medium to use directly; the generated record stores `Lowenstein--Jensen medium slants (BD 220908)` under `ingredients` with `value: '1'` and `unit: G_PER_L`.
   - Impact: the record treats a 1 L prepared-medium wrapper as if it were one gram of a chemical ingredient.

2. The generated artifact predates the normalized September repair.
   - Evidence: the maintained TOGO owner has the September `RESOLVED_JCM_REFERENCE_WRAPPER_SCORE40` history entry, a `solutions` entry for 1000 ml/L Lowenstein-Jensen Medium, and source references; the generated record was emitted from the stale single-placeholder ingredient form.
   - Impact: the generated page still exposes the pre-repair structural error even though its normalized source has been curated.

3. The JCM 712 duplicate relationship is absent from generated output.
   - Evidence: the maintained TOGO owner links to `CultureMech:003059` / `data/normalized_yaml/bacterial/lowenstein_jensen_medium.yaml` as a `SOURCE_DUPLICATE`, and the JCM and MediaDive source payloads confirm both records refer to JCM 712.
   - Impact: the generated corpus can publish separate TOGO and MediaDive records for the same commercial slant source without indicating that they are equivalent.

4. The generated record has no structured source references.
   - Evidence: the generated record stores the TOGO and JCM URLs only in free text `notes`, while the maintained owner has both URLs in `references`.
   - Impact: reference validation has no structured links to check, and source provenance is harder for downstream users to consume.

## Recommended Edits

1. Regenerate merged YAML after the September repair so TOGO M735 emits the `solutions` wrapper, `MIX` step, `references`, and `SOURCE_DUPLICATE` parent relationship from its maintained owner.
2. Keep the JCM 712 commercial slant as a solution or prepared-parent medium, not as a `G_PER_L` ingredient.
3. Reconcile `CultureMech:010144` and `CultureMech:003059` in generated output so the TOGO M735 and MediaDive J712 imports do not appear as independent recipes.

## Follow-up Checks

- Rebuild merged YAML and confirm no generated `lowenstein_jensen_medium` record contains `Lowenstein--Jensen medium slants (BD 220908)` as a `G_PER_L` ingredient.
- Re-fetch TOGO M735, JCM 712, and MediaDive J712, then confirm the regenerated wrapper still matches the source-level BD 220908 instruction.
- Re-run open schema, strict schema, reference, and term validation on the rebuilt generated record.
- Run an ignored-inclusive exact search for `lowenstein_jensen_medium`, `TOGO:M735`, `JCM_M712`, and `mediadive.medium:J712` to confirm only the intended source-duplicate representation remains active.

## Additional Notes

- Exact duplicate checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.
