# YAML Record Review: Columbia agar with sheep blood

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_agar_with_sheep_blood__5abbf9e3.yaml`
- Started UTC: `2026-09-22T10:24:49Z`
- Finished UTC: `2026-09-22T10:27:45Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:008653` for TOGO Medium `M2062`, `Columbia agar with sheep blood`, generated from `data/normalized_yaml/bacterial/columbia_agar_with_sheep_blood.yaml` on merge fingerprint `5abbf9e3d02aaed4a48994e61ef2aec8b8a2d33c2b9585ca75b9005cfc7375e1`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/columbia_agar_with_sheep_blood__5abbf9e3.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The source identity is correct: TOGO `M2062` is `Columbia agar with sheep blood`, imported from NBRC medium 1365.

TOGO represents the medium as one ready-to-use liter of `Columbia Agar with 5% Sheep Blood (BD-BBL)`. Leaving that commercial product ungrounded is appropriate because the source does not spell out a Columbia agar base formula.

An ignored-inclusive generated-record search found a separate generated record, `data/merge_yaml/merged/Columbia_agar_with_sheep_blood.yaml`, that shares the normalized snake-case name but comes from TOGO M2508, a different Columbia agar with sheep blood source. The search included ignored files.

## Evidence

The TOGO M2062 API supports a single component: `Columbia Agar with 5% Sheep Blood (BD-BBL)`, 1 L, with a 5% concentration annotation. Its comments repeat the BD-BBL ready-to-use product name and say that ready-to-use culture media are available from some distributors.

The generated record no longer matches that source. It stores the one-liter product as `1 G_PER_L`, which turns a final ready-to-use medium volume into a one-gram mass concentration.

## Completeness

The source does not disclose the Columbia agar base ingredients, preparation, pH, or blood source beyond the BD-BBL product name and 5% sheep-blood designation. Those details are correctly unresolved rather than guessed.

The maintained normalized record has already been repaired to `1000 ML_PER_L`, has explicit TOGO/NBRC references, carries `ingredients_curated` and `has_unmapped_ingredients` quality flags, and links the matching TOGO M2772 BD-BBL plate record as a source duplicate. This generated record predates that repair.

No target organism or growth evidence is present. That is an empty optional area in this source-only record.

## Findings

- Major: `Columbia Agar with 5% Sheep Blood (BD-BBL)` is stored as `1 G_PER_L`; TOGO lists 1 L of the ready-to-use product.
- Major: the generated record is stale relative to the repaired maintained input, missing the `1000 ML_PER_L` representation, explicit references, curated quality flags, and the M2772 source-duplicate link.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/bacterial/columbia_agar_with_sheep_blood.yaml` so the generated TOGO M2062 record uses `1000 ML_PER_L` and carries the repaired provenance.
- After regeneration, verify the TOGO M2772 source-duplicate link survives and does not accidentally merge M2062 with the broader M2508 Columbia agar with sheep blood source.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm the generated ingredient concentration is `1000 ML_PER_L`, not `1 G_PER_L`.
- Confirm TOGO M2062 still contains exactly one intentionally ungrounded BD-BBL ready-to-use component.
- Confirm the generated record carries the M2772 source-duplicate child link from the normalized input.

## Additional Notes

Empty optional fields are not defects.
