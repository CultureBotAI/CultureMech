# YAML Record Review: azospirillum_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/AZOSPIRILLUM_MEDIUM.yaml
- Started UTC: 2026-09-21T17:03:04Z
- Finished UTC: 2026-09-21T17:06:51Z
- Verdict: needs curation

## Target

| Field | Observed |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:004576 |
| name | azospirillum_medium |
| original_name | AZOSPIRILLUM medium |
| category | bacterial |
| media_term | KOMODO Medium 221, komodo.medium:221 |
| generated status | Generated merge artifact in data/merge_yaml/merged |
| maintained owners | data/normalized_yaml/bacterial/KOMODO_221_AZOSPIRILLUM_medium.yaml; data/normalized_yaml/bacterial/azospirillum_medium.yaml |

The target is the generated source-duplicate merge for `KOMODO_221_AZOSPIRILLUM_medium` and
`azospirillum_medium`, with merge fingerprint
`ea8b7a3069eef162caee8ffc0b7a19106222b3e676e9ceff6d04f9b17fa11b15`.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/AZOSPIRILLUM_MEDIUM.yaml` completed with no errors. |
| Strict validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/AZOSPIRILLUM_MEDIUM.yaml --out /private/tmp/AZOSPIRILLUM_MEDIUM.strict.tsv --workers 1 --quiet` completed with no errors. |
| Reference validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/AZOSPIRILLUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 checks. |
| Term validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/AZOSPIRILLUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` completed with no errors, aside from a non-fatal `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused embedded `MediaRecipe.curation_history` validator for one merge record. |
| Direct `just` validators | Not checked: the project-level `uv` environment currently fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13, with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project LinkML validator workaround above exercised the target schema, strict, reference, and term checks. |

## Identity and Grounding

- The record identity is supported. `data/normalized_yaml/bacterial/azospirillum_medium.yaml`
  is DSMZ/MediaDive Medium 221, `AZOSPIRILLUM MEDIUM`, and links to the live DSMZ
  Medium 221 PDF.
- `data/normalized_yaml/bacterial/KOMODO_221_AZOSPIRILLUM_medium.yaml` names KOMODO
  Medium 221 and explicitly records `DSMZ Medium: 221 (mediadive.medium:221)`.
- The source-duplicate relationship is supported. The DSMZ and KOMODO normalized owners
  have the same medium name, pH 7.1, physical-state model, and 13 ingredient rows with
  matching names and concentrations.
- The generated target's `medium_type: COMPLEX` and `composition_type: SEMI_DEFINED`
  are consistent with the inspected recipe because yeast extract is undefined and the
  remaining listed solutes are defined chemicals or optional agar.

## Evidence

Supported by inspected source text:

- DSMZ Medium 221 lists the AZOSPIRILLUM MEDIUM recipe with yeast extract 0.05 g,
  K2HPO4 0.25 g, FeSO4 x 7 H2O 0.01 g, Na2MoO4 x 2 H2O 1 mg,
  MnSO4 x H2O 2 mg, MgSO4 x 7 H2O 0.20 g, NaCl 0.10 g,
  CaCl2 x 2 H2O 0.02 g, (NH4)2SO4 1.00 g, Biotin 0.10 mg,
  Distilled water 950.00 ml, and a pH adjustment to 7.1.
- DSMZ Medium 221 also makes agar conditional and directs the curator to autoclave the
  basal medium for 15 min at 121 C, then add 25 ml each of filter-sterilized 20%
  glucose and 20% Na-malate.
- The generated target correctly converts the DSMZ milligram rows into final
  gram-per-liter rows: Na2MoO4 x 2 H2O `0.001 G_PER_L`,
  MnSO4 x H2O `0.002 G_PER_L`, and Biotin `0.0001 G_PER_L`.
- The `Glucose` and `Na malate` rows at `5 G_PER_L` are arithmetically consistent
  with adding 25 ml of a 20% stock of each to the 950 ml basal recipe.

Unsupported or stale in the generated target:

