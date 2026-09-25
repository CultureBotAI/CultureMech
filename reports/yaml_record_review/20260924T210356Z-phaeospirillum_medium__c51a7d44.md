# YAML Record Review: phaeospirillum_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/phaeospirillum_medium__c51a7d44.yaml
- Started UTC: 2026-09-24T21:03:56Z
- Finished UTC: 2026-09-24T21:03:56Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:003002
- Name: phaeospirillum_medium
- Source import: phaeospirillum_medium
- Primary external ID: mediadive.medium:J657
- Source URL: `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=657`

This generated record represents JCM Medium 657, PHAEOSPIRILLUM MEDIUM.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/phaeospirillum_medium__c51a7d44.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record is pointed at the correct obsolete JCM source identity, JCM_M657 / GRMD 657. The live JCM URL returned "Nothing found" on 2026-09-24, but TOGO M673 still carries a snapshot of the same `JCM_M657` recipe and preserves the original JCM URL.

Exact ignored-file searches across `data` found a sibling TOGO M673 generated record at `data/merge_yaml/merged/PHAEOSPIRILLUM_MEDIUM.yaml`. The two records describe the same JCM Phaeospirillum Medium and should converge after source normalization.

The simple salts and sodium pyruvate are grounded consistently in the MediaDive/JCM import. The problem is structural: Micronutrient solution SL7 and ferric citrate solution were expanded into top-level ingredients in ways that lose their volume and stock-solution semantics.

## Evidence

- TOGO M673 identifies its original source as JCM_M657 and lists Phaeospirillum Medium at pH 7.0.
- The TOGO M673 source payload adds 5 ml of ferric citrate at 0.1% w/v and 1 ml of Micronutrient solution SL7, referring that SL7 stock to Medium M535.
- The imported TOGO M673 sibling keeps `Micronutrient solution SL7 (see Medium [M535])` as a referenced solution rather than expanding all SL7 stock rows into the base recipe.
- The local MediaDive solution record `mediadive_4331_Micronutrient_solution_SL7.yaml` contains the same HCl, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O values that appear as final rows in this generated medium.

## Completeness

The generated record captures the base salts, sodium pyruvate, yeast extract, final 5 mM thiosulfate, and pH. It does not correctly preserve the two key stock-solution boundaries:

- `Ferric citrate` is stored as 5 G_PER_L, but the source addition is 5 ml of a 0.1% w/v ferric citrate solution.
- SL7 stock ingredients and HCl are imported as top-level base-medium ingredients even though the medium only adds 1 ml of the SL7 stock per liter-scale recipe.

## Findings

1. The ferric citrate solution volume is dimensionally wrong. A 5 ml aliquot of a 0.1% w/v stock is not 5 G_PER_L final ferric citrate.
2. Micronutrient solution SL7 was flattened into the main ingredient table. HCl and trace salts from the stock are represented as if they were final Phaeospirillum Medium concentrations.
3. The `HCl` row is especially suspect because the SL7 local solution uses a percent volume row for HCl, while this recipe stores `HCl` as 1 G_PER_L.
4. The sibling TOGO M673 and direct MediaDive/JCM records remain split even though exact ignored-file search shows that both point back to JCM GRMD 657.
5. The direct JCM URL embedded in both source records is stale and no longer resolves to the source recipe.

## Recommended Edits

- Reconstruct JCM_M657 with base salts, yeast extract, sodium pyruvate, 5 mM Na2S2O3 x 5 H2O, 5 ml of 0.1% w/v ferric citrate solution, and 1 ml of Micronutrient solution SL7 as distinct source components.
- Reference or nest the curated SL7 stock instead of copying HCl and trace salts into the Phaeospirillum base medium.
- Convert ferric citrate and SL7 aliquots only through volume-aware stock handling.
- Merge the MediaDive J657 and TOGO M673 generated identities once their normalized records use the same source structure.
- Keep an archived or TOGO-backed source note because the live JCM GRMD 657 page currently returns no recipe.

## Follow-up Checks

- Regenerate merged YAML and verify that only one Phaeospirillum Medium representation remains for JCM_M657 / TOGO M673.
- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `GRMD=657`, `mediadive.medium:J657`, and `TOGO:M673` to confirm that no stale sibling remains.
- Spot-check the generated page to ensure SL7 appears as a 1 ml stock addition, not as top-level HCl and trace-metal rows.

## Additional Notes

The primary live JCM page was checked directly and returned "Nothing found"; ignored files were included in all local duplicate searches cited above.
