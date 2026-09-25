# YAML Record Review: myxococcus_flavescens_medium__aa6b37a2

- Repository: CultureMech
- Record: data/merge_yaml/merged/myxococcus_flavescens_medium__aa6b37a2.yaml
- Started UTC: 2026-09-24T16:15:25Z
- Finished UTC: 2026-09-24T16:16:24Z
- Verdict: needs curation

## Target

Reviewed the generated MediaRecipe `CultureMech:002416` for
`myxococcus_flavescens_medium`, a JCM Medium J124 record grounded to
`mediadive.medium:J124`.

## Validation

Focused validation passed:

- LinkML `MediaRecipe` validation: passed; no issues found.
- Strict validation: passed with zero error rows in `/private/tmp/myxococcus_flavescens_medium__aa6b37a2.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The direct JCM identity is correct. The live JCM `GRMD=124` page is
`MYXOCOCCUS FLAVESCENS MEDIUM` and matches `mediadive.medium:J124`.

An exact ignored-inclusive search across `data/normalized_yaml`,
`data/merge_yaml/merged`, and top-level `data/*.tsv` files found an active TOGO
M116 owner, `CultureMech:007694`, for the same JCM `GRMD=124` source. The
generated TOGO record exists separately as
`data/merge_yaml/merged/MYXOCOCCUS_FLAVESCENS_MEDIUM.yaml`; it is not linked to
the direct JCM owner under review.

## Evidence

JCM `GRMD=124` lists:

- 1 g yeast extract
- 1 g raffinose
- 1 g sucrose
- 1 g galactose
- 5 g soluble starch
- 2.5 g Casitone (BD-Difco)
- 0.5 g MgSO4 x 7H2O
- 0.25 g K2HPO4
- 15 g agar
- 1 L distilled water

The JCM page also says to adjust pH to 6.0-6.5 and, unless otherwise stated, to
autoclave media at 121 C for 15 minutes. The live TOGO `M116` API mirrors the
same JCM `M124` formula and pH comment.

## Completeness

The generated direct JCM record preserves the nine dry ingredients and the pH
adjustment, but it is missing the source `Distilled water` row and the default
JCM autoclaving instruction.

The active TOGO duplicate contains all ten ingredient names, including
`Distilled water`, but imports JCM's 1 L water volume as `1 G_PER_L`. The two
active owners are not connected as source duplicates even though they cite the
same `GRMD=124` source.

## Findings

1. The direct JCM owner and generated record omit JCM's 1 L `Distilled water`
   row.

2. The generated record represents the pH range only as `ph_value: 6.2` plus a
   preparation step instead of storing pH 6.0-6.5 as a structured range.

3. The default JCM autoclaving instruction, 121 C for 15 minutes unless
   otherwise stated, is missing from the direct JCM generated record.

4. The active TOGO M116 owner represents the same JCM source but remains
   unlinked and generated separately.

5. The TOGO duplicate has its own water-unit defect: it models the source 1 L
   distilled water addition as `1 G_PER_L`.

## Recommended Edits

Repair both normalized owners and merge their source identity:

- Add `Distilled water`, 1 L, to
  `data/normalized_yaml/bacterial/myxococcus_flavescens_medium.yaml`.
- Correct the TOGO M116 `Distilled water` row from `1 G_PER_L` to a 1 L water
  addition.
- Represent pH 6.0-6.5 as a structured `ph_range`.
- Add the default JCM autoclave step where JCM does not override it.
- Link the direct JCM and TOGO M116 records as source duplicates so a
  regenerated merge does not leave two independent Myxococcus Flavescens
  Medium records.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged` and confirm JCM J124 and TOGO M116 collapse
  or link as source duplicates.
- Confirm the regenerated record contains all ten source ingredient rows,
  including 1 L distilled water.
- Re-run LinkML, strict, reference, and term validation on the regenerated
  record.

## Additional Notes

None found.
