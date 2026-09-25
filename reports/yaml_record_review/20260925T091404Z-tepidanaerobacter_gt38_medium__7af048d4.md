# YAML Record Review: tepidanaerobacter_gt38_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/tepidanaerobacter_gt38_medium__7af048d4.yaml`
- Started UTC: 2026-09-25T09:12:57Z
- Finished UTC: 2026-09-25T09:14:05Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:002464` for `tepidanaerobacter_gt38_medium`, the MediaDive/JCM `J1300` TEPIDANAEROBACTER GT38 MEDIUM import merged from `tepidanaerobacter_gt38_medium.yaml` with fingerprint `7af048d451ffcd95881a2bafd6f179fb8d12c6138c647a1790b7ee10bbd164e6`.

## Validation

- LinkML schema validation: Passed with `No issues found`.
- Strict validation: Passed; 1 file scanned and 0 error rows written to `/private/tmp/tepidanaerobacter_gt38_medium__7af048d4.strict.tsv`.
- Reference validation: Passed; 1 file validated, 0 external checks.
- Term validation: Passed.
- Embedded `curation_history`: Not checked; `just validate-history` validates standalone `history/`, not merged `MediaRecipe.curation_history`.

## Identity and Grounding

The generated `mediadive.medium:J1300` identity matches MediaDive's JCM Medium J1300, TEPIDANAEROBACTER GT38 MEDIUM. TOGO M1397 reports the same medium name, the same original JCM_M1300 identifier, and the same JCM `GRMD=1300` source URL.

The live JCM `GRMD=1300` page currently returns `Nothing found`, so MediaDive J1300 and TOGO M1397 are the available source payloads for this legacy JCM import. Numeric MediaDive `1300` is an unrelated DSMZ ACM-MEDIUM FOR VERMINEPHROBACTER record and must not be treated as equivalent to JCM `J1300`.

## Evidence

MediaDive J1300 and TOGO M1397 agree on 900 mL distilled water with 2.9 g K2HPO4, 1.5 g KH2PO4, 2.1 g urea, 6 g yeast extract, 0.01 g CaCl2 x 2 H2O, 4 g Na2CO3, 0.5 g L-Cysteine HCl x H2O, 0.5 mg resazurin, 0.2 mL mineral solution, and 100 mL of 10% w/v glucose solution. MediaDive defines the mineral stock separately as MgCl2 x 6 H2O, CaCl2 x 2 H2O, FeSO4 x 7 H2O, and distilled water.

The target instead folds the 10% glucose stock and mineral stock into top-level ingredients at stock concentrations: 100 g/L glucose, 25 g/L MgCl2 x 6 H2O, 37.5 g/L CaCl2 x 2 H2O, and 0.312 g/L FeSO4 x 7 H2O.

## Completeness

The target contains the expected ingredient identities, but it does not preserve the two stock additions as source rows. It also cannot distinguish the direct 0.01 g/L CaCl2 row from the mineral-stock CaCl2 row because `data-quality-cleanup-v1.0` merged them into a single `37.51 G_PER_L` row.

No target organism evidence is present in the JCM-derived recipe payloads, so the empty `target_organisms` slot is not a defect here.

## Findings

- The 0.2 mL mineral solution addition was flattened at full stock strength as final top-level MgCl2 x 6 H2O, CaCl2 x 2 H2O, and FeSO4 x 7 H2O rows.
- The main 0.01 g CaCl2 x 2 H2O row was merged with the 37.5 g/L mineral-stock CaCl2 row to produce an impossible `37.51 G_PER_L` final concentration.
- The 100 mL 10% w/v glucose solution was imported as `Glucose` at `100 G_PER_L` rather than preserved as a stock addition or converted to the final glucose contribution.
- The source duplicate in `data/merge_yaml/merged/TEPIDANAEROBACTER_GT38_MEDIUM.yaml` is emitted separately from the MediaDive/JCM target and carries the same stock-flattening defects plus unresolved `Unknown solution` rows.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/tepidanaerobacter_gt38_medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M1397_Tepidanaerobacter_GT38_Medium.yaml`, then regenerate merged YAML; do not hand-edit `data/merge_yaml/merged/*.yaml`.
- Preserve `Mineral solution` and `10% (w/v) Glucose solution` as stock additions, or scale their components to the final medium before storing final concentrations.
- Keep the direct 0.01 g/L CaCl2 x 2 H2O row separate from any expanded mineral-stock CaCl2 x 2 H2O row.
- Sanitize imported gas-property notes to ASCII in the TOGO normalized record.
- Merge TOGO M1397 and MediaDive J1300 as source duplicates after their stock additions are represented equivalently.

## Follow-up Checks

- Revalidate regenerated GT38 records with schema, strict, reference, and term validators.
- Search exact `mediadive.medium:J1300` and `TOGO:M1397` identities, including ignored files, to verify the JCM source no longer emits two independent generated records.
- Recheck the current JCM `GRMD=1300` page and MediaDive `J1300` payload before a curation fix, because the original JCM URL was unavailable during this review.

## Additional Notes

Exact GT38 identity searches used `rg --no-ignore --hidden`, so ignored files were included.
