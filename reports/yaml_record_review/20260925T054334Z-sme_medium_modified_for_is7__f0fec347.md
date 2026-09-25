# YAML Record Review: sme_medium_modified_for_is7__f0fec347

- Repository: CultureMech
- Record: data/merge_yaml/merged/sme_medium_modified_for_is7__f0fec347.yaml
- Started UTC: 2026-09-25T05:43:34Z
- Finished UTC: 2026-09-25T05:43:34Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002054`, `sme_medium_modified_for_is7`, from `data/merge_yaml/merged/sme_medium_modified_for_is7__f0fec347.yaml`.

The target record merges DSMZ medium 891, `SME MEDIUM MODIFIED FOR IS7`, with DSMZ medium 783, `HYDROGENOTHERMUS HIRSCHII MEDIUM`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is not cleanly grounded to one source formulation.

DSMZ 891 and DSMZ 783 share the Modified Wolin's mineral solution II stock but have different parent recipes and different handling instructions.

DSMZ 891 has 30 g/L parent NaCl, NaHCO3 from a separately autoclaved neutralized stock, a final H2/CO2/O2 atmosphere, and 70 C incubation.

DSMZ 783 lacks the 30 g/L NaCl parent row, adds 100 ul sterile 10% CaCO3 before use, adds 20 ml filter-sterilized air, and incubates at 60 C under shaking.

## Evidence

DSMZ medium 891 defines a parent medium with basal salts, 10 ml Modified Wolin's mineral solution II, powdered sulfur, distilled water to 1000 ml, separately added NaHCO3, pH 7.0, and H2/CO2/O2 at 78/20/2 with two atmospheres of overpressure.

DSMZ medium 783 defines a parent medium with MgSO4 x 7H2O, MgCl2 x 6H2O, KCl, NaBr, NaHCO3, NH4Cl, K2HPO4, CaCl2 x 2H2O, 10 ml Modified Wolin's mineral solution II, powdered sulfur, distilled water to 1000 ml, 100 ul of 10% sterile CaCO3 before use, H2/CO2, 20 ml filter-sterilized air, and 60 C incubation.

MediaDive resolves the DSMZ `Trace element solution (see medium 141)` cross-reference in both records to a 1 L Modified Wolin's mineral solution II stock.

## Completeness

The generated record flattens Modified Wolin's mineral solution II into the parent ingredient list.

Same-named MgSO4 x 7H2O and CaCl2 x 2H2O rows were summed across parent and stock scopes.

The required 10 ml/L Modified Wolin's mineral solution II row is absent.

The required 1000 ml/L parent and stock distilled-water rows are absent.

The generated record merges DSMZ 891 with DSMZ 783 even though DSMZ 891 has a 30 g/L NaCl parent row and DSMZ 783 does not.

The generated record loses the DSMZ 783 CaCO3, filter-sterilized air, and 60 C shaking conditions while also losing DSMZ 891's 70 C condition.

## Findings

The Modified Wolin's mineral solution II subrecipe was flattened into final-medium ingredients.

Duplicate cleanup summed salts from incompatible source scopes.

DSMZ 891 and DSMZ 783 were falsely merged into one canonical record.

Source-specific gas, additive, and incubation instructions were lost in the merge.

## Recommended Edits

Keep DSMZ 891 and DSMZ 783 as separate parent records or model DSMZ 783 as a clearly named variant if a curator intentionally wants it under the same family.

Represent Modified Wolin's mineral solution II as a 10 ml/L addition rather than flattening the stock into either parent.

Keep stock components and the stock 1000 ml water scoped under Modified Wolin's mineral solution II.

Restore 1000 ml/L parent distilled water for each parent medium.

Preserve DSMZ 891's NaCl, NaHCO3, H2/CO2/O2, and 70 C details only on DSMZ 891.

Preserve DSMZ 783's CaCO3, H2/CO2 plus air, and 60 C shaking details only on DSMZ 783.

Regenerate the merged YAML after repairing both normalized source branches.

## Follow-up Checks

Confirm the regenerated DSMZ 891 record no longer lists Modified Wolin's salts as parent ingredients.

Confirm the regenerated DSMZ 783 record exists separately or as an explicit variant and no longer disappears under the DSMZ 891 canonical record.

Confirm no parent record has summed 10 g/L MgSO4 x 7H2O or 0.6 g/L CaCl2 x 2H2O rows created by crossing stock and parent scopes.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
