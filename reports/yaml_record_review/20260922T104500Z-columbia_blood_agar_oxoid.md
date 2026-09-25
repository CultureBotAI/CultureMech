# YAML Record Review: Columbia blood agar (Oxoid)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_blood_agar_oxoid.yaml`
- Started UTC: `2026-09-22T10:42:47Z`
- Finished UTC: `2026-09-22T10:45:00Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:008812` for TOGO Medium `M2224`, `Columbia blood agar (Oxoid)`, generated from `data/normalized_yaml/bacterial/columbia_blood_agar_oxoid.yaml` on merge fingerprint `423fbc273c9fed40b8be3c68547c7a6b8c692f8e64311c2501e1a7433ebad7ff`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/columbia_blood_agar_oxoid.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The TOGO identity is coherent: TOGO `M2224` names `Columbia blood agar (Oxoid)`, reports final pH `7.3 +/- 0.2`, and describes a formula made from 1 L distilled water plus 39 g Oxoid Columbia blood agar.

The ingredient topology is wrong in the maintained normalized input and the generated record. TOGO exposes sodium chloride, starch, agar, and special peptone under a nested `Columbia blood agar (Oxoid)` subcomponent, so those rows are the disclosed composition of the 39 g Oxoid product. The local record flattens the 39 g product and each disclosed product constituent into sibling top-level ingredients, which double counts the agar base.

## Evidence

The TOGO `M2224` structured payload supports two preparation-level items: 1 L distilled water and 39 g Columbia blood agar (Oxoid). It also supports the Oxoid product's 39 g composition as 5 g sodium chloride, 1 g starch, 10 g agar, and 23 g Special peptone.

The record keeps the 39 g product row and the four internal product rows at the same top level. It also converts the 1 L water row to `1 G_PER_L` rather than `1000 ML_PER_L`, and it does not retain the source pH.

## Completeness

The record needs a source-faithful representation for the commercial base's disclosed internals. That could be an opaque 39 g/L Oxoid Columbia blood agar product row, or an expanded base composition, but not both as independent top-level ingredients.

No target organism or growth evidence is present. That is an empty optional area in this source-only TOGO recipe.

The TOGO API has an empty `src_url`, and an ignored-inclusive local search found only TOGO import and index references to `M2224`, with no PMID, DOI, or cached original paper.

## Findings

- Major: the 39 g/L Oxoid Columbia blood agar product is double counted by sibling sodium chloride, starch, agar, and special peptone rows that are only the product's disclosed subcomposition.
- Major: distilled water is represented as `1 G_PER_L`; TOGO lists `1 L`.
- Minor: final pH `7.3 +/- 0.2` at 25 C is present in TOGO but absent from the YAML.

## Recommended Edits

- In `data/normalized_yaml/bacterial/columbia_blood_agar_oxoid.yaml`, either keep `Columbia blood agar (Oxoid)` as the single 39 g/L product or replace it with a source-scoped expanded composition; do not keep both at the same ingredient level.
- Change `Distilled water` from `1 G_PER_L` to `1000 ML_PER_L`.
- Preserve TOGO `M2224` as a `references` entry and add ingredient `source` notes for the top-level formula.
- Add a preparation step or condition note for final pH `7.3 +/- 0.2` at 25 C.
- Regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm the Oxoid product composition is no longer double counted.
- Confirm the water row is `1000 ML_PER_L`, not `1 G_PER_L`.
- Confirm pH 7.3 and the TOGO M2224 source URL survive in the regenerated output.

## Additional Notes

The searches for a local original-paper reference included ignored files.
