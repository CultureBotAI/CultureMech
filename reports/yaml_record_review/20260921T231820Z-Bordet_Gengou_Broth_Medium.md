# YAML Record Review: Bordet Gengou Broth Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Bordet_Gengou_Broth_Medium.yaml
- Started UTC: 2026-09-21T23:18:20Z
- Finished UTC: 2026-09-21T23:19:03Z
- Verdict: needs curation

## Target

- Reviewed generated merged record `data/merge_yaml/merged/Bordet_Gengou_Broth_Medium.yaml`.
- Target class: `MediaRecipe`
- Stable ID: `CultureMech:008894`
- Name and source label: `bordet_gengou_broth_medium` / `Bordet Gengou Broth Medium`
- Source grounding: `TOGO:M2308`
- Immediate maintained owner: `data/normalized_yaml/bacterial/bordet_gengou_broth_medium.yaml`
- Merge status: single-source merge from `bordet_gengou_broth_medium` with fingerprint `e4795440cc101644347eee8eba79bdc60e068de633d7c1cc4d954cd93d7a3ada`

This is a derived Layer 4 record. The normalized owner already carries the ATCC Medium 35 repair, including a structured Bordet-Gengou Broth Base solution; this stale merge should be regenerated from that owner.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Bordet_Gengou_Broth_Medium.yaml` | Passed. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Bordet_Gengou_Broth_Medium.yaml --out /private/tmp/Bordet_Gengou_Broth_Medium.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Bordet_Gengou_Broth_Medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator found 0 record-level reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Bordet_Gengou_Broth_Medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; the only output was the known `pkg_resources` warning from `eutils`. |
| Embedded `curation_history` | Not checked: this repository documents `just validate-history` for standalone history files, and no focused embedded `MediaRecipe.curation_history` validator is exposed for one merged record. |

The direct `just validate-schema`, `just validate-strict`, and `just validate-terms` wrappers were not rerun for this one-record report because the project environment currently fails while trying to build `llvmlite==0.46.0` under Python 3.13. The table above uses the same focused validators through an offline Python 3.11 no-project environment.

## Identity and Grounding

- The generated `TOGO:M2308` grounding matches the live TOGO payload for ATCC Medium 35 Bordet Gengou Broth Medium.
- The live TOGO payload and the ATCC PDF both support a liquid broth medium made from glycerol, Proteose Peptone, 840 ml prepared Bordet-Gengou Broth Base, and 150 ml sterile defibrinated rabbit blood.
- A gitignore-independent exact search for `TOGO:M2308`, `M2308`, `CultureMech:008894`, fingerprint `e4795440cc101644347eee8eba79bdc60e068de633d7c1cc4d954cd93d7a3ada`, `bordet_gengou_broth_medium`, and `Bordet Gengou Broth Medium` covered `data`, `src`, and `scripts`. It found the active TOGO M2308 normalized owner, the generated merge and indexes, the September repair script, and known diagnostics; it did not find a second active owner for `TOGO:M2308`.

## Evidence

The inspected sources support the repaired normalized owner:

- ATCC Medium 35 lists 10 ml glycerol, 10.0 g Proteose Peptone, 840 ml Bordet-Gengou Broth Base, and 150 ml sterile defibrinated rabbit blood in the final broth.
- The Bordet-Gengou Broth Base is prepared from 125 g potato, 5.5 g NaCl, and DI Water brought back to 1000 ml after the potato broth is boiled and filtered.
- TOGO M2308 preserves the same root formula, nested broth-base composition, pH 6.7 +/- 0.2, autoclaving at 121 C, cooling to 45-50 C, and rabbit-blood addition.

The generated merged record is stale relative to that evidence:

- It still has glycerol, Bordet-Gengou Broth Base, DI Water, and sterile defibrinated rabbit blood as `G_PER_L`, while the normalized owner now uses `ML_PER_L` for the glycerol, broth-base, and water volumes and `PERCENT_V_V` for the rabbit blood.
- It flattened potato, NaCl, and DI Water out of the Bordet-Gengou Broth Base and into root `ingredients`.
- It is missing `ph_value: 6.7`, the broth-base `solutions` entry, `preparation_steps`, `sterilization`, `references`, ingredient `source` annotations, and the September 11 curation event.

## Completeness

- Required schema shape is complete enough to validate, but the generated record is incomplete because it predates the maintained pH, stock solution, preparation, sterilization, unit, reference, and term repairs.
- The commercial or prepared Bordet-Gengou Broth Base is correctly left without a false small-molecule term in the normalized owner; its composition is represented instead.
- Empty optional organism growth evidence is acceptable for this source recipe; the inspected ATCC and TOGO records provide a formulation, not strain-level growth tests.
- No second active TOGO M2308 owner was found by the exact, gitignore-independent search over `data`, `src`, and `scripts` described above.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale and lacks the September 11 ATCC Medium 35 repair already present in the normalized owner. | The generated merge still has `G_PER_L` volumes, a flattened broth-base subrecipe, and no pH, preparation, sterilization, references, source annotations, or structured `Bordet-Gengou Broth Base` solution. | Regenerate `data/merge_yaml/merged/Bordet_Gengou_Broth_Medium.yaml` from `data/normalized_yaml/bacterial/bordet_gengou_broth_medium.yaml`. |

## Recommended Edits

1. Regenerate the merged corpus so `data/merge_yaml/merged/Bordet_Gengou_Broth_Medium.yaml` picks up the maintained September 11 TOGO M2308 / ATCC Medium 35 repair.

## Follow-up Checks

- Confirm the regenerated merge contains 10.0 `ML_PER_L` glycerol, 840.0 `ML_PER_L` Bordet-Gengou Broth Base, 15 `PERCENT_V_V` sterile defibrinated rabbit blood, a nested broth-base composition, `ph_value: 6.7`, ATCC/TOGO references, and the four curated preparation steps.
- Rerun focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/bordet_gengou_broth_medium.yaml` if the normalized owner changes.
- Run `just verify-merges` and `just audit-merge-freshness` after merge regeneration.
- Re-run an exact ignored-file-inclusive search for `TOGO:M2308`, `M2308`, `CultureMech:008894`, fingerprint `e4795440cc101644347eee8eba79bdc60e068de633d7c1cc4d954cd93d7a3ada`, and `bordet_gengou_broth_medium` under `data`, `src`, and `scripts` after regeneration to confirm no duplicate TOGO M2308 owner was introduced.

## Additional Notes

- The exact gitignore-independent search included ignored files and found no other active `TOGO:M2308` owner.
- The generated merge's direct potato, NaCl, and DI Water rows are not wrong ingredients for the overall source document, but their root-level placement is wrong because ATCC and TOGO scope them to the Bordet-Gengou Broth Base.
