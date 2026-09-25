# YAML Record Review: bacteriovorax_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bacteriovorax_medium__7f770423.yaml
- Started UTC: 2026-09-21T18:14:00Z
- Finished UTC: 2026-09-21T18:15:21Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/bacteriovorax_medium__7f770423.yaml` |
| Generated ID | `CultureMech:000434` |
| Label | `bacteriovorax_medium` |
| Source | DSMZ Medium 1012b, `mediadive.medium:1012b` |
| Maintained owner | `data/normalized_yaml/bacterial/bacteriovorax_medium.yaml` |
| Merge fingerprint | `7f77042353a267d3f7885c2c713b2e4b3c450ec4ba589282406ce6284322e0cf` |

The target is a generated single-source merge from the lowercase DSMZ Medium 1012b owner. Its hash suffix correctly distinguishes this liquid HEPES Bacteriovorax protocol from DSMZ Medium 844 / PPYE.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bacteriovorax_medium__7f770423.yaml` | Passed |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bacteriovorax_medium__7f770423.yaml --out /private/tmp/bacteriovorax_medium__7f770423.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bacteriovorax_medium__7f770423.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 0 checks, all validations passed |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bacteriovorax_medium__7f770423.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone `history/` files |

## Identity and Grounding

The generated hash suffix and `mediadive.medium:1012b` source keep this HEPES-based Bacteriovorax recipe distinct from DSMZ Medium 844, which shares the same normalized name but has a PPYE agar formulation. DSMZ Medium 1012b supports the pH 7.2, liquid state, MgCl2 and CaCl2 amounts, and prey-cell preparation instructions.

The MgCl2 and CaCl2 rows are grounded to exact hydrate terms. The HEPES ingredient is internally inconsistent: the primary `term` is `CHEBI:46756`, the secondary link still uses deprecated `mediaingredientmech_term: MediaIngredientMech:000426`, and the packaged MIM label index maps both `HEPES` and `HEPES buffer` to `CHEBI:42334`. The local ChEBI structure index also distinguishes `CHEBI:42334`, with formula and mass, from `CHEBI:46756`, which has no formula/mass in the local snapshot.

## Evidence

DSMZ Medium 1012b supports final pH 7.2, final volume 1000 ml, 6.00 g HEPES buffer, 0.60 g `MgCl2 x 6 H2O`, 0.30 g `CaCl2 x 2 H2O`, and 1000.00 ml distilled water. It also supports both preparation steps: grow prey bacteria on agar plates, wash a 24-hour-old culture from one plate into 5 ml sterile water, autoclave the HEPES buffer at pH 7.2, then add 5 ml host-cell suspension to 50 ml HEPES buffer at room temperature and incubate the final suspension with shaking.

The generated record carries the three non-water component amounts, pH 7.2, and the source's procedural text, but omits distilled water.

## Completeness

Consequential gaps:

- Missing `Distilled water 1000.00 ml`, despite the explicit DSMZ final volume.
- HEPES uses a stale primary ChEBI ID and a deprecated `MediaIngredientMech:000426` link rather than the exact CHEBI-keyed MIM mapping.

The source text mentions DSM 116241 and DSM 115080 host-organism guidance outside the medium formulation. Those strain-specific prey instructions are not represented, but they do not change the recipe identity or amounts reviewed here.

An ignored-file-inclusive prior-report search covered `reports/yaml_record_review` for `bacteriovorax_medium__7f770423`, `mediadive.medium:1012b`, `CultureMech:000434`, and `DSMZ Medium 1012b`; it found no prior report for this generated record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The medium omits distilled water. | DSMZ Medium 1012b lists final volume 1000 ml and `Distilled water 1000.00 ml`; neither the normalized owner nor the generated merge has a water row. | `data/normalized_yaml/bacterial/bacteriovorax_medium.yaml` |
| Major | HEPES is still grounded through stale and inconsistent identifiers. | The record uses `CHEBI:46756` plus a legacy `MediaIngredientMech:000426` field. The current packaged MIM label index maps `HEPES buffer` to `CHEBI:42334`, not `CHEBI:46756`. | `data/normalized_yaml/bacterial/bacteriovorax_medium.yaml`; the id-not-found/legacy-MIM repair coverage |

## Recommended Edits

1. Add `Distilled water` as 1000.00 ml/L to `data/normalized_yaml/bacterial/bacteriovorax_medium.yaml`.
2. Re-ground `HEPES buffer` to the current exact MIM/CHEBI mapping, replacing the legacy `mediaingredientmech_term` with `mediaingredientmech_chebi_term`.
3. Regenerate `data/merge_yaml/merged/bacteriovorax_medium__7f770423.yaml`.

## Follow-up Checks

- Run `just validate data/normalized_yaml/bacterial/bacteriovorax_medium.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Re-run the no-project open-schema, strict, reference, and term validators against `data/merge_yaml/merged/bacteriovorax_medium__7f770423.yaml`.
- Manually compare the regenerated record with DSMZ Medium 1012b to confirm water, pH 7.2, the three non-water ingredients, and the prey-cell procedure are retained.

## Additional Notes

No additional issues.
