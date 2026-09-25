# YAML Record Review: marine_spirochete_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_spirochete_medium.yaml
- Started UTC: 2026-09-24T00:05:39Z
- Finished UTC: 2026-09-24T00:07:20Z
- Verdict: needs curation

## Target

- Reviewed generated record: `data/merge_yaml/merged/marine_spirochete_medium.yaml`
- Maintained upstream owner: `data/normalized_yaml/bacterial/marine_spirochete_medium.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:003513`
- Current name: `marine_spirochete_medium`
- Original name: `MARINE SPIROCHETE medium`
- Source identity: `komodo.medium:1008`
- DSMZ mapping in record notes: `mediadive.medium:1008`
- Generated status: derived single-source merge; the merged record lists
  `merged_from: marine_spirochete_medium` and should not be edited directly.

## Validation

| Check | Result |
|---|---|
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_spirochete_medium.yaml` | Passed; exited 0 with no diagnostics. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_spirochete_medium.yaml --out /private/tmp/marine_spirochete_medium.strict.tsv --workers 1 --quiet` | Passed; summary reported 1 scanned file, 0 files with errors, and 0 total error rows. The TSV had one header line only. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_spirochete_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 total reference checks. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_spirochete_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after a non-fatal `eutils`/`pkg_resources` deprecation warning. |
| Embedded `MediaRecipe.curation_history` validation | Not checked: the repository's `just validate-history` target validates standalone files under `history/`, not embedded recipe events. |

## Identity and Grounding

- The generated record and the maintained normalized source agree on
  `CultureMech:003513`, `komodo.medium:1008`, `MARINE SPIROCHETE medium`, the
  bacterial category, liquid physical state, and undefined composition.
- The live KOMODO media list verifies ID `1008` as `MARINE SPIROCHETE medium`
  and links that row to `DSMZ_Medium1008.pdf`.
- DSMZ/MediaDive REST for medium 1008 and the linked DSMZ PDF currently identify
  the underlying DSMZ formulation as `SEDIMINISPIROCHAETA MEDIUM` with pH 7.5.
  This supports the record's DSMZ Medium 1008 mapping, but it also means this
  KOMODO alias should converge with the existing MediaDive record
  `CultureMech:000424`.
- `CHEBI:8806`/Resazurin, `CHEBI:86481`/sodium thioglycolate,
  `CHEBI:17057`/cellobiose, and `CHEBI:32035`/potassium hydroxide passed OBO
  term validation. The packaged CHEBI structure index and MIM label index also
  contain exact or synonym mappings for those four CURIEs.

## Evidence

- Supported:
  - KOMODO ID `1008` is the `MARINE SPIROCHETE medium` row, and that row points
    at the DSMZ Medium 1008 PDF.
  - MediaDive REST medium 1008 and the DSMZ PDF both support pH 7.5.
  - The 2 g/l Trypticase peptone, 1 g/l yeast extract, 0.5 ml/l of 0.1% w/v
    sodium resazurin, 1 g/l Na-thioglycolate, 2 g/l cellobiose, and 800 ml/l
    charcoal-filtered natural seawater components are supported by the DSMZ
    source.
  - The variable KOH entry is supported as a preparation reagent for pH
    adjustment; DSMZ specifies 10 N KOH to adjust the medium to pH 7.5.
- Unsupported or misrepresented:
  - DSMZ lists 800 ml charcoal-filtered natural seawater plus 200 ml distilled
    water; the reviewed record stores seawater as `800` `G_PER_L` and omits
    the distilled-water make-up volume.
  - DSMZ gives a required anaerobic preparation with N2 sparging, 100% N2
    dispensing, Hungate-type tubes or serum vials, autoclaving at 121 C for 15
    min, and post-autoclave filter-sterilized cellobiose; the reviewed record
    has no `preparation_steps`.
  - The record has no parent/synonym relation to the existing MediaDive
    `CultureMech:000424` canonical record even though `CultureMech:003511` and
    `CultureMech:003512`, the two other KOMODO rows mapped to DSMZ Medium 1008,
    are already merged under that MediaDive record.
- The record carries no `sources`, `source_data`, `references`,
  `target_organisms`, or `growth_metrics` blocks. That is not a schema problem,
  and the DSMZ/KOMODO sources inspected here are source recipes rather than
  primary growth experiments.

## Completeness

- Ingredient coverage is incomplete because the 200 ml/l distilled water make-up
  volume is absent.
- Procedure coverage is incomplete because the source's anaerobic preparation
  was not carried into the KOMODO-derived normalized record.
- Variant and duplicate coverage is incomplete because the record is a
  DSMZ Medium 1008 alias but remains outside the `SEDIMINISPIROCHAETA MEDIUM`
  merge group.
