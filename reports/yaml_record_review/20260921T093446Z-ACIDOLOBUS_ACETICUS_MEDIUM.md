# YAML Record Review: acidolobus_aceticus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ACIDOLOBUS_ACETICUS_MEDIUM.yaml
- Started UTC: 2026-09-21T09:33:00Z
- Finished UTC: 2026-09-21T09:34:47Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ACIDOLOBUS_ACETICUS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:006771`
- Label: `acidolobus_aceticus_medium`
- Original name: `ACIDOLOBUS ACETICUS medium`
- Category: `archaea`
- Media term: `komodo.medium:901` / `ACIDOLOBUS ACETICUS medium`
- Generated status: generated merge from `data/normalized_yaml/archaea/KOMODO_901_ACIDOLOBUS_ACETICUS_medium.yaml`, `data/normalized_yaml/archaea/acidilobus_medium.yaml`, `data/normalized_yaml/archaea/acidilobus_saccharovorans_medium.yaml`, `data/normalized_yaml/archaea/acidolobus_aceticus_medium.yaml`, and `data/normalized_yaml/bacterial/for_dsm_16705.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACIDOLOBUS_ACETICUS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ACIDOLOBUS_ACETICUS_MEDIUM.yaml --out /private/tmp/acidolobus_aceticus.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ACIDOLOBUS_ACETICUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ACIDOLOBUS_ACETICUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target identity is internally confused. KOMODO Medium 901 and DSMZ Medium 901 both point to `ACIDOLOBUS ACETICUS MEDIUM` and should be source duplicates. KOMODO Medium 901.1 is a DSM 16705 strain-specific variant of that DSMZ 901 recipe. JCM Medium 308 is `ACIDILOBUS MEDIUM`, and JCM Medium 934 is `ACIDILOBUS SACCHAROVORANS MEDIUM`; they are Acidilobus records and should not be merged into an Acidolobus aceticus generated record.

The DSMZ 901 base recipe is itself flattened. DSMZ lists a 1 L main medium with 1 ml Trace element solution SL-10, 0.5 ml 0.1% resazurin, 10 g powdered sulfur, 3 g yeast extract, 1 ml 10x Wolin's vitamin solution, and 15 ml 3% neutralized sulfide solution. The target lists the stock compositions directly as final ingredients at stock strengths, including 1.5 g/L `FeCl2 x 4 H2O`, 0.07 g/L `ZnCl2`, vitamin rows such as 0.02 g/L biotin, and 30 g/L `Na2S x 9 H2O`.

## Evidence

Supported:

- Live DSMZ Medium 901 supports the target's base mineral salts, powdered sulfur, 3 g/L yeast extract, 0.5 ml/L resazurin, 1 ml/L SL-10, 1 ml/L Wolin's vitamin solution, 15 ml/L neutralized sulfide solution, and final pH range 3.5 - 3.8.
- Live KOMODO Medium 901 has the same DSMZ Medium 901 provenance and lists final scaled trace-element, vitamin, and sulfide amounts rather than stock-strength rows.
- Live DSMZ Medium 901 and live KOMODO Medium 901.1 both support a DSM 16705 variant with yeast extract reduced to 0.10 g/L and D-glucose added at 2.00 g/L after sterilization.
- Live JCM Medium 308 supports the JCM 308 identity of `acidilobus_medium`; that source has a distinct JCM recipe rather than DSMZ Medium 901.

Unsupported or over-scoped:

- The generated `merged_from` list includes `acidilobus_medium` / JCM 308 and `acidilobus_saccharovorans_medium` / JCM 934 even though those are not DSMZ 901 or KOMODO 901.
- `for_dsm_16705` is merged as a duplicate even though it should carry the DSM 16705 glucose and yeast-extract modifications.
- DSMZ 901 stock solutions are expanded as final ingredients at stock concentration.
- The DSMZ/JCM anaerobic preparation, gas atmosphere, sulfur steaming, filter-sterilized vitamin addition, neutralized sulfide addition, and 1 N H2SO4 final pH adjustment are absent from the generated record.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ACIDOLOBUS_ACETICUS*' -print` searched the ignored timestamped-report directory and found no pre-existing ACIDOLOBUS ACETICUS report.
- Exact `rg --no-ignore --hidden` searches for `komodo\.medium:901`, `komodo\.medium:901\.1`, `mediadive\.medium:901`, `mediadive\.medium:J308`, `mediadive\.medium:J934`, `DSMZ Medium: 901`, `ACIDOLOBUS ACETICUS`, `acidilobus_saccharovorans`, and `for_dsm_16705` covered tracked and ignored files. They found the five generated inputs, the separate `acidolobus_aceticus_medium_for_dsm_16705.yaml` TOGO branch, the separate TOGO M980 Acidilobus saccharovorans branch, and the earlier ACIDILOBUS review report.
- The earlier ACIDILOBUS review also found that JCM 308 should be represented with TOGO M303 in an Acidilobus generated record, not inside this Acidolobus aceticus merge.
- Optional organism, growth metric, evidence, and temperature arrays are absent on the source imports; that is not a target-specific defect.

