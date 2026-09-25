# YAML Record Review: ACETIC ACID BACTERIUM medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETIC_ACID_BACTERIUM_MEDIUM.yaml
- Started UTC: 2026-09-21T08:17:38Z
- Finished UTC: 2026-09-21T08:19:10Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETIC_ACID_BACTERIUM_MEDIUM.yaml`.
- Stable identifier: `CultureMech:006960`.
- Source identity asserted by the canonical record: KOMODO ModelSEED `989`, copied from DSMZ Medium 989 / MediaDive `mediadive.medium:989`.
- The generated record was merged from two source owners, `KOMODO_989_ACETIC_ACID_BACTERIUM_medium` and `acetic_acid_bacterium_medium`, on fingerprint `00af5d8180ae8a34bacf7e743234e36d2c6eb5c2b99bb93d9f071bab3c21fa0e`.
- Current authoritative owners: `data/normalized_yaml/bacterial/KOMODO_989_ACETIC_ACID_BACTERIUM_medium.yaml` and `data/normalized_yaml/bacterial/acetic_acid_bacterium_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETIC_ACID_BACTERIUM_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETIC_ACID_BACTERIUM_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETIC_ACID_BACTERIUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETIC_ACID_BACTERIUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- The KOMODO/DSMZ duplicate relationship is coherent. The KOMODO owner explicitly says it copied DSMZ Medium 989, and both normalized owners have the same ingredient/concentration signature for Bacto peptone, yeast extract, glucose, MgSO4.7H2O, and optional agar.
- The DSMZ Medium 989 PDF resolves and identifies the source as `989. ACETIC ACID BACTERIUM MEDIUM`.
- A gitignore-independent exact search for `komodo.medium:989`, `mediadive.medium:989`, `DSMZ Medium 989`, `DSMZ_Medium989`, and `KOMODO_989_ACETIC_ACID_BACTERIUM_medium` found the expected KOMODO owner, expected DSMZ owner, their generated merge, and source-index rows.
- The adjacent `gyp_for_acetic_acid_bacteria_ph_6_0_glucose_30g` record is a distinct NBRC/TOGO M3062 formula with 30 g/L glucose and pH 6.0, so it should not merge with DSMZ 989.
- The ChEBI groundings for glucose, magnesium sulfate heptahydrate, and agar are plausible label matches.

## Evidence

- DSMZ Medium 989 lists 5.0 g Bacto peptone, 5.0 g yeast extract, 5.0 g glucose, 1.0 g MgSO4.7H2O, 1000.0 ml distilled water, and 15.0 g agar if needed.
- The merged record preserves the four non-water solutes and optional agar at the correct DSMZ amounts.
- Both the direct DSMZ owner and the generated merge omit the 1000 ml distilled water row.
- The direct DSMZ owner has preparation steps to adjust to pH 6.6-7.0 and autoclave at 121  C for 15 min, but the generated merge uses the KOMODO owner as canonical and loses those preparation steps.
- The KOMODO owner still contains the malformed timestamp `2026-01-27T01:15:03.fZ`.

## Completeness

- The ingredient table is almost complete relative to DSMZ Medium 989; it is missing only distilled water.
- The generated merge is incomplete relative to the direct DSMZ owner because the canonical KOMODO record lacks the direct DSMZ pH/autoclave preparation steps.
- The merged output correctly records the parent/child `SOURCE_DUPLICATE` relationship between the KOMODO copy and the DSMZ parent.

## Findings

- MAJOR: distilled water from the DSMZ 989 formula is missing from both source owners and the generated merge.
- MAJOR: preparation steps from `data/normalized_yaml/bacterial/acetic_acid_bacterium_medium.yaml` are lost in the generated source-duplicate merge because the KOMODO copy is canonical.
- MAJOR: `data/normalized_yaml/bacterial/KOMODO_989_ACETIC_ACID_BACTERIUM_medium.yaml` retains malformed curation history timestamp `2026-01-27T01:15:03.fZ`.
- MINOR: `physical_state` is `SOLID_AGAR` even though DSMZ marks agar as optional.

## Recommended Edits

- Add the DSMZ `Distilled water 1000.0 ml` row to the DSMZ and KOMODO normalized owners, or model it as the solvent volume expected by CultureMech.
- Copy the DSMZ pH/autoclave preparation steps into the KOMODO source-duplicate child or adjust merge precedence so the generated record retains them from the DSMZ parent.
- Correct the KOMODO import timestamp to a parseable ISO 8601 timestamp.
- Consider representing the optional agar more explicitly so the medium can be used as broth or solid agar.
- Regenerate `data/merge_yaml/merged/ACETIC_ACID_BACTERIUM_MEDIUM.yaml` after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch `DSMZ_Medium989.pdf` and verify that Bacto peptone, yeast extract, glucose, MgSO4.7H2O, water, and optional agar are all present once in the merged output.
- Re-run an exact ignored-file-inclusive search for `komodo.medium:989`, `mediadive.medium:989`, and `DSMZ_Medium989` to confirm only the expected KOMODO/DSMZ source-duplicate pair remains.

## Additional Notes

- The formula itself is substantially correct; the failure is due to one omitted solvent row, lost preparation metadata, and the malformed KOMODO timestamp.
