# YAML Record Review: b_cye_agar_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/b_cye_agar_medium.yaml
- Started UTC: 2026-09-21T17:16:18Z
- Finished UTC: 2026-09-21T17:18:24Z
- Verdict: needs curation

## Target

| Field | Observed |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008646 |
| name | b_cye_agar_medium |
| original_name | B-CYEalpha agar medium |
| category | bacterial |
| media_term | TOGO Medium M2056, TOGO:M2056 |
| generated status | Generated merge artifact in data/merge_yaml/merged |
| maintained owner | data/normalized_yaml/bacterial/b_cye_agar_medium.yaml |

The target is the stale generated merge for one TOGO/NBRC source record,
`b_cye_agar_medium`, with merge fingerprint
`6493b27a9c03686f9ac101074fc4b4c9d592657af07f0b41c5dffb01320317c0`.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/b_cye_agar_medium.yaml` completed with no errors. |
| Strict validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/b_cye_agar_medium.yaml --out /private/tmp/b_cye_agar_medium.strict.tsv --workers 1 --quiet` completed with no errors. |
| Reference validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/b_cye_agar_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 checks. |
| Term validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/b_cye_agar_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` completed with no errors, aside from a non-fatal `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused embedded `MediaRecipe.curation_history` validator for one merge record. |
| Direct `just` validators | Not checked: the project-level `uv` environment currently fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13, with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project LinkML validator workaround above exercised the target schema, strict, reference, and term checks. |

## Identity and Grounding

- The record identity is supported. TOGO API data for `M2056` names
  `B-CYEalpha agar medium`, records `NBRC_M1357` as the original medium ID, and
  points to NBRC Medium 1357.
- The live NBRC Medium 1357 page renders the same B-CYEalpha agar recipe and the
  prepared E-MP96 medium note.
- The normalized owner has already repaired the source identities for
  L-Cysteine hydrochloride, Soluble iron pyrophosphate, ACES, alpha-Ketoglutarate
  potassium, and Yeast extract; the generated target has not been regenerated from
  that repaired owner.

## Evidence

Supported by inspected source text:

- TOGO M2056 and NBRC Medium 1357 list 10 g Yeast extract,
  0.4 g L-Cysteine hydrochloride, 0.25 g Soluble iron pyrophosphate,
  2 g Activated carbon, 10 g ACES, 1 g alpha-Ketoglutarate potassium, 15 g Agar,
  and 1 L Distilled water.
- TOGO and NBRC both report pH 6.9.
- NBRC notes that prepared E-MP96 medium is available from Eiken Chemical Co., Ltd.

Unsupported or stale in the generated target:

- Distilled water is still `1 G_PER_L`; the source says 1 L and the normalized owner
  has already corrected the row to `1.0 L`.
- The pH 6.9 value is absent from the generated target but present in the source and
  normalized owner.
- The generated target still has the legacy `mediaingredientmech_term` for
  L-Cysteine hydrochloride and lacks the source-supported CHEBI/MIM links that now
  exist upstream for cysteine, ACES, and ferric pyrophosphate.
- The generated target lacks the curated `references`, `data_quality_flags`, and
  2026-09-12 repair curation event now present in the normalized owner.

## Completeness

- Source provenance is sufficient to recover the source formulation: TOGO points to
  NBRC Medium 1357, and that page was live and substantive during review.
- Empty organism and growth-metric slots are acceptable for this source recipe. The
  inspected TOGO/NBRC source establishes a formulation, not a growth claim for a
  specific strain.
- Exact gitignore-independent search covered `reports/yaml_record_review` for an
  existing `b_cye_agar_medium.md` report and found no prior report for this exact
  generated record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale relative to the repaired normalized owner. | `data/normalized_yaml/bacterial/b_cye_agar_medium.yaml` already has 1 L water, pH 6.9, exact source notes, references, quality flags, and repaired cysteine/ACES/iron-pyrophosphate mappings; `data/merge_yaml/merged/b_cye_agar_medium.yaml` still has the old water unit, no pH, no references, no quality flags, and stale ingredient mappings. | Regenerate `data/merge_yaml/merged/b_cye_agar_medium.yaml` from `data/normalized_yaml/bacterial/b_cye_agar_medium.yaml`. |

No blocker or minor findings found.

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/b_cye_agar_medium.yaml` from the already-repaired
   normalized owner.
2. Re-run the merge freshness audit to confirm this generated file and any sibling
   generated records are current.

## Follow-up Checks

- `just validate-strict data/merge_yaml/merged/b_cye_agar_medium.yaml` after
  regeneration.
- `just validate-references data/normalized_yaml/bacterial/b_cye_agar_medium.yaml`
  because the repaired owner now has explicit source URLs.
- `just verify-merges` and `just audit-merge-freshness` after regenerating the merge
  layer.
- Manual comparison with TOGO M2056 and NBRC Medium 1357 to verify pH 6.9, 1 L
  Distilled water, and the curated source notes.

## Additional Notes

- `linkml-reference-validator` performed zero checks on the stale generated record
  because it has no `references` block.
