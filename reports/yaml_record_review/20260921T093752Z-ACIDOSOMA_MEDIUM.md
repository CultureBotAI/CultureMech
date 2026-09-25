# YAML Record Review: acidosoma_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ACIDOSOMA_MEDIUM.yaml
- Started UTC: 2026-09-21T09:34:48Z
- Finished UTC: 2026-09-21T09:37:52Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ACIDOSOMA_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:003973`
- Label: `acidosoma_medium`
- Original name: `ACIDOSOMA medium`
- Category: `bacterial`
- Media term: `komodo.medium:1220` / `ACIDOSOMA medium`
- Generated status: generated merge from `data/normalized_yaml/bacterial/KOMODO_1220_ACIDOSOMA_medium.yaml` and `data/normalized_yaml/bacterial/acidosoma_medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACIDOSOMA_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ACIDOSOMA_MEDIUM.yaml --out /private/tmp/acidosoma.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ACIDOSOMA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ACIDOSOMA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target identity is coherent: live DSMZ Medium 1220 and live KOMODO Medium 1220 both identify ACIDOSOMA medium at pH 5.0 - 5.5. The local merge correctly recognizes that `KOMODO_1220_ACIDOSOMA_medium.yaml` is a KOMODO copy of DSMZ Medium 1220, and the direct DSMZ `acidosoma_medium.yaml` record is the right parent.

The ingredient grounding is not source-faithful. DSMZ Medium 1220 contains a 1 L main recipe with `1.00 ml` Trace elements from DSMZ Medium 922. DSMZ Medium 922 defines that Trace elements stock with 5.00 g EDTA, 0.10 g CuCl2 x 5 H2O, 2.00 g FeSO4 x 7 H2O, 0.10 g ZnSO4 x 7 H2O, 0.02 g NiCl2 x 6 H2O, 0.20 g CoCl2 x 6 H2O, 0.03 g Na2MoO4, and 1000 ml distilled water. The generated ACIDOSOMA record stores those DSMZ 922 stock rows as direct final-medium ingredients at stock strength, so EDTA is `5` g/L instead of a `0.005` g/L contribution from 1 ml/L stock, FeSO4 x 7 H2O is `2` g/L instead of `0.002` g/L, and the other trace metals are similarly 1000x too high.

## Evidence

Supported:

- Live DSMZ Medium 1220 supports the base ACIDOSOMA salts, 0.10 g/L yeast extract, 0.50 g/L sodium gluconate, 1 ml/L Trace elements from DSMZ Medium 922, 1000 ml distilled water, final pH 5.0 - 5.5, and optional 15 g/L agar for solid medium.
- Live DSMZ Medium 922 supports the composition of the cited Trace elements stock.
- Live KOMODO Medium 1220 has the same DSMZ Medium 1220 provenance, pH 5.0 - 5.5, and complex-medium flag as the generated target.
- Live KOMODO Medium 1220 lists per-liter final trace amounts, including 5.00E-3 g EDTA, 2.00E-3 g FeSO4 x 7 H2O, 2.00E-4 g CoCl2 x 6 H2O, 9.99E-5 g CuCl2 x 5 H2O, 9.99E-5 g ZnSO4 x 7 H2O, 2.00E-5 g NiCl2 x 6 H2O, and 3.00E-5 g Na2MoO4.

Unsupported or over-scoped:

- The generated trace-element rows are DSMZ Medium 922 stock concentrations rather than the final concentrations delivered by the 1 ml/L DSMZ 922 Trace elements addition.
- The generated record omits the 1000 ml distilled water from DSMZ Medium 1220 and the internal water row that defines the DSMZ 922 Trace elements stock volume.
- The generated record lost the DSMZ preparation step, `Adjust to pH 5.0 - 5.5. Agar may be added at 15 g/l for solid media.`, because the KOMODO copy was selected as the merge primary.
- The generated record encodes optional agar as a fixed `SOLID_AGAR` recipe, even though the DSMZ source lists agar only as a conditional solid-medium addition.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ACIDOSOMA*' -print` searched the ignored timestamped-report directory and found no pre-existing ACIDOSOMA report.
- Exact `rg --no-ignore --hidden` searches for `komodo\.medium:1220`, `mediadive\.medium:1220`, `DSMZ Medium: 1220`, `ACIDOSOMA medium`, `ACIDOSOMA MEDIUM`, and `KOMODO_1220_ACIDOSOMA` covered tracked and ignored files. They found the expected direct DSMZ and KOMODO 1220 parents, the generated target, and index or manifest references.
- Exact `rg --no-ignore --hidden` searches for `DSMZ Medium: 922`, `mediadive\.medium:922`, and `Trace elements \(see medium 922\)` covered tracked and ignored files. They found the separate METHYLOCAPSA ACIDOPHILA MEDIUM recipe for DSMZ 922; DSMZ 1220 reuses only that source's Trace elements subsection.
- Optional organism, growth metric, evidence, and temperature arrays are absent on the source imports; that is not a target-specific defect.

