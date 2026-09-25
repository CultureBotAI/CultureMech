# YAML Record Review: marine_tryptone_yeast_extract_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_tryptone_yeast_extract_medium__796621c8.yaml
- Started UTC: 2026-09-24T00:10:01Z
- Finished UTC: 2026-09-24T00:11:10Z
- Verdict: needs curation

## Target

- Reviewed generated record:
  `data/merge_yaml/merged/marine_tryptone_yeast_extract_medium__796621c8.yaml`
- Maintained upstream owner:
  `data/normalized_yaml/fungal/marine_tryptone_yeast_extract_medium.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:010496`
- Source identity: `mediadive.medium:J1208`
- Source label: `MARINE TRYPTONE YEAST EXTRACT MEDIUM`
- Generated status: single-source merge of
  `marine_tryptone_yeast_extract_medium.yaml` with fingerprint
  `796621c813b1ca2959947ad6146b69cdff4e0872758337e22a929433d1d32e93`.

## Validation

| Check | Result |
|---|---|
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_tryptone_yeast_extract_medium__796621c8.yaml` | Passed; printed `No issues found`. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_tryptone_yeast_extract_medium__796621c8.yaml --out /private/tmp/marine_tryptone_yeast_extract_medium__796621c8.strict.tsv --workers 1 --quiet` | Passed; summary reported 1 scanned file, 0 files with errors, and 0 total error rows. The TSV had one header line only. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_tryptone_yeast_extract_medium__796621c8.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 total reference checks. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_tryptone_yeast_extract_medium__796621c8.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after a non-fatal `eutils`/`pkg_resources` deprecation warning. |
| Embedded `MediaRecipe.curation_history` validation | Not checked: the repository's `just validate-history` target validates standalone files under `history/`, not embedded recipe events. |

## Identity and Grounding

- MediaDive REST `J1208` and live JCM `GRMD=1208` both verify the target as
  JCM `1208`, `MARINE TRYPTONE YEAST EXTRACT MEDIUM`, pH 7.0.
- TOGO `M1294` preserves the same JCM `1208` source. TOGO `M1295` preserves the
  JCM `1208-2` sodium-pyruvate variant described in the JCM comment.
- The CHEBI terms for calcium chloride dihydrate, sodium chloride, magnesium
  chloride hexahydrate, magnesium sulfate heptahydrate, potassium chloride,
  sodium thioglycolate, resazurin, cellobiose, and sodium sulfide nonahydrate
  all passed OBO term validation.
- The record has no `sources`, `source_data`, `references`, `target_organisms`,
  `growth_metrics`, or explicit duplicate/variant edges.

## Evidence

- Supported:
  - The 2 g tryptone, 1 g yeast extract, 1 g CaCl2 x 2 H2O, 20 g NaCl,
    3.6 g MgCl2 x 6 H2O, 4.3 g MgSO4 x 7 H2O, 0.5 g KCl, 0.1 g sodium
    thioglycolate, 0.5 mg resazurin, 1 l distilled water, pH 7.0, and N2
    anaerobic preparation are supported by the live JCM 1208 page.
  - MediaDive's 1.04 l final-volume normalization supports the stored gram per
    liter values for the nine weighed non-water ingredients.
  - The two source preparation comments are carried through to
    `preparation_steps`.
- Unsupported or misrepresented:
  - JCM and MediaDive both list the last two additions as 30 ml of 0.2 M
    cellobiose solution and 10 ml of 5% Na2S x 9 H2O solution after
    autoclaving. The record instead stores `Cellobiose` as `30 G_PER_L` and
    `Na2S x 9 H2O` as `10 G_PER_L`.
  - `TOGO:M1294` is an unlinked source duplicate of the same JCM 1208 recipe,
    and `TOGO:M1295` is an unlinked sodium-pyruvate variant that JCM describes
    in the comment for strains JCM 32481, JCM 32483, JCM 32614, and JCM 32615.

## Completeness

- Ingredient and solution coverage is incomplete because the two post-autoclave
  stock additions are represented as root dry compounds instead of solution
  volumes.
- Duplicate/variant coverage is incomplete for the TOGO JCM 1208 and JCM 1208-2
  records.
- Preparation coverage is otherwise adequate for the JCM page: the record
  preserves N2 cooling, N2 dispensing, autoclaving, and the post-autoclave
  anaerobic addition boundary.
- Empty target-organism and growth-metric slots are acceptable here because the
  inspected JCM, MediaDive, and TOGO records are recipe sources, not primary
  strain-growth reports.
- A gitignore-independent exact scan of the reviewed normalized and merged YAML
  files found no `sources`, `source_data`, `references`, `target_organisms`,
  `growth_metrics`, `parent_media`, `variant_children`, or
  `variant_relationship` fields in the current target.
- A gitignore-independent exact scan of normalized indexes and exact sibling
  paths found `TOGO:M1294` and `TOGO:M1295` as the two TOGO records tied to this
  JCM 1208 lineage.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Two stock-solution additions were flattened into impossible gram-per-liter compounds. | JCM 1208 and MediaDive `J1208` list 30 ml of 0.2 M cellobiose solution and 10 ml of 5% Na2S x 9 H2O solution; the record stores `30 G_PER_L` cellobiose and `10 G_PER_L` sodium sulfide nonahydrate. | `data/normalized_yaml/fungal/marine_tryptone_yeast_extract_medium.yaml`; if recurring, fix `src/culturemech/import/mediadive_importer.py`. |
| major | Source duplicates and the sodium-pyruvate variant are not linked. | TOGO `M1294` is the same JCM 1208 recipe, and TOGO `M1295` records the JCM 1208-2 sodium-pyruvate variant; neither has a parent, child, or source-duplicate edge to the MediaDive J1208 record. | `data/normalized_yaml/fungal/marine_tryptone_yeast_extract_medium.yaml` plus the two TOGO normalized records under `data/normalized_yaml/bacterial/`. |

## Recommended Edits

1. Replace the `Cellobiose` and `Na2S x 9 H2O` root ingredients with explicit
   30 ml/l and 10 ml/l stock-solution additions that preserve the 0.2 M and 5%
   source concentrations.
2. Link `data/normalized_yaml/bacterial/marine_tryptone_yeast_extract_medium.yaml`
   as a source duplicate of the MediaDive J1208 record.
3. Represent `data/normalized_yaml/bacterial/TOGO_M1295_Marine_Tryptone_Yeast_Extract_Medium.yaml`
   as the 1.0 M sodium-pyruvate variant of this recipe, replacing the
   cellobiose stock and retaining the 5% sodium sulfide stock.
4. Add curation-history events on each edited normalized record.

## Follow-up Checks

- Re-run the focused LinkML, strict, term, and reference validators on the
  edited fungal record and on any linked TOGO records that change.
- Run `just validate-media-variant-links` after adding source-duplicate and
  variant edges.
- Regenerate merged records and verify that the MediaDive J1208 and TOGO M1294
  records are no longer uncoordinated single-source entries.
- Manually compare the edited records against live JCM 1208, MediaDive J1208,
  TOGO M1294, and TOGO M1295 for all stock-solution amounts.

## Additional Notes

- The MediaDive REST output for `J1208` was saved to `/private/tmp` during the
  review because direct curl output showed progress information without a JSON
  body in the merged terminal stream.
- TOGO source strings use non-ASCII hydrate punctuation; this report renders
  chemical hydrates with `x`, for example `Na2S x 9 H2O`, to stay ASCII-only.
