# YAML Record Review: spiribacter_medium_830_12_marine_salts

- Repository: CultureMech
- Record: data/merge_yaml/merged/spiribacter_medium_830_12_marine_salts.yaml
- Started UTC: 2026-09-25T06:09:15Z
- Finished UTC: 2026-09-25T06:10:27Z
- Verdict: needs curation

## Target

Generated merged YAML for DSMZ 1537, SPIRIBACTER MEDIUM (830 + 12% Marine salts).

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/spiribacter_medium_830_12_marine_salts.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

DSMZ 1537 is represented with the correct pH range, solid-agar state, R2A Broth amount, agar amount, NaHCO3 amount, and marine-salt component amounts.

The stock hierarchy is not correct: `Marine Salts 12%` is a named 1000 ml solution in the final medium, and NaHCO3 is added from a sterile stock before inoculation.

## Evidence

DSMZ 1537 and MediaDive 1537 list 3.0 g R2A Broth, 1000.0 ml Marine Salts 12%, and 20.0 g agar in the parent recipe at pH 7.0-7.2. They then direct sterilizing by autoclaving and adding 0.71 g NaHCO3 from a sterile stock before inoculation.

The Marine Salts 12% solution is a separate 1000 ml stock containing 78.57 g NaCl, 15.37 g MgCl2 x 6 H2O, 19.37 g MgSO4 x 7 H2O, 2.06 g KCl, 4.00 g CaCl2 x 2 H2O, and 1000.0 ml distilled water.

## Completeness

The generated record omits the explicit 1000 ml Marine Salts 12% addition and the distilled-water row in that stock solution. It also leaves NaHCO3 as a direct ingredient rather than preserving that it is added before inoculation from a sterile stock.

## Findings

- Major: `Marine Salts 12%` is flattened into the parent ingredient list, so the final recipe no longer records that the salts are supplied as 1000 ml of a named stock solution.
- Major: the 1000 ml distilled-water row for Marine Salts 12% is missing.
- Major: NaHCO3 is listed as a direct final ingredient even though the source adds it from sterile stock solutions before inoculation.

## Recommended Edits

- Repair `data/normalized_yaml/specialized/spiribacter_medium_830_12_marine_salts.yaml` to model `Marine Salts 12%` as a 1000 ml final-medium solution addition with the five salts and 1000 ml distilled water in its composition.
- Preserve NaHCO3 as a sterile stock addition before inoculation, or add notes that make that stock-addition timing explicit.
- Regenerate `data/merge_yaml/merged/spiribacter_medium_830_12_marine_salts.yaml` from the repaired normalized record.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated record.
- Confirm the regenerated record has an explicit `Marine Salts 12%` solution and no missing water for that stock.
- Confirm the pH range remains 7.0-7.2.

## Additional Notes

None found.
