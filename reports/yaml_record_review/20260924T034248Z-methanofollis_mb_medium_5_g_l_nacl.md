# YAML Record Review: methanofollis_mb_medium_5_g_l_nacl
- Repository: CultureMech
- Record: data/merge_yaml/merged/methanofollis_mb_medium_5_g_l_nacl.yaml
- Started UTC: 2026-09-24T03:41:16Z
- Finished UTC: 2026-09-24T03:42:48Z
- Verdict: needs curation

## Target
- ID: CultureMech:002095
- Name: methanofollis_mb_medium_5_g_l_nacl
- Label: METHANOFOLLIS MB MEDIUM (5 g/l NaCl)
- Category: archaea
- Source: DSMZ 924a, imported through MediaDive as mediadive.medium:924a
- Merge fingerprint: ffa5915f49356f25b306ee99a3b5d28f5f1ef642aa08e8196e6a9fc8dce12e73
- Merged from: methanofollis_mb_medium_5_g_l_nacl
- Maintained owner: data/normalized_yaml/archaea/methanofollis_mb_medium_5_g_l_nacl.yaml

## Validation
- Open schema validation: Passed; no issues found.
- Strict validation: Passed; 1 file scanned and 0 error rows.
- LinkML reference validation: Passed; 0 reference checks, all passed.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding
- The ID, name, category, source note, and `mediadive.medium:924a` term identify direct DSMZ medium 924a, METHANOFOLLIS MB MEDIUM (5 g/l NaCl).
- An exhaustive hidden and ignored search for `mediadive.medium:924a`, `CultureMech:002095`, and `methanofollis_mb_medium_5_g_l_nacl` found one maintained normalized owner plus the expected generated indexes and merged output.
- The `Sodium resazurin` source ingredient is grounded to CHEBI:8806 `Resazurin`; that term omits the source salt.
- NiCl2 x 6 H2O is grounded to generic nickel dichloride even though DSMZ 924a specifies the hexahydrate.

## Evidence
- DSMZ 924a defines a main 1011 ml medium containing basal salts, yeast extract, Trypticase peptone, 0.5 ml sodium resazurin 0.1% w/v, NaHCO3, Na-formate, 10 ml Modified Wolin's mineral solution, 1 ml Wolin's vitamin solution (10x), L-Cysteine HCl x H2O, Na2S x 9 H2O, and 1000 ml water.
- DSMZ lists Modified Wolin's mineral solution as a separate 1 L stock and instructs users to dissolve nitrilotriacetic acid first, adjust to pH 6.5 with KOH, add minerals, and adjust final pH to 7.0.
- DSMZ lists Wolin's vitamin solution (10x) as a separate 1 L stock.
- The YAML lacks a `solutions` array. The Modified Wolin mineral ingredients and Wolin vitamin ingredients are top-level final-medium ingredients at their 1 L stock concentrations.
- The top-level `NaCl` value sums the 1011 ml main-medium concentration, `4.9456 G_PER_L`, with `1.0 G_PER_L` from the mineral stock. The top-level CaCl2 x 2 H2O row likewise sums the main-medium `0.395648 G_PER_L` with the mineral-stock `0.1 G_PER_L`.
- The DSMZ preparation text for anoxic N2-CO2 sparging, bicarbonate, autoclaving, and sterile anoxic additions is preserved, but the mineral-stock pH step is stored as a second top-level `ADJUST_PH` step rather than as preparation for the Modified Wolin stock.

## Completeness
- The source main recipe, Modified Wolin mineral stock, Wolin vitamin stock, and preparation prose are all present in flattened form.
- The 10 ml mineral-stock and 1 ml vitamin-stock solution additions are absent, so stock rows cannot be diluted into the final 1011 ml medium.
- Empty optional fields are acceptable; no optional-field omission was counted as a defect.

## Findings
- Major: `data/normalized_yaml/archaea/methanofollis_mb_medium_5_g_l_nacl.yaml` flattens DSMZ 924a stock solutions into the final ingredient list instead of modeling 10 ml Modified Wolin's mineral solution and 1 ml Wolin's vitamin solution (10x).
- Major: Duplicate rows introduced by flattening were summed across incompatible scopes in `data/normalized_yaml/archaea/methanofollis_mb_medium_5_g_l_nacl.yaml`; NaCl and CaCl2 x 2 H2O each combine a final-medium amount with an undiluted mineral-stock amount.
- Major: All Modified Wolin trace minerals and Wolin vitamins are asserted as final `G_PER_L` values even though the source values belong to 1 L stock solutions.
- Minor: The Modified Wolin preparation note in `data/normalized_yaml/archaea/methanofollis_mb_medium_5_g_l_nacl.yaml` is detached from its stock solution.
- Minor: `Sodium resazurin` and NiCl2 x 6 H2O need narrower grounding if suitable CHEBI identifiers are available; the current terms are broader than the source labels.

## Recommended Edits
- Re-curate `data/normalized_yaml/archaea/methanofollis_mb_medium_5_g_l_nacl.yaml` from DSMZ 924a.
- Model Modified Wolin's mineral solution and Wolin's vitamin solution (10x) as stock solutions under the main 1011 ml DSMZ 924a recipe.
- Represent the main recipe as 10 ml of the mineral stock and 1 ml of the vitamin stock instead of promoting their children to final-medium rows.
- Remove the duplicate-summed `NaCl` and CaCl2 x 2 H2O rows and keep main-medium rows separate from mineral-stock rows.
- Scope the nitrilotriacetic-acid/KOH preparation note to the Modified Wolin mineral stock.
- Revisit sodium resazurin and NiCl2 x 6 H2O grounding for hydrate- or salt-specific CHEBI terms.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/methanofollis_mb_medium_5_g_l_nacl.yaml`.
- Confirm that Modified Wolin's mineral solution and Wolin's vitamin solution (10x) appear as solution additions, not flattened top-level ingredients.
- Confirm that duplicate `NaCl` and CaCl2 x 2 H2O values are no longer summed across the main and mineral-stock scopes.
- Confirm that Wolin vitamin rows and Modified Wolin trace-mineral rows are nested under their stock solutions.
- Rerun open schema, strict, reference, and term validation.

## Additional Notes
- The variant instructions for DSM 14663, DSM 15483, DSM 29354, DSM 19953, DSM 100756, and DSM 104444 were not modeled in this base DSMZ 924a record; they may need separate MediaVariant records if this corpus tracks DSMZ strain-specific variants.
