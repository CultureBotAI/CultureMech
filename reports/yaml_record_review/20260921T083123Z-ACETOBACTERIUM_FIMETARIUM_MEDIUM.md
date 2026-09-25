# YAML Record Review: ACETOBACTERIUM FIMETARIUM MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml
- Started UTC: 2026-09-21T08:29:58Z
- Finished UTC: 2026-09-21T08:31:23Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml`.
- Stable identifier: `CultureMech:001743`.
- Source identity asserted by the canonical record: DSMZ Medium 614 / MediaDive `mediadive.medium:614`.
- The stale generated record was merged from two source owners, `acetobacterium_fimetarium_medium` and `for_dsm_8238`, on fingerprint `be7f7c7533db17f16c26ecef23523b35fbb5e4f2d1dbf3d89aa4dc3d41270b25`.
- Current authoritative owners: `data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml` and `data/normalized_yaml/bacterial/for_dsm_8238.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- DSMZ Medium 614 resolves and identifies the source as `614: ACETOBACTERIUM FIMETARIUM MEDIUM`.
- The current normalized topology no longer matches the generated record: on 2026-09-13 `repair_komodo_614_acetobacterium_score10.py` changed `for_dsm_8238` from `SOURCE_DUPLICATE` to `PH_VARIANT` because KOMODO Medium 614.1 applies DSMZ Medium 614 at pH 7.5 for DSM 8238.
- A gitignore-independent exact search for `mediadive.medium:614`, `DSMZ_Medium614.pdf`, `DSMZ_614_ACETOBACTERIUM_FIMETARIUM_MEDIUM`, `for_dsm_8238`, and `mediadive.medium:8238` found the expected direct DSMZ owner, the pH-variant KOMODO 614.1 owner, a separate KOMODO 614 `acetobacterium_sp_medium` sibling, generated merges, source indexes, historical reports, and the topology repair script.

## Evidence

- DSMZ Medium 614 is built from 1000 ml distilled water, 10 ml Modified Wolin's mineral solution, 1 ml Wolin's vitamin solution 10x, direct KCl, MgCl2.6H2O, CaCl2.2H2O, NH4Cl, KH2PO4, yeast extract, 0.50 ml sodium resazurin 0.1% w/v, 1.00 g NaHCO3, 10.00 g D-fructose, and 0.70 g Na2S.9H2O.
- The generated record correctly rescales the direct main-medium rows to the approximately 1011 ml assembled volume: for example KCl and NH4Cl are `0.326409 G_PER_L`, MgCl2.6H2O is `0.514342 G_PER_L`, fructose is `9.8912 G_PER_L`, and sulfide is `0.692384 G_PER_L`.
- Modified Wolin's mineral solution components are flattened at stock strength instead of being diluted from the 10 ml/L addition. Nitrilotriacetic acid is `1.5 G_PER_L`, MgSO4.7H2O is `3 G_PER_L`, MnSO4.H2O is `0.5 G_PER_L`, NaCl is `1 G_PER_L`, FeSO4.7H2O is `0.1 G_PER_L`, and the trace selenium/tungsten salts are likewise imported as stock rows.
- The direct CaCl2.2H2O row and the Modified Wolin CaCl2.2H2O row were duplicate-merged as `0.317606 G_PER_L`; the correct representation would either keep the two contexts separate or add a roughly `0.001 G_PER_L` stock contribution to the direct `0.217606 G_PER_L`.
- Wolin's vitamin solution components are imported at 10x stock strength even though DSMZ adds only 1 ml of the 10x stock per liter: for example pyridoxine is `0.1 G_PER_L`, thiamine is `0.05 G_PER_L`, biotin is `0.02 G_PER_L`, and vitamin B12 is `0.001 G_PER_L`.

## Completeness

- The generated record retains DSMZ's anaerobic preparation text, the Modified Wolin preparation text, and the pH 6.8-7.0 target.
- The generated record is stale relative to current normalized curation because it still merges `for_dsm_8238` as a `SOURCE_DUPLICATE` instead of preserving it as a pH 7.5 variant child.
- Distilled water rows are absent from the main medium and stock recipes.
- The stock hierarchy is absent, so reviewers cannot tell which rows belong to the final medium, Modified Wolin's mineral solution, or Wolin's vitamin solution.

## Findings

- BLOCKER: Modified Wolin's mineral solution is flattened at stock strength instead of being represented as a 10 ml/L stock addition or correctly diluted final concentrations.
- BLOCKER: duplicate cleanup summed CaCl2.2H2O from the direct medium and Modified Wolin's mineral solution, producing `0.317606 G_PER_L`.
- BLOCKER: Wolin's vitamin solution is flattened at stock strength even though DSMZ adds only 1 ml of the 10x stock per liter.
- MAJOR: the generated merge is stale and still merges the pH 7.5 `for_dsm_8238` owner as a `SOURCE_DUPLICATE`.
- MINOR: distilled water is omitted from the main medium and stock recipes.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml` from DSMZ Medium 614 with Modified Wolin's mineral solution and Wolin's vitamin solution represented as named stocks or correctly diluted final components.
- Remove the duplicate-merged CaCl2.2H2O artifact and keep direct-medium CaCl2.2H2O distinct from Modified Wolin CaCl2.2H2O unless both are explicitly diluted to final mass.
- Apply the same stock-dilution repair to `data/normalized_yaml/bacterial/for_dsm_8238.yaml` while preserving its `PH_VARIANT` relationship to the DSMZ Medium 614 parent.
- Regenerate `data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml` so `for_dsm_8238` is no longer merged into the parent generated record.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch `DSMZ_Medium614.pdf` and verify that 10 ml Modified Wolin's mineral solution and 1 ml Wolin's vitamin solution are either still modeled as stock additions or diluted into the final medium by those volumes.
- Re-run an exact ignored-file-inclusive search for `mediadive.medium:614`, `for_dsm_8238`, `komodo.medium:614`, and `komodo.medium:614.1` to confirm the parent, pH variant, and separate KOMODO 614 sibling are represented by the intended generated records.

## Additional Notes

- The normalized 2026-09-13 topology repair already separates the pH variant correctly; the generated merge just has not caught up with that source state.
