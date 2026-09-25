# YAML Record Review: modified_w_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_w_medium.yaml
- Started UTC: 2026-09-24T13:46:22Z
- Finished UTC: 2026-09-24T13:47:00Z
- Verdict: needs curation

## Target

Reviewed merged generated record `CultureMech:008507`, `modified_w_medium`, a TOGO-imported `Modified W-medium` record grounded to TOGO `M1929` and NBRC `M1196`.

## Validation

The generated record passed the focused open schema validator, which reported `No issues found`.

Strict validation passed with 0 errors. The TSV output contained only its header row.

Reference validation passed. The checker executed 0 reference checks for this record.

Term validation passed. The validator emitted the known `eutils` / `pkg_resources` warning before reporting success.

Embedded `curation_history` entries were not checked: `just validate-history` validates standalone `history/` content, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The TOGO identity is correct. TOGO `M1929` reports `Modified W-medium`, original media id `NBRC_M1196`, and the current NBRC medium URL for `NO=1196`.

This recipe is an unreconciled duplicate of `data/normalized_yaml/bacterial/NBRC_1197.yaml`, which also points to NBRC medium 1196. The NBRC branch has a distinct `CultureMech:007463` id and its generated merge output is `data/merge_yaml/merged/1197.yaml`.

Several ingredient groundings are missing or weak. `H3BO4`, `Concentrated HCl`, `MgO`, and `Agar (if needed)` have no `term`; `FeSO4 x 7 H2O`, `CoSO4 x 7 H2O`, `MnSO4 x 4 H2O`, and `Na2HPO4 x 7 H2O` have primary terms but no `mediaingredientmech_chebi_term`.

The TOGO API maps `Substrates*` to vanillic acid, but the NBRC and TOGO footnote says `Vanillic acid and syringic acid etc.` The structured record should preserve this as a variable 10 mM aromatic substrate class instead of collapsing it to one compound or to an empty solution.

## Evidence

The live NBRC medium 1196 page names the medium `Modified W-medium` and lists one liter of water, 10 mM `Substrates*`, 0.85 g KH2PO4, 4.9 g Na2HPO4 x 7 H2O, 0.5 g ammonium sulfate, 0.1 g MgSO4 x 7 H2O, 51.3 ul concentrated HCl, 15 g `Agar (if needed)`, and these milligram-scale additions: FeSO4 x 7 H2O 9.5 mg, MgO 10.75 mg, CaCO3 2 mg, ZnSO4 x 7 H2O 1.44 mg, MnSO4 x 4 H2O 1.12 mg, CuSO4 x 5 H2O 0.25 mg, CoSO4 x 7 H2O 0.28 mg, and H3BO4 0.06 mg.

The TOGO API for `M1929` returns the same main solution, source URL, and NBRC media id, plus a comment clarifying `*Vanillic acid and syringic acid etc.` for the substrate row.

`data/normalized_yaml/bacterial/NBRC_1197.yaml` is a second normalized record for the same NBRC medium 1196 page. Its 2026-08-19 `Recovered composition from source HTML` curation entry says it reparsed the same NBRC medium 1196 composition table and restored 16 ingredients.

## Completeness

The generated TOGO record is not complete as a quantitative final recipe. Every NBRC milligram quantity except `H3BO4` and the microliter HCl quantity are present as numbers, but the units were serialized as `G_PER_L`.

The variable substrate is structurally incomplete. The generated record moves `Substrates*` to a `solutions` row with empty `composition`, 10 mM concentration, and `Unknown solution` as its solution name, losing the source footnote that explains the substrate alternatives.

The optional agar semantics are incomplete. NBRC lists `Agar (if needed)` at 15 g, so the record should either encode agar as optional or split the broth and solid variants explicitly.

## Findings

1. Source milligram additions were promoted to gram-per-liter concentrations without scaling: `FeSO4 x 7 H2O`, `ZnSO4 x 7 H2O`, `CuSO4 x 5 H2O`, `CoSO4 x 7 H2O`, `CaCO3`, `MnSO4 x 4 H2O`, `MgO`, and `H3BO4`.

2. `Concentrated HCl` was converted from `51.3 ul` in the source to `51.3 G_PER_L` in the generated record.

3. `Substrates*` was migrated into an empty solution row named `Unknown solution`, and its `Vanillic acid and syringic acid etc.` source note is no longer attached to the 10 mM carbon source.

4. `Agar (if needed)` is represented as a mandatory 15 g/L ingredient and the whole recipe is marked `SOLID_AGAR`, even though NBRC labels agar as conditional.

5. The TOGO and NBRC imports for NBRC medium 1196 are not reconciled. They carry different CultureMech ids and generated artifacts even though they describe the same live NBRC page.

6. Several hydrate salts, `H3BO4`, `MgO`, and `Concentrated HCl` still need stronger structured grounding.

## Recommended Edits

Convert milligram values to `MG_PER_L` or to scaled `G_PER_L` values, and encode concentrated HCl as `0.0513 ML_PER_L` or another supported liquid-volume unit that preserves the 51.3 ul source value.

Model `Substrates*` as a variable 10 mM aromatic substrate with the source note `Vanillic acid and syringic acid etc.` rather than as an empty local solution.

Represent `Agar (if needed)` as optional, or split Modified W-medium into broth and 15 g/L agar variants before marking a record as `SOLID_AGAR`.

Reconcile `modified_w_medium` with the recovered NBRC medium 1196 branch at `NBRC_1197.yaml`, keeping one CultureMech identity for NBRC `NO=1196` unless there is evidence for a true formulation difference.

Ground `MgO`, `Concentrated HCl`, `H3BO4`, and the hydrate salts using the same CHEBI curation logic used by adjacent manually recovered NBRC records.

## Follow-up Checks

After editing the normalized owners or the TOGO/NBRC import logic, regenerate the merged YAML and rerun open schema, strict, reference, and term validation for both generated records that point at NBRC medium 1196.

Recompare the regenerated quantities against TOGO `M1929` and the live NBRC `NO=1196` table, paying particular attention to every `mg`, `ul`, and optional agar row.

Check whether `H3BO4` is a literal NBRC source typo for boric acid and, if so, preserve the source label while grounding it to the boric acid CHEBI term with an explanatory curation note.

## Additional Notes

An exact, ignored-file-inclusive search for `TOGO:M1929`, `M1929`, `NBRC_M1196`, and `NO=1196` under `data/normalized_yaml` and `data/merge_yaml/merged` found the TOGO branch reviewed here and the separate `NBRC_1197` branch that also references NBRC medium 1196.
