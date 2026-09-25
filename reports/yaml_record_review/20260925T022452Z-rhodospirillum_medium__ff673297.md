# YAML Record Review: rhodospirillum_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rhodospirillum_medium__ff673297.yaml`
- Started UTC: 2026-09-25T02:24:51Z
- Finished UTC: 2026-09-25T02:24:51Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:002992` for JCM Medium J646 / `mediadive.medium:J646`, generated from `data/normalized_yaml/bacterial/rhodospirillum_medium.yaml`.

## Validation

- Open schema validation: passed with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The target ID, label, category, and `mediadive.medium:J646` grounding match MediaDive for Rhodospirillum medium. The live JCM `GRMD=646` page returned `Nothing found`, so the direct JCM URL is no longer sufficient evidence by itself.

TOGO M661 is the same source medium: it cites original media ID `JCM_M646`, the same JCM 646 URL, and the same JCM ingredient list. An exact ignored-inclusive search for `TOGO:M661`, `mediadive.medium:J646`, `JCM_M646`, and `GRMD=646` found only the expected JCM and TOGO maintained owners, their generated records, and their indexes under the relevant data trees.

## Evidence

MediaDive J646 lists 1 g KH2PO4, 0.5 g MgSO4 x 7H2O, 10 g yeast extract, 10 g peptone, 1 g sodium pyruvate, Na2S x 9H2O at 0.5 mM final concentration, 1000 ml distilled water, and pH 7.0. It also says to add a filter-sterilized Na2S x 9H2O solution after autoclaving. TOGO M661 reports the same JCM_M646 recipe and comments.

The generated direct JCM target preserves the six non-water rows, pH, and sulfide addition step, but omits distilled water. The TOGO owner preserves the 1 L water row but stores it as `1 G_PER_L`, and it omits the source pH and post-autoclave sulfide-addition comment.

## Completeness

The target is missing the final water row, and the generated corpus emits the same JCM 646 source twice: once as `rhodospirillum_medium__ff673297.yaml` from MediaDive and once as `RHODOSPIRILLUM_MEDIUM.yaml` from TOGO.

Empty optional literature, strain, and solution fields are not defects.

## Findings

- Major: `data/normalized_yaml/bacterial/rhodospirillum_medium.yaml` omits the 1000 ml distilled-water row from MediaDive J646, so the generated target has only six of the seven main recipe rows.
- Major: `data/normalized_yaml/bacterial/TOGO_M661_Rhodospirillum_Medium.yaml` imports the 1 L water row as `1 G_PER_L`.
- Major: `data/normalized_yaml/bacterial/TOGO_M661_Rhodospirillum_Medium.yaml` omits the source pH 7.0 and the post-autoclave addition of filter-sterilized Na2S x 9H2O solution.
- Major: `data/merge_yaml/merged` contains both lowercase JCM and uppercase TOGO Rhodospirillum medium targets instead of one source-duplicate target for JCM 646.

## Recommended Edits

- Add the 1000 ml/L distilled-water row to `data/normalized_yaml/bacterial/rhodospirillum_medium.yaml`.
- Repair `data/normalized_yaml/bacterial/TOGO_M661_Rhodospirillum_Medium.yaml` so water stays volumetric and pH 7.0 plus the post-autoclave sulfide step are represented.
- Add a source-duplicate relationship between TOGO M661 and direct MediaDive/JCM J646, then regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation for the regenerated Rhodospirillum medium.
- Confirm the regenerated final recipe has the six non-water ingredients plus distilled water.
- Confirm `data/merge_yaml/merged` no longer emits both uppercase TOGO and lowercase JCM Rhodospirillum targets.

## Additional Notes

The direct JCM endpoint for `GRMD=646` appears stale or retired, but both imported source APIs identify the same original JCM 646 recipe.
