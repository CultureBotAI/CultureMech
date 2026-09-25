# YAML Record Review: HEPES Peptone-Yeast Extract Medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/hepes_peptone_yeast_extract_medium.yaml
- Started UTC: 2026-09-23T11:52:14Z
- Finished UTC: 2026-09-23T11:52:59Z
- Verdict: needs curation

## Target

Reviewed the generated Togo M791 branch for JCM 764, `HEPES Peptone-Yeast Extract Medium`, at `data/merge_yaml/merged/hepes_peptone_yeast_extract_medium.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/hepes_peptone_yeast_extract_medium.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is grounded to `TOGO:M791`, which imports `JCM_M764`. JCM Medium 764 is the expected HEPES Peptone-Yeast Extract Medium. An exact `find` under `data/merge_yaml/merged` found a second generated `hepes_peptone_yeast_extract_medium__6c26a920.yaml` branch for the direct JCM import.

## Evidence

JCM 764 lists a one-liter main medium with 1 L distilled water, 2.38 g HEPES, 30.0 g NaCl, 2.7 g magnesium sulfate heptahydrate, 4.3 g magnesium chloride hexahydrate, 0.25 g NH4Cl, 0.5 g KCl, 0.14 g calcium chloride dihydrate, 0.14 g K2HPO4, 2.0 g Bacto peptone, 0.2 g yeast extract, 1 ml trace elements from Togo M631, and 1 ml of a 0.2% ferrous ammonium sulfate solution in 0.037% HCl. It then says to adjust to pH 7.25, autoclave, cool, and add 10 ml filter-sterilized trace vitamins from Togo M190.

The generated record imports the gram rows correctly. It converts 1 L distilled water into `1 G_PER_L`, converts the 1 ml ferrous ammonium sulfate solution into `1 G_PER_L`, converts the 1 ml trace-elements and 10 ml trace-vitamins cross-references into empty solution stubs with `G_PER_L` units, and omits the pH and preparation instructions.

## Completeness

The base salt, HEPES, peptone, and yeast-extract masses are present. The record is incomplete for cross-referenced stock recipes, post-autoclave vitamin addition, water volume, pH, and ordered preparation.

## Findings

- The solvent row is nonsensical: JCM lists 1 L distilled water, not `1 G_PER_L` water.
- The 1 ml ferrous ammonium sulfate/HCl solution is treated as a 1 g/L ingredient instead of a solution addition.
- `Trace elements (see Medium [M631])` and `Trace vitamins (see Medium [M190])` were migrated to empty `solutions` entries with default `Unknown solution` names.
- The trace-vitamins addition is post-autoclave and filter-sterilized, but there are no preparation steps to preserve that timing.
- The pH 7.25 adjustment is missing.
- The Togo and direct JCM branches for the same JCM 764 recipe remain as separate generated records.

## Recommended Edits

- Curate the Togo M791 normalized source to represent 1 L distilled water as volume and to keep the ferrous ammonium sulfate, trace-element, and trace-vitamin rows as volume additions to defined cross-referenced solutions.
- Resolve or link the M631 and M190 solution recipes instead of generating empty solution stubs.
- Add ordered preparation steps for pH 7.25 adjustment, autoclaving, cooling, and filter-sterilized vitamin addition.
- Merge or alias the Togo M791 branch with the direct JCM 764 branch after both are corrected.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated artifact.
- Confirm the regenerated record has no `G_PER_L` concentration for the 1 L water row or the 1 ml and 10 ml solution additions.

## Additional Notes

None.
