# YAML Record Review: ALKALINE NUTRIENT AGAR

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ALKALINE_NUTRIENT_AGAR.yaml`
- Started UTC: 2026-09-21T10:35:30Z
- Finished UTC: 2026-09-21T10:36:09Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ALKALINE_NUTRIENT_AGAR.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:005008` |
| Name | `alkaline_nutrient_agar` |
| Original name | `ALKALINE NUTRIENT AGAR` |
| Category | `bacterial` |
| Media term | `komodo.medium:31` / ALKALINE NUTRIENT AGAR |
| Parent source duplicate | `data/normalized_yaml/bacterial/alkaline_nutrient_agar.yaml` / `mediadive.medium:31` |
| Generated from | 53 normalized records including `KOMODO_31_ALKALINE_NUTRIENT_AGAR.yaml`, `alkaline_nutrient_agar.yaml`, and 51 `medium_31_modified_for_dsm_*` source duplicates |

This is a generated merge centered on the KOMODO import of DSMZ/MediaDive Medium
31. Future scientific fixes belong in the maintained DSMZ parent
`data/normalized_yaml/bacterial/alkaline_nutrient_agar.yaml`, the KOMODO child
`data/normalized_yaml/bacterial/KOMODO_31_ALKALINE_NUTRIENT_AGAR.yaml`, or the
KOMODO/DSMZ duplication rule that propagated the same flattened stock rows into
51 strain-specific duplicates.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALKALINE_NUTRIENT_AGAR.yaml` |
| Strict validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALKALINE_NUTRIENT_AGAR.yaml --out /private/tmp/ALKALINE_NUTRIENT_AGAR.strict.tsv --workers 1 --quiet` emitted 0 error rows |
| Reference validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALKALINE_NUTRIENT_AGAR.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 total checks |
| Term validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALKALINE_NUTRIENT_AGAR.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not a single embedded `MediaRecipe.curation_history` list in `data/merge_yaml/merged` |

The project-level `just validate-schema`, `just validate-strict`, and
`just validate-terms` wrappers currently fail before target-specific validation
because project `uv` tries to build `llvmlite==0.46.0` under Python 3.13 and
crashes in setuptools with `TypeError: Popen.__init__() got an unexpected
keyword argument 'dry_run'`; the same LinkML and validator entry points were
therefore run through an offline `--no-project` Python 3.11 environment.

## Identity and Grounding

The generated record denotes DSMZ Medium 31 as imported through KOMODO Medium
31. The generated `parent_media` link to the direct DSMZ record
`data/normalized_yaml/bacterial/alkaline_nutrient_agar.yaml` is coherent: that
record is `mediadive.medium:31`, has the same label and final pH, and has the
same peptone, meat-extract, agar, NaHCO3, and Na2CO3 amounts before correction.

The exact gitignore-independent search
`komodo.medium:31\b|mediadive.medium:31\b|KOMODO_31_ALKALINE_NUTRIENT_AGAR|ALKALINE
NUTRIENT AGAR|alkaline_nutrient_agar|DSMZ Medium: 31` covered
`data/normalized_yaml`, `data/merge_yaml`, and `data/import_tracking`. It found
the KOMODO Medium 31 parent, the direct DSMZ Medium 31 parent, 51
`medium_31_modified_for_dsm_*` exact source duplicates, and same-name
JCM/TOGO records that have distinct formulations and should remain separate.

## Evidence

- Supported by DSMZ Medium 31 and DSMZ Medium 1: the base medium contains 5 g
  peptone, 3 g meat extract, optional 15 g agar, and 1000 ml distilled water.
- Supported by DSMZ Medium 1: the base medium should be adjusted to pH 7.0 and
  can receive 10 mg MnSO4 x H2O for Bacillus sporulation.
- Supported by DSMZ Medium 31: after sterilization, sterile 1 M
  Na-sesquicarbonate solution is added at 1 ml per 10 ml to achieve pH 9.7.
- Supported inside the Na-sesquicarbonate stock: 4.2 g NaHCO3 and 5.3 g
  anhydrous Na2CO3 in 100 ml distilled water.
- Not supported: the record lacks the 1000 ml distilled-water row inherited from
  DSMZ Medium 1.
- Not supported: `42 G_PER_L` NaHCO3 and `53 G_PER_L` anhydrous Na2CO3 are
  represented as top-level final-medium ingredients. Those concentrations are
  the stock recipe's 4.2 g/100 ml and 5.3 g/100 ml values, while the final
  medium receives that stock at only 1 ml per 10 ml.
- Missing: no preparation step records the pH 7.0 base adjustment or the
  post-sterilization aseptic addition of the sterile Na-sesquicarbonate stock.

## Completeness

