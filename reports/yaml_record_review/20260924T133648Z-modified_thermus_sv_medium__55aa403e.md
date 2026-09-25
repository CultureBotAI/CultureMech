# YAML Record Review: modified_thermus_sv_medium__55aa403e
- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_thermus_sv_medium__55aa403e.yaml
- Started UTC: 2026-09-24T13:35:56Z
- Finished UTC: 2026-09-24T13:36:48Z
- Verdict: needs curation

## Target
Generated merged YAML for `modified_thermus_sv_medium`, CultureMech ID `CultureMech:002971`.

- Reviewed generated record: `data/merge_yaml/merged/modified_thermus_sv_medium__55aa403e.yaml`
- Reviewed normalized source: `data/normalized_yaml/bacterial/modified_thermus_sv_medium.yaml`
- Media term: `mediadive.medium:J625`, `MODIFIED THERMUS SV MEDIUM`
- Source note: `JCM | Link: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=625`
- Referenced base: JCM Medium 624, `MODIFIED THERMUS MEDIUM WITH 3% NaCl`
- Merge fingerprint: `55aa403eb26f8343ae457db5124cea1f3c161c384027e2b03502e55f4bda541b`

## Validation
- Open LinkML validation: Passed, `No issues found`.
- Strict validation: Passed with 0 error rows across 1 file. The strict TSV had 1 line, the header only.
- LinkML reference validation: Passed; 1 file validated, 0 checks, all validations passed.
- LinkML term validation: Passed; emitted the known `eutils`/`pkg_resources` deprecation warning and exited 0.
- Embedded `curation_history`: Not checked; the available history validator targets standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding
The JCM identity for `J625` is coherent, but the merged ingredient list does not represent `J625` chemistry.

JCM Medium 625 is a supplement recipe: it uses JCM Medium 624 and adds 3.0 g/L L-proline, with 10 ml/L trace vitamins from JCM Medium 197 as a possible substitute. The generated record instead copied an old resolved version of JCM Medium 624 and lacks the defining L-proline or trace-vitamin supplement.

Grounding is partially stale:

- `Sodium glutamate monohydrate`, `NaCl`, `Nitrilotriacetic acid`, `CaSO4 x 2 H2O`, `MgSO4 x 7 H2O`, and `FeCl3 x 6 H2O` are grounded.
- `KNO3` and `NaNO3` still carry legacy `mediaingredientmech_term` links instead of `mediaingredientmech_chebi_term`.
- The omitted `L-proline` has no structured CHEBI grounding.

## Evidence
The live JCM `GRMD=625` page resolves and states that Medium 625 uses Medium 624 supplemented with 3.0 g/L L-proline; it also says trace vitamins from Medium 197 at 10 ml/L can be substituted for L-proline.

The live MediaDive `J625` payload mirrors that instruction as the only step in `Main sol. J625`.

The normalized `modified_thermus_sv_medium.yaml` was populated in 2026-04 by copying 11 ingredients from `CultureMech:002970`, the old J624 base. That copied state predates the 2026-09-11 repairs to the J624 records and to the Castenholz basal salt solution.

## Completeness
The generated recipe is incomplete and over-flattened. It does not contain L-proline, does not model the optional Medium 197 trace-vitamin substitution, and does not retain JCM 624 as a base-medium reference. Its Castenholz-derived rows are copied as final ingredients from the old J624 flattening, including a summed NaCl row and `FeCl3 x 6 H2O` at `10 G_PER_L`.

The generated record also merged the J625 source with the J624 source on the same fingerprint, but those are not duplicates: J625 is J624 plus a supplement.

## Findings
1. Needs curation - the defining 3.0 g/L L-proline supplement is missing from the structured recipe.

2. Needs curation - the optional 10 ml/L trace vitamins substitution from Medium 197 is only prose and has no structured solution reference.

3. Needs curation - the J624 base was copied from an obsolete flattened representation. `NaCl` is a sum of base NaCl plus Castenholz stock NaCl, Castenholz salts are listed as final ingredients, and `FeCl3 x 6 H2O` appears as `10 G_PER_L` even though JCM 273 contributes 10 ml/L of a 0.03% solution to the Castenholz stock.

4. Needs curation - `modified_thermus_sv_medium` was merged with `modified_thermus_medium_with_3_nacl` as a duplicate. J625 should remain a derived variant of J624 because it adds L-proline or trace vitamins.

5. Minor - `KNO3` and `NaNO3` still have legacy `mediaingredientmech_term` links despite their primary CHEBI grounding.

## Recommended Edits
- Recurate `data/normalized_yaml/bacterial/modified_thermus_sv_medium.yaml` from live JCM `625` and MediaDive `J625`.
- Represent JCM Medium 624 as the base recipe or copy from the repaired J624 normalized source, not from the 2026-04 flattened snapshot.
- Add 3.0 g/L L-proline as the structured default supplement.
- Represent the Medium 197 trace vitamins substitution as an optional 10 ml/L solution reference rather than merging it into the default ingredient list.
- Prevent J625 from fingerprint-merging with J624 after the L-proline supplement is present.
- Replace the remaining `KNO3` and `NaNO3` legacy MediaIngredientMech links with CHEBI-keyed links during the repair.

## Follow-up Checks
- Re-fetch JCM `GRMD=625` and confirm that the repaired J625 YAML has JCM 624 plus L-proline as its default formula.
- Confirm that the regenerated J625 artifact no longer merges with J624 on the same fingerprint.
- Revalidate the regenerated YAML with open LinkML, strict schema, reference, and term validators.

## Additional Notes
None found.
