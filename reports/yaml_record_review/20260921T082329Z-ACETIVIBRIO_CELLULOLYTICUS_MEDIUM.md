# YAML Record Review: ACETIVIBRIO CELLULOLYTICUS MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
- Started UTC: 2026-09-21T08:22:07Z
- Finished UTC: 2026-09-21T08:23:29Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml`.
- Stable identifier: `CultureMech:004192`.
- Source identity asserted by the canonical record: KOMODO ModelSEED `165`, copied from DSMZ Medium 165 / MediaDive `mediadive.medium:165`.
- The generated record was merged from two source owners, `KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM` and `acetivibrio_cellulolyticus_medium`, on fingerprint `1692085e4dfac874da2d6a8b04a56840db5cceeb4f6f469564be80063c0218c5`.
- Current authoritative owners: `data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml` and `data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- The KOMODO/DSMZ duplicate relationship is coherent: the KOMODO owner says it copied DSMZ Medium 165, and both normalized owners share the same ingredient/concentration signature.
- The DSMZ Medium 165 PDF resolves and identifies the source as `165: ACETIVIBRIO CELLULOLYTICUS MEDIUM`.
- A gitignore-independent exact search for `komodo.medium:165`, `mediadive.medium:165`, `DSMZ_Medium165`, and `KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM` found the expected KOMODO owner, expected DSMZ owner, their generated merge, expected source-index rows, and unrelated DSMZ 1650-series media whose URLs also contain `DSMZ_Medium165`.
- The source is anaerobic: DSMZ instructs sparging with 80% N2 / 20% CO2, dispensing into anoxic Hungate tubes, and using sterile anoxic stocks. The KOMODO duplicate nevertheless says `Aerobic: Yes`.
- The base carbon-source relationship is misrepresented: DSMZ says cellulose can be used as an alternative to cellobiose, while the record includes both as top-level ingredients.

## Evidence

- DSMZ Medium 165 is built from 75 ml Mineral solution 1, 75 ml Mineral solution 2, 10 ml Modified Wolin's mineral solution, 20 ml FeSO4.7H2O solution, 0.50 ml sodium resazurin stock, 1 ml Wolin's vitamin solution, and direct additions of carbonate, cellobiose or cellulose, cysteine, and sulfide.
- Mineral solution 1 and Mineral solution 2 components are imported at stock strength: for example K2HPO4 is `3.9 G_PER_L`, not diluted from a 75 ml/L stock addition.
- Modified Wolin's mineral solution components are imported at stock strength and then duplicate-summed with salts from other stocks: NaCl is `0.59 + 1.0`, MgSO4.7H2O is `1.2 + 3.0`, CaCl2.2H2O is `0.72 + 0.1`, and FeSO4.7H2O is `0.1 + 1.0`.
- The separate 0.1% FeSO4.7H2O stock is imported at stock strength, and its 0.1 N H2SO4 solvent is flattened into a nonsensical `1000 G_PER_L` sulfuric acid ingredient.
- Wolin's vitamin solution components are imported at full 10x stock strength even though only 1 ml/L is added to the final medium.

## Completeness

- The generated merge is complete relative to the current KOMODO owner but incomplete relative to the direct DSMZ owner because it loses the pH 7.2-7.4 range and the DSMZ preparation steps.
- Water rows from the base medium and all stock recipes are missing.
- The stock hierarchy is absent, so reviewers cannot tell which salts belong to Mineral solution 1, Mineral solution 2, Modified Wolin's mineral solution, FeSO4 solution, or Wolin's vitamin solution.

## Findings

- BLOCKER: five DSMZ stock solutions are flattened at stock strength instead of being represented as 75 ml/L, 75 ml/L, 10 ml/L, 20 ml/L, and 1 ml/L additions.
- BLOCKER: duplicate cleanup summed components from distinct stock contexts, corrupting NaCl, MgSO4.7H2O, CaCl2.2H2O, and FeSO4.7H2O.
- BLOCKER: `H2SO4` at `1000 G_PER_L` is a unit-conversion artifact from `1000 ml` of 0.1 N sulfuric acid in the FeSO4 stock, not a final-medium ingredient.
- MAJOR: cellulose is modeled as an optional additive even though DSMZ makes it an alternative to cellobiose.
- MAJOR: the generated merge uses the KOMODO owner as canonical and drops the DSMZ pH range and preparation steps.
- MAJOR: the canonical KOMODO owner says `Aerobic: Yes`, contradicting the DSMZ anaerobic recipe it copied.
- MAJOR: `data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml` retains malformed curation history timestamp `2026-01-27T01:15:02.fZ`.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml` from DSMZ Medium 165 with Mineral solution 1, Mineral solution 2, Modified Wolin's mineral solution, FeSO4.7H2O solution, and Wolin's vitamin solution represented as named stocks or correctly diluted final components.
- Apply the same repair to `data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml`.
- Remove `H2SO4` as a final ingredient; if the FeSO4 stock is expanded, keep the 0.1 N H2SO4 as that stock's solvent.
- Model cellulose as an alternative to cellobiose rather than as an additive.
- Preserve the direct DSMZ pH range and anaerobic preparation steps in the canonical generated record.
- Remove or correct the KOMODO `Aerobic: Yes` assertion and malformed timestamp.
- Regenerate `data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml` after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch `DSMZ_Medium165.pdf` and verify that every stock component is either inside its stock recipe or diluted into the final medium by the correct stock-addition volume.
- Re-run an exact ignored-file-inclusive search for `komodo.medium:165`, `mediadive.medium:165`, and `KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM` to confirm only the expected KOMODO/DSMZ source-duplicate pair remains.

## Additional Notes

- The normalized direct DSMZ owner has the right preparation prose; the main repair is ingredient modeling rather than text recovery.
