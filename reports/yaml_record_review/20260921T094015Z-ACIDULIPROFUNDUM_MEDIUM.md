# YAML Record Review: aciduliprofundum_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml
- Started UTC: 2026-09-21T09:38:05Z
- Finished UTC: 2026-09-21T09:40:15Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:003735`
- Label: `aciduliprofundum_medium`
- Original name: `ACIDULIPROFUNDUM medium`
- Category: `archaea`
- Media term: `komodo.medium:1083` / `ACIDULIPROFUNDUM medium`
- Generated status: generated merge from `data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml` and `data/normalized_yaml/archaea/aciduliprofundum_medium.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml --out /private/tmp/aciduliprofundum.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The DSMZ/KOMODO identity is correct. DSMZ Medium 1083 and KOMODO Medium 1083 both identify ACIDULIPROFUNDUM medium at pH 4.5, and the local direct DSMZ and KOMODO normalized files are a source-duplicate pair.

The recipe body is not source-faithful. DSMZ Medium 1083 has 1 ml/L Wolfe's mineral elixir, 0.5 ml/L 0.1% sodium resazurin, and a main 1 L recipe that separately contains 30 g NaCl, 3.5 g MgSO4 x 7 H2O, and 0.38 g CaCl2 x 2 H2O. The generated record flattened Wolfe's mineral elixir into final ingredients, then summed Wolfe stock-strength MgSO4, NaCl, and CaCl2 with the same salts from the main medium. Those rows are still marked with `[Merged 2 duplicates: ...]` notes documenting the cross-scope addition.

## Evidence

Supported:

- Live DSMZ Medium 1083 supports the DSMZ/KOMODO record identity, 30 g/L NaCl, 3.5 g/L MgSO4 x 7 H2O, 2.75 g/L MgCl2 x 6 H2O, 0.38 g/L CaCl2 x 2 H2O, 0.33 g/L KCl, 0.05 g/L NaBr, 0.10 g/L ammonium sulfate, 0.28 g/L KH2PO4, 1 ml/L Wolfe's mineral elixir, 0.5 ml/L 0.1% sodium resazurin, 2.94 g/L trisodium citrate, 1 g/L yeast extract, 1 g/L tryptone, 10 g/L powdered sulfur, 0.5 g/L sodium sulfide nonahydrate, 1000 ml distilled water, and pH 4.5.
- Live DSMZ Medium 1083 supports Wolfe's mineral elixir as a 1000 ml stock from DSMZ Medium 792, not as direct final-medium rows.
- The current direct DSMZ and KOMODO normalized parents already have a `solutions` entry for 1 ml/L Wolfe's mineral elixir after `apply_cocktail_nesting.py`.
- TOGO M2669 also points to the DSMZ Medium 1083 PDF and should eventually reconcile with the DSMZ/KOMODO family once Wolfe's mineral elixir is represented consistently.

Unsupported or over-scoped:

- The generated `NaCl`, `MgSO4 x 7 H2O`, and `CaCl2 x 2 H2O` rows sum main-medium salts with the same-named Wolfe's mineral elixir stock salts, yielding 39.97 g/L NaCl, 33.4965 g/L MgSO4 x 7 H2O, and 1.37962 g/L CaCl2 x 2 H2O.
- The generated `CuSO4 x 5 H2O`, `AlK(SO4)2 x 12 H2O`, `H3BO3`, `Na2MoO4 x 2 H2O`, `(NH4)2Ni(SO4)2 x 6 H2O`, `Na2WO4 x 2 H2O`, and `Na2SeO4` rows are stock-strength Wolfe's mineral elixir components listed as if they were final g/L medium additions.
- The generated record has no `solutions` array, so it predates the August 2026 partial stock nesting now present in the two normalized parents.
- The generated record has no `preparation_steps`, so it drops DSMZ's anaerobic sparging, Hungate/serum-vial dispensing under N2/CO2, sulfur autoclaving, sulfide stock addition, and pH adjustment to 4.5.
- The generated `parent_media.path` points to `data/normalized_yaml/bacterial/aciduliprofundum_medium.yaml`, but the current source is `data/normalized_yaml/archaea/aciduliprofundum_medium.yaml`.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ACIDULIPROFUNDUM*' -print` searched the ignored timestamped-report directory and found no pre-existing ACIDULIPROFUNDUM report.
- Exact `rg --no-ignore --hidden` searches for `komodo\.medium:1083`, `mediadive\.medium:1083`, `TOGO:M2472`, `TOGO:M2669`, `DSMZ Medium: 1083`, `ACIDULIPROFUNDUM medium`, `ACIDULIPROFUNDUM MEDIUM`, and `Aciduliprofundum Medium` covered tracked and ignored files. They found the DSMZ/KOMODO 1083 pair, the separate TOGO M2472 and M2669 imports, the target merge, and two single-source hashed generated siblings for the TOGO imports.
- `find data/normalized_yaml -path '*bacterial/aciduliprofundum_medium.yaml' -print` and `find data/normalized_yaml -path '*bacterial/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml' -print` included ignored files and confirmed that the generated bacterial `parent_media` paths are stale.
- Optional organism, growth metric, evidence, and temperature arrays are absent on the source imports; that is not a target-specific defect.

