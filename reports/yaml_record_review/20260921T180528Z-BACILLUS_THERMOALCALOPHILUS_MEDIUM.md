# YAML Record Review: bacillus_thermoalcalophilus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml
- Started UTC: 2026-09-21T18:04:20Z
- Finished UTC: 2026-09-21T18:05:28Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml` |
| Generated ID | `CultureMech:006100` |
| Label | `bacillus_thermoalcalophilus_medium` |
| Source selected by merge | KOMODO Medium 610, `komodo.medium:610` |
| Duplicate parent | `data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml` / DSMZ Medium 610, `mediadive.medium:610` |
| Canonical normalized owner | `data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml` |
| Merge fingerprint | `458024ad3e97bd2b6d122cd54a2458862bc91642b0f00f7334d966c60ddc53de` |

The merged record is generated from the KOMODO Medium 610 copy and the DSMZ Medium 610 parent. Do not curate the generated merge directly; update the normalized owners or their importer/source transform and then regenerate.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml` | Passed |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml --out /private/tmp/BACILLUS_THERMOALCALOPHILUS_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 0 checks, all validations passed |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone `history/` files |

## Identity and Grounding

The medium identity is correct. DSMZ Medium 610 is `BACILLUS THERMOALCALOPHILUS MEDIUM`, the KOMODO record states `DSMZ Medium: 610`, and the two merged normalized records have the same pH, category, physical state, ingredient names, and non-water concentrations.

Most mapped ingredients agree with their source forms: `Na-acetate`, `KCl`, `Na2SO4`, `MgSO4`, `KH2PO4`, `K2HPO4`, and `FeSO4` are grounded to matching exact or anhydrous terms. `Yeast extract` remains ungrounded in both normalized records and in the generated merge even though an exact ignored-file-inclusive search of the packaged MIM label index found `Yeast extract` as a preferred-term mapping to `FOODON:03315426`.

## Evidence

DSMZ Medium 610 supports 3.00 g Na-acetate, 1.80 g KCl, 0.40 g `Na2SO4`, 0.20 g `MgSO4`, 0.30 g `KH2PO4`, 0.30 g `K2HPO4`, 0.01 g `FeSO4`, 10.00 g yeast extract, and 1000.00 ml distilled water, with pH 8.2. The normalized owners and generated merge carry all non-water amounts and pH 8.2 correctly.

The source PDF has no preparation details beyond pH 8.2. The generated record drops the DSMZ parent's one `preparation_steps` entry whose entire payload is `pH 8.2`, but the scalar `ph_value: 8.2` already represents that source claim.

## Completeness

Consequential gaps:

- Missing the DSMZ main `Distilled water 1000.00 ml` component.
- Missing exact ontology grounding for `Yeast extract`.

Empty target-organism, growth-evidence, and rich preparation fields are acceptable here. This review verified the DSMZ formulation PDF but did not inspect a primary Bacillus thermoalcalophilus growth publication.

An ignored-file-inclusive prior-report search covered `reports/yaml_record_review` for `BACILLUS_THERMOALCALOPHILUS_MEDIUM`, `bacillus_thermoalcalophilus_medium`, `KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium`, `CultureMech:006100`, and `CultureMech:001739`; it found no prior report for this record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The final medium omits distilled water. | DSMZ Medium 610 prints 1000.00 ml distilled water. Neither normalized owner nor the generated merge has a water ingredient. | `data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml`; `data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml` |
| Major | `Yeast extract` is left ungrounded despite a local exact mapping. | The generated row has only `preferred_term: Yeast extract`; `src/culturemech/data/mediaingredientmech/label_index.csv` maps the same label to `FOODON:03315426`. | `data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml`; `data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml`; the exact-term repair batch coverage if this omission is systemic |

## Recommended Edits

1. Add `Distilled water` as 1000.00 ml/L to both normalized Medium 610 owners.
2. Ground `Yeast extract` to `FOODON:03315426` in both normalized Medium 610 owners, preserving any repository convention for mixture or FOODON ingredients that are not ChEBI terms.
3. Regenerate `data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml`.

## Follow-up Checks

- Run `just validate data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml`.
- Run `just validate data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Re-run the no-project open-schema, strict, reference, and term validators against the regenerated `data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml`.
- Manually compare the regenerated record with DSMZ Medium 610 to confirm the non-water rows, distilled water, and pH 8.2 are all present.

## Additional Notes

One initial exact search used IDs from nearby Medium 65 and Medium 628 records and returned unrelated normalized hits. The prior-report result above is based on a corrected ignored-file-inclusive search using the generated ID `CultureMech:006100` and DSMZ parent ID `CultureMech:001739`.
