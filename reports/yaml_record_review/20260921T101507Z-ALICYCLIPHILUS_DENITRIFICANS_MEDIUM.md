# YAML Record Review: Alicycliphilus Denitrificans Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml
- Started UTC: 2026-09-21T10:12:45Z
- Finished UTC: 2026-09-21T10:15:07Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:009996`
- Label: `alicycliphilus_denitrificans_medium`
- Original name: `Alicycliphilus Denitrificans Medium`
- Category: `bacterial`
- Media term: `TOGO:M599`
- Generated status: generated merge of one source record, `data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml --out /private/tmp/alicycliphilus_denitrificans_medium.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target points at TOGO M599, which is the TOGO copy of JCM Medium 594. The current JCM `GRMD=594` page confirms an `ALICYCLIPHILUS DENITRIFICANS MEDIUM` recipe with Solution A, B, and C; anaerobic N2 autoclaving; a later N2-CO2 4:1 gas phase; 10 ml of 1.0 M sodium acetate solution; and 1 ml each of vitamin solution, thiamine solution, and vitamin B12 solution from JCM 403.

M599 is split from the direct `mediadive.medium:J594` import in `data/normalized_yaml/bacterial/alicycliphilus_denitrificans_medium.yaml`, which cites the same JCM page. The direct JCM import has pH 7.3 and preparation text, but it flattened the three base solutions and every stock addition into one set of final g/L ingredients, so it is not a source-faithful repair on its own.

M600 / `JCM_M594-2` is the related benzene/chlorate variant from the comment on the same JCM 594 page. It is correctly separate from M599 because it replaces NaNO3 with NaClO3 and adds water-saturated benzene, but it inherited the same solution and gas-handling representation defects.

## Evidence

Supported:

- The TOGO M599 identity, JCM_M594 provenance, Solution A/B/C topology, N2 and N2-CO2 handling, pH 7.3, and post-autoclave sodium acetate and vitamin stock additions are all supported by the live TOGO API and the live JCM `GRMD=594` page.
- KH2PO4 0.41 g, NaNO3 0.85 g, Na2HPO4 x 2 H2O 0.53 g, sodium acetate x 3 H2O 0.136 g, 900 ml distilled water, and 1 ml each of JCM 187 FeCl2, JCM 187 trace elements, and JCM 431 selenite-tungstate belong to Solution A.
- CaCl2 x 2 H2O 0.11 g, MgCl2 x 6 H2O 0.1 g, and 50 ml distilled water belong to Solution B.
- NaHCO3 3.73 g, Na2SO4 0.2 g, NH4HCO3 0.44 g, and 50 ml distilled water belong to Solution C.

Unsupported or over-scoped:

- The target flattens the Solution A/B/C internal ingredients to top-level final ingredients and merges the 900, 50, and 50 ml water rows into one `1000.0 G_PER_L` distilled-water row.
- Solution A, Solution B, and Solution C are listed as 903, 50, and 50 `G_PER_L` instead of volume additions or nested named base solutions.
- Local `mediadive.solution:5342`, `mediadive.solution:5343`, and `mediadive.solution:5312` are generic unrelated Solution A/B/C records and do not contain the JCM 594 Solution A/B/C compositions.
- The FeCl2, trace-element, selenite-tungstate, sodium-acetate, vitamin, thiamine, and vitamin B12 stock additions are encoded as empty `Unknown solution` records with `G_PER_L` units.
- CO2 and N2 were turned into unquantified final ingredients instead of anaerobic gas-handling instructions.
- No structured TOGO or JCM 594 references are present, so `linkml-reference-validator` performed zero checks.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ALICYCLIPHILUS_DENITRIFICANS_MEDIUM*' -print` searched the ignored timestamped-report directory and found no pre-existing ALICYCLIPHILUS DENITRIFICANS report.
- Exact `rg --no-ignore --hidden` searches for `TOGO:M599\b`, `JCM_M594\b`, `GRMD=594\b`, `TOGO_M599_Alicycliphilus_Denitrificans_Medium`, and `Alicycliphilus Denitrificans Medium` covered tracked and ignored files. They found the target TOGO M599 source/generated record, the direct JCM 594 source/generated record, the distinct TOGO M600 modified variant, index rows, and historical validation rows.
- The TOGO M599 and TOGO M600 APIs and the JCM `GRMD=594` HTML page were fetched live. The JCM page confirms TOGO M599's base formulation and distinguishes the M600 benzene/chlorate variant as the modified JCM 14587 formulation.
- Exact ignored-inclusive checks confirmed that TOGO M180 maps to JCM 187, TOGO M401 maps to JCM 403, and TOGO M431 maps to JCM 431, so the imported bracketed cross-reference IDs are TOGO IDs that correspond to the JCM pages cited by the live JCM 594 HTML.

