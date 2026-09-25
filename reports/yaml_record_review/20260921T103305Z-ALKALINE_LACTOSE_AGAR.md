# YAML Record Review: Alkaline Lactose Agar

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml`
- Started UTC: 2026-09-21T10:32:39Z
- Finished UTC: 2026-09-21T10:33:05Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:010329` |
| Name | `alkaline_lactose_agar` |
| Original name | `Alkaline Lactose Agar` |
| Category | `bacterial` |
| Media term | `TOGO:M90` / Alkaline Lactose Agar |
| Generated from | `data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml` |

This is a generated merge record with one normalized parent. Future fixes belong
in `data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml` or in
the TOGO importer and solution-migration path that generated its composition.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml` |
| Strict validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml --out /private/tmp/ALKALINE_LACTOSE_AGAR.strict.tsv --workers 1 --quiet` emitted 0 error rows |
| Reference validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 total checks |
| Term validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not a single embedded `MediaRecipe.curation_history` list in `data/merge_yaml/merged` |

The project-level `just validate-schema`, `just validate-strict`, and
`just validate-terms` wrappers currently fail before target-specific validation
because project `uv` tries to build `llvmlite==0.46.0` under Python 3.13 and
crashes in setuptools with `TypeError: Popen.__init__() got an unexpected
keyword argument 'dry_run'`; the same LinkML and validator entry points were
therefore run through an offline `--no-project` Python 3.11 environment.

## Identity and Grounding

TOGO M90 is Alkaline Lactose Agar and lists original media ID `JCM_M98`, so the
record has the intended TOGO identity, category, and solid-agar physical state.
The live JCM GRMD endpoint for `GRMD=98` returned a `Nothing found` page, so the
original JCM page could not be independently rechecked. TOGO M90 remains
available and internally points to the same JCM accession in the record notes.

The exact gitignore-independent search
`TOGO:M90\b|JCM_M98\b|GRMD=98\b|TOGO_M90_Alkaline_Lactose_Agar|Alkaline Lactose
Agar|alkaline_lactose_agar` covered `data/normalized_yaml`,
`data/merge_yaml`, and `data/import_tracking`. It found this TOGO M90 source and
merge plus the direct JCM import
`data/normalized_yaml/bacterial/alkaline_lactose_agar.yaml` and its generated
lowercase sibling.

## Evidence

- Supported by TOGO M90: 900 ml distilled water, 0.2 g MgSO4 x 7H2O, 5 g yeast
  extract, 1 g K2HPO4, 5 g lactose, 15 g agar, 5 g Polypepton, and 100 ml of
  10% Na2CO3 solution.
- Supported by TOGO M90: sodium carbonate solution should be sterilized by
  filtration separately, added aseptically, and the final pH should be about
  10.0.
- Not supported: distilled water is represented as `900 G_PER_L`. TOGO M90
  expresses it as 900 ml, not as a solute mass concentration.
- Not supported: the 10% Na2CO3 stock addition is represented as an empty
  `solutions` entry with `100 G_PER_L`. TOGO M90 records it as a 100 ml
  addition of a 10% stock solution.
- Not supported at exact chemical granularity: TOGO M90 says only `Lactose`.
  The specific anomer grounding `CHEBI:36218` beta-lactose is narrower than the
  source label; the adjacent direct JCM import uses the generic lactose term
  `CHEBI:17716`.

## Completeness

- The seven non-stock composition rows from TOGO M90 are all present.
- The record is missing the final pH about 10.0.
- The filter-sterilization and aseptic-addition instructions for sodium
  carbonate are missing.
- Empty target-organism, temperature, atmosphere, storage, and growth-evidence
  slots are acceptable for this import because the inspected TOGO source
  supplies no organism-specific growth claims or incubation conditions.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The 10% sodium carbonate stock is represented as a 100 g/L empty solution rather than a 100 ml stock addition. | TOGO M90 has a 100 ml row for 10% Na2CO3 solution; the generated record has a `solutions` row with empty `composition` and `100 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml` or the TOGO solution migration path |
| Major | Distilled water has the wrong unit. | TOGO M90 lists 900 ml distilled water; the record stores `900 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml` or the TOGO unit normalizer |
| Major | Preparation and final-pH claims were dropped. | TOGO M90 says the Na2CO3 stock is filter-sterilized separately and aseptically added, and that the final pH should be about 10.0; the record has no `preparation_steps` and no `ph_value`. | `data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml` |
| Minor | Lactose is over-specified to beta-lactose. | The source label is generic lactose; `CHEBI:36218` denotes beta-lactose rather than generic lactose. | TOGO enrichment for `data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml` |
| Minor | Source provenance is free text only. | TOGO M90 and JCM GRMD 98 appear only in the `notes` field; there is no structured `references` list or per-claim evidence. | `data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml`,
   represent the sodium carbonate row as 100 `ML_PER_L` of 10% Na2CO3 solution,
   or as an equivalent stock-solution addition that preserves both 10% and
   100 ml.
2. Change distilled water from `900 G_PER_L` to `900 ML_PER_L`.
3. Add preparation steps for separate filter sterilization of the Na2CO3 stock
   and aseptic addition to the medium.
4. Add the final pH about 10.0 from TOGO M90.
5. Re-ground lactose from beta-lactose to generic lactose unless a more exact
   source says the beta anomer was intended.
6. Promote TOGO M90 and the original JCM URL into structured references, marking
   JCM GRMD 98 as currently unavailable if provenance metadata supports that.
7. Regenerate the merge layer so
   `data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml` inherits the repaired
   normalized source.

## Follow-up Checks

- Re-run open schema validation on the repaired TOGO M90 source and the
  regenerated merge.
- Re-run `scripts/validate_strict.py` on both files and confirm that it emits 0
  error rows.
- Re-run the term validator after changing the lactose grounding.
- Re-run the reference validator after adding structured source links.
- Manually compare the regenerated merge with the TOGO M90 API payload to
  confirm that water and sodium carbonate stay as milliliter additions and that
  final pH 10.0 plus filter-sterile aseptic addition survive generation.

## Additional Notes

- No previous `ALKALINE_LACTOSE_AGAR` review report existed in
  `reports/yaml_record_review`; this was checked with `find`, which includes
  gitignored report files.
- The direct JCM import at
  `data/normalized_yaml/bacterial/alkaline_lactose_agar.yaml` preserves pH 10.0
  and the filter-sterile/aseptic-addition instruction, but it flattens the 100
  ml 10% Na2CO3 stock into `100 G_PER_L` of Na2CO3.