## Findings

### blocker: distinct Acidilobus JCM recipes merged into Acidolobus aceticus

`acidilobus_medium.yaml` is JCM Medium 308 `ACIDILOBUS MEDIUM`, and `acidilobus_saccharovorans_medium.yaml` is JCM Medium 934 `ACIDILOBUS SACCHAROVORANS MEDIUM`. Those records share historical stock-flattening artifacts with DSMZ/KOMODO 901, but they are not source duplicates of DSMZ Medium 901 `ACIDOLOBUS ACETICUS MEDIUM`. The generated target still merges them as synonyms of `ACIDOLOBUS_ACETICUS_MEDIUM`, so the output erases two different JCM identities.

### blocker: the DSM 16705 strain variant collapsed into the base KOMODO 901 record

DSMZ Medium 901 says DSM 16705 reduces yeast extract to 0.10 g/L and adds 2.00 g/L D-glucose after sterilization; live KOMODO Medium 901.1 has that same extra glucose and reduced yeast amount. `data/normalized_yaml/bacterial/for_dsm_16705.yaml` is now linked under KOMODO 901 as a `STRAIN_SPECIFIC_VARIANT`, but the generated record predates that repair and still folds `for_dsm_16705` into `merged_from` as if it were an exact duplicate.

### blocker: DSMZ 901 stock solutions are flattened at stock strength

The DSMZ Medium 901 main recipe should add 1 ml/L Trace element solution SL-10, 1 ml/L Wolin's vitamin solution, and 15 ml/L neutralized sulfide solution. The generated record stores SL-10 metals, Wolin vitamins, and the sulfide stock as direct final-medium ingredients at stock concentrations, making many rows roughly 1000x too high and the sulfide stock about 100x too high. The target also omits all water rows and the stock-solution boundaries that make the amounts meaningful.

### major: anaerobic preparation semantics are absent

DSMZ 901 and JCM 308 both require specialized anaerobic handling: N2/CO2 or CO2 gassing, sulfur steaming over three days, separate yeast-extract, vitamin, and sulfide sterilization, aseptic anaerobic additions, and final acidification. The generated target has no `preparation_steps`, so it cannot reproduce the source redox, gas, sulfur, sulfide, or post-sterilization constraints.

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` from the current normalized topology so `for_dsm_16705` is no longer merged into the base KOMODO 901 output as a source duplicate.
2. Remove `data/normalized_yaml/archaea/acidilobus_medium.yaml` and `data/normalized_yaml/archaea/acidilobus_saccharovorans_medium.yaml` from the Acidolobus aceticus merge; repair them under the separate Acidilobus JCM 308 / JCM 934 family.
3. Repair DSMZ Medium 901 and KOMODO Medium 901 by nesting the SL-10, Wolin vitamin, and neutralized sulfide stocks instead of flattening their contents at stock strength.
4. Repair `data/normalized_yaml/bacterial/for_dsm_16705.yaml` to include the DSM 16705 D-glucose addition and 0.10 g/L yeast-extract reduction, then keep it as a strain-specific child.
5. Preserve DSMZ 901 anaerobic preparation steps, gas atmospheres, sulfur steaming, filter-sterilized vitamins, neutralized sulfide addition, and H2SO4 pH adjustment.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ACIDOLOBUS_ACETICUS_MEDIUM.yaml`.
- Re-fetch DSMZ Medium 901 plus KOMODO Medium 901 and 901.1, then confirm the base and DSM 16705 variant have different yeast/glucose signatures.
- Search with `rg --no-ignore --hidden 'mediadive\\.medium:J308|mediadive\\.medium:J934|acidilobus_medium|acidilobus_saccharovorans_medium' data/merge_yaml/merged/ACIDOLOBUS_ACETICUS_MEDIUM.yaml` and confirm no Acidilobus JCM record remains in this Acidolobus aceticus generated record.
- Search with `rg --no-ignore --hidden 'Glucose|0\\.10|16705' data/normalized_yaml/bacterial/for_dsm_16705.yaml data/merge_yaml/merged` and confirm the DSM 16705 branch survives as a separate child with the right source modifications.

## Additional Notes

- `data/normalized_yaml/archaea/acidolobus_aceticus_medium_for_dsm_16705.yaml` is another DSM 16705 branch from TOGO that should be compared during the strain-variant repair; it was not fully reviewed here.
