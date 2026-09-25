# YAML Record Review: Alkaline Clostridial Nutrient Medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml`
- Started UTC: 2026-09-21T10:31:25Z
- Finished UTC: 2026-09-21T10:31:55Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007926` |
| Name | `alkaline_clostridial_nutrient_medium` |
| Original name | `Alkaline Clostridial Nutrient Medium` |
| Category | `bacterial` |
| Media term | `TOGO:M1391` / Alkaline Clostridial Nutrient Medium |
| Generated from | `data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml` |

This is a generated merge record with one normalized parent. Future fixes belong
in `data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml`
or in the TOGO importer and solution-migration path that generated its
composition.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml` |
| Strict validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml --out /private/tmp/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.strict.tsv --workers 1 --quiet` |
| Reference validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 total checks |
| Term validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not a single embedded `MediaRecipe.curation_history` list in `data/merge_yaml/merged` |

The project-level `just validate-schema`, `just validate-strict`, and
`just validate-terms` wrappers currently fail before target-specific validation
because project `uv` tries to build `llvmlite==0.46.0` under Python 3.13 and
crashes in setuptools with `TypeError: Popen.__init__() got an unexpected
keyword argument 'dry_run'`; the same LinkML and validator entry points were
therefore run through an offline `--no-project` Python 3.11 environment.

## Identity and Grounding

The top-level identity is correct: TOGO M1391 is Alkaline Clostridial Nutrient
Medium, TOGO lists original media ID `JCM_M1295`, and the live JCM GRMD 1295
page is medium 1295, Alkaline Clostridial Nutrient Medium. The liquid physical
state is consistent with TOGO M1391. The related TOGO M1392/JCM_M1295-2 record
is the solid gellan-gum variant from the same JCM page and should stay a
separate generated record.

The exact gitignore-independent search
`TOGO:M1391\b|JCM_M1295\b|GRMD=1295\b|TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium|Alkaline
Clostridial Nutrient Medium|alkaline_clostridial_nutrient_medium` covered
`data/normalized_yaml`, `data/merge_yaml`, and `data/import_tracking`. It found
this TOGO M1391 source and merge, the adjacent TOGO M1392 solid variant, the
direct JCM import `data/normalized_yaml/bacterial/alkaline_clostridial_nutrient_medium.yaml`,
and generated siblings for both those alternate imports.

## Evidence

- Supported: TOGO M1391 and JCM 1295 both define the liquid recipe as 900 ml
  Solution A, 100 ml Solution B, and N2 as an optional cultivation atmosphere.
- Supported in Solution A: 3 g yeast extract, 5 g peptone, 10 g beef extract,
  5 g glucose, 0.5 g L-Cysteine HCl H2O, 5 g NaCl, 3 g sodium acetate, 1 g
  soluble starch, and 900 ml distilled water.
- Supported in Solution B: 7 g Na2CO3, 2.9 g NaHCO3, and 100 ml distilled
  water.
- Supported preparation claims that are missing from the generated record: set
  Solution A to pH 6.5-7.0, separately autoclave Solutions A and B, and combine
  them after cooling.
- Not faithfully supported: `mediadive.solution:5342` and
  `mediadive.solution:5343` are unrelated corpus-level Solution A and Solution B
  records. The Solution A and Solution B names in JCM 1295 are local headings
  that denote the subrecipes on that page.
- Not faithfully supported: the two water rows are summed into a single
  top-level `1000.0 G_PER_L` ingredient even though they are 900 ml and 100 ml
  preparation volumes scoped to different subsolutions.

## Completeness

- The solute set for liquid TOGO M1391 is present, and the N2 gas row reflects
  the source's cultivation atmosphere option.
- Solution membership is lost. The record should preserve Solution A and
  Solution B as local subrecipes rather than as two empty imported solution
  references.
- The pH adjustment, separate autoclaving, post-cooling combination, and static
  or N2 cultivation condition are absent from `preparation_steps`.
- Empty target-organism, temperature, storage, and growth-evidence slots are
  acceptable for this import because neither inspected TOGO/JCM source supplies
  organism-specific growth claims or an incubation temperature for JCM 1295.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Local Solution A and Solution B were migrated to unrelated global solution references with mass-concentration amounts. | TOGO M1391 and JCM 1295 define 900 ml Solution A and 100 ml Solution B on the page; the generated record points to `mediadive.solution:5342` and `mediadive.solution:5343`, which contain unrelated stock compositions, and gives the additions as `900 G_PER_L` and `100 G_PER_L`. | TOGO solution migration and `data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml` |
| Major | Water from the two local solutions was summed and assigned the wrong unit. | The source has 900 ml water in Solution A and 100 ml water in Solution B; the record has one `1000.0 G_PER_L` water ingredient with a duplicate-merge note. | TOGO import/unit normalization and duplicate-ingredient cleanup |
| Major | Preparation and cultivation conditions were dropped. | The source says Solution A is adjusted to pH 6.5-7.0, Solutions A and B are separately autoclaved and combined after cooling, and cultivation is static or under N2; the generated record has no `preparation_steps` and no structured atmosphere or static-culture note. | `data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml` |
| Minor | Source provenance is free text only. | TOGO M1391 and JCM 1295 appear only in the `notes` field; there is no structured `references` list or per-claim evidence. | `data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml` |

## Recommended Edits

1. Replace the migrated `mediadive.solution:5342` and
   `mediadive.solution:5343` references with local Solution A and Solution B
   structures scoped to JCM 1295.
2. Move yeast extract, peptone, beef extract, glucose, L-Cysteine HCl H2O, NaCl,
   sodium acetate, soluble starch, and 900 ml distilled water into Solution A.
3. Move Na2CO3, NaHCO3, and 100 ml distilled water into Solution B.
4. Record pH 6.5-7.0 adjustment for Solution A, separate autoclaving of both
   local solutions, and post-cooling combination of Solution A and Solution B.
5. Preserve the static or N2 atmosphere option in a schema-native condition slot
   or a reviewed preparation note.
6. Promote TOGO M1391 and JCM 1295 into structured source references.
7. Regenerate the merge layer so
   `data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml` inherits
   the repaired normalized source.

## Follow-up Checks

- Re-run open schema validation on the maintained TOGO M1391 source and the
  regenerated merge.
- Re-run `scripts/validate_strict.py` on both files and confirm that it emits 0
  error rows.
- Re-run the term validator and verify that the existing ingredient groundings
  remain accepted after the ingredients are nested under local solutions.
- Re-run the reference validator after adding structured TOGO/JCM references.
- Manually compare the regenerated record against JCM 1295 and TOGO M1391 to
  confirm that the 900 ml and 100 ml water rows, Solution A/Solution B grouping,
  pH 6.5-7.0 adjustment, separate autoclaving, and post-cooling mixing survived
  generation.

## Additional Notes

- No previous `ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM` review report existed in
  `reports/yaml_record_review`; this was checked with `find`, which includes
  gitignored report files.
- The ignored search found existing duplicate and plausibility reports at
  `data/import_tracking/reports/merged_duplicates.tsv` and
  `data/import_tracking/reports/concentration_plausibility.tsv` for this exact
  normalized TOGO source's summed water row.
