# YAML Record Review: bacillus_thermoglucosidasius_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml
- Started UTC: 2026-09-21T18:05:40Z
- Finished UTC: 2026-09-21T18:07:32Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml` |
| Generated ID | `CultureMech:004843` |
| Label | `bacillus_thermoglucosidasius_medium` |
| Source selected by merge | KOMODO Medium 305, `komodo.medium:305` |
| Duplicate parent | `data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml` / DSMZ Medium 305, `mediadive.medium:305` |
| Canonical normalized owner | `data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml` |
| Merge fingerprint | `292ea32e36b057dc40840bf5010e1c988d5f82d4946591d96ca46304c3e1f281` |

The target is a generated merge of the KOMODO-imported Medium 305 record and the DSMZ Medium 305 normalized parent. Future edits belong in those normalized records or in source transforms, followed by regeneration.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml` | Passed |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml --out /private/tmp/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 0 checks, all validations passed |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone `history/` files |

## Identity and Grounding

The record identity is correct: DSMZ Medium 305 is `BACILLUS THERMOGLUCOSIDASIUS MEDIUM`, and the KOMODO duplicate explicitly says it copied from DSMZ Medium 305. The pH 7.0, solid-agar state, and ingredient concentrations all match the DSMZ parent other than the missing water row noted below.

The `Starch` ChEBI grounding is chemically compatible because the packaged MIM label index maps `Soluble starch` to `CHEBI:28017` / starch, but the `preferred_term` no longer preserves the exact supplied form from the source PDF. `Peptone` and `Yeast extract` are ungrounded in both normalized owners despite exact preferred-term mappings to `MICRO:0000178` and `FOODON:03315426`, respectively. `Meat extract` is also ungrounded, but an ignored-file-inclusive exact search found no local `Meat extract` label mapping; the available `Beef extract` FOODON mappings are not exact evidence for DSMZ's broader `Meat extract` label.

## Evidence

DSMZ Medium 305 supports 10.0 g soluble starch, 5.0 g peptone, 3.0 g meat extract, 3.0 g yeast extract, 3.0 g `KH2PO4`, 30.0 g agar, 1000.0 ml distilled water, and final pH 7.0. The generated record carries the non-water amounts and pH correctly.

The DSMZ parent carries the only preparation claim as `Adjust final pH to 7.0`. The generated KOMODO-backed merge lacks that `preparation_steps` entry, but `ph_value: 7.0` already represents the claim, so this is not a material preparation loss.

## Completeness

Consequential gaps:

- Missing the DSMZ main `Distilled water 1000.0 ml` component.
- `Soluble starch` has been collapsed to `Starch` as the `preferred_term`.
- `Peptone` and `Yeast extract` are missing exact local MIM links.

Empty target-organism and growth-evidence fields are not defects for this imported DSMZ medium. This review verified the source recipe PDF but did not inspect a primary Bacillus thermoglucosidasius growth publication.

An ignored-file-inclusive prior-report search covered `reports/yaml_record_review` for `BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM`, `bacillus_thermoglucosidasius_medium`, `KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium`, `CultureMech:004843`, and `CultureMech:001404`; it found no prior report for this record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The final medium omits distilled water. | DSMZ Medium 305 includes 1000.0 ml distilled water; neither normalized owner nor the generated merge has a water ingredient. | `data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml`; `data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml` |
| Major | `Soluble starch` was normalized to the broader `Starch` label. | DSMZ prints `Soluble starch 10.0 g`; both owners and the generated merge use `preferred_term: Starch`. The MIM label index maps `Soluble starch` to the same ChEBI term, so the ontology ID is acceptable but the source ingredient label is not preserved. | `data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml`; `data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml` |
| Major | Two exact complex ingredients are left ungrounded. | `Peptone` and `Yeast extract` have exact preferred-term rows in `src/culturemech/data/mediaingredientmech/label_index.csv`; the Medium 305 rows have only `preferred_term` and concentration. | `data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml`; `data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml`; exact-term repair coverage |

## Recommended Edits

1. Add `Distilled water` as 1000.0 ml/L to both normalized Medium 305 owners.
2. Change the `Starch` preferred term in both normalized owners back to DSMZ's exact `Soluble starch` while retaining `CHEBI:28017`.
3. Ground `Peptone` to `MICRO:0000178` and `Yeast extract` to `FOODON:03315426` in both normalized owners.
4. Leave `Meat extract` ungrounded unless a curator adds or verifies an exact mapping; do not substitute the adjacent `Beef extract` mapping.
5. Regenerate `data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml`.

## Follow-up Checks

- Run `just validate data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml`.
- Run `just validate data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Re-run the no-project open-schema, strict, reference, and term validators against the regenerated `data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml`.
- Manually compare the regenerated record with DSMZ Medium 305 to confirm exact soluble starch wording, main water, pH 7.0, and all six non-water ingredients are retained.

## Additional Notes

No additional issues.