## Findings

### blocker: Wolfe's mineral elixir is flattened into final ingredients

DSMZ Medium 1083 should add 1 ml/L Wolfe's mineral elixir. The generated record instead puts many Wolfe stock components into the final ingredient list at stock strength. Where the stock reuses names from the main recipe, the generated row sums unrelated scopes: 30 g/L main NaCl plus 10 g/L stock NaCl, 3.5 g/L main MgSO4 x 7 H2O plus 30 g/L stock MgSO4 x 7 H2O, and 0.38 g/L main CaCl2 x 2 H2O plus 1 g/L stock CaCl2 x 2 H2O. Those are stock-definition rows, not extra bulk salts for the final medium.

### major: the generated merge is stale relative to the normalized parents

Both normalized DSMZ/KOMODO 1083 parents now contain a `solutions` entry for Wolfe's mineral elixir, but the generated target still has the pre-repair flattened row set and no `solutions` array. Even the normalized repair is partial because it moved only four Wolfe components and left the same-named main/stock MgSO4, NaCl, and CaCl2 rows summed, but the generated target is older and worse than the current source files.

### major: anaerobic preparation constraints were dropped

The direct DSMZ import preserves the source instructions to sparge with 80% N2 / 20% CO2, dispense under the same gas phase into vessels already containing powdered sulfur, autoclave for 60 min at 105 C, add anoxic sulfide stock under 100% N2 before inoculation, and adjust the complete medium to pH 4.5. The generated record selected the KOMODO copy as primary and has no `preparation_steps`, so the published merge cannot reproduce the anaerobic and post-sterilization handling.

### minor: generated parent paths still point at the old bacterial directory

The generated `parent_media.path` says `data/normalized_yaml/bacterial/aciduliprofundum_medium.yaml`, and the normalized DSMZ parent says its KOMODO child is under `data/normalized_yaml/bacterial/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml`. Those files are now under `data/normalized_yaml/archaea/`; the stale embedded paths do not resolve.

## Recommended Edits

1. Repair `data/normalized_yaml/archaea/aciduliprofundum_medium.yaml` and `data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml` so Wolfe's mineral elixir is fully nested at 1 ml/L, including MgSO4, NaCl, CaCl2, CuSO4, AlK(SO4)2, H3BO3, Na2MoO4, ammonium nickel sulfate, Na2WO4, Na2SeO4, and its 1000 ml water row.
2. Remove the summed main-plus-stock values for NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O; keep the main-medium values as 30, 3.50, and 0.38 g/L respectively.
3. Preserve the 1000 ml distilled water row from the DSMZ main recipe.
4. Carry the DSMZ anaerobic preparation steps into the source selected as merge primary, or make the merger union compatible duplicate preparation steps.
5. Reconcile `data/normalized_yaml/archaea/TOGO_M2669_Aciduliprofundum_Medium.yaml` with the DSMZ/KOMODO 1083 family after stock nesting is consistent.
6. Regenerate `data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml` so it contains a nested Wolfe's mineral elixir solution and current `data/normalized_yaml/archaea/...` parent paths.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml`.
- Re-fetch DSMZ Medium 1083 and confirm the generated main `NaCl`, `MgSO4 x 7 H2O`, and `CaCl2 x 2 H2O` rows are not summed with Wolfe's mineral elixir stock rows.
- Search with `rg --no-ignore --hidden 'Merged 2 duplicates: 29\\.97, 10\\.0|Merged 2 duplicates: 3\\.4965, 30\\.0|Merged 2 duplicates: 0\\.37962, 1\\.0' data/normalized_yaml/archaea data/merge_yaml/merged` and confirm no Aciduliprofundum source still has cross-scope summed ingredients.
- Search with `rg --no-ignore --hidden 'preferred_term: Wolfe|preferred_term: CuSO4 x 5 H2O|preferred_term: Na2SeO4' data/normalized_yaml/archaea/aciduliprofundum_medium.yaml data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml` and confirm Wolfe stock components live under the `solutions` array.
- Search with `rg --no-ignore --hidden 'data/normalized_yaml/bacterial/.*ACIDULIPROFUNDUM|data/normalized_yaml/bacterial/aciduliprofundum' data/normalized_yaml data/merge_yaml/merged` and confirm no stale parent path remains.

## Additional Notes

- `data/merge_yaml/merged/aciduliprofundum_medium__c274440d.yaml` is a TOGO M2472 / ATCC import with a related but distinct source URL and should remain separate until an ATCC source review proves equivalence.
