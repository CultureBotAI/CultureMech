# YAML Record Review: Lowenstein-Jensen Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/lowenstein_jensen_medium__f8a67c53.yaml`
- Started UTC: `2026-09-23T20:27:28Z`
- Finished UTC: `2026-09-23T20:28:32Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:003059`
- `name`: `lowenstein_jensen_medium`
- `original_name`: `LOWENSTEIN-JENSEN MEDIUM`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `mediadive.medium:J712`
- `merge_fingerprint`: `f8a67c53302e1826c9aabcadcde38b3955c1f5d583664e0d4996bb44387cca83`
- `merged_from`: `lowenstein_jensen_medium`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/lowenstein_jensen_medium__f8a67c53.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:003059`, `mediadive.medium:J712`, `JCM_M712`, `GRMD=712`, `lowenstein_jensen_medium`, `Lowenstein-Jensen_Medium`, and the merge fingerprint found the maintained MediaDive J712 owner, this generated MediaDive J712 record, the TOGO M735 same-source owner, and a generated TOGO M735 sibling.
- JCM 712 identifies the source as `LOWENSTEIN-JENSEN MEDIUM` and instructs users to use commercially available Lowenstein-Jensen medium slants, BD 220908.
- MediaDive REST resolves JCM J712 to the same JCM source link and the same BD 220908 commercial-slant instruction.
- TOGO M735 also resolves to original media ID `JCM_M712`, confirming that the TOGO and MediaDive records describe the same JCM 712 source.
- The maintained MediaDive J712 owner now has a `SOURCE_DUPLICATE` child link to the TOGO M735 owner, but this generated record was emitted before that September relationship was added.

## Evidence

- The JCM and MediaDive sources provide the commercial product instruction but do not list the expanded BD 220908 formula.
- The generated record expands BD 220908 into eight locally curated ingredients: L-asparagine, monopotassium phosphate, magnesium sulfate, magnesium citrate, potato flour, glycerol, malachite green, and whole eggs.
- Each expanded ingredient cites only `BD 220908` in a free-text `source` field; there is no `references` block with a BD, JCM, or MediaDive source URL.
- The `Magnesium citrate` ingredient maps to `CHEBI:6637` with label `magnesium dihydroxide`, which does not match the preferred term.

## Completeness

- The generated record carries the expanded commercial-product ingredient list and the JCM 712 preparation step.
- Whole eggs are represented as `variable` `VARIABLE`, with the 1000 ml per 600 ml base quantity preserved in notes rather than a structured recipe ratio.
- The generated record has no structured references for the JCM/MediaDive source or for the BD 220908 ingredient expansion.
- The generated record has no source-duplicate link to the TOGO M735 `CultureMech:010144` sibling.

## Findings

1. One curated ingredient has the wrong ontology mapping.
   - Evidence: the row named `Magnesium citrate` maps to `CHEBI:6637` with label `magnesium dihydroxide`.
   - Impact: downstream ChEBI consumers will read the ingredient as magnesium dihydroxide rather than magnesium citrate.

2. The BD 220908 expansion is not traceable to a structured formula reference.
   - Evidence: JCM 712 and MediaDive J712 only instruct users to use BD 220908 commercial slants, and the generated record gives each expanded ingredient a free-text `source: BD 220908` but no `references` entry for a BD formula or instructions-for-use document.
   - Impact: the expanded formula is not independently auditable from the generated YAML.

3. The same JCM 712 source is still emitted as a separate TOGO generated record.
   - Evidence: TOGO M735 reports original media ID `JCM_M712`, the maintained MediaDive J712 owner links to the TOGO owner as a `SOURCE_DUPLICATE`, and `data/merge_yaml/merged/lowenstein_jensen_medium.yaml` is a separate generated record for TOGO M735.
   - Impact: the generated corpus can show two active Lowenstein-Jensen records for one JCM source without carrying the curated equivalence relationship.

4. The whole-egg quantity remains partly unstructured.
   - Evidence: the generated `Whole eggs` ingredient has concentration `variable` / `VARIABLE` while `1000 mL per 600 mL base` is stored only in `notes`.
   - Impact: the key egg-to-base ratio in this commercial formulation is not machine-actionable.

## Recommended Edits

1. Correct the `Magnesium citrate` term to a magnesium citrate ChEBI entry before regenerating output.
2. Add structured references for the JCM source, the MediaDive J712 source, and the BD 220908 formula used by `expand_lowenstein_jensen`.
3. Rebuild merged YAML after the September source-duplicate link so JCM J712 and TOGO M735 are reconciled in generated output.
4. Represent the whole-egg addition with a structured relative quantity if the schema can express the 1000 ml per 600 ml base ratio; otherwise, retain `VARIABLE` and document the schema limitation explicitly.

## Follow-up Checks

- Re-run term validation after correcting the magnesium citrate mapping and confirm the row no longer labels it as magnesium dihydroxide.
- Re-fetch JCM 712, MediaDive J712, and TOGO M735 to verify all three sources still point to the same BD 220908 commercial slant.
- Re-run open schema, strict schema, reference, and term validation on the rebuilt record.
- Run an ignored-inclusive exact search for `lowenstein_jensen_medium`, `TOGO:M735`, `JCM_M712`, and `mediadive.medium:J712` to confirm the generated source-duplicate relationship is visible.

## Additional Notes

- Exact duplicate checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.
