# YAML Record Review: Alkaline Cellulose Agar

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ALKALINE_CELLULOSE_AGAR.yaml`
- Started UTC: 2026-09-21T10:29:52Z
- Finished UTC: 2026-09-21T10:30:37Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ALKALINE_CELLULOSE_AGAR.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007544` |
| Name | `alkaline_cellulose_agar` |
| Original name | `Alkaline Cellulose Agar` |
| Category | `bacterial` |
| Media term | `TOGO:M102` / Alkaline Cellulose Agar |
| Generated from | `data/normalized_yaml/bacterial/TOGO_M102_Alkaline_Cellulose_Agar.yaml` |

This is a generated merge record with one normalized parent. Future fixes belong
in `data/normalized_yaml/bacterial/TOGO_M102_Alkaline_Cellulose_Agar.yaml` or
in the TOGO importer and solution-migration path that generated its composition.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALKALINE_CELLULOSE_AGAR.yaml` |
| Strict validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALKALINE_CELLULOSE_AGAR.yaml --out /private/tmp/ALKALINE_CELLULOSE_AGAR.strict.tsv --workers 1 --quiet` emitted 0 error rows |
| Reference validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALKALINE_CELLULOSE_AGAR.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 total checks |
| Term validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALKALINE_CELLULOSE_AGAR.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not a single embedded `MediaRecipe.curation_history` list in `data/merge_yaml/merged` |

The project-level `just validate-schema`, `just validate-strict`, and
`just validate-terms` wrappers currently fail before target-specific validation
because project `uv` tries to build `llvmlite==0.46.0` under Python 3.13 and
crashes in setuptools with `TypeError: Popen.__init__() got an unexpected
keyword argument 'dry_run'`; the same LinkML and validator entry points were
therefore run through an offline `--no-project` Python 3.11 environment.

## Identity and Grounding

The top-level identity is correct: TOGO M102 is Alkaline Cellulose Agar, TOGO
lists original media ID `JCM_M110`, and the live JCM GRMD 110 page is medium
110, Alkaline Cellulose Agar. The category and solid-agar physical state are
also consistent with the JCM formulation.

The exact gitignore-independent search
`TOGO:M102\b|JCM_M110\b|GRMD=110\b|TOGO_M102_Alkaline_Cellulose_Agar|Alkaline
Cellulose Agar|alkaline_cellulose_agar|MacConkey Agar` covered
`data/normalized_yaml`, `data/merge_yaml`, and `data/import_tracking`. It found
this normalized TOGO source, this generated merge, the direct JCM import at
`data/normalized_yaml/bacterial/alkaline_cellulose_agar.yaml`, the generated
direct-JCM sibling `data/merge_yaml/merged/alkaline_cellulose_agar__89c9ed0e.yaml`,
and multiple independent MacConkey-contaminated records.

## Evidence

- Supported: the record's TOGO/JCM identity is the intended Alkaline Cellulose
  Agar source.
- Supported but structurally collapsed: TOGO M102 and JCM 110 both describe two
  local subsolutions. The final mix should use 900 ml of Solution A and 100 ml
  of Solution B after sterilization.
- Supported in Solution A: cellulose powder MN 300, NH4NO3, K2HPO4, MgSO4 x
  7H2O, CaCl2, peptone, yeast extract, agar, and 900 ml distilled water, with
  pH adjusted to 7.0 using 1 N HCl.
- Supported in Solution B: 6 g Na2CO3 and 100 ml distilled water, with pH
  adjusted to 9.4 using 6% NaHCO3 solution.
- Not supported: the record includes MacConkey Agar constituents: 17 g/L
  peptone, 3 g/L proteose peptone, 10 g/L lactose monohydrate, 1.5 g/L bile
  salts, 5 g/L sodium chloride, 0.03 g/L neutral red, 0.001 g/L crystal violet,
  and a second 13.5 g/L agar row. Those rows come with MacConkey supplier notes
  and do not appear in TOGO M102 or JCM 110.
- Not supported: the required 15 g cellulose powder MN 300 row is absent.
- Not supported: the two distilled-water rows from Solution A and Solution B
  were merged into one `1000.0 G_PER_L` ingredient. They are preparation
  volumes, not a final 1000 g/L solute.
- Not supported: `mediadive.solution:5342` and `mediadive.solution:5343` point
  to corpus-level Solution A and Solution B records whose compositions are
  unrelated to JCM 110. The JCM headings are local names scoped to this recipe.

## Completeness

- The record is compositionally incomplete and contaminated: it lacks the
  cellulose carbon source, carries eight MacConkey-only ingredient rows, and
  duplicates the JCM 15 g agar with a MacConkey 13.5 g agar row.
- Solution A, Solution B, 1 N HCl, and 6% NaHCO3 are not faithfully modeled.
  The maintained source should preserve local subsolution membership, pH
  adjustment of each subsolution, and the 900 ml/100 ml aseptic final mix.
- The adjacent direct JCM import preserves cellulose and the three preparation
  steps but flattens local-solution arithmetic; it is useful as a comparison
  point, not as a complete replacement.
