# YAML Record Review: caldococcus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/caldococcus_medium__ec9b2b10.yaml
- Started UTC: 2026-09-22T02:46:34Z
- Finished UTC: 2026-09-22T02:48:04Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002864`, `caldococcus_medium`, `CALDOCOCCUS MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `caldococcus_medium` on fingerprint `ec9b2b10a5a58bb37738b997b1c9dc715d24bc047d628e4078ec708faf4c5b91`.
- Authoritative owner: `data/normalized_yaml/archaea/caldococcus_medium.yaml`.
- Claimed source identity: JCM / MediaDive Medium `J513`, `CALDOCOCCUS MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- JCM Medium 513 is `CALDOCOCCUS MEDIUM`; the live JCM page confirms this record's pH 2.7 value and preparation text.
- JCM Medium 513 lists final-medium rows for 0.1 g NaCl, 0.1 g calcium chloride dihydrate, 0.05 g ferrous sulfate heptahydrate, 0.1 g yeast extract, 0.1 g casamino acids, 0.8 g peptone, 10 ml trace vitamins from JCM Medium 197, 1 ml trace mineral solution, 2 g sulfur, 1 mg resazurin, 0.5 g sodium sulfide nonahydrate, and 1 L distilled water.
- The direct final-medium chemical identities are source-compatible, but the numeric ingredient rows are slightly underconcentrated by a constant 1000/1011 factor.
- The nested `Trace mineral solution` correctly records the 1 ml/L stock addition, and the MnSO4, CoSO4, and ZnSO4 rows under that solution are source-compatible.
- The CuSO4 x 5 H2O, H3BO3, and Na2MoO4 x 2 H2O trace-mineral stock rows are also source-compatible, but they remain flattened in top-level final `ingredients`.
- The biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic-acid rows are JCM 197 trace-vitamins stock components, not direct Caldococcus final-medium rows.
- Yeast extract and casamino acids are intentionally ungrounded as undefined biological mixtures.

## Evidence

- The generated record's `0.098912`, `0.049456`, `0.791296`, `1.97824`, `0.00098912`, and `0.49456` final-medium values are exactly JCM's `0.1`, `0.05`, `0.8`, `2`, `0.001`, and `0.5` gram-per-liter-equivalent rows divided by 1.011.
- The 1.011 divisor matches the 10 ml trace-vitamins and 1 ml trace-mineral additions, so final-medium masses appear to have been renormalized after treating stock additions as final-volume expansion.
- JCM defines `Trace mineral solution` as a 1 L stock containing MnSO4 x n H2O, CoSO4 x 7 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, H3BO3, and Na2MoO4 x 2 H2O.
- JCM 197 defines `Trace vitamins` as a 1 L stock containing biotin, folic acid, pyridoxine hydrochloride, thiamine hydrochloride, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid.
- The generated record has no final distilled-water row despite JCM 513 listing 1 L final water.
- An exact `find` found a second active owner, `data/normalized_yaml/archaea/TOGO_M514_Caldococcus_Medium.yaml`, imported from the same JCM 513 source through TOGO Medium `M514`.

## Completeness

- The pH value is present.
- The preparation text is present and source-compatible.
- The 1 ml/L trace-mineral solution addition is present, but its stock recipe is incomplete.
- The 10 ml/L trace-vitamins addition is absent.
- The 1 L final distilled-water row is absent.
- Three trace-mineral stock ingredients and all ten trace-vitamin stock ingredients are misplaced as final-medium ingredient rows.
- Empty `target_organisms` and `source_references` are not inherently defects for this JCM / MediaDive import; the source verifies the formulation rather than an organism-specific growth assertion.

## Findings

- Major: final-medium mass rows are lower than the JCM 513 formula by a constant 1000/1011 factor.
- Major: the generated record omits JCM's 1 L final distilled-water row.
- Major: the 10 ml/L trace-vitamins stock addition is missing.
- Major: all ten JCM 197 trace-vitamins components are flattened into top-level final `ingredients` at stock strength, 100x above their 10 ml/L final contribution.
- Major: three of the six local trace-mineral stock components remain flattened into top-level final `ingredients` at stock strength, 1000x above their 1 ml/L final contribution.
- Major: the nested `Trace mineral solution` is incomplete because it carries MnSO4, CoSO4, and ZnSO4 but omits CuSO4, H3BO3, Na2MoO4, and distilled water.
- Minor: the same JCM 513 recipe is split from the TOGO `M514` import rather than reconciled as a duplicate or variant relationship.

## Recommended Edits

- Curate `data/normalized_yaml/archaea/caldococcus_medium.yaml`, not the generated merge.
- Restore exact JCM final-medium values without the 1000/1011 renormalization.
- Add the JCM 1 L final distilled-water row.
- Keep `Trace mineral solution` as a 1 ml/L stock addition and move CuSO4 x 5 H2O, H3BO3, and Na2MoO4 x 2 H2O under the stock composition.
- Add `Trace vitamins` as a 10 ml/L stock addition using the JCM 197 formula, and move the ten flattened vitamin rows under that stock.
- Preserve the pH 2.7 and JCM preparation notes during regeneration.
- Reconcile this direct JCM owner with `data/normalized_yaml/archaea/TOGO_M514_Caldococcus_Medium.yaml` after both imports are curated.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized JCM / MediaDive owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/caldococcus_medium__ec9b2b10.yaml`.
- Compare the regenerated direct owner against JCM 513 and JCM 197, checking for exact final masses, pH 2.7, 1 L final water, 1 ml/L trace mineral solution with all six stock salts, and 10 ml/L trace vitamins with all ten stock vitamins.
- Re-run duplicate detection between the JCM / MediaDive J513 and TOGO M514 owners after both are curated.

## Additional Notes

- `find data/merge_yaml/merged data/normalized_yaml \( -iname 'caldococcus*' -o -iname 'TOGO_M514_Caldococcus_Medium.yaml' \) -print` ignored `.gitignore` rules and found only the two generated Caldococcus records and their two active normalized owners.
- A gitignore-independent structured-data search for `mediadive.medium:J513`, the JCM 513 URL, `CALDOCOCCUS MEDIUM`, `TOGO:M514`, and `TOGO_M514_Caldococcus` found the active direct JCM owner, the TOGO owner, both generated records, registry/catalog rows, current content review manifest rows, current concentration-plausibility rows for the TOGO sibling, and current deep-research priority rows for both Caldococcus owners.
