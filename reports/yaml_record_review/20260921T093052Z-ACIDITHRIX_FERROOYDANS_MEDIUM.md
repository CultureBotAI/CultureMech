# YAML Record Review: acidithrix_ferrooydans_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ACIDITHRIX_FERROOYDANS_MEDIUM.yaml
- Started UTC: 2026-09-21T09:29:15Z
- Finished UTC: 2026-09-21T09:30:53Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ACIDITHRIX_FERROOYDANS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:007588`
- Label: `acidithrix_ferrooydans_medium`
- Original name: `Acidithrix Ferrooydans Medium`
- Category: `bacterial`
- Media term: `TOGO:M1070` / `Acidithrix Ferrooydans Medium`
- Generated status: generated singleton from `data/normalized_yaml/bacterial/TOGO_M1070_Acidithrix_Ferrooydans_Medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACIDITHRIX_FERROOYDANS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ACIDITHRIX_FERROOYDANS_MEDIUM.yaml --out /private/tmp/acidithrix_ferrooydans.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ACIDITHRIX_FERROOYDANS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ACIDITHRIX_FERROOYDANS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The JCM identity is correct despite the unusual spelling: live JCM Medium 1012 is titled `ACIDITHRIX FERROOYDANS MEDIUM`, TOGO M1070 points to `JCM_M1012`, and both sources list the same top-level recipe.

The generated target is stale relative to its maintained normalized owner. The live JCM/TOGO recipe has 100 ml UBS solution from Medium 729, 10 ml Trace minerals from Medium 151, 10 ml Ni-Se-W solution from Medium 244, 0.9 g glucose, 0.2 g yeast extract, 1.0 L distilled water, adjustment to pH 2.5 with H2SO4, autoclaving, and 5 ml filter-sterilized 1 M FeSO4 solution at pH 2.0 after cooling. `data/normalized_yaml/bacterial/TOGO_M1070_Acidithrix_Ferrooydans_Medium.yaml` was repaired on 2026-09-11 to carry that hierarchy, but the generated merge still reflects the earlier flat import from 2026-08-06.

## Evidence

Supported:

- JCM Medium 1012 and the TOGO M1070 API support the target's TOGO/JCM source identity, glucose, yeast extract, distilled-water, H2SO4, UBS, Trace minerals, Ni-Se-W, and 1 M FeSO4 ingredients.
- The normalized TOGO owner now supports the main pH 2.5, nested UBS, Trace minerals, Ni-Se-W, and FeSO4 solution rows, and the post-cooling filter-sterilized FeSO4 addition.

Unsupported or incomplete in the generated target:

- `Distilled water` still has `1 G_PER_L` even though the normalized owner now carries the source's 1.0 L water amount.
- UBS, Trace minerals, Ni-Se-W, and 1 M FeSO4 are empty `solutions` placeholders with source milliliter amounts encoded as `G_PER_L`.
- `ph_value: 2.5`, nested stock compositions, source references, curation flags, and structured preparation steps were all added to the normalized owner on 2026-09-11 but are absent from the generated YAML.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ACIDITHRIX*' -print` searched the ignored timestamped-report directory and found no pre-existing ACIDITHRIX report.
- Exact `rg --no-ignore --hidden` searches for `TOGO:M1070`, `M1070`, `JCM_M1012`, `GRMD=1012`, `jcm_grmd\?GRMD=1012`, `Ferrooydans`, and `Acidithrix` covered tracked and ignored files. They found the reviewed TOGO owner, a separate direct JCM J1012 owner, unrelated NBRC/JCM medium-number collisions, and no earlier review report.
- `data/normalized_yaml/bacterial/acidithrix_ferrooydans_medium.yaml` and `data/merge_yaml/merged/acidithrix_ferrooydans_medium__b3120235.yaml` are a separate direct JCM J1012 import for the same original recipe; that direct owner still flattens referenced JCM stocks into top-level ingredients and should be repaired or deduplicated against the curated TOGO M1070 owner.
- Optional organism, growth metric, evidence, and temperature arrays are absent on the source import; that is not a target-specific defect.

## Findings

### blocker: generated TOGO M1070 is stale after a source repair

The maintained TOGO owner has already been repaired by `repair_togo_m1070_score15.py`: it has `ph_value: 2.5`, 100/10/10/5 `ML_PER_L` solution additions, nested stock compositions copied from JCM 729/151/244, references, preparation steps, and the post-autoclave FeSO4 addition. `data/merge_yaml/merged/ACIDITHRIX_FERROOYDANS_MEDIUM.yaml` was generated before that repair, so it still has the pre-repair flat shape with no pH, no nested compositions, no preparation steps, and no provenance for the cross-medium stocks.

### major: source volumes are stored as gram-per-liter solution concentrations

The generated target stores 1.0 L distilled water as `1 G_PER_L`, 100 ml UBS solution as `100 G_PER_L`, 10 ml Trace minerals as `10 G_PER_L`, 10 ml Ni-Se-W solution as `10 G_PER_L`, and 5 ml 1 M FeSO4 solution as `5 G_PER_L`. Those values are volumes in the JCM and TOGO sources; representing them as mass concentrations makes the generated solution rows dimensionally wrong even before considering their missing compositions.

### major: the direct JCM 1012 import remains separate and flattened

The exact JCM source search found a same-source direct JCM owner, `data/normalized_yaml/bacterial/acidithrix_ferrooydans_medium.yaml`, which feeds `data/merge_yaml/merged/acidithrix_ferrooydans_medium__b3120235.yaml`. That sibling still expands JCM 729/151/244 stock components into the top-level final medium, merges stock-scoped `MgSO4 x 7 H2O` rows to 8.0 g/L, stores the 5 ml FeSO4 addition as 5 g/L, and lacks the curated TOGO source hierarchy. The current target will remain duplicated until that sibling is reconciled.

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` with `just merge-recipes` so `ACIDITHRIX_FERROOYDANS_MEDIUM.yaml` inherits the repaired TOGO M1070 owner.
2. Repair `data/normalized_yaml/bacterial/acidithrix_ferrooydans_medium.yaml` using the same JCM 1012 hierarchy now present in the TOGO M1070 owner, or deprecate the direct JCM duplicate after confirming the intended source-deduplication path.
3. Confirm regenerated TOGO and direct-JCM records either merge as one canonical JCM 1012 recipe or carry an explicit source-duplicate relationship.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ACIDITHRIX_FERROOYDANS_MEDIUM.yaml`.
- Re-fetch TOGO M1070 and JCM `GRMD=1012`, then confirm pH 2.5, 100 ml UBS, 10 ml Trace minerals, 10 ml Ni-Se-W, 1.0 L water, and 5 ml filter-sterilized 1 M FeSO4 solution survive regeneration.
- Search with `rg --no-ignore --hidden '100 G_PER_L|10 G_PER_L|5 G_PER_L|8\\.0|b3120235|ACIDITHRIX_FERROOYDANS' data/merge_yaml/merged data/normalized_yaml/bacterial` and confirm the old empty-solution and flattened-stock artifacts are gone or isolated to an intentionally deprecated input.

## Additional Notes

- The live JCM page spells the medium name `ACIDITHRIX FERROOYDANS MEDIUM`; this review treats that spelling as source-supported rather than as a CultureMech typo.