- Empty target-organism and growth-metric slots are acceptable for this source
  recipe: no strain-specific growth evidence was asserted by the record.
- A gitignore-independent exact scan of the reviewed normalized and merged YAML
  files found no `preparation_steps`, `sources`, `source_data`, `references`,
  `target_organisms`, `growth_metrics`, `parent_media`, `variant_children`, or
  `variant_relationship` fields in the current target.
- A gitignore-independent exact scan of normalized source indexes and the
  sibling files found `CultureMech:003511`, `CultureMech:003512`, and
  `CultureMech:000424` as the other current records tied to DSMZ Medium 1008.
  The local `data/raw/komodo*` directories contain tracked README files only;
  ignored raw JSON captures were not present in this checkout.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The DSMZ solvent quantities are wrong or incomplete. | DSMZ Medium 1008 uses 800 ml charcoal-filtered natural seawater and 200 ml distilled water per liter; the record encodes seawater as `800` `G_PER_L` and omits distilled water. | `data/normalized_yaml/bacterial/marine_spirochete_medium.yaml`; if recurring in KOMODO DSMZ enrichment, also audit `src/culturemech/import/komodo_web_importer.py` and the DSMZ composition resolver that copied Medium 1008 ingredients. |
| major | Required anaerobic preparation did not survive enrichment. | DSMZ specifies N2 sparging, anoxic dispensing, autoclaving, and sterile anoxic filtered cellobiose addition; the KOMODO-derived record has no `preparation_steps`. The MediaDive sibling for the same DSMZ medium already carries those steps. | `data/normalized_yaml/bacterial/marine_spirochete_medium.yaml`; if recurring, compare `src/culturemech/import/mediadive_importer.py` and the KOMODO DSMZ enrichment path. |
| major | The record remains a separate canonical merge even though it is a DSMZ Medium 1008 duplicate alias. | KOMODO ID `1008`, `1008_19205`, and `1008_19230` all point to `DSMZ_Medium1008.pdf`; only the two modified records are linked under `CultureMech:000424`. `marine_spirochete_medium` differs by the variable KOH ingredient and therefore has merge fingerprint `158892addc4a95d6a6b2360c5f1dc6b0f14ae91cbd7de6bb592f84854da485d7` instead of the Medium 1008 sibling fingerprint `91642e3d67d42f4c35fa0e83b932b6d1e243af51385c0132f5913111f8d6fea2`. | `data/normalized_yaml/bacterial/marine_spirochete_medium.yaml` and, after the scientific content is normalized, `src/culturemech/merge/merge_recipes.py` if pH-adjustment reagents should not split source duplicates. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/marine_spirochete_medium.yaml`, change the
   DSMZ base-fluid representation from `800 G_PER_L` seawater to the
   source-supported 800 ml/l seawater plus 200 ml/l distilled water.
2. Copy the DSMZ Medium 1008 anaerobic preparation and Biomaris bottled-seawater
   note into `preparation_steps`, preserving the N2 atmosphere, KOH pH
   adjustment, autoclave conditions, and filter-sterilized anoxic cellobiose
   addition.
3. Link `marine_spirochete_medium` as a `SOURCE_DUPLICATE` of
   `data/normalized_yaml/bacterial/sediminispirochaeta_medium.yaml`, or adjust
   merge fingerprinting after curation so the KOMODO alias merges with
   `CultureMech:000424` rather than publishing separately.
4. Add a curation-history event describing the source-backed DSMZ corrections
   and the duplicate-link decision.

## Follow-up Checks

- Re-run the focused LinkML, strict, term, and reference validators on
  `data/normalized_yaml/bacterial/marine_spirochete_medium.yaml`.
- Re-run `just validate-media-variant-links` if a `SOURCE_DUPLICATE` edge is
  added.
- Regenerate merged records with `src/culturemech/merge/merge_recipes.py` and
  verify that the KOMODO Medium 1008 alias no longer appears as an unlinked
  single-source merge.
- Manually compare the post-edit record against DSMZ Medium 1008 PDF text and
  MediaDive REST output for all components, pH, and preparation steps.

## Additional Notes

- The live KOMODO MediaList and DSMZ PDF were fetched during this review because
  only `data/raw/komodo/README.md` and `data/raw/komodo_web/README.md` were
  present under `data/raw/komodo*`; the ignored raw JSON captures were absent
  in a gitignore-independent `find`.
- One exploratory search for `KOH`, `Charcoal-filtered, natural seawater`, and
  manifest `VARIABLE_CONCENTRATION` was too broad and returned many unrelated
  rows. Duplicate and completeness conclusions in this report rely on exact
  searches for `CultureMech:003513`, the reviewed path, and the DSMZ Medium
  1008 sibling IDs instead.
