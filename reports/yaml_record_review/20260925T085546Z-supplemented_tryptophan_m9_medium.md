# YAML Record Review: supplemented_tryptophan_m9_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/supplemented_tryptophan_m9_medium.yaml`
- Started UTC: 2026-09-25T08:54:30Z
- Finished UTC: 2026-09-25T08:55:47Z
- Verdict: needs curation

## Target

Generated merged record `CultureMech:001561` for
`supplemented_tryptophan_m9_medium`, with `mediadive.medium:451`, fingerprint
`473e40eb74603ec7dfb3f4f1366b9f51b9046d021b7565ecabd007592fefa0d4`, and one
merged source, `supplemented_tryptophan_m9_medium`.

## Validation

- LinkML schema: passed.
- Strict validator: passed with 0 ERROR rows.
- Reference validator: passed with 0 checks.
- Term validator: passed.
- Embedded `curation_history`: Not checked: the available history validator checks
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The record is correctly grounded to DSMZ/MediaDive medium 451, named
`SUPPLEMENTED (TRYPTOPHAN) M9 MEDIUM`, at pH 7.4. DSMZ medium 451 is a
derivative of DSMZ medium 382; the current DSMZ 451 PDF states only that
20 mg/l tryptophan should be added to medium 382.

MediaDive expands medium 451 into the M9 base plus two added amino acids:
20 mg proline and 20 mg/l tryptophan. The current DSMZ 451 PDF supports the
tryptophan addition but did not support the proline addition, so this ingredient
needs source reconciliation before it is treated as current DSMZ evidence.

## Evidence

MediaDive 451 lists `Main sol. 451`, with 100 ml of `10 x M9 salts (per l)`,
1 ml of 1 M MgSO4, 1 ml of 0.1 M CaCl2, 1 ml of filter-sterilized 1 M
thiamine-HCl x 2 H2O, 10 ml of 20% glucose, 20 mg proline, 20 mg/l tryptophan,
and 900 ml distilled water.

MediaDive 451 also embeds stock solution 5541, `10 x M9 salts (per l)`, as
Na2HPO4 60 g, KH2PO4 30 g, NH4Cl 10 g, and NaCl 5 g per liter of stock.
Because only 100 ml of this 10x stock is added per final liter, those four
ingredients contribute one tenth of the stock recipe to the finished medium.

DSMZ medium 382, the base recipe referenced by the DSMZ 451 PDF, independently
prints the same 100 ml 10x M9 salts addition, MgSO4, CaCl2, thiamine, glucose,
900 ml water, separate sterilization instructions, pH 7.4, and 10x M9 salts
stock recipe.

## Completeness

The generated YAML includes the M9 base compounds, glucose, proline, and
tryptophan, but the four M9 salts from the 10x stock are present at stock
strength rather than final strength. If the record flattens stock recipes, the
expected final concentrations are Na2HPO4 6 g/l, KH2PO4 3 g/l, NH4Cl 1 g/l,
and NaCl 0.5 g/l.

The generated record does not preserve the nested 10x M9 stock identity or the
fact that 100 ml is used per final liter. This loses the source preparation
structure that explains the final salt concentrations.

## Findings

- `Na2HPO4`, `KH2PO4`, `NH4Cl`, and `NaCl` are tenfold too high in the flattened
  generated recipe because the importer copied the 10x stock's per-liter values
  instead of scaling the 100 ml stock addition into a final liter.
- `Proline` is present at 0.02 g/l in the MediaDive expansion and generated YAML,
  but the current DSMZ 451 PDF says to add only tryptophan to DSMZ medium 382.
  This mismatch needs reconciliation against a MediaDive or DSMZ change history
  before proline is retained.
- The generated record has only flat ingredient rows and therefore loses the
  DSMZ/MediaDive stock-solution boundary around `10 x M9 salts (per l)`.

## Recommended Edits

- Fix the MediaDive import or normalization path for stock additions so the
  10x M9 salts are either modeled as `100 ml` of solution 5541 or flattened to
  final onefold amounts: `Na2HPO4` 6 g/l, `KH2PO4` 3 g/l, `NH4Cl` 1 g/l, and
  `NaCl` 0.5 g/l.
- Reconcile the generated `Proline` row with current DSMZ medium 451. If
  MediaDive intentionally stores a historical DSMZ version, add an evidence note;
  otherwise remove proline from the tryptophan variant and keep it only on the
  arginine/proline recipe that explicitly supports it.
- Preserve the DSMZ 382 relationship as provenance for this derivative instead
  of making medium 451 look like a standalone fully printed recipe.

## Follow-up Checks

- After the salt scaling fix, verify that the M9 salt masses are not the 10x
  stock values from MediaDive solution 5541.
- Re-fetch `DSMZ_Medium451.pdf` and confirm whether it still instructs curators
  to add only tryptophan to DSMZ medium 382.
- Revalidate the generated merge after the normalized DSMZ/MediaDive source is
  repaired.

## Additional Notes

None found
