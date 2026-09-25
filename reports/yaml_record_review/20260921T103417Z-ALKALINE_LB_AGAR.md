# YAML Record Review: Alkaline LB Agar

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml`
- Started UTC: 2026-09-21T10:33:51Z
- Finished UTC: 2026-09-21T10:34:17Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009956` |
| Name | `alkaline_lb_agar` |
| Original name | `Alkaline LB Agar` |
| Category | `bacterial` |
| Media term | `TOGO:M561` / Alkaline LB Agar |
| Generated from | `data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml` |

This is a generated merge record with one normalized parent. Future fixes belong
in `data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml` or in the
TOGO importer that generated its composition.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml` |
| Strict validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml --out /private/tmp/ALKALINE_LB_AGAR.strict.tsv --workers 1 --quiet` emitted 0 error rows |
| Reference validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 total checks |
| Term validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not a single embedded `MediaRecipe.curation_history` list in `data/merge_yaml/merged` |

The project-level `just validate-schema`, `just validate-strict`, and
`just validate-terms` wrappers currently fail before target-specific validation
because project `uv` tries to build `llvmlite==0.46.0` under Python 3.13 and
crashes in setuptools with `TypeError: Popen.__init__() got an unexpected
keyword argument 'dry_run'`; the same LinkML and validator entry points were
therefore run through an offline `--no-project` Python 3.11 environment.

## Identity and Grounding

TOGO M561 and JCM GRMD 557 both identify the recipe as Alkaline LB Agar. The
category, solid-agar state, TOGO source ID, original JCM source ID, and
single-source merge lineage are internally consistent.

The exact gitignore-independent search
`TOGO:M561\b|JCM_M557\b|GRMD=557\b|TOGO_M561_Alkaline_LB_Agar|Alkaline LB
Agar|alkaline_lb_agar` covered `data/normalized_yaml`, `data/merge_yaml`, and
`data/import_tracking`. It found this normalized TOGO M561 source and merge plus
the direct JCM import `data/normalized_yaml/bacterial/alkaline_lb_agar.yaml` and
its generated lowercase sibling.

## Evidence

- Supported: TOGO M561 and JCM 557 both list 10 g Tryptone (BD-Difco), 5 g
  Yeast extract (BD-Difco), 15 g NaCl, 5 g Na2CO3, 15 g agar, and 1 L distilled
  water.
- Supported: both inspected sources specify separate filtration sterilization
  and aseptic addition of Na2CO3, with final pH about 8.5.
- Not supported: distilled water is represented as `1 G_PER_L`. The source row
  is 1 L water, not 1 g/L water.
- Missing: final pH 8.5 and the sodium-carbonate filtration/aseptic-addition
  instruction are not represented in the generated record.

## Completeness

- All six ingredient rows from the source are present.
- The water unit, final pH, and Na2CO3 handling are the only consequential
  scientific omissions found in the inspected TOGO M561/JCM 557 source pair.
- Empty target-organism, temperature, atmosphere, storage, and growth-evidence
  slots are acceptable for this import because neither inspected source supplies
  organism-specific growth claims or incubation conditions.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Distilled water has the wrong unit. | TOGO M561 and JCM 557 list 1 L distilled water; the record stores `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml` or the TOGO unit normalizer |
| Major | Final pH and Na2CO3 handling were dropped. | Both inspected sources state that Na2CO3 is filter-sterilized separately and added aseptically, and that the final pH should be about 8.5; the generated record has no `ph_value` or `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml` |
| Minor | Source provenance is free text only. | TOGO M561 and JCM 557 appear only in the `notes` field; there is no structured `references` list or per-claim evidence. | `data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml` |

## Recommended Edits

1. Change the water row in
   `data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml` from
   `1 G_PER_L` to `1 L_PER_L` or the schema-preferred equivalent for 1 L per
   liter of final medium.
2. Add final pH about 8.5.
3. Add a preparation step that preserves separate filter sterilization of
   Na2CO3 and aseptic addition to the medium.
4. Promote TOGO M561 and JCM 557 into structured source references.
5. Regenerate the merge layer so
   `data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml` inherits the repaired
   normalized source.

## Follow-up Checks

- Re-run open schema validation on the repaired normalized source and the
  regenerated merge.
- Re-run `scripts/validate_strict.py` on both files and confirm that it emits 0
  error rows.
- Re-run the term validator to ensure the existing ChEBI groundings remain
  accepted.
- Re-run the reference validator after adding structured TOGO/JCM references.
- Manually compare the regenerated record with TOGO M561 and JCM 557 to confirm
  that the 1 L water row, pH about 8.5, and filter-sterile aseptic Na2CO3
  handling are present.

## Additional Notes

- No previous `ALKALINE_LB_AGAR` review report existed in
  `reports/yaml_record_review`; this was checked with `find`, which includes
  gitignored report files.
- The direct JCM import at `data/normalized_yaml/bacterial/alkaline_lb_agar.yaml`
  preserves pH 8.5 and the Na2CO3 handling note, but it omits the distilled
  water row.