- Empty target-organism, temperature, storage, and growth-evidence slots are
  acceptable for this import because neither inspected TOGO/JCM source supplies
  organism-specific growth claims for JCM 110.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | The source recipe has been contaminated with MacConkey Agar constituents that make the record no longer denote only JCM 110 Alkaline Cellulose Agar. | TOGO M102 and JCM 110 do not list lactose, bile salts, neutral red, crystal violet, sodium chloride, proteose peptone, 17 g/L peptone, or 13.5 g/L agar; the generated record lists all of them with MacConkey supplier annotations. | `data/normalized_yaml/bacterial/TOGO_M102_Alkaline_Cellulose_Agar.yaml` and the external constituent-enrichment path that inserted MacConkey rows |
| Blocker | The 15 g cellulose-powder carbon source is missing. | Both inspected source layers list Cellulose powder MN 300 in Solution A; there is no cellulose ingredient in the generated record. | `data/normalized_yaml/bacterial/TOGO_M102_Alkaline_Cellulose_Agar.yaml` |
| Major | Local JCM Solution A and Solution B were flattened and grounded to unrelated global `mediadive.solution` IDs. | The generated record uses `mediadive.solution:5342` and `mediadive.solution:5343`; those solution files have unrelated NaCl/citrate/amino-acid compositions and are referenced by many other media. JCM 110's Solution A and Solution B are local subrecipes for this medium. | TOGO solution migration and `data/normalized_yaml/bacterial/TOGO_M102_Alkaline_Cellulose_Agar.yaml` |
| Major | Water rows were summed and assigned a mass concentration. | The source has 900 ml water in Solution A and 100 ml water in Solution B; the record has one `1000.0 G_PER_L` water ingredient with a duplicate-merge note. | TOGO import/unit normalization and duplicate-ingredient cleanup |
| Major | The pH-adjustment and post-sterilization assembly procedure is missing. | JCM 110 and TOGO M102 both specify pH adjustment of Solution A with 1 N HCl, pH adjustment of Solution B with 6% NaHCO3, and axenic mixing of 900 ml and 100 ml after sterilization; the generated record has no `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M102_Alkaline_Cellulose_Agar.yaml` |
| Minor | Source provenance is free text only. | TOGO M102, JCM 110, and the unrelated MacConkey page all appear in `notes`; there is no structured `references` list or per-claim evidence. | `data/normalized_yaml/bacterial/TOGO_M102_Alkaline_Cellulose_Agar.yaml` |

## Recommended Edits

1. Remove the MacConkey Agar graft from
   `data/normalized_yaml/bacterial/TOGO_M102_Alkaline_Cellulose_Agar.yaml`,
   including lactose, bile salts, neutral red, crystal violet, sodium chloride,
   proteose peptone, 17 g/L peptone, 13.5 g/L agar, all MacConkey
   `supplier_catalog` entries, and the MacConkey notes block.
2. Restore `Cellulose powder MN 300 (Macherey-Nagel Co.)`, 15 g in Solution A,
   with a cellulose grounding if an exact term is available.
3. Replace the three migrated solution placeholders with two local subsolution
   structures: Solution A at 900 ml and Solution B at 100 ml. Do not link them
   to `mediadive.solution:5342` or `mediadive.solution:5343`.
4. Split water back into its source-scoped 900 ml and 100 ml volume rows inside
   Solution A and Solution B instead of the top-level `1000.0 G_PER_L` sum.
5. Add preparation steps for pH 7.0 adjustment of Solution A with 1 N HCl, pH
   9.4 adjustment of Solution B with 6% NaHCO3, sterilization, and axenic
   post-sterilization mixing of the two local solutions.
6. Promote TOGO M102 and JCM 110 into structured source references and remove
   the unrelated MacConkey source.
7. Regenerate the merge layer so the generated
   `data/merge_yaml/merged/ALKALINE_CELLULOSE_AGAR.yaml` inherits the repaired
   normalized record.

## Follow-up Checks

- Re-run open schema validation on the maintained TOGO source and regenerated
  merge.
- Re-run `scripts/validate_strict.py` on both files and confirm that it emits 0
  error rows.
- Re-run the term validator to ensure the restored cellulose, HCl, and NaHCO3
  rows are either exactly grounded or intentionally ungrounded.
- Re-run the reference validator after adding structured TOGO/JCM references.
- Repeat the exact gitignore-independent MacConkey search against the repaired
  normalized file and regenerated merge to confirm no MacConkey-specific rows,
  `supplier_catalog` blocks, or notes remain in JCM 110.
- Manually compare the regenerated record against JCM 110 and TOGO M102 to
  confirm that Solution A, Solution B, both pH adjustments, and the final 900 ml
  plus 100 ml assembly survived generation.

## Additional Notes

- No previous `ALKALINE_CELLULOSE_AGAR` review report existed in
  `reports/yaml_record_review`; this was checked with `find`, which includes
  gitignored report files.
- The ignored search found existing duplicate reports at
  `data/import_tracking/reports/merged_duplicates.tsv` for repeated peptone and
  agar rows in this exact normalized TOGO M102 source, plus a
  `WATER_AS_VOLUME` concentration-plausibility warning for its 1000 g/L water
  row.