## Findings

### blocker: JCM Solution A/B/C topology was destroyed

JCM 594 is organized as separately autoclaved Solution A, Solution B, and Solution C. The target flattens those solution internals into one top-level ingredient list, merges their water rows into `1000.0 G_PER_L`, and keeps only placeholder `Unknown solution` rows for Solution A, B, and C.

### blocker: all solution additions use mass units and several are empty

Every solution addition is encoded with `unit: G_PER_L`, including 903 ml Solution A, 50 ml Solution B, 50 ml Solution C, 1 ml FeCl2 solution, 1 ml trace-element solution, 1 ml selenite-tungstate solution, 10 ml 1.0 M sodium acetate solution, and the three 1 ml vitamin stocks. The seven referenced stock additions also have empty `composition: []`, so the cross-media requirements from JCM 187, JCM 431, and JCM 403 are not represented.

### major: gas handling and preparation text were lost

JCM 594 says to autoclave all solutions under N2, combine them after cooling, replace the gas phase with N2-CO2 4:1, add the post-autoclave stocks aseptically and anaerobically, and check that final pH is about 7.3. The target instead stores `Carbon dioxide gas` and `N2` as variable final ingredients and has no preparation steps.

### major: the direct JCM 594 duplicate remains split

`data/normalized_yaml/bacterial/alicycliphilus_denitrificans_medium.yaml` cites the same JCM `GRMD=594` source and has the missing pH/preparation text, but it is generated separately as `data/merge_yaml/merged/alicycliphilus_denitrificans_medium__b7e62cdd.yaml` because it flattened JCM 594 differently from the TOGO M599 copy.

## Recommended Edits

1. Fix `data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml` and `data/normalized_yaml/bacterial/alicycliphilus_denitrificans_medium.yaml`; do not edit either generated merge YAML directly.
2. Represent JCM 594 Solution A, Solution B, and Solution C as real nested base solutions with volume units, or preserve equivalent scoped solution sections so their water rows and internal gram amounts are not flattened as final g/L solutes.
3. Replace the generic `mediadive.solution:5342`, `mediadive.solution:5343`, and `mediadive.solution:5312` links with JCM 594-local Solution A/B/C structures.
4. Change the FeCl2, trace-element, selenite-tungstate, sodium-acetate, vitamin, thiamine, and vitamin B12 additions from `G_PER_L` to their source ml additions and expand or correctly cross-reference the M180/JCM 187, M401/JCM 403, and M431/JCM 431 source stocks.
5. Move N2 and CO2 out of `ingredients` and restore the anaerobic preparation steps, N2-CO2 4:1 gas-phase replacement, aseptic post-autoclave stock additions, and final pH 7.3 check.
6. Mark the direct JCM 594 and TOGO M599 records as source duplicates after both are repaired; keep TOGO M600 as a distinct variant that replaces nitrate with chlorate and adds benzene.
7. Add structured TOGO M599 and JCM 594 references.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml`.
- Fetch TOGO M599, TOGO M600, and JCM `GRMD=594` again and confirm M599 retains Solution A/B/C topology while M600 remains the chlorate/benzene variant.
- Search with `rg --no-ignore --hidden 'TOGO:M599\b|mediadive.medium:J594\b|TOGO:M600\b|mediadive.solution:5342|mediadive.solution:5343|mediadive.solution:5312' data/normalized_yaml/bacterial data/merge_yaml/merged` and confirm repaired M599/J594 records no longer link to the unrelated generic Solution A/B/C records.

## Additional Notes

- M599 itself is a complex multi-stock anaerobic recipe; optional organism and growth metric data were not part of the inspected JCM 594 evidence and were not treated as defects.