- The direct KOMODO record, direct DSMZ record, and 51 KOMODO strain-specific
  records merged here have the same flattened ingredient signature; the defect
  is therefore upstream of the merge and should be fixed in the maintained
  normalized inputs or common DSMZ enrichment path.
- The optional 15 g agar row is preserved with an `(if necessary)` note, which
  matches the DSMZ Medium 1 wording closely enough for a solid-agar generated
  record.
- Empty target-organism, temperature, atmosphere, storage, and growth-evidence
  slots are acceptable for this medium-level source because the inspected DSMZ
  Medium 31 and DSMZ Medium 1 PDFs supply no organism-specific growth claims or
  incubation conditions.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Na-sesquicarbonate stock components were flattened into final-medium ingredients at stock concentration. | DSMZ Medium 31 says to add 1 M Na-sesquicarbonate at 1 ml per 10 ml after sterilization and separately lists NaHCO3 4.2 g plus anhydrous Na2CO3 5.3 g in 100 ml stock; the generated record lists `NaHCO3` at `42 G_PER_L` and `Na2CO3 anhydrous` at `53 G_PER_L` as top-level ingredients. | `data/normalized_yaml/bacterial/alkaline_nutrient_agar.yaml`, `data/normalized_yaml/bacterial/KOMODO_31_ALKALINE_NUTRIENT_AGAR.yaml`, and the DSMZ resolver feeding the 51 KOMODO duplicates |
| Major | Distilled water from the inherited base medium is missing. | DSMZ Medium 31 says it is the same as Medium 1 plus Na-sesquicarbonate; DSMZ Medium 1 lists 1000 ml distilled water. | DSMZ Medium 31 import/enrichment |
| Major | Required preparation steps are missing. | DSMZ Medium 1 specifies base pH adjustment to 7.0, and DSMZ Medium 31 specifies post-sterilization addition of sterile 1 M Na-sesquicarbonate to reach pH 9.7; the generated record has `ph_value: 9.7` but no `preparation_steps`. | DSMZ Medium 31 import/enrichment |
| Minor | Source provenance is free text only. | The record notes mention KOMODO and DSMZ Medium 31, but no structured `references` list points to KOMODO, MediaDive, `DSMZ_Medium31.pdf`, or inherited `DSMZ_Medium1.pdf`. | DSMZ/KOMODO normalized records |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/alkaline_nutrient_agar.yaml`,
   `data/normalized_yaml/bacterial/KOMODO_31_ALKALINE_NUTRIENT_AGAR.yaml`, and
   their shared DSMZ-enrichment path, replace top-level `42 G_PER_L` NaHCO3 and
   `53 G_PER_L` Na2CO3 with a 1 M Na-sesquicarbonate stock composition of
   4.2 g NaHCO3 and 5.3 g anhydrous Na2CO3 in 100 ml water.
2. Represent addition of the sterile Na-sesquicarbonate stock at 1 ml per 10 ml
   final medium after sterilization.
3. Restore the 1000 ml distilled-water row inherited from DSMZ Medium 1.
4. Add preparation steps for base pH 7.0 adjustment, sterilization, and
   post-sterilization stock addition to pH 9.7.
5. Preserve the Bacillus sporulation note about optional 10 mg MnSO4 x H2O as a
   conditional preparation or variant note rather than dropping it entirely.
6. Promote KOMODO/DSMZ provenance into structured source references, including
   DSMZ Medium 31 and the inherited DSMZ Medium 1 source.
7. Regenerate the merge layer so the corrected DSMZ/KOMODO records collapse
   into `data/merge_yaml/merged/ALKALINE_NUTRIENT_AGAR.yaml` without stock
   flattening.

## Follow-up Checks

- Re-run open schema validation on the repaired DSMZ/KOMODO normalized records
  and the regenerated merge.
- Re-run `scripts/validate_strict.py` on the same files and confirm that it
  emits 0 error rows.
- Re-run the term validator to ensure sodium hydrogencarbonate, anhydrous
  sodium carbonate, and any stock-solution representation are exactly grounded
  or intentionally ungrounded.
- Re-run the reference validator after adding structured DSMZ/KOMODO source
  links.
- Manually compare the regenerated merge against `DSMZ_Medium31.pdf` and
  `DSMZ_Medium1.pdf` to confirm that distilled water, base pH 7.0, sterile 1 M
  Na-sesquicarbonate addition, final pH 9.7, and the optional Bacillus MnSO4
  note survive generation.

## Additional Notes

- No previous `ALKALINE_NUTRIENT_AGAR` review report existed in
  `reports/yaml_record_review`; this was checked with `find`, which includes
  gitignored report files.
- The generated record has 51 `variant_children` and 53 `merged_from` entries:
  the KOMODO parent, the direct DSMZ parent, and 51 KOMODO records named as
  DSMZ-strain modifications but marked as exact `SOURCE_DUPLICATE` records.
