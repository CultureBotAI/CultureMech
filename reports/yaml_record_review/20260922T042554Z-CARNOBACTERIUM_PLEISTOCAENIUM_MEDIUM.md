# YAML Record Review: Carnobacterium Pleistocaenium Medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml`
- Started UTC: 2026-09-22T04:22:30Z
- Finished UTC: 2026-09-22T04:25:54Z
- Verdict: needs curation

## Target

`CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml` is the generated `MediaRecipe` for `CultureMech:009755`, the TOGO M374 import of JCM 379 `Carnobacterium Pleistocaenium Medium`.

The generated record was merged only from `data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml` on fingerprint `5e0a1a39f4fce94b21acde27062fa021939c9d8fdda9c465c6f317d445d20e69`.

## Validation

- LinkML validation against `MediaRecipe`: pass.
- `scripts/validate_strict.py`: pass with 0 strict errors.
- `linkml-reference-validator`: pass; 1 file checked, 0 reference checks.
- `linkml-term-validator`: pass.
- Embedded `curation_history`: not checked; the available `just validate-history` target validates standalone files under `history/`, not embedded history events inside merged YAML.

## Identity and Grounding

The high-level source identity is correct: TOGO M374 points to JCM_M379 and the live JCM 379 page for `CARNOBACTERIUM PLEISTOCAENIUM MEDIUM`. The generated recipe is also bacterial, complex, and liquid, as expected.

The recipe did not merge with the separate MediaDive/JCM J379 import at `data/normalized_yaml/bacterial/carnobacterium_pleistocaenium_medium.yaml` because the TOGO importer preserved JCM source quantities but normalized several units incorrectly and left both JCM cross-references as empty `Unknown solution` placeholders.

Several grounding issues follow from those import problems:

- `D--Glucose` is misspelled and ungrounded; the JCM/MediaDive import uses `D-Glucose` and `CHEBI:17634`.
- `MgSO4.7H2O`, `CaSO4.2H2O`, and `Na2S.9H2O` have primary CHEBI terms but no `mediaingredientmech_chebi_term` mirrors.
- The N2 atmosphere was promoted to a variable final ingredient instead of remaining in preparation metadata.

## Evidence

The JCM 379 page lists 1 L distilled water, 0.1 g MgSO4.7H2O, 5 g NaCl, 0.3 g KH2PO4, 0.3 g KCl, 12.5 mg CaSO4.2H2O, 1 g NH4Cl, 0.4 g NaHCO3, 5 g D-Glucose, 1 g Bacto peptone, 0.2 g yeast extract, 10 ml Trace vitamins, 1 ml Trace minerals solution, 1 mg Resazurin, and 0.4 g Na2S.9H2O.

The TOGO JSON preserves the original units, including `unit: L` for distilled water, `unit: mg` for CaSO4.2H2O and Resazurin, and `unit: ml` for Trace vitamins and Trace minerals solution. The generated YAML has:

- `Distilled water`, `value: 1`, `unit: G_PER_L`.
- `CaSO4.2H2O`, `value: 12.5`, `unit: G_PER_L`.
- `Resazurin`, `value: 1`, `unit: G_PER_L`.
- `Trace vitamins`, `value: 10`, `unit: G_PER_L`, `composition: []`, `name: Unknown solution`.
- `Trace minerals solution`, `value: 1`, `unit: G_PER_L`, `composition: []`, `name: Unknown solution`.

The separate MediaDive/JCM J379 import shows the expected normalized direct concentrations for the direct rows, such as 0.012364 g/L CaSO4.2H2O and 0.00098912 g/L Resazurin after scaling the 1011 ml final volume.

## Completeness

The generated TOGO record drops the JCM preparation instructions: boil the basal mix, cool under N2, add NaHCO3, dispense anaerobically, autoclave, separately autoclave a 5% Na2S.9H2O solution under N2, aseptically add sulfide before inoculation, and check final pH 7.2-7.4.

The TOGO M374 `meta.ph` value of 7.2-7.4 is not represented as `ph_range`, and the 10 ml/1 ml stock additions are not linked to concrete vitamin/mineral solution compositions. The record has no target organism or strain growth evidence.

## Findings

- Needs curation: liter, milligram, and milliliter source units were normalized as `G_PER_L`, making water nonsensical, CaSO4.2H2O 1000x too concentrated, Resazurin 1000x too concentrated, and both stock additions dimensionally wrong.
- Needs curation: Trace vitamins and Trace minerals solution cross-references were migrated to empty `Unknown solution` placeholders instead of being resolved to JCM 197 / JCM 228 or a local equivalent.
- Needs curation: JCM 379 preparation and final pH metadata were dropped.
- Needs curation: the N2 preparation atmosphere was promoted to a variable final ingredient.
- Needs curation: the TOGO M374 and MediaDive/JCM J379 imports should be reconciled as duplicate source imports of JCM 379 after unit repairs.
- Minor: `D--Glucose`, the hydrated salt mirrors, and several empty-solution names need term/label cleanup.

## Recommended Edits

- Fix the TOGO importer or normalized M374 owner so `L`, `mg`, and `ml` quantities are converted to recipe water, milligram-to-gram concentrations, or milliliter solution additions rather than `G_PER_L`.
- Resolve `Trace vitamins (see Medium [M190])` and `Trace minerals solution (see Medium [M221])` to concrete solution records or to the JCM 197 / JCM 228 compositions used by JCM 379.
- Restore the JCM 379 preparation instructions and pH 7.2-7.4 range.
- Keep N2 as anaerobic preparation atmosphere metadata instead of an ingredient.
- Reconcile `TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml` with the MediaDive/JCM J379 normalized owner once their formulas are comparable.
- Correct `D--Glucose` to `D-Glucose` and add the missing CHEBI mirrors.

## Follow-up Checks

- Regenerate the merged YAML and verify that M374 no longer emits empty `Unknown solution` entries or `G_PER_L` water.
- Compare the regenerated direct rows against the JCM 379 page and MediaDive J379 main-solution JSON.
- Check that M374 no longer remains isolated from the MediaDive/JCM J379 duplicate family for purely unit-conversion reasons.
- Run LinkML, strict, reference, and term validation after the import repair.

## Additional Notes

Generated `data/merge_yaml/merged` files are derived. Apply durable fixes to `data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml` or the TOGO import/conversion code before regenerating this output.
