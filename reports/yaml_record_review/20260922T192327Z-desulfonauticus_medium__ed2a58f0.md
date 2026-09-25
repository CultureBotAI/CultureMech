# YAML Record Review: desulfonauticus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfonauticus_medium__ed2a58f0.yaml
- Started UTC: 2026-09-22T19:20:00Z
- Finished UTC: 2026-09-22T19:23:27Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/desulfonauticus_medium__ed2a58f0.yaml` |
| Generated or maintained | Generated merge output |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M472_Desulfonauticus_Medium.yaml` |
| Related normalized record | `data/normalized_yaml/bacterial/JCM_J471_DESULFONAUTICUS_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009861` |
| Label | `desulfonauticus_medium` |
| Original label | `Desulfonauticus Medium` |
| Source identity | TOGO M472 from original JCM M471 |
| Merge lineage | `merge_recipes.py` merged one source record, `TOGO_M472_Desulfonauticus_Medium.yaml`, into fingerprint `ed2a58f0e23aea1099c6984af44a6e21bdf6e6fd356e32458771954b20911d14` |

I read the full generated record and used a gitignore-independent exact search for the Desulfonauticus label and JCM 471 identifiers. The search found `JCM_J471_DESULFONAUTICUS_MEDIUM.yaml`, a MediaDive import of the same JCM medium that has been folded into `data/merge_yaml/merged/MARINE_SRB_MEDIUM.yaml`, plus DSMZ 383-derived Desulfonauticus records that share the normalized name but are different source formulations.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfonauticus_medium__ed2a58f0.yaml` | Passed; no issues found |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/desulfonauticus_medium__ed2a58f0.yaml --out /private/tmp/desulfonauticus_medium__ed2a58f0.strict.tsv --workers 1 --quiet` | Passed; 0 errors |
| Reference validator, `linkml-reference-validator validate data data/merge_yaml/merged/desulfonauticus_medium__ed2a58f0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator, `linkml-term-validator validate-data data/merge_yaml/merged/desulfonauticus_medium__ed2a58f0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only the known `eutils` / `pkg_resources` deprecation warning was emitted |
| Embedded `curation_history` | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` entries |

The documented `just` wrappers were not used for this focused record check because the local project `uv` environment currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools`. The equivalent validators above were run offline with Python 3.11 and the cached `linkml`, `pyyaml`, `linkml-reference-validator`, and `linkml-term-validator` packages.

## Identity and Grounding

The TOGO identity is correct. The target's `TOGO:M472` term, TOGO M472 API payload, and note all resolve to Desulfonauticus Medium from original JCM M471, and the live JCM `GRMD=471` page confirms that medium number and label.

The generated corpus does not consistently merge the JCM M471 identity. MediaDive J471 is present locally as `JCM_J471_DESULFONAUTICUS_MEDIUM.yaml` and was merged into `MARINE_SRB_MEDIUM`, while this TOGO M472 representation of the same original JCM page remains a separate generated record.

The generated gas rows are not ingredient identities. The JCM M471 instruction uses an H2-CO2 atmosphere and pressure condition; the TOGO expansion also carries an inherited N2-CO2 note from Medium 383. The generated record turns carbon dioxide, nitrogen, and hydrogen into variable-concentration chemical ingredients.

## Evidence

The inspected JCM page defines Medium 471 as Medium 383 modified by replacing sodium lactate with 0.7 g/L sodium acetate and 2.0 g/L yeast extract, preparing under an H2-CO2 4:1 atmosphere, reducing the medium with final 0.1 g/L sodium sulfide and 0.03 g/L sodium dithionite, and pressurizing inoculated vessels to 100 kPa H2-CO2.

TOGO M472 expands the Medium 383 reference into individual main components and carries cross-references to the Medium 180 FeCl2 and trace-element stocks and the Medium 190 trace vitamins. The generated target preserves those three inherited stock names only as empty `Unknown solution` stubs.

Several generated quantities are not supported by the inspected TOGO payload:

- TOGO records resazurin as 1 mg; the generated target has `Resazurin` at `1 G_PER_L`.
- TOGO records Na2SeO3 as 3 ug; the generated target has `Na2SeO3` at `3 G_PER_L`.
- TOGO records distilled water as 1 L; the generated target has `Distilled water` at `1 G_PER_L`.
- TOGO records the H2, CO2, and inherited N2 atmosphere as gas context; the generated target models them as ingredients with `VARIABLE` concentrations.

