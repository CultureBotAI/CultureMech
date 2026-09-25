# YAML Record Review: calroanaerobacter_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/calroanaerobacter_medium__375948ba.yaml
- Started UTC: 2026-09-22T02:58:27Z
- Finished UTC: 2026-09-22T02:59:36Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002227`, `calroanaerobacter_medium`, `CALROANAEROBACTER MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `calroanaerobacter_medium` on fingerprint `375948baaccb49933f73ea6a888095e7e5b31fdbfd1b367a43b58579ab39978e`.
- Authoritative owner: `data/normalized_yaml/bacterial/calroanaerobacter_medium.yaml`.
- Claimed source identity: JCM / MediaDive Medium `J1042`, `CALROANAEROBACTER MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The cited JCM 1042 URL now returns `Nothing found`, so JCM itself was not available for a live cross-check.
- TOGO Medium M1107 is imported from the same JCM medium number and gives a recoverable source payload for the same Calroanaerobacter formula, pH, artificial-seawater subcomponent, and M190/M142 cross-references.
- The direct basal sodium pyruvate, PIPES, yeast extract, and tryptone identities are source-compatible but are slightly underconcentrated.
- The artificial-seawater chemical identities are source-compatible but are slightly underconcentrated and flattened out of the artificial-seawater subcomponent.
- The M142 trace-mineral NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O rows are source-compatible only as internal trace-mineral stock rows, but the generated record sums them into the flattened artificial-seawater salts.
- The M190 trace-vitamin and M142 trace-mineral rows are source-compatible only as internal stock rows.
- Yeast extract and tryptone are intentionally ungrounded as undefined biological mixtures.

## Evidence

- TOGO M1107 lists 5 g sodium pyruvate, 3.46 g PIPES, 2 g yeast extract, 2 g tryptone, 5 ml Trace vitamins from M190, and 1 L Artificial seawater in the final formula.
- The generated basal rows are those TOGO M1107 rows divided by about 1.005; for example, 5 g sodium pyruvate appears as 4.97512 g/L, 3.46 g PIPES appears as 3.44279 g/L, and 2 g yeast extract appears as 1.99005 g/L.
- The 1.005 divisor matches the 5 ml Trace vitamins addition, so the importer appears to have renormalized the 1 L Artificial seawater base plus 5 ml vitamins to 1005 ml.
- TOGO M1107 lists the Artificial seawater subcomponent as its own 1 L recipe with a 5 ml Trace minerals addition from M142.
- The generated `NaCl` row is `22.8905 G_PER_L` with merge parts `21.8905` and `1.0`; the generated `MgSO4 x 7 H2O` row is `8.97015 G_PER_L` with merge parts `5.97015` and `3.0`; the generated `CaCl2 x 2 H2O` row is `0.39850700000000006 G_PER_L` with merge parts `0.298507` and `0.1`.
- The M190 vitamin stock and M142 trace-mineral stock are flattened at their stock strengths into top-level final `ingredients`.

## Completeness

- The pH 7.0 value and JCM-style preparation text are present.
- The 1 L/L artificial-seawater addition is absent as a structured base solution.
- The 5 ml/L Trace vitamins stock addition is absent.
- The 5 ml/L Trace minerals stock addition under artificial seawater is absent.
- All internal artificial-seawater, M190, and M142 ingredients are flattened into final `ingredients`.
- Stock and artificial-seawater rows that share `NaCl`, `MgSO4 x 7 H2O`, and `CaCl2 x 2 H2O` were summed instead of kept at their separate formulation levels.
- Empty `target_organisms` and `source_references` are not inherently defects for this JCM / MediaDive import; the available TOGO mirror verifies the formulation rather than an organism-specific growth assertion.

## Findings

- Major: basal final-medium rows are lower than the inspected TOGO M1107 formula by a constant 1000/1005 factor.
- Major: Artificial seawater is flattened into final `ingredients`; TOGO M1107 calls for a distinct 1 L artificial-seawater base.
- Major: Trace vitamins from M190 are flattened into top-level `ingredients`; TOGO M1107 calls for 5 ml of this stock per final liter.
- Major: Trace minerals from M142 are flattened into top-level `ingredients`; the artificial-seawater base calls for 5 ml of this stock per artificial-seawater liter.
- Major: `NaCl`, `MgSO4 x 7 H2O`, and `CaCl2 x 2 H2O` incorrectly sum artificial-seawater rows with M142 trace-mineral stock rows.
- Major: the generated record omits explicit stock additions for the 1 L artificial seawater, 5 ml M190 Trace vitamins, and 5 ml M142 Trace minerals formula layers.
- Minor: the same source medium is split from the TOGO M1107 import rather than reconciled as a duplicate or variant relationship.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/calroanaerobacter_medium.yaml`, not the generated merge.
- Restore exact TOGO/JCM basal final-medium concentrations before the 1000/1005 renormalization.
- Model Artificial seawater as a structured 1 L/L base solution and move its internal salts into that subcomponent.
- Split M142 NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O out of the flattened artificial-seawater rows.
- Model the TOGO M190 Trace vitamins addition as a 5 ml/L stock and populate its composition from TOGO M190 / JCM 197.
- Model the TOGO M142 Trace minerals addition under Artificial seawater as a 5 ml/L stock and populate its composition from TOGO M142 / JCM 151.
- Reconcile this direct JCM / MediaDive J1042 owner with `data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml` after both imports are curated.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized direct JCM / MediaDive owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/calroanaerobacter_medium__375948ba.yaml`.
- Compare the regenerated direct record against TOGO M1107, M190, and M142, with special attention to 1 L Artificial seawater, 5 ml Trace vitamins, 5 ml Trace minerals, and absence of M142 NaCl/MgSO4/CaCl2 from the artificial-seawater salt rows.
- Re-run duplicate detection between the direct JCM / MediaDive J1042 and TOGO M1107 owners after both are curated.

## Additional Notes

- `find data/merge_yaml/merged data/normalized_yaml \( -iname '*calroanaerobacter*' -o -iname '*caloranaerobacter*' -o -iname '*DSMMZ*' \) -print` ignored `.gitignore` rules and found only the two generated Calroanaerobacter records plus their two active normalized owners.
- A gitignore-independent structured-data search for `TOGO:M1107`, `TOGO_M1107_Calroanaerobacter`, `mediadive.medium:J1042`, `JCM_M1042`, the JCM 1042 URL, and Calroanaerobacter labels found the active TOGO owner, the direct JCM / MediaDive owner, both generated records, registry/catalog rows, current content-review rows, and current deep-research priority rows for both Calroanaerobacter owners.