- The target has no `Distilled water` row even though DSMZ Medium 221 lists 950.00 ml.
- The target has no `preparation_steps` even though the DSMZ normalized source owner
  preserves the pH adjustment, optional agar, autoclave, and post-sterilization
  glucose and Na-malate additions.

## Completeness

- Source provenance is sufficient to recover the formulation: the KOMODO owner points to
  DSMZ Medium 221, and the DSMZ owner carries the cited DSMZ PDF URL.
- Empty organism, growth-metric, and standalone `references` slots are acceptable for
  this source recipe. The inspected DSMZ source establishes a formulation, not a growth
  claim for a specific Azospirillum strain.
- Exact gitignore-independent search found no raw KOMODO JSON payload for
  `komodo.medium:221`; it covered `data/raw/komodo`, `data/raw/komodo_web`,
  `data/import_tracking`, and `data/normalized_yaml/bacterial`. The checked-in
  KOMODO raw directories currently contain only README files, so the normalized
  KOMODO source duplicate was verified through its DSMZ cross-reference.
- Exact gitignore-independent search covered `reports/yaml_record_review` for existing
  report metadata pointing at `data/merge_yaml/merged/AZOSPIRILLUM_MEDIUM.yaml`;
  no prior Markdown report for this exact generated record was found.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The DSMZ 950 ml water base is missing. | DSMZ Medium 221 lists 950.00 ml Distilled water, but neither the generated target nor either normalized source owner contains a water ingredient row. | `data/normalized_yaml/bacterial/azospirillum_medium.yaml`; mirror into `data/normalized_yaml/bacterial/KOMODO_221_AZOSPIRILLUM_medium.yaml` if source-duplicate owners are expected to stay formulation-identical. |
| Major | The generated merge drops the only preparation step. | The DSMZ owner preserves the pH 7.1 adjustment, conditional 1.5% agar, 121 C autoclave, and filter-sterilized glucose and Na-malate additions. The generated merge has no `preparation_steps`, and `RecipeMerger` merges only ingredients, categories, synonyms, and merge provenance from noncanonical duplicates. | `src/culturemech/merge/merger.py`, then regenerate `data/merge_yaml/merged/AZOSPIRILLUM_MEDIUM.yaml`. |

No blocker or minor findings found.

## Recommended Edits

1. Add the missing DSMZ water row to `data/normalized_yaml/bacterial/azospirillum_medium.yaml`
   as `950.0 ML_PER_L` or an equivalent supported volume representation.
2. Decide whether source-duplicate KOMODO records copied from DSMZ should also retain the
   water and preparation fields from their DSMZ counterparts; if so, update
   `data/normalized_yaml/bacterial/KOMODO_221_AZOSPIRILLUM_medium.yaml` or the
   DSMZ-to-KOMODO composition enrichment path.
3. Teach `RecipeMerger` to preserve unique source-supported `preparation_steps` when an
   ingredient-fingerprint merge selects a canonical recipe that lacks them.
4. Regenerate `data/merge_yaml/merged/AZOSPIRILLUM_MEDIUM.yaml` from the corrected
   normalized and merge inputs.

## Follow-up Checks

- `just validate-strict data/normalized_yaml/bacterial/azospirillum_medium.yaml` after
  adding the missing distilled-water volume.
- `just validate-terms data/normalized_yaml/bacterial/azospirillum_medium.yaml` after
  grounding the water row to CHEBI:15377.
- A focused `RecipeMerger` unit test showing that a KOMODO/DSMZ source-duplicate merge
  keeps preparation steps present only on the DSMZ owner.
- `just verify-merges` after regenerating the merge layer.
- Manual comparison with DSMZ Medium 221 to verify the 950 ml basal water, pH 7.1,
  optional agar, and 25 ml post-autoclave glucose and Na-malate additions.

## Additional Notes

- `linkml-reference-validator` performed zero checks because this generated record has
  no `references` block.
- DSMZ Medium 221 uses optional agar. The existing `Agar` ingredient row carries
  `notes: ' (if required)'`, so the conditional agar text is partially preserved even
  before the generated merge regains the full preparation step.
