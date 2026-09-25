# YAML Record Review: caldococcus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDOCOCCUS_MEDIUM.yaml
- Started UTC: 2026-09-22T02:41:38Z
- Finished UTC: 2026-09-22T02:46:34Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009905`, `caldococcus_medium`, `Caldococcus Medium`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `TOGO_M514_Caldococcus_Medium` on fingerprint `91e027b0b298241129fbfd55e7461be10c9e24ed19336b7f2c0abd5a1812b4a3`.
- Authoritative owner: `data/normalized_yaml/archaea/TOGO_M514_Caldococcus_Medium.yaml`.
- Claimed source identity: TOGO Medium `M514`, imported from JCM Medium 513, `CALDOCOCCUS MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- TOGO `M514` is correctly a TOGO copy of JCM Medium 513, `CALDOCOCCUS MEDIUM`.
- JCM Medium 513 confirms the top-level Caldococcus formula has 0.1 g NaCl, 0.1 g calcium chloride dihydrate, 0.05 g ferrous sulfate heptahydrate, 0.1 g yeast extract, 0.1 g casamino acids, 0.8 g peptone, 10 ml trace vitamins from JCM Medium 197, 1 ml trace mineral solution, 2 g sulfur, 1 mg resazurin, 0.5 g sodium sulfide nonahydrate, and 1 L distilled water.
- JCM Medium 513 confirms the final medium is adjusted to pH 2.7 before autoclaving and to pH 3.0 before inoculation.
- The final-medium sodium chloride, calcium chloride dihydrate, ferrous sulfate heptahydrate, yeast extract, casamino acids, peptone, sulfur, and sodium sulfide masses are source-compatible.
- Resazurin is the right ingredient but has a 1000x unit slip: the source row is `1 mg`, while the generated record stores `1 G_PER_L`.
- Sulfuric acid, nitrogen, carbon dioxide, and hydrogen are procedural pH/gas-phase reagents in JCM, not standalone variable-concentration final-medium ingredients.
- Sodium molybdate dihydrate, boric acid, zinc sulfate heptahydrate, copper sulfate pentahydrate, cobalt sulfate heptahydrate, and manganese sulfate are source-compatible only as internal trace-mineral stock ingredients.

## Evidence

- The live JCM 513 page directly lists the Caldococcus final formula and trace-mineral stock formula; it links the final formula's 10 ml trace-vitamins addition to Medium 197.
- The TOGO `M514` API payload preserved the JCM final formula, the local trace-mineral stock, the JCM source URL, and pH `3.0`.
- The generated record has no `ph_value` and no `preparation_steps`, even though JCM and the TOGO API carry the pH/preparation text.
- The active normalized TOGO owner has already repaired the generated merge's 2.0 g/L distilled-water row to 1.0 g/L, so `data/merge_yaml/merged/CALDOCOCCUS_MEDIUM.yaml` is stale relative to `data/normalized_yaml/archaea/TOGO_M514_Caldococcus_Medium.yaml`.
- The active normalized direct JCM/MediaDive owner for JCM 513 is a separate generated record, `data/merge_yaml/merged/caldococcus_medium__ec9b2b10.yaml`, and preserves the JCM pH and preparation text.
- TOGO's payload cross-references trace vitamins as `M190`, but the live JCM 513 page links the trace-vitamins row to JCM Medium 197; JCM 190 is LYS Medium, while JCM 197 defines the biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic-acid stock formula.

## Completeness

- The top-level final medium is partly complete.
- The JCM `pH 2.7` target before autoclaving and `pH 3.0` adjustment before inoculation are absent.
- The JCM preparation steps for separately autoclaving sodium sulfide, tyndallizing sulfur, filter-sterilizing the trace vitamins, replacing the headspace with H2-CO2, sealing with butyl stoppers, and pressurizing inoculated bottles are absent.
- The 10 ml/L trace-vitamins stock addition and 1 ml/L trace-mineral stock addition are present only as empty `Unknown solution` objects with `G_PER_L` concentrations.
- The trace-vitamins stock composition is entirely absent.
- The trace-mineral stock composition is present only as flattened final-medium rows.
- Empty `target_organisms` and `source_references` are not inherently defects for this TOGO import; the source verifies the formulation rather than an organism-specific growth assertion.

