# YAML Record Review: oscillibacter_gh_medium__b282de4f

- Repository: CultureMech
- Record: data/merge_yaml/merged/oscillibacter_gh_medium__b282de4f.yaml
- Started UTC: 2026-09-24T19:33:00Z
- Finished UTC: 2026-09-24T19:33:00Z
- Verdict: needs curation

## Target

Reviewed generated MediaRecipe `CultureMech:003280`, `oscillibacter_gh_medium`, generated from `data/normalized_yaml/bacterial/oscillibacter_gh_medium.yaml` for JCM Medium J932 / OSCILLIBACTER GH MEDIUM.

## Validation

- Open LinkML validation: Passed; exited 0 with `No issues found`.
- Strict validation: Passed; scanned 1 file with 0 ERROR rows. `/private/tmp/oscillibacter_gh_medium__b282de4f.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The identifier and source term are coherent for the direct MediaDive import: the generated record uses JCM Medium J932 with `mediadive.medium:J932`, pH 6.0, and JCM source URL `GRMD=932`.

The same JCM 932 formulation is also present through TOGO M978. An ignored-inclusive exact search for `mediadive.medium:J932`, `GRMD=932`, `oscillibacter_gh_medium`, and `J932` across `data/merge_yaml` and `data/normalized_yaml` found `data/normalized_yaml/bacterial/TOGO_M978_Oscillibacter_GH_Medium.yaml` and generated sibling `data/merge_yaml/merged/OSCILLIBACTER_GH_MEDIUM.yaml`.

## Evidence

MediaDive REST for JCM J932 lists a 1012 ml main solution containing 5 g yeast extract, 5 g Polypeptone, 0.03 g Tween 80, 10 ml Trace vitamins, 1 ml FeCl2 solution, 1 ml Trace element solution, and 1000 ml distilled water. Its only preparation step instructs adjusting to pH 6.0, distributing under an N2 stream, sealing with butyl rubber stoppers, and autoclaving. TOGO M978 points to the same JCM medium, carries pH 6.0, and lists the same water, Tween 80, yeast extract, Polypeptone, three stock-addition rows, and N2 gas handling.

The direct normalized source has already repaired this structure: it keeps distilled water as 988.142 `ML_PER_L`, Trace vitamins as a 9.88142 `ML_PER_L` stock addition with JCM 197 composition, FeCl2 solution and Trace element solution as 0.988142 `ML_PER_L` stock additions with JCM 187 composition, four explicit preparation steps, sterilization notes, references, and a `SOURCE_DUPLICATE` child pointing at the TOGO M978 source. The TOGO normalized source mirrors the repair and points back at the direct MediaDive source as its `SOURCE_DUPLICATE` parent.

## Completeness

The generated record is materially incomplete because it omits the main distilled-water row, omits the three final-medium stock-addition rows, omits all nested `solutions`, drops curated references and data-quality flags, collapses the four curated preparation steps into one imported prose step, and keeps only the direct MediaDive source in `merged_from`.

## Findings

1. The generated record flattened all JCM 187 and JCM 197 stock constituents into top-level final-medium ingredients at stock strength.

   JCM 932 uses 10 ml Trace vitamins, 1 ml FeCl2 solution, and 1 ml Trace element solution in a 1012 ml main solution. The normalized record represents those as 9.88142, 0.988142, and 0.988142 `ML_PER_L` solution additions with nested stock composition. The generated record instead emits Biotin through Lipoic acid, HCl, FeCl2 x 4 H2O, and trace metal salts directly under `ingredients` using the stock concentrations such as Biotin 0.002 `G_PER_L`, HCl 2.5 `G_PER_L`, and FeCl2 x 4 H2O 1.5 `G_PER_L`. Those are not final-medium concentrations and erase the JCM stock hierarchy.

2. The generated record dropped distilled water from the main medium.

   JCM 932 and the repaired direct normalized source both retain the 1000 ml distilled-water row, normalized to 988.142 `ML_PER_L` after accounting for 12 ml of stock additions in the 1012 ml main solution. The generated record has no water ingredient at all.

3. Source-duplicate merging split the same JCM 932 formula into two generated records.

   The normalized direct MediaDive and TOGO M978 sources both mark each other as `SOURCE_DUPLICATE` for the same JCM Medium 932 formula. Generation still emitted `oscillibacter_gh_medium__b282de4f.yaml` from only `oscillibacter_gh_medium.yaml` and `OSCILLIBACTER_GH_MEDIUM.yaml` from only `TOGO_M978_Oscillibacter_GH_Medium.yaml`, so consumers see two records for one formulation.

## Recommended Edits

- Preserve `solutions` as first-class `MediaRecipe` content during generation or merging instead of promoting nested stock composition into final `ingredients`.
- Keep final-medium solution additions as `ML_PER_L` rows and include the repaired 988.142 `ML_PER_L` distilled-water row in generated output.
- Use `parent_media` and `variant_children` relationships with `SOURCE_DUPLICATE` to group the repaired MediaDive J932 and TOGO M978 records into one generated JCM 932 output.
- Preserve curated references, data-quality flags, and the structured four-step preparation sequence from normalized YAML when emitting merged YAML.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/oscillibacter_gh_medium__b282de4f.yaml` after changing solution handling and confirm that Biotin, HCl, and trace salts remain nested under their JCM 197 or JCM 187 solution compositions.
- Run an ignored-inclusive exact search for `GRMD=932`, `TOGO:M978`, and `mediadive.medium:J932` after regeneration and confirm there is only one generated JCM 932 record.
- Re-run open, strict, reference, and term validation on the regenerated YAML.

## Additional Notes

None found.
