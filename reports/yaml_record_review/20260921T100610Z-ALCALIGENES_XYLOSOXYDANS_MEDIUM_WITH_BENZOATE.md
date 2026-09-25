# YAML Record Review: ALCALIGENES XYLOSOXYDANS MEDIUM WITH BENZOATE

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
- Started UTC: 2026-09-21T10:04:02Z
- Finished UTC: 2026-09-21T10:06:10Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:005585`
- Label: `alcaligenes_xylosoxydans_medium_with_benzoate`
- Original name: `ALCALIGENES XYLOSOXYDANS MEDIUM WITH BENZOATE`
- Category: `bacterial`
- Media term: `komodo.medium:471`
- Generated status: generated single-source record from `data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml --out /private/tmp/alcaligenes_xylosoxydans_medium_with_benzoate.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The generated record is intended to represent KOMODO 471, a copy of DSMZ Medium 471. The broad medium identity is correct: the direct DSMZ 471 import has the same `ALCALIGENES XYLOSOXYDANS MEDIUM WITH BENZOATE` name and the same component vocabulary.

The composition is not source-faithful. DSMZ 471 is a three-part recipe: Solution A is 500 ml with K2HPO4, KH2PO4, and pH adjustment to 9.0 with KOH; Solution B is 500 ml with NH4Cl, CaCl2, MgSO4.7H2O, KNO3, and sodium benzoate; Solution C is 2 ml Trace element solution SL-4. SL-4 itself contains EDTA, FeSO4.7H2O, 100 ml Trace element solution SL-6, and 900 ml distilled water; SL-6 contains the Zn/Mn/B/Co/Cu/Ni/Mo salts. The target flattens every nested stock directly into final ingredients.

## Evidence

Supported:

- `K2HPO4`, `KH2PO4`, `NH4Cl`, `CaCl2`, `MgSO4 x 7 H2O`, `KNO3`, and `Na-benzoate` all belong to DSMZ 471 Solutions A or B.
- The pH 9.0 adjustment with KOH belongs to Solution A before the three solutions are autoclaved separately.
- The final DSMZ pH is 8.2 after Solutions A, B, and C are combined.

Unsupported or over-scoped:

- Solution A and B solutes were doubled: K2HPO4 is 10.24 g/L instead of 5.12 g/L final, KH2PO4 is 3 g/L instead of 1.5 g/L, NH4Cl is 0.6 g/L instead of 0.3 g/L, CaCl2 is 0.02 g/L instead of 0.01 g/L, MgSO4.7H2O is 0.4 g/L instead of 0.2 g/L, KNO3 is 4 g/L instead of 2 g/L, and sodium benzoate is 1.84 g/L instead of 0.92 g/L.
- SL-4 is added at 2 ml/L, but its EDTA and FeSO4.7H2O stock concentrations are published as 0.5 g/L and 0.2 g/L final ingredients.
- SL-6 is nested at 100 ml/L of SL-4 and then diluted again by the 2 ml/L SL-4 final addition, but its Zn/Mn/B/Co/Cu/Ni/Mo rows are published at their undiluted SL-6 stock concentrations.
- The target sets `ph_value: 9.0` and adds variable `KOH` as a final ingredient; the final medium should be pH 8.2, and KOH is used to adjust only Solution A.
- The source preparation steps for separate A/B/C autoclaving, final pH adjustment, and SL-4 assembly are absent.
- KNO3 still carries a deprecated `mediaingredientmech_term: MediaIngredientMech:000170` field.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE*' -print` searched the ignored timestamped-report directory and found no pre-existing report for this exact generated record.
- Exact `rg --no-ignore --hidden` searches for `komodo.medium:471\b`, `mediadive.medium:471\b`, `DSMZ Medium 471`, and `KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE` covered tracked and ignored files. They found the KOMODO 471 target/source, the direct DSMZ 471 source, the modified DSMZ 7136 sibling in the lowercase generated record, and index references.
- The DSMZ 471 PDF was fetched live and extracted locally with `mutool`; it confirms the nested Solution A, Solution B, SL-4, and SL-6 formulation described above.
- The generated direct DSMZ 471 sibling, `data/merge_yaml/merged/alcaligenes_xylosoxydans_medium_with_benzoate__ce78ad10.yaml`, keeps some source preparation steps and pH 8.2, but it has the same flattened stock concentrations and also needs repair before it can be merged with KOMODO 471.

## Findings

### blocker: nested DSMZ stock solutions were flattened at stock strength

The target flattened Solution A, Solution B, SL-4, and SL-6 without multiplying by their final-volume fractions. This doubles the Solution A/B ingredients, publishes SL-4 rows hundreds of times too high, and publishes SL-6 rows thousands of times too high.

### major: pH 9.0 and KOH are attached to the final medium

DSMZ 471 uses KOH to adjust Solution A to pH 9.0, then combines Solutions A/B/C and adjusts the final medium to pH 8.2. The target's `ph_value: 9.0` and variable `KOH` final ingredient move a solution-specific preparation step to the complete recipe.

### major: preparation topology is absent

The source explicitly says to autoclave Solutions A, B, and C separately before combining, and it describes how to dissolve EDTA for SL-4. The generated target is only a flat ingredient list.

### minor: a deprecated MediaIngredientMech link survived

`KNO3` still carries `mediaingredientmech_term: MediaIngredientMech:000170` even though the June 2026 migration notes say legacy MediaIngredientMech IDs were deprecated in favor of CHEBI-keyed links.

## Recommended Edits

1. Fix `data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml` and `data/normalized_yaml/bacterial/alcaligenes_xylosoxydans_medium_with_benzoate.yaml`; do not edit generated YAML directly.
2. Preserve Solution A, Solution B, Solution C, Trace element solution SL-4, and Trace element solution SL-6 as composed solutions, or carefully scale every nested component into the final medium with the 500 ml / 500 ml / 2 ml / 100 ml dilution factors.
3. Set the final pH to 8.2 and move the pH 9.0 KOH adjustment to the Solution A preparation step.
4. Restore the separate-autoclave and SL-4 preparation steps from DSMZ 471.
5. Replace the stale `MediaIngredientMech:000170` KNO3 link with a CHEBI-keyed mapping.
6. Add structured DSMZ 471 references to both normalized source records and regenerate so KOMODO 471 and direct DSMZ 471 reconcile.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml`.
- Fetch the DSMZ Medium 471 PDF again and compare the regenerated solution hierarchy, final pH, and preparation steps against the source.
- Search with `rg --no-ignore --hidden 'Solution A|Solution B|SL-4|SL-6|KOH|MediaIngredientMech:000170' data/normalized_yaml/bacterial data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml` and confirm the nested stocks are explicit, KOH is not a final ingredient, and the stale MIM link is gone.

## Additional Notes

- Optional organism and growth metric data are absent from the available DSMZ 471 evidence and were not treated as defects.