## Findings

- Major: the generated `Distilled water` row is stale at `2.0 G_PER_L`; the maintained owner repaired this to `1.0 G_PER_L`, and both values still model JCM's final 1 L water as grams per liter.
- Major: the generated record omits JCM 513's pH 2.7 / pH 3.0 state and all preparation instructions.
- Major: the 10 ml trace-vitamins addition was migrated into an empty `Trace vitamins (see Medium [M190])` / `Unknown solution` row with concentration `10 G_PER_L` instead of a 10 ml/L stock addition.
- Major: the 1 ml trace-mineral addition was migrated into an empty `Trace mineral solution (see below)` / `Unknown solution` row with concentration `1 G_PER_L` instead of a 1 ml/L stock addition.
- Major: six trace-mineral stock ingredients were flattened into top-level final-medium `ingredients` at stock strength.
- Major: the source's 1 mg resazurin row was imported as `1 G_PER_L`.
- Major: TOGO's vitamin cross-reference points at `M190`, but JCM 513 cites Medium 197 for the trace-vitamins stock formula and the normalized record carries no guard against propagating the wrong cross-reference.
- Minor: H2SO4, N2, CO2, and H2 are modeled as variable final-medium ingredients instead of pH-adjustment and headspace procedure details.

## Recommended Edits

- Curate `data/normalized_yaml/archaea/TOGO_M514_Caldococcus_Medium.yaml`, not the generated merge.
- Update final water handling so the JCM `1.0 L` final distilled-water row is not represented as `G_PER_L`.
- Convert the 1 mg resazurin row to the correct mass-per-final-liter representation.
- Model the trace-vitamins and trace-mineral solutions as 10 ml/L and 1 ml/L stock additions.
- Move Na2MoO4 x 2 H2O, H3BO3, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, CoSO4 x 7 H2O, and MnSO4 x n H2O into the trace-mineral stock composition.
- Replace the TOGO `M190` vitamin-stock cross-reference with the JCM 513 evidence for Medium 197, or record both with an explicit source-discrepancy note if the TOGO import must be preserved verbatim.
- Add the JCM pH and preparation instructions, keeping sulfur, sodium sulfide, gas replacement, and final pressure as procedural details.
- Reconcile the TOGO-derived owner with the direct JCM/MediaDive owner so the two Caldococcus imports do not remain split without an explicit duplicate or variant decision.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized TOGO owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/CALDOCOCCUS_MEDIUM.yaml`.
- Compare the regenerated TOGO-derived record against the live JCM 513 page, with special attention to pH, preparation text, `1 mg` resazurin, 10 ml/L trace vitamins, 1 ml/L trace mineral solution, and 1 L final distilled water.
- Re-run duplicate detection between the TOGO M514 and direct JCM/MediaDive J513 owners after both are curated.
- Verify that any JCM-to-TOGO stock cross-reference mapping does not continue to translate JCM Medium 197 into TOGO `M190`.

## Additional Notes

- `find data/merge_yaml/merged data/normalized_yaml \( -iname 'caldococcus*' -o -iname 'TOGO_M514_Caldococcus_Medium.yaml' \) -print` ignored `.gitignore` rules and found only the two generated Caldococcus records and their two active normalized owners.
- A gitignore-independent structured-data search for `TOGO:M514`, `TOGO_M514_Caldococcus`, `mediadive.medium:J513`, `JCM_M513`, the JCM 513 URL, and the Caldococcus labels found the active TOGO owner, the direct JCM/MediaDive owner, both generated records, registry/catalog rows, current content review rows, current concentration-plausibility rows that already flag the TOGO resazurin and trace-salt magnitudes, and old archive rows.
