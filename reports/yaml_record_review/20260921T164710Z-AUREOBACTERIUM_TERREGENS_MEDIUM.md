# YAML Record Review: aureobacterium_terregens_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/AUREOBACTERIUM_TERREGENS_MEDIUM.yaml
- Started UTC: 2026-09-21T16:45:43Z
- Finished UTC: 2026-09-21T16:47:10Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/AUREOBACTERIUM_TERREGENS_MEDIUM.yaml`, a
generated `MediaRecipe` with stable ID `CultureMech:004580`, normalized name
`aureobacterium_terregens_medium`, original name
`AUREOBACTERIUM TERREGENS medium`, category `bacterial`, `medium_type:
COMPLEX`, `composition_type: UNDEFINED`, `physical_state: LIQUID`,
`ph_value: 7.0`, media term `komodo.medium:226`, and merge fingerprint
`eae9e88699ef37466e54ceca2ddf22c5318ce1aeb4fc50d3309d858c26af37d1`.

The generated merge combines two maintained sources,
`data/normalized_yaml/bacterial/KOMODO_226_AUREOBACTERIUM_TERREGENS_medium.yaml`
and `data/normalized_yaml/bacterial/aureobacterium_terregens_medium.yaml`.
Both are maintained inputs; future fixes should land there, or in merge rules,
then regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/AUREOBACTERIUM_TERREGENS_MEDIUM.yaml` | Pass, `No issues found`. |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/AUREOBACTERIUM_TERREGENS_MEDIUM.yaml --out /private/tmp/AUREOBACTERIUM_TERREGENS_MEDIUM.strict.tsv --workers 1 --quiet` | Pass: 1 file scanned, 0 files with errors, 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/AUREOBACTERIUM_TERREGENS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass: 1 file validated, 0 reference checks emitted. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/AUREOBACTERIUM_TERREGENS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass; the validator also emitted only the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused validator for `MediaRecipe.curation_history` in one generated merge record. |

The direct `just validate-schema`, `just validate-strict`, `just
validate-references`, and `just validate-terms` entrypoints were not used for
this target because this checkout currently reaches a project `uv` build of
`llvmlite==0.46.0` under Python 3.13 before target-specific validation and
crashes in setuptools with `TypeError: Popen.__init__() got an unexpected
keyword argument 'dry_run'`.

## Identity and Grounding

The KOMODO/DSMZ duplicate identity is internally consistent. KOMODO Medium 226
explicitly cites DSMZ Medium 226, both normalized owners have identical pH,
physical state, ingredient names, ingredient amounts, and source-duplicate
links, and the generated merge records the DSMZ/MediaDive owner as
`parent_media`.

A gitignore-independent exact search covered `data`, `reports`, `history`, and
`.claude` for `CultureMech:004580`, `CultureMech:001330`,
`komodo.medium:226`, `mediadive.medium:226`,
`KOMODO_226_AUREOBACTERIUM_TERREGENS_medium`,
`aureobacterium_terregens_medium`, and `AUREOBACTERIUM TERREGENS`. It found
only the two maintained normalized owners as current data owners, plus
generated indexes, archived pre-rename validation rows, organism-review leads,
and the archive that recorded the DSMZ/KOMODO source-duplicate relationship.
An exhaustive `find` confirmed the two current owner paths.

## Evidence

The inspected DSMZ Medium 226 PDF supports all seven represented base
ingredients: Casamino acids 2.0 g/L, Yeast extract 1.0 g/L, Glucose 1.0 g/L,
ammonium citrate 1.0 g/L, K2HPO4 2.0 g/L, MgSO4 x 7 H2O 0.5 g/L, and
FeCl3 x 6 H2O 10.0 mg/L.

The DSMZ source also instructs pH adjustment to 7.0 and a post-sterilization
aseptic addition of 1 ml/L of a 10% acetylacetone solution in ethanol. The
DSMZ/MediaDive normalized owner preserves that addition only in free-text
`preparation_steps`, and the generated merge drops the step entirely when it
chooses the KOMODO duplicate as the canonical source.

## Completeness

The missing target organism and growth-evidence fields are not findings in
this imported DSMZ/KOMODO recipe: the inspected medium recipe does not assert a
strain growth outcome.

The generated target is materially incomplete because it omits the
acetylacetone solution addition from DSMZ 226. Before writing this report,
`find reports/yaml_record_review -maxdepth 1 -name '*AUREOBACTERIUM_TERREGENS_MEDIUM.md' -print`
covered ignored and unignored files in the review-report directory and found no
prior exact report for this generated stem.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The DSMZ post-sterilization acetylacetone stock addition is absent from the generated canonical record. | DSMZ Medium 226 adds 1 ml/L of a 10% acetylacetone solution in ethanol after sterilization; the DSMZ normalized owner keeps that only as preparation prose, the KOMODO owner lacks it, and the generated merge has no preparation step or solution row for it. | `data/normalized_yaml/bacterial/aureobacterium_terregens_medium.yaml`, `data/normalized_yaml/bacterial/KOMODO_226_AUREOBACTERIUM_TERREGENS_medium.yaml`, and merge handling for `SOURCE_DUPLICATE` records. |

No blockers or minor findings were found beyond this missing-addition major
finding.

## Recommended Edits

1. Add the 10% acetylacetone-in-ethanol stock addition at 1 ml/L to the
   authoritative DSMZ 226 representation and, if the KOMODO duplicate remains
   canonical, to the KOMODO duplicate or source-duplicate merge overlay.
2. Preserve DSMZ's pH 7.0 and post-sterilization addition instructions in the
   regenerated canonical merge.
3. Regenerate `data/merge_yaml/merged/` so
   `AUREOBACTERIUM_TERREGENS_MEDIUM.yaml` carries the structured acetylacetone
   addition.

## Follow-up Checks

- Re-run open-schema LinkML, `scripts/validate_strict.py`, the reference
  validator, and the term validator against both edited normalized owners and
  the regenerated `data/merge_yaml/merged/AUREOBACTERIUM_TERREGENS_MEDIUM.yaml`.
- Manually compare the regenerated merge with DSMZ Medium 226 to verify the
  post-sterilization acetylacetone stock is no longer lost.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  generated merges.

## Additional Notes

The DSMZ Medium 226 PDF was fetched successfully and source text was extracted
with the cached Python `pypdf` package through `uv --no-project --offline`.
