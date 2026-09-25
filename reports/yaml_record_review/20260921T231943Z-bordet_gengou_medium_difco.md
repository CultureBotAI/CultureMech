# YAML Record Review: BORDET-GENGOU-MEDIUM (DIFCO)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bordet_gengou_medium_difco.yaml
- Started UTC: 2026-09-21T23:19:43Z
- Finished UTC: 2026-09-21T23:20:39Z
- Verdict: needs curation

## Target

- Reviewed generated merged record `data/merge_yaml/merged/bordet_gengou_medium_difco.yaml`.
- Target class: `MediaRecipe`
- Stable ID: `CultureMech:005286`
- Name and source label: `bordet_gengou_medium_difco` / `BORDET-GENGOU-MEDIUM (DIFCO)`
- Source grounding: `komodo.medium:438`, with source duplicate parent `mediadive.medium:438`
- Maintained owners: `data/normalized_yaml/bacterial/KOMODO_438_BORDET-GENGOU-MEDIUM_DIFCO.yaml` and `data/normalized_yaml/bacterial/bordet_gengou_medium_difco.yaml`
- Merge status: two-source merge from `KOMODO_438_BORDET-GENGOU-MEDIUM_DIFCO` and `bordet_gengou_medium_difco` with fingerprint `ea662aa166e9c7fbc8c95cd673197b407d2bf9392c25c4be879422c0c2039228`

