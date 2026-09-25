# YAML Record Review: HS medium-methanol-acetate medium (125 and 40 mM, respectively)
- Repository: CultureMech
- Record: data/merge_yaml/merged/hs_medium_methanol_acetate_medium_125_and_40_mm_respectively.yaml
- Started UTC: 2026-09-23T12:45:58Z
- Finished UTC: 2026-09-23T12:47:00Z
- Verdict: needs curation

## Target

Reviewed the generated TOGO branch for TOGO Medium M2643, `HS medium-methanol-acetate medium (125 and 40 mM, respectively)`, at `data/merge_yaml/merged/hs_medium_methanol_acetate_medium_125_and_40_mm_respectively.yaml`. The maintained source is `data/normalized_yaml/bacterial/hs_medium_methanol_acetate_medium_125_and_40_mm_respectively.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/hs_medium_methanol_acetate_medium_125_and_40_mm_respectively.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record ID, label, and `TOGO:M2643` grounding all identify TOGO's HS medium-methanol-acetate medium. This is not the same source record as MediaDB 472: it explicitly defines a 1 L `HS medium` base plus 125 mM methanol and 40 mM acetate, and then expands the `HS medium` base in a separate paragraph.

## Evidence

TOGO M2643 lists a top-level 125 mM methanol row, a 40 mM acetate row, and 1 L of `HS medium`. It then defines `HS medium` as 1 L distilled water, 0.4 M NaCl, 5 mM KH2PO4, 19 mM NH4Cl, 4 uM resazurin, 54 mM MgCl2 x 6 H2O, 0.4 mM Na2S x 9 H2O, 13 mM KCl, 45 mM NaHCO3, 2 mM CaCl2, and 2.8 mM cysteine-HCl. The source comment says Methanosarcina species were grown as single cells in this medium at 35 C and cites Appl. Environ. Microbiol. 59:3832-3839 (1993).

The generated record faithfully carries methanol, acetate, and each explicit HS-medium molar concentration. It imports the 1 L `HS medium` parent and the 1 L distilled-water row as `1 G_PER_L` ingredients, losing the inline base-medium boundary and the source volume unit.

## Completeness

The record has no preparation steps, pH, source URL, or structured target-organism entries. The empty pH and preparation slots are acceptable because TOGO M2643 did not provide those details, but the source comment is consequential growth context and needs a follow-up check against the 1993 paper before being promoted into organism/growth evidence.

## Findings

- **major**: The 1 L `HS medium` base is represented as an ungrounded `1 G_PER_L` ingredient instead of a nested 1 L base-medium solution.
- **major**: The 1 L distilled-water row inside the HS-medium base is represented as `1 G_PER_L` instead of a liter or 1000 ml of water.
- **major**: The nested paragraph boundary between methanol/acetate additions and the HS-medium base is flattened away.
- **minor**: `cysteine . HCl` remains ungrounded even though the TOGO source labels it as L-cysteine hydrochloride.
- **minor**: The TOGO comment about Methanosarcina growth at 35 C is not represented as a scoped target-organism or growth-evidence item.

## Recommended Edits

- In `data/normalized_yaml/bacterial/hs_medium_methanol_acetate_medium_125_and_40_mm_respectively.yaml`, remodel the 1 L `HS medium` row as a nested solution or parent-medium reference rather than an ingredient measured in grams.
- Preserve the TOGO subcomponent boundary so the HS base components stay grouped under the HS-medium solution.
- Change the nested `Distilled Water` row from `1 G_PER_L` to an explicit 1 L or 1000 ml water volume.
- Ground `cysteine . HCl` to the exact L-cysteine hydrochloride term after verifying the intended hydrate/salt state.
- Inspect Appl. Environ. Microbiol. 59:3832-3839 (1993) before adding any target-organism or growth-condition entries from the TOGO comment.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Re-open TOGO M2643 to confirm methanol, acetate, HS-medium, water, and HS-base concentrations after the nested representation is regenerated.
- Run the repository's merge freshness audit after regenerating the merged artifact.

## Additional Notes

None.
