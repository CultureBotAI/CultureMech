# YAML Record Review: Alkaline Xylan Agar

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ALKALINE_XYLAN_AGAR.yaml`
- Started UTC: 2026-09-21T10:39:51Z
- Finished UTC: 2026-09-21T10:40:20Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ALKALINE_XYLAN_AGAR.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:010340` |
| Name | `alkaline_xylan_agar` |
| Original name | `Alkaline Xylan Agar` |
| Category | `bacterial` |
| Media term | `TOGO:M91` / Alkaline Xylan Agar |
| Generated from | `data/normalized_yaml/bacterial/TOGO_M91_Alkaline_Xylan_Agar.yaml` |

This is a generated merge record with one normalized parent. Future fixes belong
in `data/normalized_yaml/bacterial/TOGO_M91_Alkaline_Xylan_Agar.yaml` or in the
TOGO importer and solution-migration path that generated its composition.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALKALINE_XYLAN_AGAR.yaml` |
| Strict validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALKALINE_XYLAN_AGAR.yaml --out /private/tmp/ALKALINE_XYLAN_AGAR.strict.tsv --workers 1 --quiet` emitted 0 error rows |
| Reference validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALKALINE_XYLAN_AGAR.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 total checks |
| Term validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALKALINE_XYLAN_AGAR.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not a single embedded `MediaRecipe.curation_history` list in `data/merge_yaml/merged` |

The project-level `just validate-schema`, `just validate-strict`, and
`just validate-terms` wrappers currently fail before target-specific validation
because project `uv` tries to build `llvmlite==0.46.0` under Python 3.13 and
crashes in setuptools with `TypeError: Popen.__init__() got an unexpected
keyword argument 'dry_run'`; the same LinkML and validator entry points were
therefore run through an offline `--no-project` Python 3.11 environment.

## Identity and Grounding

TOGO M91 is Alkaline Xylan Agar and lists original media ID `JCM_M99`; the live
JCM GRMD 99 page is medium 99, ALKALINE XYLAN AGAR. The record's TOGO identity,
category, solid-agar state, and merge lineage are internally consistent.

The exact gitignore-independent search
`TOGO:M91\b|JCM_M99\b|GRMD=99\b|TOGO_M91_Alkaline_Xylan_Agar|Alkaline Xylan
Agar|alkaline_xylan_agar` covered `data/normalized_yaml`, `data/merge_yaml`,
and `data/import_tracking`. It found this TOGO M91 source and merge plus the
direct JCM import `data/normalized_yaml/bacterial/alkaline_xylan_agar.yaml` and
its generated lowercase sibling.

## Evidence

- Supported by both TOGO M91 and JCM 99: the medium contains 10 g xylan, 5 g
  yeast extract, 5 g peptone-family product, 1 g K2HPO4, 0.2 g MgSO4 x 7H2O,
  15 g agar, and 1 L distilled water.
- Supported by both inspected sources: after autoclaving, the pH should be
  adjusted to 10.0 with sterilized 10% Na2CO3 solution.
- Source conflict: TOGO M91 calls the carbon source `Larchwood xylan (Sigma)`
  and the peptone `Polypepton (Nihon Pharm. Co.)`; the live JCM page calls them
  generic xylan and Hipolypepton from FUJIFILM Wako.
- Not supported: distilled water is represented as `1 G_PER_L`. Both inspected
  sources express it as 1 L, not a 1 g/L mass concentration.
- Not supported: the sodium carbonate solution appears as an empty `VARIABLE`
  solution stub. TOGO M91 says it is a 10% Na2CO3 solution, and both inspected
  sources use it as a post-autoclave pH adjuster to pH 10.0.

## Completeness

- All seven non-stock, non-procedural rows are present with source-supported
  amounts.
- The record is missing final pH 10.0.
- The record is missing the post-autoclave pH-adjustment step with sterilized
  10% Na2CO3.
- Empty target-organism, temperature, atmosphere, storage, and growth-evidence
  slots are acceptable for this import because neither inspected source supplies
  organism-specific growth claims or incubation conditions.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Distilled water has the wrong unit. | TOGO M91 and JCM 99 list 1 L distilled water; the record stores `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M91_Alkaline_Xylan_Agar.yaml` or the TOGO unit normalizer |
| Major | The 10% sodium carbonate pH adjuster is an empty variable solution and the final pH step was dropped. | TOGO M91 identifies the pH adjuster as 10% Na2CO3 solution, and both inspected sources say to adjust pH to 10.0 with sterilized 10% Na2CO3 solution after autoclaving; the record has no nested Na2CO3 composition, no `ph_value`, and no `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M91_Alkaline_Xylan_Agar.yaml` |
| Minor | Supplier-specific xylan and peptone labels disagree across inspected source layers. | The generated TOGO record follows TOGO's Larchwood xylan and Polypepton labels, while the live original JCM page has generic xylan and a different supplier-specific Hipolypepton row. | Manual review of `data/normalized_yaml/bacterial/TOGO_M91_Alkaline_Xylan_Agar.yaml` against current JCM 99 |
| Minor | Source provenance is free text only. | TOGO M91 and JCM 99 appear only in `notes`; there is no structured `references` list or per-claim evidence. | `data/normalized_yaml/bacterial/TOGO_M91_Alkaline_Xylan_Agar.yaml` |

## Recommended Edits

1. Change distilled water in
   `data/normalized_yaml/bacterial/TOGO_M91_Alkaline_Xylan_Agar.yaml` from
   `1 G_PER_L` to `1 L_PER_L` or the schema-preferred 1 L/L equivalent.
2. Replace the empty sodium-carbonate stub with a 10% Na2CO3 solution used as a
   variable post-autoclave pH adjuster.
3. Add `ph_value: 10.0` and a preparation step for post-autoclave adjustment
   with sterilized 10% Na2CO3.
4. Reconcile the TOGO-vs-current-JCM labels for the xylan and peptone rows, or
   add a source note that preserves the disagreement if TOGO captured an older
   JCM version.
5. Promote TOGO M91 and JCM 99 into structured source references.
6. Regenerate the merge layer so
   `data/merge_yaml/merged/ALKALINE_XYLAN_AGAR.yaml` inherits the repaired
   normalized source.

## Follow-up Checks

- Re-run open schema validation on the repaired TOGO M91 source and the
  regenerated merge.
- Re-run `scripts/validate_strict.py` on both files and confirm that it emits 0
  error rows.
- Re-run the term validator after nesting the Na2CO3 row in a 10% solution.
- Re-run the reference validator after adding structured source links.
- Manually compare the regenerated record with TOGO M91 and JCM 99 to confirm
  that the water row, 10% Na2CO3 pH adjuster, pH 10.0, and source-specific
  xylan/peptone labels are intentionally represented.

## Additional Notes

- No previous `ALKALINE_XYLAN_AGAR` review report existed in
  `reports/yaml_record_review`; this was checked with `find`, which includes
  gitignored report files.
- The direct JCM import at
  `data/normalized_yaml/bacterial/alkaline_xylan_agar.yaml` preserves the pH
  adjustment note but omits the water row and does not structure the 10% Na2CO3
  stock solution.