## Completeness

The generated record is incomplete because it does not carry the full Medium 383, Medium 180, and Medium 190 stock topology needed to follow JCM 471. It names FeCl2 solution, trace element solution, and trace vitamins, but all three have empty `composition: []` arrays and `G_PER_L` concentrations that are not the JCM addition volumes.

A gitignore-independent search of the generated target, the TOGO owner, the MediaDive J471 duplicate, and `MARINE_SRB_MEDIUM.yaml` found no top-level `references:` or `target_organisms:` keys. Empty strain-level growth evidence is acceptable for these source-recipe imports.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Unit parsing changed mg and ug quantities by orders of magnitude. | TOGO M472 has 1 mg resazurin and 3 ug Na2SeO3; the target stores `1 G_PER_L` and `3 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M472_Desulfonauticus_Medium.yaml` and the TOGO unit importer. |
| Major | Inherited stock solution references are empty and have wrong units. | Medium M472 inherits FeCl2, trace element, and trace vitamins references from the JCM 383 formulation. The generated `solutions:` entries have no composition and use `1`, `1`, and `10 G_PER_L` instead of milliliter stock addition volumes with Medium 180 and Medium 190 compositions. | `data/normalized_yaml/bacterial/TOGO_M472_Desulfonauticus_Medium.yaml`; fix source cross-reference resolution for TOGO medium references. |
| Major | Gas atmosphere conditions were modeled as chemical ingredients. | JCM 471 mentions H2-CO2 as preparation and pressurization atmosphere; TOGO also carries inherited N2-CO2 preparation text. The generated record adds carbon dioxide, nitrogen, and hydrogen as variable `ingredients`. | `data/normalized_yaml/bacterial/TOGO_M472_Desulfonauticus_Medium.yaml` and TOGO gas parsing. |
| Major | The same original JCM M471 medium is split across two generated records. | The target is TOGO M472 with `Original source: JCM - JCM_M471`; the MediaDive `mediadive.medium:J471` import appears as a synonym inside `MARINE_SRB_MEDIUM`. | TOGO and MediaDive JCM 471 normalized records plus merge source crosswalk logic. |
| Minor | `Distilled water` is dimensionally wrong. | TOGO has 1 L distilled water, but the generated target has `1 G_PER_L`; the row still signals solvent presence but is not a usable volume. | `data/normalized_yaml/bacterial/TOGO_M472_Desulfonauticus_Medium.yaml`. |

## Recommended Edits

1. Repair TOGO import unit handling for this record so 1 mg resazurin, 3 ug sodium selenite, and 1 L distilled water retain their source units.
2. Resolve the inherited Medium 383 topology: expand the FeCl2 solution, trace element solution, and trace vitamins references through their authoritative Medium 180 and Medium 190 stock recipes instead of leaving empty stubs.
3. Keep H2-CO2 and any inherited N2-CO2 text as preparation and atmosphere metadata, not variable-concentration ingredients.
4. Reconcile `data/normalized_yaml/bacterial/TOGO_M472_Desulfonauticus_Medium.yaml` with `data/normalized_yaml/bacterial/JCM_J471_DESULFONAUTICUS_MEDIUM.yaml` so original JCM M471 is represented once after generation.
5. Regenerate `data/merge_yaml/merged/desulfonauticus_medium__ed2a58f0.yaml` from the corrected normalized source rather than hand-editing the generated YAML.

## Follow-up Checks

1. Rerun open schema, strict schema, term, and reference validation on the edited TOGO M472, MediaDive J471, and regenerated generated records.
2. Compare the regenerated recipe against live JCM `GRMD=471` and TOGO M472, confirming the acetate, yeast extract, sodium sulfide, sodium dithionite, H2-CO2 pressure, and Medium 180/190 cross-references.
3. Verify the regenerated merged directory no longer has a separate TOGO-only Desulfonauticus record for original JCM 471.
4. Recheck concentration plausibility and confirm `Resazurin` and `Na2SeO3` are no longer flagged as top-level unit slips.

## Additional Notes

- `find` and `rg --no-ignore --hidden` were used for absence-sensitive searches, so ignored review reports and generated files were included where relevant.
- No report for `desulfonauticus_medium__ed2a58f0` existed under `reports/yaml_record_review/` before this one; that ignored directory was checked with `find`.
