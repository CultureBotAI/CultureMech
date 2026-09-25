# YAML Record Review: Bordet Gengou Agar Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Bordet_Gengou_Agar_Medium.yaml
- Started UTC: 2026-09-21T23:13:49Z
- Finished UTC: 2026-09-21T23:15:02Z
- Verdict: needs curation

## Target

- Reviewed generated merged record `data/merge_yaml/merged/Bordet_Gengou_Agar_Medium.yaml`.
- Target class: `MediaRecipe`
- Stable ID: `CultureMech:008893`
- Name and source label: `bordet_gengou_agar_medium` / `Bordet Gengou Agar Medium`
- Source grounding: `TOGO:M2307`
- Immediate maintained owner: `data/normalized_yaml/bacterial/bordet_gengou_agar_medium.yaml`
- Merge status: single-source merge from `bordet_gengou_agar_medium` with fingerprint `a0ceb0166779c54650f19a83d05e57fca3bb0c9971d91f5c1899e5a70cb5c0f9`

This is a derived Layer 4 record. Most field-level defects in the generated YAML are already repaired in the normalized owner by `repair_togo_m2307_m2308_bordet_atcc_score15.py`; this merge needs regeneration after any remaining normalized correction.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Bordet_Gengou_Agar_Medium.yaml` | Passed. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Bordet_Gengou_Agar_Medium.yaml --out /private/tmp/Bordet_Gengou_Agar_Medium.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Bordet_Gengou_Agar_Medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator found 0 record-level reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Bordet_Gengou_Agar_Medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; the only output was the known `pkg_resources` warning from `eutils`. |
| Embedded `curation_history` | Not checked: this repository documents `just validate-history` for standalone history files, and no focused embedded `MediaRecipe.curation_history` validator is exposed for one merged record. |

The direct `just validate-schema`, `just validate-strict`, and `just validate-terms` wrappers were not rerun for this one-record report because the project environment currently fails while trying to build `llvmlite==0.46.0` under Python 3.13. The table above uses the same focused validators through an offline Python 3.11 no-project environment.

## Identity and Grounding

- The TOGO API for `M2307` and the ATCC PDF named by TOGO both identify this medium as Bordet Gengou Agar Medium from ATCC Medium 35.
- The generated `TOGO:M2307` grounding and `SOLID_AGAR` physical state are supported by the inspected recipe.
- A gitignore-independent exact search for `TOGO:M2307`, `M2307`, `bordet_gengou_agar_medium`, `CultureMech:008893`, fingerprint `a0ceb0166779c54650f19a83d05e57fca3bb0c9971d91f5c1899e5a70cb5c0f9`, `mediadive.medium:780`, and `Bordet Gengou Agar Medium` covered `data`, `src`, and `scripts`. It found the active TOGO M2307 normalized owner, the generated merge and indexes, the September repair script, and known diagnostics; it did not find a second active owner for `TOGO:M2307`.
- The generated and normalized records both carry `kg_microbe_match: mediadive.medium:780`. Exact gitignore-independent lookup of that CURIE found that `mediadive.medium:780` denotes DSMZ Medium 780 / MIDDLEBROOK MEDIUM WITH MYCOBACTIN, not Bordet-Gengou Agar.

## Evidence

The inspected TOGO and ATCC sources support the corrected formulation now present in the normalized owner:

- ATCC Medium 35 lists Bordet-Gengou Agar Base (BD 248200) 30.0 g, glycerol 10.0 ml, Proteose Peptone 10.0 g, and DI Water 840 ml.
- The source adjusts the base to pH 6.7 +/- 0.2, autoclaves it at 121 C, cools it to 45-50 C, and then adds 150 ml sterile defibrinated rabbit blood.
- The live TOGO M2307 payload carries the same ingredients, pH comment, autoclave comment, cooling comment, and original ATCC PDF URL.

The generated merged record is stale relative to that repaired evidence:

- It still has glycerol, DI Water, and sterile defibrinated rabbit blood as `G_PER_L`; the normalized owner now uses `ML_PER_L` for glycerol and water and `PERCENT_V_V` for 150 ml/L rabbit blood.
- It is missing the maintained `ph_value: 6.7`, preparation steps, `sterilization`, `references`, ingredient `source` annotations, and September 11 curation event.
- It keeps the erroneous `kg_microbe_match: mediadive.medium:780`, and that same unsupported match is still present in the current normalized owner.

## Completeness

- The generated record is schema-valid but incomplete because it predates the pH, preparation, sterilization, unit, reference, and term repairs in `data/normalized_yaml/bacterial/bordet_gengou_agar_medium.yaml`.
- The commercial Bordet-Gengou Agar Base is intentionally left without a false small-molecule term in the normalized owner; that is not a review defect.
- Empty optional organism growth evidence is acceptable for this source recipe; the inspected ATCC Medium 35 PDF and TOGO payload provide a formulation, not strain-level growth tests.
- No second active TOGO M2307 owner was found by the exact, gitignore-independent search over `data`, `src`, and `scripts` described above.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale and lacks the September 11 ATCC Medium 35 repair already present in the normalized owner. | The generated merge still has `G_PER_L` for glycerol, DI water, and rabbit blood, and it lacks pH, preparation, sterilization, source annotations, and ATCC/TOGO references. `data/normalized_yaml/bacterial/bordet_gengou_agar_medium.yaml` has all of those fields. | Regenerate `data/merge_yaml/merged/Bordet_Gengou_Agar_Medium.yaml` from `data/normalized_yaml/bacterial/bordet_gengou_agar_medium.yaml`. |
| Major | The KG Microbe match points to a different medium. | `kg_microbe_match: mediadive.medium:780` resolves in this corpus to DSMZ Medium 780, MIDDLEBROOK MEDIUM WITH MYCOBACTIN. That is not TOGO M2307 / ATCC Medium 35 Bordet Gengou Agar. | `data/normalized_yaml/bacterial/bordet_gengou_agar_medium.yaml`. |

## Recommended Edits

1. Remove or replace `kg_microbe_match: mediadive.medium:780` in `data/normalized_yaml/bacterial/bordet_gengou_agar_medium.yaml`; do not point this ATCC/TOGO Bordet-Gengou recipe at DSMZ Medium 780.
2. Regenerate the merged corpus so `data/merge_yaml/merged/Bordet_Gengou_Agar_Medium.yaml` picks up the maintained September 11 repair.

## Follow-up Checks

- Rerun the focused open-schema, strict, term, and reference validators on `data/normalized_yaml/bacterial/bordet_gengou_agar_medium.yaml` after the KG Microbe match is removed or corrected.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating merges.
- Confirm the regenerated `data/merge_yaml/merged/Bordet_Gengou_Agar_Medium.yaml` contains 10.0 `ML_PER_L` glycerol, 840.0 `ML_PER_L` DI Water, 15 `PERCENT_V_V` sterile defibrinated rabbit blood, `ph_value: 6.7`, ATCC/TOGO references, and the four curated preparation steps.
- Re-run an exact ignored-file-inclusive search for `TOGO:M2307`, `M2307`, `bordet_gengou_agar_medium`, `CultureMech:008893`, fingerprint `a0ceb0166779c54650f19a83d05e57fca3bb0c9971d91f5c1899e5a70cb5c0f9`, and `Bordet Gengou Agar Medium` under `data`, `src`, and `scripts` after regeneration to confirm no duplicate TOGO M2307 owner was introduced.

## Additional Notes

- The exact gitignore-independent searches included ignored files. The search for `mediadive.medium:780` found other stale or wrong `kg_microbe_match` uses in `ncg_minimum_medium` and `ypg_medium__f8dd146e`; those are outside this one-record review.
- The stale merge's schema success is expected: the obsolete `G_PER_L` unit choices and missing preparation fields are shape-valid even though the maintained source record has since corrected them.
