# YAML Record Review: telmatospirillum_peat_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/telmatospirillum_peat_medium.yaml`
- Started UTC: 2026-09-25T09:10:32Z
- Finished UTC: 2026-09-25T09:11:38Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:001485` for `telmatospirillum_peat_medium`, the DSMZ/MediaDive Medium 380a TELMATOSPIRILLUM (PEAT) MEDIUM import merged from `telmatospirillum_peat_medium.yaml` with fingerprint `00ff2f0d73c67123b5afa31feb5c87bbd434af739d1c4af7a244e8b512c24f49`.

## Validation

- LinkML schema validation: Passed with `No issues found`.
- Strict validation: Passed; 1 file scanned and 0 error rows written to `/private/tmp/telmatospirillum_peat_medium.strict.tsv`.
- Reference validation: Passed; 1 file validated, 0 external checks.
- Term validation: Passed.
- Embedded `curation_history`: Not checked; `just validate-history` validates standalone `history/`, not merged `MediaRecipe.curation_history`.

## Identity and Grounding

The generated `mediadive.medium:380a` grounding matches DSMZ Medium 380a, TELMATOSPIRILLUM (PEAT) MEDIUM. Exact searches for `mediadive.medium:380a`, `DSMZ_Medium380a.pdf`, and `telmatospirillum_peat_medium` found only this DSMZ-derived generated record and its normalized source among bacterial normalized and merged YAML records.

The target still carries one stale legacy MediaIngredientMech mapping: `NaNO3` has `CHEBI:63005` but keeps `mediaingredientmech_term: MediaIngredientMech:000171`.

## Evidence

The DSMZ Medium 380a PDF and the MediaDive 380a payload agree on a 1008 mL final volume with KH2PO4, NaNO3, L(+)-tartaric acid, succinic acid, Na-acetate, 5 mL Modified Wolin's mineral solution, 2 mL Fe(III) quinate solution 0.01 M, 0.5 mL sodium resazurin 0.1% w/v, D-xylose, 1 mL Wolin's vitamin solution (10x), 0.05 g Na-thioglycolate, and 1000 mL distilled water.

DSMZ defines the three stock solutions after the main recipe: Modified Wolin's mineral solution from medium 141, Fe(III) quinate solution 0.01 M from medium 380, and Wolin's vitamin solution (10x) from medium 120.

## Completeness

The generated record contains the correct directly weighed solutes and the source pH range, but it no longer preserves the DSMZ stock-solution structure. The Fe(III) quinate solution, Modified Wolin's mineral solution, and Wolin's vitamin solution rows are missing as named top-level additions.

The generated record is also stale relative to `data/normalized_yaml/bacterial/telmatospirillum_peat_medium.yaml` for `(-)-Quinic acid`: the normalized record has the CHEBI:17521 grounding added in August, while the generated merge predates that update.

## Findings

- The 5 mL Modified Wolin's mineral solution was expanded into stock-strength mineral concentrations; for example, nitrilotriacetic acid is recorded as `1.5 G_PER_L` instead of being scaled from 5 mL of a 1.5 g/L stock into the 1008 mL final medium.
- The 2 mL Fe(III) quinate solution was expanded into stock-strength rows for 2.7 g/L FeCl3 x 6 H2O and 1.9 g/L `(-)-Quinic acid` rather than represented as a 2 mL stock addition or scaled to final concentration.
- The 1 mL Wolin vitamin solution was expanded into stock-strength vitamin concentrations; the 10x vitamin stock should not be copied into the final recipe at full stock strength.
- The generated top-level preparation includes stock-preparation pH and filtration steps as if they applied to the final peat medium.
- `NaNO3` still has a legacy `mediaingredientmech_term`, and generated `(-)-Quinic acid` is missing the CHEBI grounding now present in normalized YAML.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/telmatospirillum_peat_medium.yaml`, then regenerate merged YAML; do not hand-edit `data/merge_yaml/merged/telmatospirillum_peat_medium.yaml`.
- Represent Modified Wolin's mineral solution, Fe(III) quinate solution 0.01 M, and Wolin's vitamin solution (10x) as named solutions added at 5 mL, 2 mL, and 1 mL respectively, or scale their expanded components by the appropriate volume fractions before storing final concentrations.
- Keep the stock-specific pH 6.5/7.0 KOH adjustment and filtration steps scoped to the stock solutions, not the final medium preparation.
- Refresh the generated output so `NaNO3` uses `mediaingredientmech_chebi_term` and `(-)-Quinic acid` keeps its `CHEBI:17521` term.

## Follow-up Checks

- Revalidate the regenerated Telmatospirillum peat record with schema, strict, reference, and term validators.
- Search exact `mediadive.medium:380a`, `DSMZ_Medium380a.pdf`, and `telmatospirillum_peat_medium`, including ignored files, to confirm the only remaining bacterial merged output is the repaired DSMZ 380a record.
- Search the regenerated record for `mediaingredientmech_term`, including ignored files, to confirm the legacy NaNO3 link is gone.

## Additional Notes

The initial `Medium 1127` search was too broad for this target and hit unrelated TPT 18 and JCM Medium 1127 records; those results were discarded. The exact DSMZ 380a searches used `rg --no-ignore --hidden`, so ignored files were included.
