# YAML Record Review: Abyssisolibacter Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ABYSSISOLIBACTER_MEDIUM.yaml
- Started UTC: 2026-09-21T08:14:24Z
- Finished UTC: 2026-09-21T08:16:12Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ABYSSISOLIBACTER_MEDIUM.yaml`.
- Stable identifier: `CultureMech:007754`.
- Source identity asserted by the record: TOGO `M1226`, `Abyssisolibacter Medium`, with original JCM source `JCM_M1144` at `GRMD=1144`.
- The generated record was merged from one owner, `TOGO_M1226_Abyssisolibacter_Medium`, on fingerprint `69be680b6fe5109a11eea71fc7c8b76cd7723ffcfeaca4c5d7017c5f2d566367`.
- Current authoritative owner: `data/normalized_yaml/bacterial/TOGO_M1226_Abyssisolibacter_Medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ABYSSISOLIBACTER_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ABYSSISOLIBACTER_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ABYSSISOLIBACTER_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ABYSSISOLIBACTER_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- The record is grounded to the expected TOGO medium: the TOGO API for `M1226` returns `Abyssisolibacter Medium`, original medium `JCM_M1144`, and the same JCM `GRMD=1144` URL.
- The JCM `GRMD=1144` page resolves and agrees with the TOGO source on the ABYSSISOLIBACTER MEDIUM identity, main-solution masses, 1 ml trace-mineral and trace-vitamin additions, 40 ml bicarbonate addition, 5 ml glucose addition, 10 ml reducing-agent additions, pH 7.0, and anaerobic N2-CO2/N2 preparation.
- A gitignore-independent exact search for `TOGO:M1226`, `JCM_M1144`, `GRMD=1144`, and `mediadive.medium:J1144` found two local owners for JCM 1144: this TOGO record and the direct MediaDive/JCM record at `data/normalized_yaml/bacterial/abyssisolibacter_medium.yaml`.
- The generated merge is complete relative to its current TOGO normalized owner; it differs only by merge metadata.
- The simple-salt ChEBI groundings are mostly plausible label matches. `Sodium acetate.3H2O` is grounded to generic sodium acetate, so its hydrate specificity is not retained.

## Evidence

- The JCM primary page lists per-litre main-solution masses for NaCl, MgSO4.7H2O, MgCl2.6H2O, NH4Cl, KCl, CaCl2.2H2O, KH2PO4, yeast extract, sodium acetate.3H2O, FeSO4.7H2O, and 1 mg resazurin in 955 ml distilled water.
- The target imports resazurin as `1 G_PER_L`; that is a 1000-fold unit error for a 1 mg/L JCM ingredient.
- The target preserves post-autoclave liquid additions only as empty solution records whose `concentration` values are the source volumes: `1`, `1`, `40`, `5`, `10`, and `10`.
- The final calculated post-autoclave amounts are 3.2 g/L NaHCO3 from 40 ml/L of 8% NaHCO3, 0.5 g/L glucose from 5 ml/L of 10% glucose, 0.5 g/L Na2S.9H2O from 10 ml/L of 5% stock, and 0.5 g/L L-cysteine.HCl.H2O from 10 ml/L of 5% stock.
- The direct MediaDive/JCM duplicate contains the pH and anaerobic preparation text missing from the TOGO target, but it also expanded repeated components differently and should not be copied without source arithmetic checks.

## Completeness

- The main-solution component list is complete relative to TOGO and JCM except that distilled water is stored as `955 G_PER_L` rather than 955 ml.
- The final-medium reducing agents, bicarbonate, and glucose are incomplete because the record stores stock-addition volumes as concentrations and keeps the solution compositions empty.
- The trace-mineral and trace-vitamin additions are incomplete because Medium M142 and M190 are cross-referenced but not linked or expanded.
- The TOGO-derived target lacks the JCM pH 7.0 setting, N2-CO2 autoclaving, anaerobic serum-bottle dispensing, and final reduction steps.

## Findings

- BLOCKER: every post-autoclave solution addition imported from TOGO is encoded as `G_PER_L` even though the source values are ml volumes; this corrupts trace minerals, trace vitamins, NaHCO3, glucose, Na2S.9H2O, and L-cysteine.HCl.H2O.
- BLOCKER: resazurin is imported at `1 G_PER_L`, but the JCM and TOGO sources both specify `1 mg`.
- MAJOR: the final post-autoclave chemical concentrations are not calculated or otherwise represented; the record says 40 g/L for an 8% NaHCO3 solution addition that should yield 3.2 g/L NaHCO3 if flattened to final medium.
- MAJOR: JCM 1144 is represented twice locally, once through TOGO `M1226` and once through MediaDive `J1144`; the two owners did not merge and the direct import has already merged several duplicate ingredients internally.
- MINOR: the TOGO-derived target omits pH 7.0 and all anaerobic preparation instructions from the JCM source.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/TOGO_M1226_Abyssisolibacter_Medium.yaml` so stock-solution rows preserve addition volumes or flatten to final per-litre chemical masses.
- Convert resazurin from 1 mg/L to `0.001 G_PER_L`.
- Convert the 8% NaHCO3, 10% glucose, 5% Na2S.9H2O, and 5% L-cysteine.HCl.H2O additions to final-medium amounts, or attach those stocks as structured solution additions with ml units.
- Add pH 7.0 and structured preparation steps for N2-CO2 autoclaving, anaerobic post-autoclave addition, serum-bottle dispensing, and final reduction under N2.
- Reconcile the MediaDive `J1144` duplicate after verifying trace mineral and trace vitamin expansion against JCM Medium 151 and JCM Medium 197.
- Regenerate `data/merge_yaml/merged/ABYSSISOLIBACTER_MEDIUM.yaml` after repairing the normalized owners.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-run exact ignored-file-inclusive searches for `TOGO:M1226`, `JCM_M1144`, `GRMD=1144`, and `mediadive.medium:J1144` to confirm there is only one unreconciled JCM 1144 formula.
- Fetch TOGO M142/M190 and JCM 151/197 before expanding trace minerals or trace vitamins.

## Additional Notes

- The JCM note for strain JCM 39191 changes NaCl to 15.0 g/L and pH to 7.5; that appears to be a strain-specific variant and should not overwrite the base Abyssisolibacter Medium formula.
