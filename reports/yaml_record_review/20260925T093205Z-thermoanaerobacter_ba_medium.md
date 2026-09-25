# YAML Record Review: Thermoanaerobacter (BA) Medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoanaerobacter_ba_medium.yaml`
- Started UTC: `2026-09-25T09:32:05Z`
- Finished UTC: `2026-09-25T09:33:35Z`
- Verdict: needs curation

## Target
Generated TOGO-branch bacterial recipe `CultureMech:009278`, `thermoanaerobacter_ba_medium`, with medium term `TOGO:M2728` and label `Thermoanaerobacter (BA) Medium`.

It is a merged generated record from two imported TOGO recipes: `TOGO_M2728_Thermoanaerobacter_BA_Medium` and `TOGO_M2730_Thermoanaerobacter_BA_Medium`.

## Validation
- LinkML schema validation: passed; `linkml-validate` reported `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file and wrote only the TSV header, with 0 error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` exited 0 after its startup warning.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The intended source identity is DSMZ Medium 671, `THERMOANAEROBACTER (BA) MEDIUM`; the TOGO target cites `DSMZ_Medium671.pdf`, and both TOGO source IDs point to that same DSMZ recipe.

The same DSMZ 671 identity is still present as a separate generated record, `data/merge_yaml/merged/thermoanaerobacter_ba_medium__416883c0.yaml`, whose MediaDive/KOMODO branch carries `mediadive.medium:671` and two KOMODO DSMZ 671 variants. The two generated branches therefore remain source-equivalent duplicates.

One ingredient has a stale legacy regrounding mismatch: `MgSO4 x 7 H2O` has the correct primary `term` `CHEBI:31795` but its `mediaingredientmech_chebi_term` is still generic `CHEBI:32599`, `magnesium sulfate`.

## Evidence
DSMZ Medium 671 and MediaDive medium 671 describe one main solution containing NH4Cl, NaCl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, K2HPO4 x 3 H2O, 10 ml Modified Wolin's mineral solution, yeast extract, 0.5 ml 0.1% sodium resazurin, Na2CO3, cellobiose, optional 2 g/L Avicel cellulose, 1 ml Wolin's vitamin solution 10x, Na2S x 9 H2O, and water to 1000 ml.

The generated TOGO record collapses the main water plus the stock-solution waters into a single `3000.0 G_PER_L` row, merges direct and stock contributions for NaCl and CaCl2, and promotes the contents of Modified Wolin's mineral solution into top-level ingredients at their stock recipe concentrations.

The same stock-flattening happened to Wolin's vitamin solution 10x: `Biotin` is represented as `2 G_PER_L`, `p-Aminobenzoic acid` as `5 G_PER_L`, `Pyridoxine-HCl` as `10 G_PER_L`, and the other vitamin stock components have similarly stock-level `G_PER_L` values instead of representing a 1 ml/L addition of the vitamin stock.

The mineral stock also retained its source recipe's milligram rows as gram rows: DSMZ gives `Na2SeO3 x 5 H2O` at 0.30 mg/L and `Na2WO4 x 2 H2O` at 0.40 mg/L within the stock solution, but the target has them as `0.3 G_PER_L` and `0.4 G_PER_L` top-level medium concentrations.

## Completeness
The main DSMZ preparation notes are missing from the TOGO branch: cellobiose, vitamins, sulfide, and carbonate must be added from separately sterilized anoxic stocks under the specified gas atmospheres, with final pH adjusted to 7.0.

The optional substrate variants are also incomplete on this branch. DSMZ lists optional Avicel cellulose at 2 g/L for adapted strains and a D-xylose replacement for DSM 29083 and DSM 25963; those notes are only represented in the unmerged MediaDive/KOMODO branch.

## Findings
1. Needs curation: the generated TOGO branch represents stock solution recipes as if they were direct medium ingredients. This changes final concentrations by orders of magnitude and destroys the distinction between the main recipe and the Modified Wolin and Wolin vitamin stocks.
2. Needs curation: DSMZ/MediaDive/KOMODO source-equivalent data for DSMZ 671 remain in `thermoanaerobacter_ba_medium__416883c0.yaml`, so CultureMech now has two generated records for the same underlying medium.
3. Needs curation: the TOGO branch lacks DSMZ preparation semantics for separately sterilized anoxic stock additions, pH adjustment, optional cellulose adaptation, and D-xylose replacement for specific DSM accessions.
4. Minor issue: `MgSO4 x 7 H2O` still has a generic `mediaingredientmech_chebi_term` even though its primary CHEBI grounding was corrected to magnesium sulfate heptahydrate.

## Recommended Edits
1. Normalize the TOGO M2728 and M2730 source records, not the generated merge file, so DSMZ Medium 671 has a single main solution plus nested stock additions for Modified Wolin's mineral solution, Wolin's vitamin solution 10x, sodium resazurin, carbonate, sulfide, and KOH where applicable.
2. Preserve the DSMZ preparation instructions in structured `preparation_steps`, including anoxic sparging with 80% N2 and 20% CO2, the separate anoxic stock additions, sterile filtration of cellobiose and vitamins, and pH 7.0 final adjustment.
3. Merge the TOGO and MediaDive/KOMODO DSMZ 671 branches by source identity after normalization so `TOGO:M2728`, `TOGO:M2730`, `mediadive.medium:671`, `komodo.medium:671`, and `komodo.medium:671_replace_Cellobiose_with_Cellulose` resolve into one canonical generated DSMZ 671 record.
4. Keep the cellulose adaptation and D-xylose-for-strain-specific-use notes as optional or variant semantics rather than unconditional base-medium ingredients.
5. Refresh `mediaingredientmech_chebi_term` on the normalized sources after regrounding so `MgSO4 x 7 H2O` consistently uses `CHEBI:31795`.

## Follow-up Checks
After source normalization and merge regeneration, re-run LinkML schema validation, strict validation, reference validation, term validation, and an exact duplicate search with ignored files included for `TOGO:M2728`, `TOGO:M2730`, `mediadive.medium:671`, `komodo.medium:671`, and `DSMZ_Medium671`.

Confirm that the generated canonical DSMZ 671 record has one main water basis, no top-level duplicate contribution from stock waters, nested stock additions for the mineral and vitamin stocks, and no inflated milligram-to-gram vitamin or trace-metal concentrations.

## Additional Notes
Exact duplicate-source searches included ignored files.
