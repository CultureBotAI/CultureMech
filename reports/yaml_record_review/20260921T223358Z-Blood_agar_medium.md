# YAML Record Review: blood_agar_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/Blood_agar_medium.yaml`
- Started UTC: 2026-09-21T22:33:59Z
- Finished UTC: 2026-09-21T22:34:42Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Generated record ID | `CultureMech:008862` |
| Generated label | `blood_agar_medium` |
| Original name | `Blood agar medium` |
| Source term | `TOGO:M2276` / `Blood agar medium` |
| Maintained owner | `data/normalized_yaml/bacterial/blood_agar_medium.yaml` |
| Generated status | Derived from one active normalized TOGO input by `merge_recipes.py`; future fixes belong in normalized YAML or TOGO import/repair rules, followed by merge regeneration |

The ignored-file-inclusive exact search for `CultureMech:008862`, `TOGO:M2276`,
and `M2276` found one active normalized owner plus generated normalized-index
and merged-record copies. It did not find another maintained YAML owner for the
same stable ID or TOGO accession.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Blood_agar_medium.yaml` | Passed with no diagnostics |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Blood_agar_medium.yaml --out /private/tmp/Blood_agar_medium.strict.tsv --workers 1 --quiet` | Passed, 1 file scanned, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Blood_agar_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed, 0 checks, all validations passed |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Blood_agar_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/` |

The documented `just validate-schema`, `just validate-strict`, and
`just validate-terms` entrypoints were not used directly because this checkout's
project `uv` environment currently tries to build `llvmlite==0.46.0` under
Python 3.13 and fails inside `setuptools` before a target-specific check runs.
The no-project Python 3.11 commands above exercise the same target validators.

## Identity and Grounding

- `TOGO:M2276` identifies `Blood agar medium`, and the TOGO API record contains
  a single component named `Blood agar medium`.
- The TOGO API grounds that component to GMO `GMO_002397`, label `Blood agar
  plate`, with `Undefined component` and `Complex component` properties.
- The current normalized owner has already been repaired to source-faithfully
  represent the opaque TOGO component as `1000 ML_PER_L`; the generated merge
  still carries the pre-repair placeholder `1 G_PER_L` row.
- There is no checked source support for expanding TOGO M2276 below the opaque
  ready-to-use Blood agar medium component.

## Evidence

Inspected sources:

| Source | Scope checked |
| --- | --- |
| `/private/tmp/togo-M2276.json` | TOGO M2276 name, one-liter component, GMO label, and component properties |
| `data/normalized_yaml/bacterial/blood_agar_medium.yaml` | Maintained owner state after the Sept 8 TOGO blood-agar repair |

Supported:

- The maintained normalized owner correctly records a one-liter opaque Blood
  agar medium ingredient, because TOGO M2276 reports `volume: 1` and `unit: L`.
- The maintained normalized owner correctly keeps the lower formulation
  unresolved and explicit: TOGO M2276 exposes `Blood agar medium` as a complex,
  undefined `Blood agar plate` component and provides no constituent list.
- `SOLID_AGAR` is supported by the TOGO GMO label `Blood agar plate`.

Unsupported or over-scoped:

- The generated merge row `Blood agar medium` at `1 G_PER_L` is not supported
  by TOGO; the source quantity is one liter of an opaque blood agar plate
  medium, not one gram per liter of an ingredient.
- The generated merge is stale with respect to the Sept 8 normalized repair and
  omits the repaired ingredient amount, curated note, preparation step,
  `data_quality_flags`, and source reference.

## Completeness

- Complete enough upstream: TOGO M2276 does not expose constituent ingredients,
  pH, organism growth claims, or preparation details beyond the one-liter
  opaque Blood agar medium component.
- Consequentially incomplete in the generated layer: the current merge is
  missing the normalized repair that marks the opaque TOGO row as curated and
  keeps the lower formula unresolved rather than misquantified.
- Bounded search: ignored files were included in the exact TOGO M2276 search
  described under `Target`, and no duplicate maintained owner for M2276 was
  found.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The generated merge is stale and still publishes the old `Blood agar medium` `1 G_PER_L` placeholder. TOGO M2276 and the repaired normalized owner both represent one liter of opaque Blood agar medium. | TOGO M2276 API JSON; `data/normalized_yaml/bacterial/blood_agar_medium.yaml` Sept 8 repair. | No normalized edit is needed; regenerate `data/merge_yaml/merged/Blood_agar_medium.yaml` from `data/normalized_yaml/bacterial/blood_agar_medium.yaml`. |

## Recommended Edits

1. Rerun the merge generator so `data/merge_yaml/merged/Blood_agar_medium.yaml`
   inherits the repaired `1000 ML_PER_L` opaque ingredient, curated note,
   `preparation_steps`, `data_quality_flags`, and `references` from
   `data/normalized_yaml/bacterial/blood_agar_medium.yaml`.
2. Do not expand TOGO M2276 into lower-level blood agar constituents unless a
   new inspected source for that exact TOGO medium provides those rows.

## Follow-up Checks

- Run the focused schema, strict, term, and reference validators on
  `data/normalized_yaml/bacterial/blood_agar_medium.yaml`.
- Run the same validators on `data/merge_yaml/merged/Blood_agar_medium.yaml`
  after merge regeneration.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  merge outputs.
- Re-fetch the TOGO M2276 API response and confirm the regenerated merge still
  preserves the one-liter opaque component boundary.

## Additional Notes

- `find reports/yaml_record_review -name '*Blood_agar_medium.md'` returned no
  path before this report was created.
- This review intentionally wrote only this Markdown report. The generated
  merge record and normalized owner YAML were left unchanged.
