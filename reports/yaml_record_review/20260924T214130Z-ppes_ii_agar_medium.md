# YAML Record Review: ppes_ii_agar_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ppes_ii_agar_medium.yaml
- Started UTC: 2026-09-24T21:41:30Z
- Finished UTC: 2026-09-24T21:41:30Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:002607
- Name: ppes_ii_agar_medium
- Source import: JCM Medium J246
- Primary external ID: mediadive.medium:J246
- Maintained input: data/normalized_yaml/bacterial/JCM_J246_PPES-II_AGAR_MEDIUM.yaml

This generated record represents PPES-II AGAR MEDIUM from JCM 246, merged with DSMZ Medium 1075 and the KOMODO import of DSMZ Medium 1075.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/ppes_ii_agar_medium.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

JCM 246 and MediaDive 1075 agree on the PPES-II AGAR MEDIUM formula: 2 g peptone, 1 g Proteose peptone no. 3, 1 g Soytone, 1 g yeast extract, 0.1 g Fe(III)-EDTA, 15 g agar, and 1 L artificial seawater adjusted to pH 7.8.

The artificial seawater subrecipe is also the same across the inspected source branches: 30 g NaCl, 0.7 g KCl, 10.8 g MgCl2 x 6 H2O, 5.4 g MgSO4 x 7 H2O, 1 g CaCl2 x 2 H2O, and 1 L distilled water.

The generated record preserves the final organic, agar, Fe(III)-EDTA, and artificial-seawater salt concentrations, but it flattens the 1 L artificial seawater ingredient and the nested artificial-seawater water row into a flat salt list with no distilled water. TOGO M238 for the same JCM 246 source and TOGO M1571 for the NBRC 374 source are still emitted as separate hashed generated records.

Exact ignored-file searches across `data/normalized_yaml` and `data/merge_yaml` for `JCM_J246_PPES-II_AGAR_MEDIUM`, `KOMODO_1075_PPES-II_AGAR_medium`, exact `name: ppes_ii_agar_medium`, `mediadive.medium:J246`, `mediadive.medium:1075`, `GRMD=246`, `DSMZ Medium: 1075`, and `PPES-II` found the JCM and DSMZ sources merged here plus separate TOGO M238 and TOGO M1571 generated records for the same PPES-II Agar formula.

## Evidence

- JCM 246 lists the six main non-seawater ingredients, 1 L artificial seawater, pH 7.8, and the five-salt artificial-seawater subrecipe in 1 L distilled water.
- MediaDive 1075 lists a main solution with 1000 ml Artificial sea water and a nested Artificial sea water solution containing the same salts plus 1000 ml distilled water.
- TOGO M238 imports JCM_M246 / `GRMD=246` with the same main solution and artificial-seawater subcomponent.
- TOGO M1571 and NBRC 374 list the same main solution and artificial-seawater subcomponent, with Bacto Proteose Peptone No.3 as the branded proteose peptone row.

## Completeness

The generated record is source-identifiable and numerically preserves the final salt amounts, but it is incomplete against the explicit source topology: it omits the artificial-seawater ingredient itself, omits the 1 L distilled water carrier for that artificial seawater, and leaves the JCM and NBRC TOGO imports split into separate generated records.

## Findings

1. Major: The 1 L artificial-seawater base is flattened away, so the generated record exposes only its salts and no longer states that the PPES-II medium is made with 1 L artificial seawater.
2. Major: The artificial-seawater subrecipe's 1 L distilled-water row is absent from the generated merge.
3. Major: TOGO M238 for JCM 246 and TOGO M1571 for NBRC 374 are still emitted as separate generated PPES-II Agar records instead of being reconciled with the JCM / DSMZ 1075 duplicate cluster.
4. Minor: Brand-preserving labels from the JCM and NBRC pages, including `Proteose peptone No. 3 (BD-Difco)` and `Bacto Proteose Peptone No.3 (Difco)`, are collapsed to generic `Proteose peptone no. 3` in the canonical output.

## Recommended Edits

- Represent the artificial seawater as a nested solution or explicit constituent medium on the JCM 246 and DSMZ 1075 normalized inputs, including 1 L distilled water for its preparation.
- Reconcile TOGO M238 and TOGO M1571 with the direct JCM 246 / DSMZ 1075 branch so all PPES-II Agar authority imports are handled in one duplicate cluster or deliberately variant-linked.
- Regenerate `data/merge_yaml/merged/ppes_ii_agar_medium.yaml` after the nested artificial-seawater structure and split TOGO imports are curated.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after normalized curation and regeneration.
- Run exact ignored-file searches for `JCM_M246`, `TOGO:M238`, `TOGO:M1571`, `NBRC_M374`, `GRMD=246`, and `mediadive.medium:1075` to confirm all PPES-II Agar source branches are reconciled.
- Spot-check regenerated output for six main ingredients, 1 L artificial seawater, the five artificial-seawater salts, 1 L distilled water inside the artificial-seawater subrecipe, and pH 7.8.

## Additional Notes

None found.
