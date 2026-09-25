# YAML Record Review: desulfamplus_medium__9fe31284

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfamplus_medium__9fe31284.yaml`
- Started UTC: 2026-09-22T17:33:26Z
- Finished UTC: 2026-09-22T17:33:26Z
- Verdict: needs curation

## Target

Generated bacterial `desulfamplus_medium` record for TOGO M964, linked to JCM Medium 918.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to TOGO M964 and keeps the JCM GRMD 918 URL in `notes`.

The complex/undefined classification is supported by yeast extract.

The live JCM GRMD 918 page has drifted from the TOGO import: the current page points Modified Wolfe's mineral solution and Vitamin solution to JCM Medium 915, while the generated record still carries TOGO's M961 references.

## Evidence

JCM 918 lists basal salts, HEPES, fumarate, yeast extract, 0.4 mg Resazurin, and 1 L water before autoclaving, then adds 1.8 ml 0.5 M potassium phosphate buffer, 0.5 ml Vitamin solution, 2.35 ml 8% NaHCO3, 8 ml 5% L-Cysteine-HCl-H2O, and optional 10 ml 0.01 M FeSO4-5H2O in 0.02 N HCl per liter.

All five post-autoclave stock additions became empty `solutions` placeholders with `G_PER_L` concentrations: Modified Wolfe at `5 G_PER_L`, 8% NaHCO3 at `2.35 G_PER_L`, 5% cysteine at `8 G_PER_L`, optional FeSO4 at `10 G_PER_L`, and Vitamin solution at `0.5 G_PER_L`.

The source 0.4 mg Resazurin row was imported as `0.4 G_PER_L`. The source 1 L water row was imported as `1 G_PER_L`.

The generated top-level `0.5 M Potassium phosphate buffer (pH 7.0)` row represents 1.8 ml stock addition as `1.8 G_PER_L` and loses the molarity as structured information.

NaOH, N2, and HCl are carried as variable-concentration ingredients even though they appear only in pH adjustment, anaerobic dispensing, and final readjustment instructions.

## Completeness

The generated record lacks JCM's preparation steps entirely: adjustment to pH 7.0 with NaOH, N2 dispensing before autoclaving, anaerobic post-autoclave stock additions, final pH 7.2-7.5 readjustment, colorless-resazurin inoculation condition, and the optional FeSO4 note for magnetosome formation.

The five stock solution records have empty compositions and stale cross-references for the two JCM-defined external stocks.

## Findings

- Needs curation: all five milliliter stock additions are encoded as gram-per-liter amounts.
- Needs curation: the Resazurin milligram row and the water litre row have wrong `G_PER_L` units.
- Needs curation: Modified Wolfe's mineral solution and Vitamin solution point to stale JCM Medium 961 rather than the current Medium 915 references.
- Needs curation: all generated solution records are empty.
- Needs curation: NaOH, N2, and HCl are modeled as ingredients instead of pH and anaerobic preparation conditions.
- Needs curation: the optional FeSO4 stock is not represented as optional.
- Needs curation: preparation steps and pH 7.2-7.5 are missing.

## Recommended Edits

- Refresh `data/normalized_yaml/bacterial/TOGO_M964_Desulfamplus_Medium.yaml` from live JCM GRMD 918 before regenerating.
- Replace M961 stock references with the current JCM Medium 915 references.
- Model Modified Wolfe's mineral solution, Vitamin solution, 8% NaHCO3, 5% L-Cysteine-HCl-H2O, 0.01 M FeSO4-5H2O, and 0.5 M potassium phosphate buffer as stock additions rather than `G_PER_L` placeholders.
- Preserve the optional status of the FeSO4 stock.
- Correct Resazurin and water units.
- Move NaOH, N2, and HCl into preparation or condition fields, along with pH 7.2-7.5 and the colorless-medium inoculation check.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after regeneration.
- Recheck generated stock references against the live JCM GRMD 918 page.
- Confirm no milliliter addition is emitted as `G_PER_L`.
- Confirm the optional FeSO4 stock stays optional.

## Additional Notes

TOGO M964 and JCM GRMD 918 were both reachable during review.
