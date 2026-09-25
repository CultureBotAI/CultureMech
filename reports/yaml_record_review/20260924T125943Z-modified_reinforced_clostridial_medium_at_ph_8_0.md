# YAML Record Review: modified_reinforced_clostridial_medium_at_ph_8_0

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_reinforced_clostridial_medium_at_ph_8_0.yaml
- Started UTC: 2026-09-24T12:59:43Z
- Finished UTC: 2026-09-24T13:00:44Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:002442`, `modified_reinforced_clostridial_medium_at_ph_8_0`, generated from `data/normalized_yaml/bacterial/modified_reinforced_clostridial_medium_at_ph_8_0.yaml` plus `data/normalized_yaml/bacterial/modified_reinforced_clostridial_medium.yaml`.
- The record represents MediaDive `J1276`, sourced from JCM `GRMD=1276`, named `MODIFIED REINFORCED CLOSTRIDIAL MEDIUM AT pH 8.0`.
- The generated MediaDive record was compared with JCM `GRMD=1276`, MediaDive `J1276`, and the curated TOGO `M1372` pH-variant record for the same JCM source.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` reported no issues.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- JCM `GRMD=1276` and MediaDive `J1276` identify Modified Reinforced Clostridial Medium at pH 8.0 by reference to JCM Medium 1217.
- The record is not a source duplicate of the pH 6.0-6.5 parent; it is a pH variant that adjusts the complete parent medium to pH 8.0.
- A gitignore-independent exact search for the JCM/MediaDive identifiers found a curated TOGO maintained record, `data/normalized_yaml/bacterial/TOGO_M1372_Modified_Reinforced_Clostridial_Medium_AT_pH_8.0.yaml`, that already models JCM `GRMD=1276` as a `PH_VARIANT`.
- `Yeast extract`, `Tryptone`, and `Beef extract` are ungrounded.
- No inspected source payload identified a target organism for this medium.

## Evidence

- JCM `GRMD=1276` says to use JCM Medium 1217 adjusted to pH 8.0.
- MediaDive `J1276` preserves the same instruction as a one-step formula with no local ingredient rows.
- JCM `GRMD=1217` is Modified Reinforced Clostridial Medium whose non-solid base has Yeast extract, Tryptone, Beef extract, Glucose, L-Cysteine HCl x H2O, NaCl, Sodium acetate, Soluble starch, and 1 L distilled water, adjusted to pH 6.0-6.5.
- The curated TOGO `M1372` normalized record resolves JCM 1276 as a pH 8.0 variant of TOGO `M1305` / JCM 1217, with `variant_relationship: PH_VARIANT` and a `parent_media` link to that parent.

## Completeness

- The copied JCM 1217 ingredients are present.
- The pH 8.0 instruction survives only in a preparation step and is not represented as structured `ph_value: 8.0`.
- The pH 8.0 variant and pH 6.0-6.5 parent were merged together on identical ingredient fingerprint.
- The generated record carries `variant_relationship: SOURCE_DUPLICATE`, which contradicts the pH-variant semantics.
- The curated TOGO `M1372` `PH_VARIANT` metadata, references, pH value, and preparation steps are absent from this generated record.

## Findings

- Blocker: the pH 8.0 variant was merged with the referenced pH 6.0-6.5 parent as a source duplicate because the copied ingredient signature is identical. This collapses a biologically meaningful pH variant into its parent medium.
- Major: the generated record records `SOURCE_DUPLICATE` instead of `PH_VARIANT`, despite the source instruction being exactly the pH 8.0 modification.
- Major: structured `ph_value: 8.0` is absent; pH 8.0 appears only in prose.
- Major: already-curated TOGO `M1372` pH-variant fields, including `parent_media`, `references`, `data_quality_flags`, and structured preparation steps, are not reflected in the generated record.

## Recommended Edits

- Exclude pH variants from ingredient-fingerprint duplicate merging, or include pH and variant relationship in the merge key.
- Preserve JCM 1276 as a `PH_VARIANT` of JCM 1217 / TOGO M1305 rather than a `SOURCE_DUPLICATE`.
- Set structured `ph_value: 8.0` on the generated pH variant.
- Reconcile MediaDive `J1276` with curated TOGO `M1372` so the generated record keeps the curated pH-variant metadata and references.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting pH-variant merge behavior.
- Recompare the regenerated record against JCM `GRMD=1276`, MediaDive `J1276`, and curated TOGO `M1372`.
- Confirm that `modified_reinforced_clostridial_medium_at_ph_8_0.yaml` is no longer merged as a source duplicate of `modified_reinforced_clostridial_medium.yaml`.

## Additional Notes

None found.
