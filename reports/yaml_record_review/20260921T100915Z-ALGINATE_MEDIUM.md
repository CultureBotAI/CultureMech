# YAML Record Review: Alginate Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ALGINATE_MEDIUM.yaml
- Started UTC: 2026-09-21T10:07:42Z
- Finished UTC: 2026-09-21T10:09:15Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ALGINATE_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:010427`
- Label: `alginate_medium`
- Original name: `Alginate Medium`
- Category: `bacterial`
- Media term: `TOGO:M999`
- Generated status: generated merge of one source record, `data/normalized_yaml/bacterial/TOGO_M999_Alginate_Medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALGINATE_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALGINATE_MEDIUM.yaml --out /private/tmp/alginate_medium.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALGINATE_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALGINATE_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target points at TOGO M999, which is a TOGO copy of JCM_M952 / JCM `GRMD=952`. The current TOGO API names the recipe `Alginate Medium`, reports `original_media_id: JCM_M952`, carries the source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=952`, and reports pH 5.5.

The same JCM 952 recipe is imported directly as `data/normalized_yaml/bacterial/alginate_medium.yaml` and generated separately as `data/merge_yaml/merged/alginate_medium__8987a8ad.yaml`. The direct JCM record has the same six non-water solutes, keeps pH 5.5, and represents the HCl text as `Adjust pH to 5.5 with HCl`; the TOGO record left the pH out of the normalized pH fields and materialized `HCl` as a variable-concentration ingredient.

## Evidence

Supported:

- The six solutes `(NH4)2SO4`, `MgSO4 x 7 H2O`, `Na2HPO4 x 2 H2O`, `CaCl2 x 2 H2O`, `K2HPO4`, and sodium alginate are supported at 2, 0.2, 0.5, 0.1, 0.5, and 10 g/L respectively by both the TOGO M999 API and the local direct JCM 952 import.
- TOGO M999 supports distilled water at 1 L for the recipe.
- TOGO M999 supports pH adjustment to 5.5 with HCl.

Unsupported or under-specified:

- The target represents TOGO's `Distilled water` 1 L row as `1 G_PER_L`, which changes a volume to a mass concentration.
- The target represents HCl as a variable final ingredient instead of a pH-adjustment reagent.
- The target omits the source pH 5.5 and has no preparation step for the HCl pH adjustment.
- The `Na2HPO4 x 2 H2O` row is grounded to generic `CHEBI:34683` / disodium hydrogenphosphate; the hydrate-specific direct JCM sibling uses `CHEBI:91258` / disodium hydrogenphosphate dihydrate.
- No structured TOGO or JCM source references are present, so `linkml-reference-validator` performed zero checks.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ALGINATE_MEDIUM*' -print` searched the ignored timestamped-report directory and found no pre-existing ALGINATE MEDIUM report.
- Exact `rg --no-ignore --hidden` searches for `TOGO:M999\b`, `JCM_M952\b`, `GRMD=952\b`, `TOGO_M999_Alginate_Medium\b`, and `\bAlginate Medium\b` covered tracked and ignored files. They found the target TOGO source, a direct JCM 952 source, a split direct-JCM generated record, derived index rows, historical validation/report rows, and no earlier timestamped review report.
- The TOGO M999 API was fetched live and confirms the six solutes, 1 L distilled water, HCl pH-adjustment reagent, original JCM_M952 identity, original JCM URL, and pH 5.5.
- The live JCM `GRMD=952` page now returns `Nothing found`, so the JCM-specific evidence is limited to the local direct import that cites the same URL.

## Findings

### blocker: the JCM 952 recipe is split into two generated records

TOGO M999 explicitly came from JCM_M952 and the direct `alginate_medium` record cites the same JCM `GRMD=952` page. These are the same recipe, but the generated directory has `ALGINATE_MEDIUM.yaml` for TOGO and `alginate_medium__8987a8ad.yaml` for the direct JCM import because the TOGO copy gained erroneous distilled-water/HCl ingredients and lost pH 5.5.

### major: TOGO's 1 L water row became 1 g/L

The TOGO API gives the solvent as `Distilled water`, `volume: 1`, `unit: L`. The target encodes that row as `value: '1'` with `unit: G_PER_L`, so the record no longer distinguishes a 1 L final-volume row from a 1 g/L solute.

### major: HCl pH adjustment was converted into a variable-concentration ingredient

TOGO lists HCl as an unquantified component and carries the actual instruction as `Adjust pH to 5.5 with HCl`. The direct JCM source imports this as an `ADJUST_PH` preparation step. The target instead has no pH field or preparation step and includes HCl as a `VARIABLE` final ingredient.

### minor: Na2HPO4 hydrate specificity was lost in the TOGO source

The source label is `Na2HPO4 x 2 H2O`, and the direct JCM 952 import grounds it to `CHEBI:91258` / disodium hydrogenphosphate dihydrate. The TOGO source and generated target use generic `CHEBI:34683` / disodium hydrogenphosphate.

## Recommended Edits

1. Fix `data/normalized_yaml/bacterial/TOGO_M999_Alginate_Medium.yaml` and `data/normalized_yaml/bacterial/alginate_medium.yaml`; do not edit either generated merge YAML directly.
2. Normalize TOGO M999 to the same six-solute signature as the direct JCM 952 record, while representing the TOGO 1 L distilled-water row with a volume-aware unit or a curation note if final water rows are intentionally omitted.
3. Move HCl out of `ingredients`, add `ph_value: 5.5`, and add an `ADJUST_PH` preparation step equivalent to `Adjust pH to 5.5 with HCl`.
4. Ground `Na2HPO4 x 2 H2O` to `CHEBI:91258` in the TOGO source.
5. Mark TOGO M999 and direct JCM J952 as source duplicates so regeneration emits one generated Alginate Medium record.
6. Add structured source references for TOGO M999 and JCM 952.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ALGINATE_MEDIUM.yaml`.
- Fetch TOGO M999 again and confirm pH 5.5, HCl pH adjustment, the 1 L water row, and the six solute quantities.
- Search with `rg --no-ignore --hidden 'TOGO:M999\b|mediadive.medium:J952\b|GRMD=952\b|mediadive.solution:4974\b' data/normalized_yaml data/merge_yaml/merged` to confirm TOGO M999 and JCM 952 merge as source duplicates and `Main sol. J952` remains either connected as a source solution or out of the generated MediaRecipe set.

## Additional Notes

- `data/normalized_yaml/bacterial/mediadive_4974_Main_sol_J952.yaml` duplicates the same six solutes as a standalone source solution named `Main sol. J952` and encodes its distilled-water row as `1000 PERCENT_V_V`; it should be audited with the JCM 952 repair but was not the direct target of this generated-record review.
