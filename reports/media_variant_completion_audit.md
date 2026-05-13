# Media Variant Completion Audit

Date: 2026-05-11

## Objective Restated

Review the CultureMech media YAML corpus to assess ingredient validity,
concentration coverage, and possible media variations. Represent reviewed
media variations as child YAML records with explicit parent links, and add
child links on parent media records, across the current
`data/normalized_yaml/**/*.yaml` corpus.

## Prompt-To-Artifact Checklist

| Requirement | Evidence | Current status |
|---|---|---|
| Assess the current YAML media corpus | `reports/media_content_review_manifest.tsv`, `reports/media_content_review_manifest_summary.md`, `reports/media_ingredient_variant_state_assessment.md` | Covered for all 15,827 normalized YAML records. |
| Validate ingredient state | Manifest counts ingredient entries, CHEBI coverage, MediaIngredientMech coverage, non-CHEBI IDs, unexpected ingredient keys, and missing/blank terms | Partially covered. Review exists, but ingredient normalization is incomplete. |
| Validate concentration state | Manifest counts missing/malformed concentration objects, missing values/units, non-schema units, and `VARIABLE` concentrations | Partially covered. Syntactic coverage is high, but many semantic concentration issues remain. |
| Identify possible variation groups | `reports/media_variation_candidate_groups.tsv/json`, `reports/media_variant_link_proposals.tsv/json`, `reports/media_variant_parent_group_proposals.tsv/json` | Covered as candidate discovery; not all proposals are curated. |
| Add schema support for parent/child variant records | `src/culturemech/schema/culturemech.yaml`, regenerated dataclasses, `tests/test_media_variant_links.py` | Implemented and tested. |
| Represent variations as child YAML records | Applied parent/child links in normalized YAML records; latest validation counts 1,529 child links | Partially complete. Curated subset applied, not full corpus. |
| Parent media YAML contains links to each child | `variant_children` links validated by `scripts/validate_media_variant_links.py` | Partially complete for applied families. |
| Validate bidirectional links | `reports/media_variant_link_validation.md/tsv` | Covered for current corpus state: 15,827 records, 1,529 parent links, 1,529 child links, 0 errors, 0 warnings. |
| Avoid applying broad or ambiguous groups blindly | `reports/media_variant_algae_source_duplicate_review.md` | Covered for broad algae exact-signature groups; 103 algae proposals downgraded to review-required. |
| Apply a non-duplicate concentration-variant family | `reports/media_variant_zahorchak_grid_review.md`, Zahorchak YAML edits | Covered for two Zahorchak ATP/Mg2+ concentration-grid groups, 28 child links. |
| Apply a salinity-variant family | `reports/media_variant_m63_salinity_grid_review.md`, modified M63 YAML edits | Covered for three modified M63 salinity grids, 9 child links. |
| Apply another salinity-variant family | `reports/media_variant_802_salinity_grid_review.md`, 802 YAML edits | Covered for one TOGO/NBRC 802 NaCl grid, 3 child links. |
| Apply another salinity-variant family | `reports/media_variant_rdm_salinity_grid_review.md`, RDM YAML edits | Covered for one MediaDB RDM NaCl grid, 2 child links. |
| Validate changed YAML | Targeted schema validation loops for 30 Zahorchak files, 12 modified M63 files, 4 802 files, and 3 RDM files; link validator; focused tests | Covered for the latest batch. |

## Current Verified State

- YAML records scanned: 15,827
- Total component entries in assessment: 170,715
- Records with complete concentration object/value/unit coverage: 15,453
- Records where every component has a CHEBI `term.id`: 1,822
- Candidate ingredient-identity variation groups: 1,451
- Candidate parent-child links: 9,145
- Current parent-to-child links: 1,529
- Current child-to-parent links: 1,529
- Current link validation errors: 0
- Current link validation warnings: 0

## Completed Batches

- Schema/dataclass/test support for explicit parent/child media variant links.
- Validator and proposal/apply scripts for parent/child links.
- Multiple curated `SOURCE_DUPLICATE` family batches.
- Remaining broad algae exact-signature groups downgraded to
  `REVIEW_REQUIRED`.
- Zahorchak et al. ATP/Mg2+ concentration-grid batch applied as
  `CONCENTRATION_VARIANT`.
- Modified M63 ectoine/glucose/hydroxyectoine salinity-grid batch applied as
  `SALINITY_VARIANT`.
- TOGO/NBRC 802 NaCl salinity-grid batch applied as `SALINITY_VARIANT`.
- MediaDB RDM NaCl salinity-grid batch applied as `SALINITY_VARIANT`.

## Remaining Gaps

- The full 15k-record corpus has not been fully migrated into parent/child
  variant structure.
- Most non-duplicate proposals still need source/formulation review before
  links should be applied.
- Ingredient normalization remains incomplete:
  - only 1,822 records currently have CHEBI IDs on every component
  - 1,872 component entries use non-CHEBI `term.id` values
  - some entries have blank ingredient names, including exogenous-ATP
    components in the Zahorchak grid
- Concentration normalization remains incomplete:
  - 533 non-schema concentration units
  - 6,649 records using `VARIABLE` concentration units
- Current proposal counts include already-applied links; future status reports
  should distinguish proposed, applied, and deferred relationships explicitly.

## Completion Judgment

The objective is not complete. The repo now has corpus-wide assessment,
schema/model support, validation tooling, curated batches, and clean
bidirectional links for 1,529 relationships, but many candidate variations and
ingredient/concentration normalization issues remain unresolved.
