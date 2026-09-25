# YAML Record Review: ARTFICIAL MARINE WATER MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/artficial_marine_water_medium__703fe0e5.yaml`
- Started UTC: 2026-09-21T14:54:36Z
- Finished UTC: 2026-09-21T14:54:51Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:015384` |
| Label | `artficial_marine_water_medium` |
| Source identity | MediaDive `J1123`, JCM Medium 1123 |
| Generated status | Generated merge under `data/merge_yaml/merged/`; do not edit in place |
| Maintained owners | `data/normalized_yaml/specialized/artficial_marine_water_medium.yaml`; `data/normalized_yaml/bacterial/artficial_brackish_water_medium.yaml`; the merge recipe that writes `data/merge_yaml/merged/` |
| Merge provenance | `merged_from` lists MediaDive `J1122` brackish water and MediaDive `J1123` marine water |

This review covers exactly `data/merge_yaml/merged/artficial_marine_water_medium__703fe0e5.yaml`. `find reports/yaml_record_review -name '*artficial_marine_water_medium__703fe0e5.md' -print` searched the ignored `reports/yaml_record_review/` tree and found no prior report named for this target.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/artficial_marine_water_medium__703fe0e5.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/artficial_marine_water_medium__703fe0e5.yaml --out /private/tmp/artficial_marine_water_medium__703fe0e5.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/artficial_marine_water_medium__703fe0e5.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/artficial_marine_water_medium__703fe0e5.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The only emitted message was the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | `just validate-history` | Not checked: the repository exposes this validator for standalone `history/*.yaml` records, not for embedded `MediaRecipe.curation_history` blocks in one merged recipe. |

The project `just` wrappers were not rerun in this pass because this checkout currently resolves through Python 3.13 and attempts to build `llvmlite==0.46.0`, which fails before any target-specific YAML validation. The no-project commands above exercise the narrow validators against this one generated record.

## Identity and Grounding

The intended source identity is valid: the generated record says `mediadive.medium:J1123`, and the MediaDive REST payload for J1123 reports `id: J1123`, `name: ARTFICIAL MARINE WATER MEDIUM`, `source: JCM`, and the JCM 1123 link. JCM Medium 1123 has the same title.

The generated merge is invalid because it also absorbed MediaDive J1122, `ARTFICIAL BRACKISH WATER MEDIUM`. The problem is visible in the generated content: the ID and title are J1123, but the first salts use the J1122 brackish values, for example KH2PO4 0.197824, NH4Cl 0.24728, KCl 0.356083, NaCl 12.8586, Na2SO4 1.40455, and Resazurin 0.00098912 `G_PER_L`. MediaDive J1123 instead normalizes those same rows to 0.188501, 0.235627, 0.678605, 24.5052, 3.77003, and 0.000942507 `G_PER_L`.

Most simple chemical groundings are plausible, but `NiCl2 x 6 H2O` is mapped to `CHEBI:34887` / `nickel dichloride`; the source string is the hexahydrate and should not be grounded to the anhydrous salt.

## Evidence

MediaDive J1123 preserves named `FeCl2 solution`, `Trace element solution`, and `Selenite-tungstate solution` records instead of flattening those stock recipes into the final medium. It also records 30 ml 8% NaHCO3, 40 ml 1 M MgCl2 x 6H2O, 10 ml 1 M CaCl2 x 2H2O, 1 ml each of the three JCM 403 vitamin-family stocks, 10 ml 1 M glucose, and 5 ml 5% Na2S x 9H2O as final-medium stock additions.

The maintained specialized owner has the correct J1123 first-salt `g_l` values, but it flattens the MediaDive FeCl2, Trace element, and Selenite-tungstate solution records into direct ingredients. The generated record keeps that flattening problem and additionally swaps in J1122 brackish first-salt values through the overbroad merge.

JCM Medium 1123 gives two procedural paragraphs. The normalized owner and generated record keep them as two `AUTOCLAVE` steps, but the first paragraph combines base autoclaving with post-cooling stock addition, and the second paragraph combines anaerobic distribution with the reduce-before-use Na2S addition. The action labels are too coarse and partially wrong.

## Completeness

The 960 ml `Distilled water` row from MediaDive's `Main sol. J1123` is absent from both the generated record and the maintained specialized owner.

The generated record has no formal `references` list. The JCM 1123 page, the MediaDive J1123 REST source, JCM 187, JCM 403, and JCM 431 are all needed to recover the full layered recipe.

Optional `target_organisms` are absent; that is acceptable because the JCM and MediaDive medium records inspected here do not curate a strain-level growth claim.

## Findings

| Severity | Finding | Evidence | Maintained owner for a fix |
|---|---|---|---|
| Blocker | MediaDive J1122 and J1123 were merged as duplicates even though the generated canonical claims J1123. | `merged_from` lists `artficial_brackish_water_medium` and `artficial_marine_water_medium`. The generated J1123 record carries J1122 values for the first six ingredients. | Regenerate `data/merge_yaml/merged/` with a fingerprint that distinguishes J1122 brackish water from J1123 marine water. |
| Major | The maintained J1123 owner flattens nested stock solutions into direct final-medium ingredients. | MediaDive J1123 has solution records `3846`, `3847`, and `4172`; the generated record lists HCl, FeCl2 x 4H2O, trace metals, NaOH, selenite, and tungstate directly under `ingredients` at lines 125-244. | Move the three MediaDive nested stocks under `solutions` in `data/normalized_yaml/specialized/artficial_marine_water_medium.yaml`. |
| Major | Milliliter stock additions are represented as gram-per-liter compounds. | MediaDive J1123 lists NaHCO3, MgCl2 x 6H2O, CaCl2 x 2H2O, glucose, and Na2S x 9H2O as ml additions of percent or molar stocks; the generated record stores the same numeric values as `G_PER_L`. | Represent these additions as stock solutions with `ML_PER_L` amounts in the specialized owner. |
| Major | The three JCM 403 vitamin-family references are empty and have wrong units. | Lines 308-326 contain `composition: []`, `unit: G_PER_L`, and `name: Unknown solution` for Vitamin, Thiamine, and Vitamin B12 solution additions. | Curate JCM 403 stock compositions into the specialized owner. |
| Major | Source preparation was collapsed into two overbroad `AUTOCLAVE` steps. | Step 2 is not an autoclave step; it describes anaerobic distribution and pre-use reduction. | Split preparation in `data/normalized_yaml/specialized/artficial_marine_water_medium.yaml` into base mixing, autoclaving, post-cooling stock addition, anaerobic aliquoting, and pre-use reduction. |
| Major | The 960 ml main-solution water row is missing. | MediaDive J1123 recipe order 10 and JCM 1123 both list Distilled water at 960 ml; no water ingredient is present. | Restore the direct water row in the specialized owner. |
| Major | A hydrated nickel salt is grounded as anhydrous nickel dichloride. | `NiCl2 x 6 H2O` maps to `CHEBI:34887` / `nickel dichloride`, while MediaDive J1123 and JCM 187 specify `NiCl2 x 6H2O`. | Resolve an exact hexahydrate term through the packaged MIM label index, or leave the hydrate ungrounded. |

## Recommended Edits

1. Keep MediaDive J1122 and J1123 separate during merge generation; they differ by source ID, title, salt concentrations, water volume, and MgCl2/CaCl2 stock amounts.
2. Rework `data/normalized_yaml/specialized/artficial_marine_water_medium.yaml` to keep the J1123 direct ingredients, referenced stock additions, and nested stock recipes in separate YAML structures.
3. Fill the JCM 403 vitamin, thiamine, and vitamin B12 stock compositions from the JCM Medium 403 source.
4. Restore 960 ml distilled water and add formal references for MediaDive J1123 plus JCM Media 1123, 187, 403, and 431.
5. Split the two broad preparation records into the five distinct operations described by JCM 1123.
6. Correct or remove the `NiCl2 x 6 H2O` CHEBI grounding if no exact hexahydrate term is available.

## Follow-up Checks

- Run `just validate data/normalized_yaml/specialized/artficial_marine_water_medium.yaml` after the normalized edit.
- Run `just verify-merges` after regeneration and confirm J1122 and J1123 no longer share fingerprint `703fe0e52980a52f3b2d85dba3af8fd562e4b23845fcdce72909021e118e7337`.
- Run the same open-schema, strict, reference, and term validators against the regenerated J1123 merged record.
- Manually compare the regenerated output against MediaDive J1123, JCM 1123, JCM 187, JCM 403, and JCM 431.

## Additional Notes

- The TOGO M1201 bacterial owner for JCM 1123 was repaired on 2026-09-11, but the MediaDive J1123 specialized owner was not; do not assume the curated TOGO record automatically fixes this MediaDive record.
