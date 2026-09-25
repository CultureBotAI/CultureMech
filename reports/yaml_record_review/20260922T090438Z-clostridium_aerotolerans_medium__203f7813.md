# YAML Record Review: clostridium_aerotolerans_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/clostridium_aerotolerans_medium__203f7813.yaml
- Started UTC: 2026-09-22T09:02:30Z
- Finished UTC: 2026-09-22T09:04:38Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/clostridium_aerotolerans_medium__203f7813.yaml`, a generated `MediaRecipe` for `CultureMech:010174` / `clostridium_aerotolerans_medium`.

The record is generated from the single maintained source `data/normalized_yaml/bacterial/TOGO_M767_Clostridium_Aerotolerans_Medium.yaml` with merge fingerprint `203f7813ba70d7af23d3beecf33f7faf4b5b7a333e061b2e759a23ebfa419ff8`.

The source identity is `TOGO:M767`, labelled `Clostridium Aerotolerans Medium`, with original source JCM Medium 742.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/clostridium_aerotolerans_medium__203f7813.yaml` | Pass |
| `python scripts/validate_strict.py data/merge_yaml/merged/clostridium_aerotolerans_medium__203f7813.yaml --out /private/tmp/clostridium_aerotolerans_medium__203f7813.strict.tsv --workers 1 --quiet` | Pass; TSV contained only the header row |
| `linkml-reference-validator validate data data/merge_yaml/merged/clostridium_aerotolerans_medium__203f7813.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/clostridium_aerotolerans_medium__203f7813.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass; emitted only the expected NCBI E-utilities deprecation warning |
| Embedded curation-history validation | Not checked: the documented `just validate-history` target validates standalone `history/` records, not embedded `MediaRecipe.curation_history` nodes in generated YAML |

`just` wrapper validators were not used because the project environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails inside setuptools. The equivalent focused LinkML, strict, reference, and term validators were run under `/usr/local/bin/python3.11` with offline cached packages.

## Identity and Grounding

The record correctly identifies TOGO M767 as a TOGO representation of JCM Medium 742. The TOGO API reports `original_media_id` `JCM_M742`, `src_url` `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=742`, and `ph` `7.0`; the fetched JCM page returns Medium 742, `CLOSTRIDIUM AEROTOLERANS MEDIUM`.

The chemical identities are mostly sound. JCM 742 and TOGO agree on MgSO4.7H2O, CaCl2.2H2O, Na2S.9H2O, L-Cysteine.HCl.H2O, both phosphate salts, ammonium sulfate, NaCl, yeast extract, xylan, and resazurin. The June `mgso4-heptahydrate-term-fix-v1.0` event preserved magnesium sulfate heptahydrate correctly.

Two unit conversions are wrong:

- JCM and TOGO both state 1 L distilled water, but the YAML stores 1 `G_PER_L`.
- JCM and TOGO both state 1 mg resazurin, but the YAML stores 1 `G_PER_L`.

An ignored-inclusive search of `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` for `CultureMech:010174`, `TOGO:M767`, `M767`, `JCM_M742`, `GRMD=742`, the merge fingerprint, `TOGO_M767_Clostridium_Aerotolerans_Medium.yaml`, and the exact label found the reviewed TOGO owner and also found the direct JCM/MediaDive owner `data/normalized_yaml/bacterial/clostridium_aerotolerans_medium.yaml` for the same JCM 742 page.

## Evidence

The inspected TOGO M767 JSON and JCM 742 HTML support the 10 dry ingredients, xylan, L-cysteine hydrochloride monohydrate, and the 1 L water row. TOGO also preserves the JCM URL and pH 7.0 in its `meta` object.

The reviewed YAML does not preserve every source claim. The TOGO payload's pH and `Adjust pH to 7.0.` comment are not present as `ph_value` or `preparation_steps`, and the resazurin source unit was changed from `mg` to `G_PER_L`.

The direct MediaDive/JCM owner for the same URL, `CultureMech:003085`, already has the correct `Resazurin` value of 0.001 `G_PER_L`, `ph_value: 7.0`, and an `ADJUST_PH` preparation step, but it was not merged with the TOGO owner being reviewed.

The exact ignored-inclusive search also surfaced `data/import_tracking/reports/concentration_plausibility.tsv`, which flags the reviewed TOGO owner for an `INDICATOR_UNIT_SLIP` on `Resazurin` at 1 `G_PER_L`.

## Completeness

The ingredient list is otherwise complete for the short JCM 742 page: no source ingredient besides the 1 L final water row is missing, and the source does not name stock solutions, storage conditions, salinity, light, gas, or target strains.

Three consequential gaps remain:

- The water and resazurin units make the formula materially wrong.
- The pH 7.0 preparation instruction from both TOGO and JCM is missing from the reviewed TOGO owner.
- The TOGO and direct JCM records for `GRMD=742` are duplicates with complementary corrections and should not publish as separate CultureMech recipes.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `Resazurin` is a 1 mg row in JCM 742 and TOGO M767 but is stored as 1 `G_PER_L`, a 1000-fold unit slip already detected in `data/import_tracking/reports/concentration_plausibility.tsv`. | `data/normalized_yaml/bacterial/TOGO_M767_Clostridium_Aerotolerans_Medium.yaml`; likely the TOGO importer |
| Major | `Distilled water` is a 1 L final-volume row in JCM 742 and TOGO M767 but is stored as 1 `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M767_Clostridium_Aerotolerans_Medium.yaml`; likely the TOGO importer |
| Major | The source-supported pH 7.0 adjustment is absent from the TOGO owner despite being present in the TOGO `meta` and comment payload and in the direct JCM owner. | `data/normalized_yaml/bacterial/TOGO_M767_Clostridium_Aerotolerans_Medium.yaml` |
| Major | The same JCM `GRMD=742` source exists as direct JCM `CultureMech:003085` and TOGO-derived `CultureMech:010174`; the duplicate records have not been merged or reconciled. | MediaDive/TOGO deduplication or merge logic; direct owners are `data/normalized_yaml/bacterial/clostridium_aerotolerans_medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M767_Clostridium_Aerotolerans_Medium.yaml` |
| Minor | The TOGO preferred term `L--Cysteine.HCl.H2O` retains a source normalization artifact; JCM spells it as L-Cysteine.HCl.H2O and the direct JCM import already has a cleaner label. | `data/normalized_yaml/bacterial/TOGO_M767_Clostridium_Aerotolerans_Medium.yaml` |

No blocker findings were found. The record denotes the intended TOGO/JCM medium and passes the focused schema, strict, term, and reference validators.

## Recommended Edits

1. Replace `Resazurin` 1 `G_PER_L` with the supported 1 mg per 1 L final medium, or 0.001 `G_PER_L` if normalized.
2. Represent distilled water as the 1 L final volume rather than a 1 `G_PER_L` solute.
3. Add the JCM/TOGO pH 7.0 adjustment as `ph_value` and a preparation step.
4. Deduplicate the direct MediaDive/JCM 742 owner and TOGO M767 owner so the direct record's corrected pH/resazurin data and the TOGO record's original-source metadata resolve to one generated recipe.
5. Normalize the L-cysteine label to the JCM spelling while preserving the exact hydrochloride monohydrate grounding.

## Follow-up Checks

- Rerun the focused schema, strict, term, and reference validators on the maintained TOGO owner.
- Regenerate merged YAML and rerun the same validators on the generated JCM 742 record.
- Rerun concentration plausibility and confirm the M767 `Resazurin` indicator-unit warning disappears.
- Inspect an ignored-inclusive exact search for `GRMD=742`, `JCM_M742`, and `TOGO:M767` to confirm the direct JCM and TOGO owners no longer publish separate generated recipes.
- Manually compare the regenerated formula against both TOGO M767 JSON and JCM Medium 742 HTML.

## Additional Notes

The exact duplicate/source search was gitignore-independent and covered `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports`. Other hits for the bare token `M767` referred to JCM Medium 767 in unrelated Synbiobacterium KA13 records and were not treated as duplicates.
