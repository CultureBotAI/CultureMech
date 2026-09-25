# YAML Record Review: persephonella_medium__fd71a565

- Repository: CultureMech
- Record: data/merge_yaml/merged/persephonella_medium__fd71a565.yaml
- Started UTC: 2026-09-24T20:32:20Z
- Finished UTC: 2026-09-24T20:32:20Z
- Verdict: needs curation

## Target

Generated bacterial MediaRecipe `CultureMech:002181`, `persephonella_medium`, from the maintained direct DSMZ/MediaDive owner `data/normalized_yaml/bacterial/persephonella_medium.yaml`.

The record represents DSMZ / MediaDive medium 996, PERSEPHONELLA MEDIUM. It has the main salts, pH 6.0, defined-medium classification, DSMZ preparation text, and trace-element salts flattened as top-level ingredients.

## Validation

- Open LinkML validation: Passed with no issues.
- Strict validator: Passed; `/private/tmp/persephonella_medium__fd71a565.strict.tsv` was header-only, so there were 0 strict errors.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The direct DSMZ/MediaDive identity is internally consistent: `mediadive.medium:996` names PERSEPHONELLA MEDIUM and links to the same DSMZ medium 996 PDF named by the maintained owner.

An exact ignored-inclusive search also found the TOGO M2284 owner, `data/normalized_yaml/bacterial/TOGO_M2284_Persephonella_Medium.yaml`, and its generated sibling `data/merge_yaml/merged/persephonella_medium__849ec992.yaml`. TOGO M2284 points to the same DSMZ medium 996 PDF and should be reconciled with this direct owner after the stock-solution structure is repaired.

## Evidence

MediaDive medium 996 and the linked DSMZ medium 996 PDF both list 10 ml `Trace element solution` plus 990 ml distilled water in the final medium, not individual trace-metal salts in the final medium.

Both sources then define the trace-element stock as a separate 1 L solution with Na-EDTA, CoCl2, MnCl2, FeSO4, ZnCl2, AlCl3, Na2O4W, CuCl, NiSO4, H2SeO3, H3BO3, Na2MoO4, and a separate 1000 ml distilled water row. The direct CultureMech owner flattens those stock rows into the final ingredient list and drops both source water rows.

The direct owner correctly preserves pH 6.0, defined-medium classification, and the DSMZ preparation text for anoxic CO2 handling, O2 addition, H2 pressurization, and incubation.

## Completeness

The record preserves source identity, main non-water ingredients, pH, and preparation text, but the stock-solution structure is incomplete. The final-medium recipe is missing both the 10 ml stock addition and 990 ml water, and the trace-element stock is missing its own 1000 ml water.

The direct record is also split from the TOGO M2284 representation of the same DSMZ medium 996 recipe.

## Findings

1. Needs curation: the generated record omits the final-medium `Trace element solution` 10 ml addition and 990 ml `Distilled water` row from DSMZ / MediaDive medium 996.
2. Needs curation: the trace-element stock composition is flattened into the final ingredient list. Na-EDTA, CoCl2, MnCl2, FeSO4, ZnCl2, AlCl3, Na2O4W, CuCl, NiSO4, H2SeO3, H3BO3, and Na2MoO4 belong to a separate 1 L stock solution with its own water row and pH-adjustment step.
3. Needs curation: this direct DSMZ 996 generated record is split from the TOGO M2284 generated sibling; both need stock-solution scoping repairs before they can be reconciled.
4. Needs curation: several trace-element formulas or groundings should be reviewed while the stock is repaired, especially ungrounded `Na2O4W x 2 H2O` and generic nickel sulfate grounding for `NiSO4 x 6 H2O`.

## Recommended Edits

1. Keep the final-medium ingredient list to the DSMZ main solution and add `Trace element solution` as a 10 ml volume addition plus the 990 ml distilled water row.
2. Move the trace-element salts into a populated `Trace element solution` with its own 1000 ml distilled water row.
3. Preserve the trace-stock pH 3 instruction on that stock and keep the final anoxic/gas preparation instructions on the final medium.
4. Repair trace-element formula/grounding details while preserving source labels where needed.
5. Reconcile and regenerate the direct DSMZ 996 and TOGO M2284 owners so the same DSMZ medium is no longer split into two generated records.

## Follow-up Checks

1. Re-run open, strict, reference, and term validation on the repaired maintained owners and regenerated merged record.
2. Repeat an exact ignored-inclusive search for `mediadive.medium:996`, `TOGO:M2284`, `DSMZ_Medium996`, and both Persephonella owners after regeneration to confirm DSMZ medium 996 has the intended representation.

## Additional Notes

The exact ignored-inclusive duplicate search covered `data`, `src`, and `scripts` for `TOGO:M2284`, `M2284`, `DSMZ_Medium996`, `CultureMech:008870`, and `Persephonella_Medium`.
