# YAML Record Review: Bordet Gengou agar (supplemented with 15% defibrinated horse blood)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood.yaml
- Started UTC: 2026-09-21T23:15:38Z
- Finished UTC: 2026-09-21T23:16:20Z
- Verdict: needs curation

## Target

- Reviewed generated merged record `data/merge_yaml/merged/bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood.yaml`.
- Target class: `MediaRecipe`
- Stable ID: `CultureMech:009394`
- Name and source label: `bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood` / `Bordet Gengou agar (supplemented with 15% defibrinated horse blood)`
- Source grounding: `TOGO:M2851`
- Immediate maintained owner: `data/normalized_yaml/bacterial/bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood.yaml`
- Merge status: single-source merge from `bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood` with fingerprint `948e1684cb79bce369206c4c36ffd4436cf626de0c89a1767947de678ff75fa3`

This is a derived Layer 4 record. The source-level repair is already present in the normalized TOGO owner; the generated merge predates that repair and needs regeneration.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood.yaml` | Passed. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood.yaml --out /private/tmp/bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator found 0 record-level reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; the only output was the known `pkg_resources` warning from `eutils`. |
| Embedded `curation_history` | Not checked: this repository documents `just validate-history` for standalone history files, and no focused embedded `MediaRecipe.curation_history` validator is exposed for one merged record. |

The direct `just validate-schema`, `just validate-strict`, and `just validate-terms` wrappers were not rerun for this one-record report because the project environment currently fails while trying to build `llvmlite==0.46.0` under Python 3.13. The table above uses the same focused validators through an offline Python 3.11 no-project environment.

## Identity and Grounding

- The generated record's `TOGO:M2851` grounding matches the live TOGO payload for Bordet Gengou agar supplemented with 15% defibrinated horse blood.
- The live TOGO payload carries a 1 L Difco Bordet Gengou agar component and a defibrinated horse blood component; its comment supplies the 15% horse-blood supplement and incubation at 37 C for 3 d.
- A gitignore-independent exact search for `TOGO:M2851`, `M2851`, `CultureMech:009394`, fingerprint `948e1684cb79bce369206c4c36ffd4436cf626de0c89a1767947de678ff75fa3`, `bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood`, and `15% defibrinated horse blood` covered `data`, `src`, and `scripts`. It found the active normalized owner, the generated merge and indexes, and import diagnostics; it did not find a second active owner for `TOGO:M2851`.
- The base-medium product is correctly left opaque in the repaired normalized owner: M2851 names a 1 L Difco Bordet Gengou agar product and does not spell out a base formulation.

## Evidence

The source text supports the normalized owner, not the stale generated merge:

- `data/normalized_yaml/bacterial/bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood.yaml` now records `Bordet Gengou agar (Difco)` as 1000 `ML_PER_L`, not 1 `G_PER_L`.
- The normalized owner now records `Defibrinated horse blood (TCS Biologicals)` as 15 `PERCENT_V_V`, derived from the TOGO comment.
- The normalized owner now records `temperature_value: 37.0`, a TOGO M2851 reference, ingredient `source` annotations, and notes that keep the base opaque.

The generated merge still has the pre-repair representation:

- `Bordet Gengou agar (Difco)` is encoded as 1 `G_PER_L`, even though the source lists 1 L of prepared agar.
- Defibrinated horse blood is still `VARIABLE`, because the generated record predates the repair that read 15% from the source comment.
- The generated record lacks the maintained `temperature_value`, reference, source annotations, and September 7 curation event.

## Completeness

- Required schema shape is complete enough to validate, but the generated record is stale relative to the normalized owner and is missing the structured 15% supplement.
- Empty optional pH and sterilization fields are acceptable for M2851; the inspected TOGO payload does not provide them.
- Empty optional organism growth evidence is acceptable here. The source comment says bacteria grew on this medium but does not name a recoverable taxon or strain in the TOGO payload.
- No duplicate active owner for `TOGO:M2851` was found by the exact, gitignore-independent search over `data`, `src`, and `scripts` described above.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale and still loses the source's volume and 15% horse-blood supplement. | The generated record has 1 `G_PER_L` Difco Bordet Gengou agar and variable defibrinated horse blood. The repaired normalized owner has 1000 `ML_PER_L` prepared agar and 15 `PERCENT_V_V` defibrinated horse blood. | Regenerate `data/merge_yaml/merged/bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood.yaml` from `data/normalized_yaml/bacterial/bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood.yaml`. |

## Recommended Edits

1. Regenerate the merged corpus so this generated record receives the September 7 TOGO M2851 repair.

## Follow-up Checks

- Confirm the regenerated merge keeps `Bordet Gengou agar (Difco)` at 1000 `ML_PER_L` and defibrinated horse blood at 15 `PERCENT_V_V`.
- Rerun focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood.yaml` if the normalized owner changes.
- Run `just verify-merges` and `just audit-merge-freshness` after merge regeneration.
- Re-run the exact ignored-file-inclusive search for `TOGO:M2851`, `M2851`, `CultureMech:009394`, fingerprint `948e1684cb79bce369206c4c36ffd4436cf626de0c89a1767947de678ff75fa3`, and `bordet_gengou_agar_supplemented_with_15_defibrinated_horse_blood` under `data`, `src`, and `scripts` after regeneration to confirm no duplicate owner was introduced.

## Additional Notes

- The exact gitignore-independent search included ignored files and found no other active `TOGO:M2851` owner.
- This record should not be auto-expanded from the more detailed ATCC Medium 35 Bordet-Gengou Agar record. M2851 cites a one-liter commercial Difco Bordet Gengou agar component and the inspected TOGO payload does not state that it is equivalent to ATCC Medium 35.
