# YAML Record Review: Archaeoglobus MCR Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Archaeoglobus_MCR_Medium.yaml
- Started UTC: 2026-09-21T13:54:54Z
- Finished UTC: 2026-09-21T13:55:34Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007814 |
| Name | archaeoglobus_mcr_medium |
| Original name | Archaeoglobus MCR Medium |
| Category | archaea |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| Source | TOGO:M1280 / JCM_M1195 |
| Maintained owner | data/normalized_yaml/archaea/TOGO_M1280_Archaeoglobus_MCR_Medium.yaml |
| Generated record | data/merge_yaml/merged/Archaeoglobus_MCR_Medium.yaml |
| Merge fingerprint | 0833eb81dfac35f3627b3c4df32143294b48f2d6861ded56c6589ed122efa42f |

The target is a generated one-source merge. Its maintained owner is
`data/normalized_yaml/archaea/TOGO_M1280_Archaeoglobus_MCR_Medium.yaml`, and
the generated file predates a 2026-09-10 repair that resolved the parent-medium
cross-reference to TOGO M1279.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Archaeoglobus_MCR_Medium.yaml` | Passed, `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Archaeoglobus_MCR_Medium.yaml --out /private/tmp/Archaeoglobus_MCR_Medium.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Archaeoglobus_MCR_Medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 active checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Archaeoglobus_MCR_Medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with the known `eutils` / `pkg_resources` warning. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone files under `history/`; no focused embedded `MediaRecipe.curation_history` validator is documented for a single generated merge record. |

## Identity and Grounding

The record identifies the expected sparse TOGO/JCM medium wrapper:
`media_term.id` is `TOGO:M1280`, `media_term.label` is `Archaeoglobus MCR
Medium`, and the inspected TOGO M1280 API reports `name: Archaeoglobus MCR
Medium` with `original_media_id: JCM_M1195`.

An ignored-file-inclusive bounded search for
`CultureMech:007814|CultureMech:007812|TOGO:M1280|TOGO:M1279|TOGO_M1280_Archaeoglobus_MCR_Medium|Archaeoglobus_MCR_Medium`
across `data/normalized_yaml`, `data/merge_yaml`,
`data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`,
`reports/media_content_review_manifest.tsv`,
`data/import_tracking/reports/concentration_plausibility.tsv`, and
`data/import_tracking/reports/merged_duplicates.tsv` found one maintained
M1280 owner, its generated merge, the maintained M1279 parent, the generated
M1279 merge, and the expected registry, catalog, manifest, and index rows. It
did not find a second maintained M1280 owner in the searched corpus.

The sodium sulfate grounding is correct: `Na2SO4` is grounded to
`CHEBI:32149`, sodium sulfate.

## Evidence

The inspected TOGO M1280 API supports the sparse wrapper semantics. Its
component list contains only 2.8 `g/L` `Na2SO4` and 1 `L`
`METHANOTHERMOCOCCUS HHB MEDIUM (see Medium [M1279])`, and its comments say to
use Medium No. 1194 supplemented with 2.8 g/L `Na2SO4`. The TOGO payload also
declares `reference_media_id: M1279` for the base-medium item.

The normalized owner already preserves that relationship: sodium sulfate has a
source-backed note, the base medium is represented as a 1 `L` solution with
`culturemech_term: CultureMech:007812`, `parent_media` points to
`data/normalized_yaml/archaea/TOGO_M1279_Methanothermococcus_HHB_Medium.yaml`,
and `variant_relationship` is `SUPPLEMENTED_VARIANT`.

The generated merge is stale. It still represents the parent as an empty
`Unknown solution`, keeps the parent amount as 1 `G_PER_L`, lacks
`culturemech_term`, lacks `parent_media`, lacks the supplemented-variant
metadata, lacks the 2026-09-10 curation event, and retains older free-text
source notes rather than the curated M1280 summary.

## Completeness

The maintained owner is complete enough for the sparse M1280 wrapper: it keeps
the supported sodium sulfate supplement and intentionally delegates the base
recipe to M1279 rather than flattening that parent recipe into M1280.

The generated record is incomplete because it has not been regenerated since
that repair. The generated file still has the old parent-medium placeholder and
does not publish the structured link to CultureMech:007812.

Two adjacent items are intentionally out of scope for this generated M1280
review:

- The current JCM `GRMD=1195` page returns `Nothing found`, so the inspected
  support for M1280 came from the TOGO M1280 API instead of the stale original
  JCM URL embedded in the import.
- The M1279 parent itself still has unit and stock-solution issues and is
  flagged `NEEDS_REVIEW` in `reports/media_content_review_manifest.tsv`; those
  should be handled while reviewing `METHANOTHERMOCOCCUS_HHB_MEDIUM.yaml`, not
  in this M1280 wrapper.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale relative to its normalized owner. | The generated file was last merged on 2026-08-06. On 2026-09-10, `data/normalized_yaml/archaea/TOGO_M1280_Archaeoglobus_MCR_Medium.yaml` resolved the M1279 base-medium cross-reference, changed the parent amount from 1 `G_PER_L` to 1 `L`, added a `CultureMech:007812` link, added `parent_media`, added `variant_relationship: SUPPLEMENTED_VARIANT`, added `data_quality_flags`, and added a TOGO reference. | Regenerate `data/merge_yaml/merged/Archaeoglobus_MCR_Medium.yaml` from the maintained normalized owner. |

No blockers found. No minor findings found.

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/Archaeoglobus_MCR_Medium.yaml` and
   downstream pages/indexes from
   `data/normalized_yaml/archaea/TOGO_M1280_Archaeoglobus_MCR_Medium.yaml`.
2. After regeneration, confirm the merge keeps the M1279 parent amount as 1
   `L`, includes `culturemech_term: CultureMech:007812`, preserves
   `parent_media`, and no longer names the parent `Unknown solution`.
3. Leave the M1279 base-medium formula nested by reference in this sparse M1280
   wrapper. Review and curate the parent M1279 record separately.

## Follow-up Checks

- Re-run open-schema, strict, term, and reference validation on the regenerated
  merge.
- Inspect the regenerated record to confirm it includes the 2026-09-10
  `repair_archaeoglobus_mcr_score20.py` history entry and the TOGO M1280
  reference.
- Inspect the rendered page and ensure Archaeoglobus MCR Medium reads as a
  supplemented variant of Methanothermococcus HHB Medium plus 2.8 g/L sodium
  sulfate, not as a standalone 1 g/L unknown solution.

## Additional Notes

- The vanished JCM 1195 page was checked directly; it returned a JCM `Medium
  data` page whose body says `Nothing found`.
- The maintained M1280 owner is already marked `PASS` in
  `reports/media_content_review_manifest.tsv`; the stale generated merge is the
  remaining issue for this target.
