# YAML Record Review: spirochaeta_medium__e024fce6

- Repository: CultureMech
- Record: data/merge_yaml/merged/spirochaeta_medium__e024fce6.yaml
- Started UTC: 2026-09-25T06:15:58Z
- Finished UTC: 2026-09-25T06:17:28Z
- Verdict: needs curation

## Target

Generated merged YAML for JCM 852, SPIROCHAETA MEDIUM.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/spirochaeta_medium__e024fce6.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The record is grounded to the correct JCM 852, SPIROCHAETA MEDIUM, source and preserves the pH 7.5 liquid-medium identity.

The generated ingredient list partially normalizes the base recipe against the final 1004 ml volume, but it also flattens three 1 L stock recipes into the parent ingredient list at their undiluted concentrations.

## Evidence

JCM 852 lists KH2PO4, MgCl2 x 6 H2O, CaCl2 x 2 H2O, NH4Cl, NaCl, yeast extract, sucrose, maltose, 2.0 ml vitamin solution, 1.0 ml trace mineral solution, 1.0 ml Se/W solution, NaHCO3, 1.0 mg resazurin, L-cysteine HCl x H2O, Na2S x 9 H2O, and 1.0 L distilled water in the parent table.

The trace mineral solution is a separate 1.0 L stock with FeCl2 x 4 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, ZnCl2, CuCl2 x 2 H2O, H3BO3, Na2MoO4 x 2 H2O, NiCl2 x 6 H2O, AlCl3, and distilled water. The Se/W solution is a separate 1.0 L stock with Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, and distilled water. The vitamin solution is a separate 1.0 L stock with 10 vitamin and growth-factor rows.

JCM 852 directs dissolving all compounds except Na2S x 9 H2O and L-cysteine HCl x H2O, adjusting the pH to 7.5, dispensing 19 ml into vials, purging with N2-CO2 (80:20), autoclaving, and then adding filter-sterilized Na2S x 9 H2O and L-cysteine HCl x H2O as reducing agents.

## Completeness

The generated record omits the explicit 1.0 L parent distilled-water row, all three named stock-addition rows, and every distilled-water row inside the trace mineral, Se/W, and vitamin stocks. It also leaves the reducing agents as ordinary parent ingredients even though the JCM instructions add them after autoclaving from filter-sterilized solution.

## Findings

- Major: the 2.0 ml vitamin solution, 1.0 ml trace mineral solution, and 1.0 ml Se/W solution additions are not represented as named solution additions.
- Major: stock contents are flattened into the parent ingredient list at undiluted stock concentrations instead of nested under the vitamin, trace mineral, and Se/W solutions.
- Major: L-cysteine HCl x H2O and Na2S x 9 H2O are direct parent rows even though JCM 852 instructs adding them after autoclaving as filter-sterilized reducing agents.
- Major: the 1.0 L parent distilled water and the 1.0 L distilled-water rows from each stock solution are missing.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/spirochaeta_medium.yaml` to model vitamin solution, trace mineral solution, and Se/W solution as 2.0 ml, 1.0 ml, and 1.0 ml final-medium additions.
- Move the trace mineral, Se/W, and vitamin component rows under their named stock solutions, preserving each stock's 1.0 L distilled-water row.
- Preserve the parent 1.0 L distilled-water row and the pH 7.5 vial-culture preparation instructions.
- Model Na2S x 9 H2O and L-cysteine HCl x H2O as post-autoclave filter-sterilized reducing-agent additions or annotate that timing explicitly.
- Regenerate `data/merge_yaml/merged/spirochaeta_medium__e024fce6.yaml` from the repaired normalized record.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated record.
- Confirm the regenerated parent ingredient list no longer contains undiluted vitamin, trace mineral, or Se/W stock rows.
- Confirm the three named stock additions are present with source milliliter amounts.
- Confirm pH 7.5 and the N2-CO2 vial-culture preparation survive regeneration.

## Additional Notes

None found.
