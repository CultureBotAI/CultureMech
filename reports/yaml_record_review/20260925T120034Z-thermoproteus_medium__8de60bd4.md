# YAML Record Review: thermoproteus_medium__8de60bd4

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoproteus_medium__8de60bd4.yaml
- Started UTC: 2026-09-25T12:00:34Z
- Finished UTC: 2026-09-25T12:00:34Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:009231`, `thermoproteus_medium`, generated from TOGO Medium M2676 and ultimately sourced from DSMZ Medium 185.

## Validation

- LinkML schema: Passed with `linkml-validate`; no issues found.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermoproteus_medium__8de60bd4.strict.tsv` contained only the header.
- Reference validation: Passed; the validator ran 0 checks for this record.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

TOGO M2676 is grounded to DSMZ Medium 185, "THERMOPROTEUS MEDIUM". The same DSMZ 185 source is also present as a direct MediaDive import in `thermoproteus_medium__ec4b4683.yaml`.

## Evidence

- DSMZ 185 lists a main recipe containing 1 ml Trace elements solution, yeast extract, soluble starch, powdered sulfur, Na2S x 9H2O, 1 mg resazurin, and 1000 ml distilled water.
- DSMZ 185 defines a separate 1 L Trace elements solution with NaF 840 mg, MnCl2 x 4 H2O 180 mg, Na2B4O7 x 10 H2O 450 mg, ZnSO4 x 7 H2O 22 mg, CuCl2 x 2 H2O 5 mg, Na2MoO4 x 2 H2O 3 mg, CoSO4 x 7 H2O 1 mg, and distilled water.
- DSMZ 185 prepares the medium without starch, sodium sulfide, and sulfur under N2, adjusts to pH 5.5 with H2SO4, tyndallises medium in sulfur-containing tubes, and adds starch and sodium sulfide before use.

## Completeness

The generated record contains all named source ingredients but flattens the Trace elements solution into the top-level medium. It also merges main and stock water, converts milligram rows as if they were gram rows, and omits DSMZ preparation.

## Findings

- `Distilled water` 2000 G_PER_L merges the 1000 ml main water row with the 1000 ml Trace elements solution water row.
- The 1 ml Trace elements solution addition is recorded as a `solutions` entry with 1 G_PER_L and the name `Unknown solution`.
- `Resazurin` 1 G_PER_L copies a 1 mg/L source row as grams per liter.
- Trace-element milligram values are emitted as gram-scale concentrations: for example `NaF` 840 G_PER_L, `MnCl2 x 4 H2O` 180 G_PER_L, and `Na2B4O7 x 10 H2O` 450 G_PER_L.
- `N2 gas` and `H2SO4 solution` appear as variable solute-like entries rather than anaerobic handling and pH-adjustment reagents.
- The preparation steps from DSMZ 185 are absent.

## Recommended Edits

- Prefer repairing and merging into the direct DSMZ 185 record instead of retaining this TOGO duplicate independently.
- Restore Trace elements solution as a separate stock with a 1 ml/L addition.
- Split main water from stock water and fix all mg-to-G_PER_L conversions.
- Add pH 5.5 and preparation steps for N2 preparation, H2SO4 adjustment, tyndallisation with sulfur, and pre-use starch/sodium sulfide addition.

## Follow-up Checks

- Compare this TOGO M2676 record with `thermoproteus_medium__ec4b4683.yaml` after both have water and stock scoping.
- Decide whether `high_metal: true` belongs on this record after the trace stock is no longer flattened into top-level final concentrations.

## Additional Notes

No target-organism evidence was reviewed. The exact source search included ignored and hidden files and found TOGO M2676, the direct DSMZ 185 record, and a KOMODO/DSMZ 185 record.