## Findings

### blocker: DSMZ 922 trace elements are flattened at stock strength

DSMZ Medium 1220 should add 1 ml/L of the Trace elements stock defined under DSMZ Medium 922. The generated record instead lists every stock constituent as if it were a final g/L ACIDOSOMA ingredient. This makes EDTA, FeSO4 x 7 H2O, CoCl2 x 6 H2O, CuCl2 x 5 H2O, ZnSO4 x 7 H2O, NiCl2 x 6 H2O, and Na2MoO4 1000x too concentrated and hides the stock boundary that explains why those rows belong to ACIDOSOMA at all.

### major: water rows were dropped from both the main recipe and the trace stock

DSMZ Medium 1220 brings the main ACIDOSOMA recipe to 1000 ml with distilled water, and the DSMZ 922 Trace elements stock is itself a 1000 ml aqueous stock. The generated record has no water ingredient or nested solution volume, so a downstream consumer cannot distinguish the main medium water from the cited trace-stock water.

### major: DSMZ preparation semantics were lost in the merge

The direct DSMZ import kept one preparation step for pH 5.0 - 5.5 and optional 15 g/L agar for solid medium, but the generated record selected the KOMODO copy as primary and has no `preparation_steps`. That leaves the scalar `ph_range` and fixed agar row without the DSMZ prose that makes agar conditional.

## Recommended Edits

1. Repair `data/normalized_yaml/bacterial/acidosoma_medium.yaml` so DSMZ Medium 1220 contains the 1 ml/L Trace elements stock from DSMZ Medium 922 instead of direct stock-strength metals.
2. Repair `data/normalized_yaml/bacterial/KOMODO_1220_ACIDOSOMA_medium.yaml` so it either nests the same Trace elements stock or uses KOMODO's final scaled trace amounts.
3. Restore the DSMZ Medium 1220 distilled-water row and preserve the DSMZ 922 stock volume instead of discarding both water contexts.
4. Model agar as the DSMZ optional 15 g/L solid-medium addition rather than an unconditional base ingredient, or split liquid and solid variants if the schema cannot represent optionality.
5. Regenerate `data/merge_yaml/merged/ACIDOSOMA_MEDIUM.yaml` from the repaired normalized sources and confirm the generated record carries the DSMZ pH/agar preparation step.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ACIDOSOMA_MEDIUM.yaml`.
- Re-fetch DSMZ Medium 1220 and 922 and confirm ACIDOSOMA contains one 1 ml/L Trace elements addition rather than final rows at DSMZ 922 stock strength.
- Re-fetch KOMODO Medium 1220 and confirm the generated trace rows match KOMODO's scaled final amounts if KOMODO remains a direct source.
- Search with `rg --no-ignore --hidden 'EDTA|FeSO4 x 7 H2O|Trace elements|mediadive\\.medium:922' data/normalized_yaml/bacterial/acidosoma_medium.yaml data/normalized_yaml/bacterial/KOMODO_1220_ACIDOSOMA_medium.yaml data/merge_yaml/merged/ACIDOSOMA_MEDIUM.yaml` and confirm the DSMZ 922 stock boundary is preserved without flattening.
- Search with `rg --no-ignore --hidden 'Adjust to pH 5\\.0|Agar may be added|SOLID_AGAR' data/normalized_yaml/bacterial/acidosoma_medium.yaml data/merge_yaml/merged/ACIDOSOMA_MEDIUM.yaml` and confirm the agar condition and pH adjustment survived regeneration.

## Additional Notes

- The existing `mediaingredientmech_chebi_term` ids are mostly consistent with each row's current ChEBI grounding. The defect is concentration scope, not the selected ChEBI identifiers.