This is a derived Layer 4 source-duplicate merge. Both normalized inputs have been repaired to the same DSMZ Medium 438 formulation, but the generated merge predates that repair.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bordet_gengou_medium_difco.yaml` | Passed. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bordet_gengou_medium_difco.yaml --out /private/tmp/bordet_gengou_medium_difco.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bordet_gengou_medium_difco.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator found 0 record-level reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bordet_gengou_medium_difco.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; the only output was the known `pkg_resources` warning from `eutils`. |
| Embedded `curation_history` | Not checked: this repository documents `just validate-history` for standalone history files, and no focused embedded `MediaRecipe.curation_history` validator is exposed for one merged record. |

The direct `just validate-schema`, `just validate-strict`, and `just validate-terms` wrappers were not rerun for this one-record report because the project environment currently fails while trying to build `llvmlite==0.46.0` under Python 3.13. The table above uses the same focused validators through an offline Python 3.11 no-project environment.

## Identity and Grounding

- DSMZ Medium 438 is BORDET-GENGOU-MEDIUM (DIFCO), and the inspected DSMZ PDF states that Bordet-Gengou-Agar-Base is supplemented with 15% horse blood.
- The KOMODO normalized owner states DSMZ Medium 438 provenance and is correctly linked to the direct DSMZ/MediaDive owner as a `SOURCE_DUPLICATE`.
- A gitignore-independent exact search for `komodo.medium:438`, `mediadive.medium:438`, `DSMZ Medium: 438`, `CultureMech:005286`, `CultureMech:001546`, fingerprint `ea662aa166e9c7fbc8c95cd673197b407d2bf9392c25c4be879422c0c2039228`, and `bordet_gengou_medium_difco` covered `data`, `src`, and `scripts`. It found exactly the two maintained source owners for DSMZ/KOMODO 438, the generated merge and indexes, the September repair script, and known diagnostics.
- Both maintained owners still carry `kg_microbe_match: mediadive.medium:101`. Exact lookup shows `mediadive.medium:101` belongs to DSMZ Medium 101, `nutrient_agar_or_broth_with_nacl`, not DSMZ Medium 438.

## Evidence

The inspected DSMZ 438 PDF supports only the concise repaired formulation:

- Bordet-Gengou-Agar-Base supplemented with 15% horse blood.
- A note to rehydrate freeze-dried ampoules in liquid medium 220 or 1.

The generated merge is stale relative to the repaired normalized inputs:

- It still encodes `Bordet-Gengou-Agar-Base` as 1000 `G_PER_L`; both normalized inputs now preserve it as 1000 `ML_PER_L`.
- It still encodes horse blood as 150 `G_PER_L`; both normalized inputs now preserve the source supplement as 15 `PERCENT_V_V`.
- It still carries `Peptone`, `Meat extract`, `Casein peptone`, `Soy peptone`, `NaCl`, and a doubled 30 g/L `Agar` row. None of those are spelled out by DSMZ Medium 438, which names an opaque commercial Bordet-Gengou-Agar-Base instead.
- It is missing the `preparation_steps`, `references`, ingredient `source` annotations, `data_quality_flags`, and September 11 curation events now present in both normalized source records.

## Completeness

- Required schema shape is complete enough to validate, but the generated record is incomplete because it predates the maintained repair that made the commercial base opaque and restored the 15% v/v horse-blood supplement.
- Empty optional pH, temperature, and sterilization fields are acceptable for this record; DSMZ Medium 438 does not provide those details.
- Empty optional organism growth evidence is acceptable for the source recipe; the inspected PDF provides a formulation, not a strain-level growth test.
- The source-duplicate relationship between the KOMODO and DSMZ owners is represented in both maintained inputs and in the stale generated merge.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale and still expands an opaque DSMZ Bordet-Gengou-Agar-Base product into unsupported direct ingredients. | DSMZ Medium 438 lists Bordet-Gengou-Agar-Base plus 15% horse blood only. Both normalized owners now match that; the generated merge still contains peptone, meat extract, casein peptone, soy peptone, NaCl, and doubled agar rows from the old import. | Regenerate `data/merge_yaml/merged/bordet_gengou_medium_difco.yaml` from the repaired DSMZ and KOMODO normalized records. |
| Major | The KG Microbe match points to the wrong DSMZ medium. | `kg_microbe_match: mediadive.medium:101` resolves in this corpus to DSMZ Medium 101 / Nutrient Agar or Broth with NaCl, not DSMZ Medium 438. The wrong match is present in both normalized source-duplicate owners. | `data/normalized_yaml/bacterial/bordet_gengou_medium_difco.yaml` and `data/normalized_yaml/bacterial/KOMODO_438_BORDET-GENGOU-MEDIUM_DIFCO.yaml`. |

## Recommended Edits

1. Remove or replace `kg_microbe_match: mediadive.medium:101` in both normalized DSMZ/KOMODO 438 owners.
2. Regenerate the merged corpus so `data/merge_yaml/merged/bordet_gengou_medium_difco.yaml` picks up the September 11 DSMZ 438 repair and the KG-match correction.

## Follow-up Checks

- Rerun focused open-schema, strict, reference, and term validators on both normalized owners after the KG Microbe match is corrected.
- Confirm the regenerated merge contains only `Bordet-Gengou-Agar-Base` at 1000 `ML_PER_L` and `Horse blood` at 15 `PERCENT_V_V`.
- Run `just verify-merges` and `just audit-merge-freshness` after merge regeneration.
- Re-run the exact ignored-file-inclusive search for `komodo.medium:438`, `mediadive.medium:438`, `DSMZ Medium: 438`, `CultureMech:005286`, `CultureMech:001546`, fingerprint `ea662aa166e9c7fbc8c95cd673197b407d2bf9392c25c4be879422c0c2039228`, and `bordet_gengou_medium_difco` under `data`, `src`, and `scripts` after regeneration to confirm there are still exactly two active normalized owners for this DSMZ/KOMODO source duplicate.

## Additional Notes

- The exact gitignore-independent searches included ignored files. The `mediadive.medium:101` lookup found many stale or wrong KG matches to DSMZ Medium 101 outside this one-record review; they were not assessed here.
- The `Bordet-Gengou-Agar-Base` row is deliberately left unmapped in the repaired normalized inputs. DSMZ names a commercial base, not a single chemical.
