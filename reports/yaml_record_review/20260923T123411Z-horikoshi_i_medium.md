# YAML Record Review: Horikoshi-I Medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/horikoshi_i_medium.yaml
- Started UTC: 2026-09-23T12:32:36Z
- Finished UTC: 2026-09-23T12:34:11Z
- Verdict: needs curation

## Target

Reviewed the generated TOGO branch for TOGO Medium M174 and JCM Medium 181, `Horikoshi-I Medium`, at `data/merge_yaml/merged/horikoshi_i_medium.yaml`. The maintained source is `data/normalized_yaml/bacterial/TOGO_M174_Horikoshi-I_Medium.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/horikoshi_i_medium.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record ID, label, category, and `TOGO:M174` grounding all point to the Horikoshi-I medium imported from TOGO Medium M174 and JCM Medium 181. The source identity is not conflated with the nearby salinity variants for 2%, 3.5%, 5%, or 10% NaCl, which are separate JCM/TOGO media linked from the maintained normalized source.

## Evidence

TOGO Medium M174 lists 10 g glucose, 5 g `Polypepton (Nihon Pharm. Co.)`, 5 g yeast extract, 1 g K2HPO4, 0.2 g MgSO4 hydrate, 15 g agar, 900 ml distilled water, and 100 ml of 10% Na2CO3 solution with final pH 10.0. It also carries JCM Medium 181 as its original upstream source.

The generated artifact is stale relative to the September 2026 normalized source repair. It still stores the 900 ml distilled-water component as `900 G_PER_L`, still has an empty `Na2CO3 solution` with `100 G_PER_L`, and has no structured `preparation_steps`, `sterilization`, or `ph_value`.

The inspected JCM Medium 181 page confirms the same glucose, yeast extract, K2HPO4, MgSO4 hydrate, agar, distilled-water, post-autoclave 10% Na2CO3, final-pH, and default autoclave claims. Its peptone line is `Hipolypepton (FUJIFILM Wako)`, while the TOGO M174 API has `Polypepton (Nihon Pharm. Co.)` as the component name and `Hipolypepton (Nihon seiyaku)` as the label. That source-version disagreement is not preserved in either the generated artifact or the maintained normalized source.

## Completeness

The six non-water agar-base rows are present and the magnesium sulfate heptahydrate term is chemically appropriate, but following the generated record would put 900 g water and 100 g Na2CO3 solution into the recipe instead of building a 900 ml base plus a 100 ml sterile 10% sodium carbonate addition. The generated record also loses the final pH of about 10.0 and the default JCM 121 C for 15 min autoclave instruction.

No `target_organisms`, growth metrics, or strain-specific growth evidence are asserted, so there are no over-scoped organism claims to review.

## Findings

- The generated artifact is stale and no longer reflects the maintained September 2026 source repair in `data/normalized_yaml/bacterial/TOGO_M174_Horikoshi-I_Medium.yaml`.
- The 900 ml distilled-water row is represented as `900 G_PER_L`, which changes a volume into a mass and overstates the final recipe.
- The 100 ml sterile 10% Na2CO3 post-autoclave addition is represented as an empty solution with `100 G_PER_L`, losing both the 100 ml dilution boundary and the 10% stock concentration.
- JCM's default autoclave step, the post-autoclave aseptic addition, and final pH 10.0 are absent from the generated record.
- The peptone product label disagrees between TOGO M174 and the fetched JCM Medium 181 page; the record follows TOGO but does not preserve that upstream version conflict.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/horikoshi_i_medium.yaml` from `data/normalized_yaml/bacterial/TOGO_M174_Horikoshi-I_Medium.yaml` so the merged record inherits the repaired water amount, structured pH, autoclave step, sodium-carbonate stock solution, and sodium-carbonate post-autoclave addition.
- Audit the merge pipeline if regeneration does not carry `ML_PER_L`, nested `solutions`, `sterilization`, `preparation_steps`, and `ph_value` from the maintained source.
- In `data/normalized_yaml/bacterial/TOGO_M174_Horikoshi-I_Medium.yaml`, reconcile or explicitly note the source-version difference between the TOGO `Polypepton (Nihon Pharm. Co.)` row and the fetched JCM `Hipolypepton (FUJIFILM Wako)` row.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation against the regenerated merged record.
- Re-open TOGO M174 and JCM Medium 181 to confirm the regenerated record carries 900 ml water, 100 ml of sterile 10% Na2CO3, final pH 10.0, the JCM default 121 C for 15 min autoclave instruction, and the resolved peptone label.
- Run the repository's merge freshness audit to prove `data/merge_yaml/merged/horikoshi_i_medium.yaml` no longer lags its normalized source.

## Additional Notes

The generated record also retains the old non-ASCII middle-dot hydrate spelling for the magnesium sulfate row. The maintained normalized source has already switched that display string to `MgSO4 x 7 H2O`, so the same regeneration should remove the presentation issue.
