# YAML Record Review: acidithiobacillus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ACIDITHIOBACILLUS_MEDIUM.yaml
- Started UTC: 2026-09-21T09:25:00Z
- Finished UTC: 2026-09-21T09:26:49Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ACIDITHIOBACILLUS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:001459`
- Label: `acidithiobacillus_medium`
- Original name: `ACIDITHIOBACILLUS MEDIUM`
- Category: `bacterial`
- Media term: `mediadive.medium:35` / `DSMZ Medium 35`
- Generated status: generated singleton from `data/normalized_yaml/bacterial/acidithiobacillus_medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACIDITHIOBACILLUS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ACIDITHIOBACILLUS_MEDIUM.yaml --out /private/tmp/acidithiobacillus_medium.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ACIDITHIOBACILLUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ACIDITHIOBACILLUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The DSMZ identity is correct: DSMZ Medium 35 is `ACIDITHIOBACILLUS MEDIUM`, has final pH 4.2 and final volume 1000 ml, and is represented by `mediadive.medium:35`.

Most ingredient identities are source-faithful. The DSMZ source lists 0.10 g NH4Cl, 3.00 g KH2PO4, 0.10 g `MgCl2 x 6 H2O`, 0.14 g `CaCl2 x 2 H2O`, and 10.00 g powdered sulfur; the target preserves those gram amounts as 1 L final concentrations and keeps chemically compatible CHEBI terms. The source also explicitly lists 1000.00 ml distilled water, which the target omits.

The source sulfur row is more specific than the target's `Sulfur` label because DSMZ calls for powdered sulfur, but the row remains identifiable and the preparation text preserves the special sulfur sterilization and surface-layering procedure.

## Evidence

Supported:

- DSMZ supports the target's name, MediaDive 35 source, liquid state, pH 4.2, static-incubation note, and five non-water ingredient rows.
- DSMZ supports dissolving all non-sulfur ingredients, adjusting to pH 4.2, and autoclaving the basal medium.
- DSMZ supports sterilizing sulfur separately in screw-capped tubes or bottles with a few drops of water for 3 hours at 90 - 100 degrees C in a water bath on each of three successive days.
- DSMZ supports aseptically layering the sterilized sulfur onto the surface of the autoclaved liquid basal medium before use.

Unsupported or incomplete:

- The target omits the DSMZ `Distilled water` row at 1000.00 ml.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ACIDITHIOBACILLUS_MEDIUM*' -print` searched the ignored timestamped-report directory and found no pre-existing ACIDITHIOBACILLUS MEDIUM report.
- Exact `rg --no-ignore --hidden` searches for `DSMZ_Medium35\.pdf`, `mediadive\.medium:35`, `komodo.medium:35`, `KOMODO ModelSEED | ID: 35`, `35.1`, `105150`, and `for_dsm_105150` covered tracked and ignored files. They found the expected direct DSMZ Medium 35 owner, the KOMODO Medium 35 / 35.1 family, and no representation of the DSM 105150 pH 3.0 note.
- KOMODO Medium 35 and 35.1 are separate normalized imports, and `for_dsm_612.yaml` is already linked under `thiobacillus_thiooxidans_medium`; do not merge those into this direct DSMZ owner without a dedicated variant review.
- Optional organism, growth metric, evidence, and temperature arrays are absent on the source import; that is not a target-specific defect.

## Findings

### major: DSMZ distilled water is missing

DSMZ Medium 35 explicitly lists `Distilled water 1000.00 ml` after the five gram-based ingredients. `data/normalized_yaml/bacterial/acidithiobacillus_medium.yaml` omits that solvent/final-volume row, so the generated singleton has no structured representation of the water that makes the basal medium up to 1 L.

### minor: the DSMZ 35 PDF has unmodeled strain notes

The source PDF includes three strain-specific notes: DSM 612 receives 0.10 g/L yeast extract, DSM 9463 uses complete-medium pH 3.5, and DSM 105150 uses complete-medium pH 3.0. The direct DSMZ Medium 35 owner has no `variant_children`; `for_dsm_612.yaml` exists as a KOMODO 35.1 child under the KOMODO Medium 35 family, no record for DSM 105150 was found, and the exact `for_dsm_9463.yaml` hit is an unrelated KOMODO Medium 670 variant. This does not corrupt the base pH 4.2 recipe, but the DSMZ 35 strain-note coverage is incomplete.

## Recommended Edits

1. Add the source `Distilled water` row to `data/normalized_yaml/bacterial/acidithiobacillus_medium.yaml`, using the repository's supported final-volume representation for a 1000 ml DSMZ solvent row.
2. Decide whether DSMZ Medium 35's DSM 612, DSM 9463, and DSM 105150 notes should be represented as variant children of the direct DSMZ owner or left under source-specific KOMODO imports.
3. If variants are represented under the direct DSMZ owner, add the missing pH 3.0 DSM 105150 variant and verify that any DSM 9463 record points at DSMZ Medium 35 rather than the unrelated KOMODO 670 MS-MEDIUM source.
4. Regenerate `data/merge_yaml/merged/` with `just merge-recipes`.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ACIDITHIOBACILLUS_MEDIUM.yaml`.
- Re-fetch `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium35.pdf` and confirm the five non-water ingredient rows, 1000 ml distilled-water row, pH 4.2, sulfur heat-treatment procedure, static-incubation note, and three strain-specific DSM notes are either structured or intentionally scoped out.
- Search with `rg --no-ignore --hidden '105150|for_dsm_105150|DSMZ Medium: 35' data/normalized_yaml data/merge_yaml` and confirm DSMZ Medium 35 strain-specific variants have the intended topology.

## Additional Notes

- The sulfur row uses `CHEBI:26833` / `sulfur atom`, which is broad for powdered elemental sulfur but internally consistent with nearby sulfur-containing culture records in this repository.
