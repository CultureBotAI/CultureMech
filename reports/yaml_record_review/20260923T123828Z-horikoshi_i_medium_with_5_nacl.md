# YAML Record Review: HORIKOSHI-I MEDIUM WITH 5% NaCl
- Repository: CultureMech
- Record: data/merge_yaml/merged/horikoshi_i_medium_with_5_nacl.yaml
- Started UTC: 2026-09-23T12:37:15Z
- Finished UTC: 2026-09-23T12:38:28Z
- Verdict: needs curation

## Target

Reviewed the generated MediaDive/JCM branch for JCM Medium 406, `HORIKOSHI-I MEDIUM WITH 5% NaCl`, at `data/merge_yaml/merged/horikoshi_i_medium_with_5_nacl.yaml`. The maintained 5% source is `data/normalized_yaml/bacterial/horikoshi_i_medium_with_5_nacl.yaml`; the stale generated artifact also merged `data/normalized_yaml/bacterial/horikoshi_i_medium_with_2_nacl.yaml`, `data/normalized_yaml/bacterial/horikoshi_i_medium_with_3_5_nacl.yaml`, and `data/normalized_yaml/bacterial/JCM_J345_HORIKOSHI-1_MEDIUM_WITH_10_NaCl.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/horikoshi_i_medium_with_5_nacl.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record ID, `original_name`, and `media_term` say this record is the 5% NaCl variant, JCM Medium 406. Its `merged_from`, `curation_history`, and `synonyms` say the 2%, 3.5%, and 10% NaCl variants were merged into the same canonical record, and its visible NaCl amount is 100 g/L from the 10% JCM Medium 345 recipe. This is an identity-level conflation of four distinct salinity variants.

The stale `parent_media` points to the 2% NaCl variant. The maintained September 2026 sources have since repaired all four variants to point to JCM Medium 181 Horikoshi-I medium as their parent.

## Evidence

The inspected JCM records define four different media: JCM 409 is 1 L Horikoshi-I medium plus 20 g NaCl, JCM 1028 is 1 L Horikoshi-I medium plus 35 g NaCl, JCM 406 is 1 L Horikoshi-I medium plus 50 g NaCl, and JCM 345 is 1 L Horikoshi-I medium plus 100 g NaCl. These are distinct 2%, 3.5%, 5%, and 10% salinity variants, not duplicate formulations.

The current maintained normalized sources now encode those four NaCl amounts as 20, 35, 50, and 100 `G_PER_L`, each with a 1000 `ML_PER_L` `Horikoshi-I medium` solution and a `SALINITY_VARIANT` parent link to `data/normalized_yaml/bacterial/horikoshi_i_medium.yaml`.

## Completeness

The generated artifact is missing the JCM 406 50 g/L NaCl amount, models `Horikoshi-I medium` as an ungrounded `1000 G_PER_L` ingredient instead of a 1000 ml parent-medium solution, marks the agar-containing variant as `LIQUID`, and lacks the JCM default autoclave preparation step. The canonical merge also erased the independent 20, 35, and 100 g/L sibling records by folding them into synonyms on the 5% record.

No `target_organisms`, growth metrics, or strain-specific growth evidence are asserted, so there are no over-scoped organism claims to review.

## Findings

- **blocker**: The generated record conflates four distinct JCM salinity variants into one canonical 5% NaCl record.
- **blocker**: The record identified as JCM 406 5% NaCl contains 100 g/L NaCl from JCM 345 instead of the JCM 406 50 g/L amount.
- **major**: The stale `parent_media` points at the 2% NaCl sibling instead of the unsalted JCM Medium 181 Horikoshi-I parent.
- **major**: The 1 L Horikoshi-I parent medium is modeled as `1000 G_PER_L` of an ungrounded ingredient rather than `1000 ML_PER_L` of the CultureMech parent solution.
- **major**: The physical state is `LIQUID`, but the parent Horikoshi-I medium contains agar and the repaired normalized source correctly marks the variant as `SOLID_AGAR`.
- **major**: The default JCM autoclave step is absent.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/` from the four repaired salinity sources so the 2%, 3.5%, 5%, and 10% NaCl variants produce distinct merged artifacts instead of a single merged record.
- Recheck the merge fingerprint for these variants if regeneration still folds 20, 35, 50, and 100 g/L NaCl into one branch.
- For the JCM 406 5% branch, carry through the maintained `50 G_PER_L` NaCl row, `1000 ML_PER_L` CultureMech parent-medium solution, `SOLID_AGAR` physical state, and parent link to `data/normalized_yaml/bacterial/horikoshi_i_medium.yaml`.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation against each regenerated salinity variant.
- Re-open JCM 345, 406, 409, 1028, and 181 to confirm the regenerated variants retain the intended NaCl values and all point to Horikoshi-I medium as their base.
- Run the repository's merge freshness audit to prove the generated salinity variants no longer lag their September 2026 normalized sources.

## Additional Notes

None.
