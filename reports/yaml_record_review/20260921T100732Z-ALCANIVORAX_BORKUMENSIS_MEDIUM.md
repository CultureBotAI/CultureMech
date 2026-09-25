# YAML Record Review: ALCANIVORAX BORKUMENSIS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
- Started UTC: 2026-09-21T10:06:47Z
- Finished UTC: 2026-09-21T10:07:32Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:006526`
- Label: `alcanivorax_borkumensis_medium`
- Original name: `ALCANIVORAX BORKUMENSIS MEDIUM`
- Category: `bacterial`
- Media term: `komodo.medium:809`
- Generated status: generated merge of `data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml` and `data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml --out /private/tmp/alcanivorax_borkumensis_medium.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target is a valid source-duplicate merge of KOMODO 809 and direct DSMZ 809. KOMODO says it was copied from DSMZ Medium 809, and the two normalized parents carry the same eight solute rows with the same concentrations.

The live DSMZ 809 PDF confirms the source identity, the eight salt and sodium pyruvate rows, and the pH range of 7.0-7.5. The generated target correctly preserves the pH range and all non-water ingredient quantities as g/L after conversion from DSMZ's per-1000 ml recipe.

## Evidence

Supported:

- KOMODO 809 and DSMZ 809 are source duplicates with identical non-water ingredient signatures.
- NaCl, MgSO4 x 7 H2O, MgCl2 x 2 H2O, CaCl2 x 2 H2O, Na2HPO4 x 7 H2O, NaNO3, FeSO4 x 7 H2O, and sodium pyruvate are all present at the source concentrations.
- The pH range 7.0-7.5 is supported by DSMZ 809.

Unsupported or under-specified:

- DSMZ 809 includes `Distilled water 1000.00 ml`, but neither normalized parent nor the generated merge represents the water row.
- No structured DSMZ or KOMODO source references are present, so `linkml-reference-validator` performed zero checks.
- The NaNO3 row still has a stale `mediaingredientmech_term: MediaIngredientMech:000171` link while the other seven ingredients were migrated to `mediaingredientmech_chebi_term`.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ALCANIVORAX_BORKUMENSIS_MEDIUM*' -print` searched the ignored timestamped-report directory and found no pre-existing ALCANIVORAX BORKUMENSIS report.
- Exact `rg --no-ignore --hidden` searches for `komodo.medium:809\b`, `mediadive.medium:809\b`, `DSMZ Medium 809`, and `KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM` covered tracked and ignored files. They found the KOMODO 809 parent, the DSMZ 809 parent, the generated merge, registry/index rows, and historical validation/report rows, but no additional live normalized parent to reconcile.
- The DSMZ 809 PDF was fetched live from `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf` and extracted locally with `mutool`; it confirms the g/1000 ml ingredient table and pH line.

## Findings

### major: the record has no structured source references

The source provenance is present only in free-text `notes` and `media_term`. The generated record contains no structured DSMZ 809, MediaDive 809, or KOMODO 809 citation, which leaves the reference validator with zero source checks.

### minor: DSMZ 809's distilled-water row is absent

DSMZ 809 explicitly gives `Distilled water 1000.00 ml`. The generated record contains the eight solutes but omits the solvent, so a regenerated version should include distilled water or document why source water rows are intentionally suppressed.

### minor: NaNO3 still uses a stale MediaIngredientMech identifier

The NaNO3 ingredient resolves to `CHEBI:63005`, but it still carries legacy `mediaingredientmech_term: MediaIngredientMech:000171` metadata. Its sibling rows use `mediaingredientmech_chebi_term` after the CHEBI migration.

## Recommended Edits

1. Fix `data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml` and `data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml`; do not edit the generated merge YAML directly.
2. Add structured source references for DSMZ Medium 809 / MediaDive 809 and KOMODO 809 so reference validation can check real citations.
3. Add DSMZ 809's 1000 ml distilled-water row, or add a source-grounded curation note if DSMZ water rows are deliberately omitted from these normalized recipes.
4. Replace the stale NaNO3 `mediaingredientmech_term` with a CHEBI-keyed ingredient link consistent with `CHEBI:63005`.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml`.
- Fetch DSMZ Medium 809 again and confirm the regenerated merge retains the eight non-water rows, the distilled-water row, and pH 7.0-7.5.
- Search with `rg --no-ignore --hidden 'MediaIngredientMech:000171|DSMZ Medium 809|mediadive.medium:809|komodo.medium:809' data/normalized_yaml/bacterial data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml` and confirm the stale NaNO3 link is gone while the two source identifiers remain documented.

## Additional Notes

- DSMZ 809 does not include preparation text beyond the pH line, so the generated merge did not lose substantive setup, sterilization, or stock-solution instructions.
