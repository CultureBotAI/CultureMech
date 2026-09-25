# YAML Record Review: acidithiobacillus_ferrivorans_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml
- Started UTC: 2026-09-21T09:19:25Z
- Finished UTC: 2026-09-21T09:21:16Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:003073`
- Label: `acidithiobacillus_ferrivorans_medium`
- Original name: `ACIDITHIOBACILLUS FERRIVORANS MEDIUM`
- Category: `bacterial`
- Media term: `mediadive.medium:J729` / `JCM Medium J729`
- Generated status: generated singleton from `data/normalized_yaml/bacterial/JCM_J729_ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml --out /private/tmp/acidithiobacillus_ferrivorans.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The JCM identity is correct: the live `GRMD=729` page is `ACIDITHIOBACILLUS FERRIVORANS MEDIUM`, and the target points at `mediadive.medium:J729`.

The recipe body is not source-faithful. JCM J729 is a 1 L medium built from:

- 845 ml distilled water
- 100 ml `UBS solution`
- 10 ml `Trace minerals` from JCM Medium 151
- 10 ml `Ni-Se-W solution` from JCM Medium 244
- pH adjustment to 2.5 with H2SO4 before autoclaving
- 25 ml of 0.1 M K2S4O6 and 10 ml of 10 mM FeSO4, both filter-sterilized and added after cooling

The target instead puts UBS, trace-mineral, Ni-Se-W, tetrathionate, and ferrous-sulfate stock components directly into the final ingredient list as `G_PER_L` values. The target also loses the 845 ml water row and the explicit 100/10/10/25/10 ml stock-addition volumes.

## Evidence

Supported:

- The target's ID, label, pH 2.5, and JCM provenance are supported by JCM J729.
- JCM supports a 1 L UBS stock containing 14 g Na2SO4, 30 g ammonium sulfate, 1 g KCl, 5 g MgSO4 x 7 H2O, 0.5 g K2HPO4, and 0.14 g Ca(NO3)2 x 4 H2O.

Unsupported or over-scoped:

- The UBS salts are stored at stock strength, so Na2SO4, ammonium sulfate, MgSO4 x 7 H2O, K2HPO4, and Ca(NO3)2 x 4 H2O are roughly 10x too high for a 100 ml/L addition.
- `K2S4O6` is stored as 25 g/L even though JCM adds 25 ml of a 0.1 M solution.
- `FeSO4` is stored as 10 g/L even though JCM adds 10 ml of a 10 mM solution at pH 2.0.
- Components from the JCM 151 trace-mineral and JCM 244 Ni-Se-W cross-references are flattened as if they were direct gram-per-liter additions to this medium.
- The preparation step says to add filter-sterilized solutions but does not name or model the five post-cooling additions.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ACIDITHIOBACILLUS_FERRIVORANS*' -print` searched the ignored timestamped-report directory and found no pre-existing ACIDITHIOBACILLUS FERRIVORANS report.
- Exact `rg --no-ignore --hidden` searches for `GRMD=729`, `mediadive.medium:J729`, `JCM_J729`, `TOGO_M752`, `mediadive.medium:1234`, and `komodo.medium:1234` covered `data/merge_yaml`, `data/normalized_yaml`, and the ignored `reports/yaml_record_review` directory. They found the expected JCM target, the TOGO JCM import, the separate DSMZ 1234 / KOMODO 1234 same-name family, and no earlier ACIDITHIOBACILLUS FERRIVORANS review report.
- DSMZ Medium 1234 is a similar Acidithiobacillus ferrivorans medium with final concentrations and a Modified Wolin's mineral solution; it should remain separate from JCM J729 until the JCM stock volumes and cross-references are correctly represented.
- Optional organism, growth metric, and evidence arrays are absent on the source import; that is not a target-specific defect.

## Findings

### blocker: stock and cross-reference solutions are flattened into direct final ingredients

JCM J729 is defined by adding five stock solutions to 845 ml water: UBS at 100 ml/L, JCM 151 Trace minerals at 10 ml/L, JCM 244 Ni-Se-W at 10 ml/L, 0.1 M K2S4O6 at 25 ml/L, and 10 mM FeSO4 at 10 ml/L. `data/normalized_yaml/bacterial/JCM_J729_ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml` stores the contents of those solutions at stock strength as ordinary `G_PER_L` final ingredients. That makes the UBS salts about 10x too concentrated, makes tetrathionate and ferrous sulfate unrelated to the source additions, and erases two JCM cross-medium references. The generated singleton inherits those unsupported rows directly from the maintained JCM input.

### major: post-autoclave solution handling is only prose

JCM requires K2S4O6 and FeSO4 to be filter-sterilized and added after cooling, with the FeSO4 stock held at pH 2.0. The target has only a generic preparation sentence that says filter-sterilized solutions are added after cooling; because the actual solution rows were flattened, the record cannot tell which chemicals are post-autoclave additions or how to prepare the 0.1 M and 10 mM stocks.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/JCM_J729_ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml`, restore the top-level JCM recipe as 845 ml water plus 100 ml UBS solution, 10 ml Trace minerals, 10 ml Ni-Se-W solution, 25 ml 0.1 M K2S4O6, and 10 ml 10 mM FeSO4.
2. Nest the UBS solution with its six source components at stock concentrations and point the Trace minerals and Ni-Se-W rows at JCM Medium 151 and JCM Medium 244 rather than expanding those cross-references as direct ingredients of JCM J729.
3. Preserve the post-cooling, filter-sterilized addition semantics for K2S4O6 and FeSO4.
4. Apply the same JCM J729 structural repair to `data/normalized_yaml/bacterial/TOGO_M752_Acidithiobacillus_Ferrivorans_Medium.yaml`, whose importer preserved empty solution placeholders for this source but not their compositions.
5. Regenerate `data/merge_yaml/merged/` with `just merge-recipes`.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml`.
- Re-fetch JCM `GRMD=729` and the TOGO M752 API payload, then confirm all five addition volumes and the UBS stock composition survive regeneration.
- Search with `rg --no-ignore --hidden '0.1 M K2S4O6|10 mM FeSO4|Trace minerals|Ni-Se-W' data/normalized_yaml/bacterial/JCM_J729_ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml data/merge_yaml/merged/ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml` and confirm those labels are represented as solutions rather than flattened direct ingredients.

## Additional Notes

- The generated DSMZ/KOMODO 1234 Acidithiobacillus ferrivorans records are nearby same-name siblings but have a distinct DSMZ source and a Modified Wolin's mineral stock. They need separate reviews before any JCM-vs-DSMZ variant relationship is asserted.
- `Na2SeO4` still carries a legacy `mediaingredientmech_term` while most other rows have `mediaingredientmech_chebi_term`; the structural flattening defects are more severe than that legacy-link cleanup.
