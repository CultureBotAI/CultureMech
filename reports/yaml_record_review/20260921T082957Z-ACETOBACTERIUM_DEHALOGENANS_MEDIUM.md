# YAML Record Review: ACETOBACTERIUM DEHALOGENANS MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml
- Started UTC: 2026-09-21T08:28:37Z
- Finished UTC: 2026-09-21T08:29:57Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml`.
- Stable identifier: `CultureMech:000819`.
- Source identity asserted by the canonical record: DSMZ Medium 135b / MediaDive `mediadive.medium:135b`.
- The generated record was merged from one source owner, `acetobacterium_dehalogenans_medium`, on fingerprint `02a0047bfe6db287db5faf767ee55ca22305c10642bfdce945a230e65e2932b3`.
- Current authoritative owner: `data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- DSMZ Medium 135b resolves and identifies the source as `135b: ACETOBACTERIUM DEHALOGENANS MEDIUM`.
- A gitignore-independent exact search for `mediadive.medium:135b`, `DSMZ_Medium135b.pdf`, `DSMZ_135b_ACETOBACTERIUM_DEHALOGENANS_MEDIUM`, and `KOMODO_787_ACETOBACTERIUM_DEHALOGENANS_medium` found the expected direct DSMZ owner, expected KOMODO 787 owner, current generated DSMZ merge, source indexes, historical reports, and the KOMODO 787 repair script.
- `data/normalized_yaml/bacterial/KOMODO_787_ACETOBACTERIUM_DEHALOGENANS_medium.yaml` is a separately repaired archived DSMZ Medium 787 / KOMODO source record with different final concentrations; it should not be force-merged with current DSMZ Medium 135b by name alone.

## Evidence

- DSMZ Medium 135b is built from 970 ml distilled water, 20 ml Modified Wolin's mineral solution, 15 ml Na-syringate solution 0.3 M, 1 ml Wolin's vitamin solution 10x, direct salts, 2 g yeast extract, 0.50 ml sodium resazurin 0.1% w/v, 1.50 g Na2CO3, and 0.50 g cysteine.
- The generated record correctly rescales the direct main-medium salts to the 1006 ml assembled volume: for example NH4Cl is `0.994036 G_PER_L`, KH2PO4 is `0.328032 G_PER_L`, K2HPO4 is `0.447316 G_PER_L`, and the basal MgSO4 contribution is `0.0994036 G_PER_L`.
- Modified Wolin's mineral solution components are flattened at stock strength instead of being diluted from the 20 ml/L addition. Nitrilotriacetic acid is `1.5 G_PER_L`, MnSO4.H2O is `0.5 G_PER_L`, NaCl is `1 G_PER_L`, FeSO4.7H2O is `0.1 G_PER_L`, and the trace selenium/tungsten salts are likewise imported as stock rows.
- The basal MgSO4 row and the Modified Wolin MgSO4 row were duplicate-merged as `3.0994036 G_PER_L`; the correct representation would either keep the two contexts separate or add a roughly `0.0596 G_PER_L` stock contribution to the basal `0.0994 G_PER_L`.
- Wolin's vitamin solution components are imported at 10x stock strength even though only 1 ml is added to approximately 1 L final medium: for example pyridoxine is `0.1 G_PER_L`, thiamine is `0.05 G_PER_L`, biotin is `0.02 G_PER_L`, and vitamin B12 is `0.001 G_PER_L`.
- Na-syringate solution is flattened as `60 G_PER_L` syringic acid plus `50 G_PER_L` NaOH, rather than as a 15 ml addition of 0.3 M Na-syringate stock or a correctly diluted sodium syringate final concentration.

## Completeness

- The generated record retains DSMZ's main anaerobic preparation text, the Modified Wolin preparation text, the Wolin vitamin stock, the Na-syringate stock, the pH 7.4 target, and the note to add more Na-syringate after growth starts.
- Distilled water rows are absent from the main medium and all stock recipes.
- The stock hierarchy is absent, so reviewers cannot tell which rows belong to Modified Wolin's mineral solution, Wolin's vitamin solution, or Na-syringate solution.

## Findings

- BLOCKER: Modified Wolin's mineral solution is flattened at stock strength instead of being represented as a 20 ml/L stock addition or correctly diluted final concentrations.
- BLOCKER: duplicate cleanup summed MgSO4 from the basal medium and Modified Wolin's mineral solution, producing `3.0994036 G_PER_L`.
- BLOCKER: Wolin's vitamin solution is flattened at stock strength even though DSMZ adds only 1 ml of the 10x stock per liter.
- BLOCKER: Na-syringate solution is flattened as full-strength syringic acid and NaOH; NaOH is especially wrong because the source lists about 50 ml of 5 N NaOH to dissolve the 1 L stock, not 50 g/L in final medium.
- MINOR: distilled water is omitted from the main medium and from every stock recipe.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml` from DSMZ Medium 135b with Modified Wolin's mineral solution, Wolin's vitamin solution, and Na-syringate solution represented as named stocks or correctly diluted final components.
- Remove the duplicate-merged MgSO4 artifact and keep basal MgSO4 distinct from Modified Wolin MgSO4 unless both are explicitly diluted to final mass.
- Represent Na-syringate as the 15 ml/L 0.3 M stock addition or as correctly calculated final sodium syringate, not as syringic acid and NaOH final ingredients.
- Add distilled water rows for the main medium and stock recipes if direct DSMZ imports standardize explicit solvent rows.
- Regenerate `data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml` after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch `DSMZ_Medium135b.pdf` and verify that 20 ml Modified Wolin's mineral solution, 1 ml Wolin's vitamin solution, and 15 ml Na-syringate solution are either still modeled as stock additions or diluted into the final medium by those volumes.
- Re-run an exact ignored-file-inclusive search for `mediadive.medium:135b`, `DSMZ_Medium135b.pdf`, `KOMODO_787_ACETOBACTERIUM_DEHALOGENANS_medium`, and `komodo.medium:787` to confirm the current DSMZ 135b and archived KOMODO 787 records remain distinct.

## Additional Notes

- The repaired KOMODO 787 record shows the same general stock-dilution approach that this direct DSMZ 135b owner still needs.
