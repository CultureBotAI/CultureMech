# YAML Record Review: brain-heart infusion broth (supplemented with 0.1% Tris base and 0.001% thiamine monophosphate)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_0_1_tris_base_and_0_001_thiamine_monophosphate.yaml
- Started UTC: 2026-09-22T00:07:27Z
- Finished UTC: 2026-09-22T00:08:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009497 |
| Label | brain-heart infusion broth (supplemented with 0.1% Tris base and 0.001% thiamine monophosphate) |
| Source accession | TOGO:M2974 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_broth_supplemented_with_0_1_tris_base_and_0_001_thiamine_monophosphate.yaml |
| Generated status | Generated merge with one normalized owner; stale relative to its owner |
| Merge fingerprint | d19e7f4c3f759a198af6ebfddfd7f41cd1fe97c6584c7886b1a6fdd095ce573c |

The reviewed file is the generated TOGO M2974 BHI-TT record. Its normalized
owner already contains a later targeted repair; future work should regenerate
merged YAML from the maintained owner rather than hand-edit this derived file.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_0_1_tris_base_and_0_001_thiamine_monophosphate.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_0_1_tris_base_and_0_001_thiamine_monophosphate.yaml --out /private/tmp/brain_heart_infusion_broth_supplemented_with_0_1_tris_base_and_0_001_thiamine_monophosphate.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_0_1_tris_base_and_0_001_thiamine_monophosphate.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_0_1_tris_base_and_0_001_thiamine_monophosphate.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `TOGO:M2974` identifies BHI-TT: brain-heart infusion broth from Difco
  Laboratories supplemented with 0.1% Tris base and 0.001% thiamine
  monophosphate.
- TOGO M2974 lists 1 L prepared brain-heart infusion broth, 0.1% Tris, and
  0.001% thiamine monophosphate.
- A local repair script, `scripts/repair_togo_m2974_bhi_tt_score15.py`, rewrote
  the normalized owner on 2026-09-11 to store the BHI row as `1000.0 ML_PER_L`,
  ground thiamine monophosphate to `CHEBI:9533`, preserve source notes, add a
  preparation step, and add a TOGO reference.
- The generated record was emitted on 2026-08-06, before that repair, and still
  has the original imported `1 G_PER_L` BHI row.
- A gitignore-independent exact search for `TOGO:M2974`,
  `CultureMech:009497`, the merge fingerprint, and the normalized slug covered
  generated records, normalized records, local indexes, reports, source,
  scripts, `justfile`, and `.claude`; it found the single normalized owner, the
  stale generated record, and the focused repair script.

The record's identity is correct, but the generated artifact is stale relative
to its already-corrected maintained owner.

## Evidence

TOGO M2974 supports 1 L prepared brain-heart infusion broth from Difco
Laboratories supplemented with 0.1% Tris base and 0.001% thiamine
monophosphate. The generated record incorrectly stores that 1 L source volume
as `1 G_PER_L`.

The maintained owner already corrects the BHI row to `1000.0 ML_PER_L`, records
that TOGO does not spell out the commercial broth composition, grounds
thiamine monophosphate to `CHEBI:9533`, and models a `MIX` preparation step for
the supplementation.

The reviewed merge lacks the maintained owner's 2026-09-11
`RESOLVED_TOGO_M2974_BHI_TT_SCORE15` curation event, source notes,
`references`, `data_quality_flags`, corrected ingredient order, corrected
units, and preparation step, confirming this is a stale generated file rather
than an unresolved normalized-owner defect.

## Completeness

- Consequential gap: the generated BHI row has the wrong unit and value.
- Consequential gap: the generated thiamine monophosphate row lacks the owner
  record's CHEBI grounding.
- Consequential gap: the generated file lacks the owner record's TOGO reference
  and source-preserving notes.
- Consequential gap: the generated file lacks the owner record's BHI-TT mixing
  step and quality flags.
- A gitignore-independent exact search under `reports/yaml_record_review` for
  the normalized slug, the M2974 merge fingerprint, `CultureMech:009497`, and
  `TOGO:M2974` found no prior report for this target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale relative to the maintained owner. | The generated record was emitted on 2026-08-06 and stores the TOGO 1 L BHI component as `1 G_PER_L`; `data/normalized_yaml/bacterial/brain_heart_infusion_broth_supplemented_with_0_1_tris_base_and_0_001_thiamine_monophosphate.yaml` has a 2026-09-11 `RESOLVED_TOGO_M2974_BHI_TT_SCORE15` event and stores the same row as `1000.0 ML_PER_L`. | Merge generator / generated `data/merge_yaml/merged` outputs; the normalized owner is already repaired |
| Major | The generated record omits source-preserving fields already present upstream. | The normalized owner has TOGO notes on all three ingredients, a `MIX` preparation step, a TOGO reference, and curation flags; the generated record has none of those fields. | Merge generator / generated `data/merge_yaml/merged` outputs; the normalized owner is already repaired |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_0_1_tris_base_and_0_001_thiamine_monophosphate.yaml`
   from `data/normalized_yaml/bacterial/brain_heart_infusion_broth_supplemented_with_0_1_tris_base_and_0_001_thiamine_monophosphate.yaml`.
2. Preserve the existing normalized-owner representation of the TOGO 1 L BHI
   component as `1000.0 ML_PER_L`.
3. Preserve the owner record's TOGO reference, source notes, BHI-TT `MIX`
   preparation step, thiamine monophosphate grounding, data-quality flags, and
   `RESOLVED_TOGO_M2974_BHI_TT_SCORE15` history event in the regenerated merge.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validators on the
  regenerated merge.
- Rerun `just validate` after the project `llvmlite` build issue is resolved.
- Compare the regenerated file against the current normalized owner and confirm
  no pre-2026-09-11 generated content remains.
- Manually compare the regenerated file against the TOGO M2974 API payload.

## Additional Notes

- The generated record itself was reviewed read-only; no derived YAML was
  patched.
