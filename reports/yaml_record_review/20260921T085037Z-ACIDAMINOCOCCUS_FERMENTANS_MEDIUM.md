# YAML Record Review: ACIDAMINOCOCCUS FERMENTANS MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACIDAMINOCOCCUS_FERMENTANS_MEDIUM.yaml
- Started UTC: 2026-09-21T08:49:13Z
- Finished UTC: 2026-09-21T08:50:37Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACIDAMINOCOCCUS_FERMENTANS_MEDIUM.yaml`.
- Stable identifier: `CultureMech:005241`.
- Source identity asserted by the canonical record: KOMODO ModelSEED `414`, copied from DSMZ Medium 414 / MediaDive `mediadive.medium:414`.
- The generated record was merged from `KOMODO_414_ACIDAMINOCOCCUS_FERMENTANS_medium` and `acidaminococcus_fermentans_medium` on fingerprint `6d26e71ada3ccaad7ca4d5d3c318f604d34eca6e94e94b291c01c1c3fa2951b0`.
- Current authoritative source owners: `data/normalized_yaml/bacterial/KOMODO_414_ACIDAMINOCOCCUS_FERMENTANS_medium.yaml` and `data/normalized_yaml/bacterial/acidaminococcus_fermentans_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACIDAMINOCOCCUS_FERMENTANS_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACIDAMINOCOCCUS_FERMENTANS_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACIDAMINOCOCCUS_FERMENTANS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACIDAMINOCOCCUS_FERMENTANS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- DSMZ Medium 414 resolves and identifies the source as `414: ACIDAMINOCOCCUS FERMENTANS MEDIUM`.
- The KOMODO/DSMZ duplicate relationship is coherent: the KOMODO owner says it copied DSMZ Medium 414, and the direct DSMZ owner carries `mediadive.medium:414`.
- A bounded gitignore-independent exact search for `komodo.medium:414`, `mediadive.medium:414`, `TOGO:M2686`, `DSMZ_Medium414.pdf`, `ACIDAMINOCOCCUS_FERMENTANS_MEDIUM`, and `acidaminococcus_fermentans_medium` found the expected KOMODO owner, direct DSMZ owner, a TOGO owner that cites the same DSMZ Medium 414 PDF, expected source-index rows, the current generated KOMODO/DSMZ merge, and the split TOGO-generated sibling `data/merge_yaml/merged/acidaminococcus_fermentans_medium__d515a0ab.yaml`.

## Evidence

- DSMZ Medium 414 directly lists 5.0 g Trypticase peptone, 10.0 g casamino acids, 5.0 g yeast extract, 5.0 g glucose, 4.0 g Na-glutamate, 1.0 g arginine, 1.0 g glycine, 0.1 g DL-tryptophan, 2.0 g KH2PO4, 0.5 ml Tween 80, 0.5 g cysteine-HCl.H2O, and 1000.0 ml distilled water, with final pH 7.0-7.2.
- The generated KOMODO/DSMZ merge matches the DSMZ gram-denominated rows exactly.
- The DSMZ `0.5 ml` Tween 80 addition is represented as `0.5 G_PER_L`, losing that the source specified a volume.
- The TOGO M2686 owner cites the same DSMZ Medium 414 PDF but was not merged with the direct DSMZ/KOMODO source family; its generated sibling also carries a `Distilled water` row at `1000 G_PER_L`, which explains part of the fingerprint divergence.
- The direct DSMZ owner preserves preparation steps for pH 7.0-7.2 and Hungate-technique anaerobic handling; the canonical generated record is KOMODO-derived and drops preparation steps.

## Completeness

- The direct DSMZ and KOMODO duplicate relationship is complete.
- The TOGO M2686 duplicate for the same DSMZ Medium 414 source is not reconciled.
- DSMZ distilled water is absent from the generated KOMODO/DSMZ merge.
- The generated canonical record lacks the direct DSMZ preparation steps.

## Findings

- MAJOR: the generated record stores DSMZ's `0.5 ml` Tween 80 volume as `0.5 G_PER_L`.
- MAJOR: TOGO M2686 cites DSMZ Medium 414 but generates separately from the KOMODO/DSMZ source-duplicate merge.
- MAJOR: the generated record uses the KOMODO owner as canonical and drops the direct DSMZ pH and anaerobic-handling preparation steps.
- MAJOR: `data/normalized_yaml/bacterial/KOMODO_414_ACIDAMINOCOCCUS_FERMENTANS_medium.yaml` retains malformed curation history timestamp `2026-01-27T01:15:02.fZ`.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/acidaminococcus_fermentans_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_414_ACIDAMINOCOCCUS_FERMENTANS_medium.yaml` so Tween 80 preserves the DSMZ `0.5 ml/L` volume addition.
- Repair `data/normalized_yaml/bacterial/TOGO_M2686_Acidaminococcus_Fermentans_Medium.yaml` so its distilled-water volume is not stored as `1000 G_PER_L`.
- Reconcile TOGO M2686 with the direct DSMZ/KOMODO Medium 414 owners after normalized repair.
- Preserve the direct DSMZ preparation steps in the canonical generated record.
- Remove or correct the malformed KOMODO timestamp.
- Regenerate merged records after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch `DSMZ_Medium414.pdf` and verify that the regenerated record still matches every gram-denominated ingredient exactly while preserving Tween 80 as a volume.
- Re-run ignored-file-inclusive exact searches for `komodo.medium:414`, `mediadive.medium:414`, `TOGO:M2686`, and `ACIDAMINOCOCCUS_FERMENTANS_MEDIUM` to confirm all DSMZ Medium 414 owners are reconciled.

## Additional Notes

- Optional empty fields were not treated as defects.
