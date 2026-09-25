# YAML Record Review: . OMIZ-PAT Medium (modified)

- Repository: CultureMech
- Record: data/merge_yaml/merged/omiz_pat_medium_modified.yaml
- Started UTC: 2026-09-24T19:21:46Z
- Finished UTC: 2026-09-24T19:23:12Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:000962`, the generated `omiz_pat_medium_modified` record merged from `data/normalized_yaml/bacterial/omiz_pat_medium_modified.yaml`.

## Validation

Passed LinkML validation against `MediaRecipe` with no issues reported.

Passed strict validation; the TSV contained only the header row.

Passed LinkML reference validation with zero reference checks.

Passed LinkML term validation.

Embedded `curation_history` validation was not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` blocks in generated YAML.

## Identity and Grounding

The identity is grounded to DSMZ/MediaDive Medium 1494. MediaDive and the DSMZ PDF both identify the record as `. OMIZ-PAT Medium (modified)`, and the generated record preserves `media_term.term.id: mediadive.medium:1494`.

An ignored-inclusive exact search for `mediadive.medium:1494`, `DSMZ_Medium1494`, and `omiz_pat_medium_modified` under `data/merge_yaml` and `data/normalized_yaml` found only the single normalized owner, the single generated derivative, and generated index mentions.

## Evidence

MediaDive REST and the DSMZ PDF both describe a 200 ml final recipe: 100 ml distilled water, 10 ml each of Solutions A through G, 200 ul Solution H, 8 ul Solution I, 2 ul Solution J, 40 ul Solution K, 2 ml Solution L, 1:1000 pre-diluted trace element additions, water up to 200 ml, supplements, then 10 ml rabbit serum followed by flushing with N2CO2, pH adjustment to 6.9, and filter sterilization.

The stock solutions have their own preparation recipes. For example, Solution A is a 100 ml amino-acid stock, Solution I contains four volatile acids measured as 10 ul each, Solution L is a fresh yeast homogenate/supernatant, and Trace elements I through III are concentrated stocks that must be pre-diluted 1:1000 before addition to the final medium.

The generated YAML collapses every stock component into one top-level ingredient list.

## Completeness

The generated `ph_value: 6.9` and the final filter-sterilization step are source-backed.

Many source components are present by label, but the loss of solution topology makes the reported concentrations stock-strength rather than final-medium concentrations.

Target organisms are absent. This is not a defect for this generated DSMZ record because the fetched DSMZ and MediaDive medium definitions do not list strains or organisms.

## Findings

- The record is globally flattened: stock-solution concentrations such as 0.9 g/L L-alanine in 100 ml Solution A, 5 g/L MgSO4 x 7 H2O in 100 ml Solution B, 0.1 g/L vitamins in 100 ml stock solutions, and trace metal stock concentrations are all emitted as final `G_PER_L` medium concentrations even though the main recipe adds only fixed aliquots to a 200 ml final medium.
- Main-solution water rows are missing, including the initial 100 ml distilled water, the "add up to 200 ml" water row, and multiple stock waters. This makes the flattened recipe impossible to reconstruct as either a stock recipe or a final medium recipe.
- Trace elements I, II, and III are especially mis-scaled: DSMZ says to pre-dilute these stocks 1:1000 before using 2 ml or 200 ul, but the generated YAML emits stock concentrations directly, such as 28.7 g/L `ZnSO4 x 7 H2O`.
- The source's Solution I contains four 10 ul volatile-acid components; generated YAML omits `2-methylbutyric acid` and converts the remaining microliter ingredients to `10 G_PER_L` stock entries.
- Shared solvents and acids from independent stocks are merged together. `Ethanol` is summed across Solution J and Supplement 4 as `1.9 G_PER_L`, and `HCl` is summed across Trace elements I, II, III, and Supplement 1 as `0.47397999999999996 G_PER_L`.
- The parsed ingredient `D` is really DSMZ `D,L-lactic acid, sodium salt`; it is incorrectly grounded to `CHEBI:29958` / `L-aspartic acid residue`.
- The `Tryptone`, `Yeast extract`, and `Sodium chloride` LB Medium constituent expansion is not present in DSMZ Medium 1494 or the MediaDive 1494 source JSON. It came from a generic external LB Medium note and should not be injected into this DSMZ record.
- `Rabbit serum` is a 10 ml addition to a 200 ml recipe, but the generated YAML reports it as `10 G_PER_L`.

## Recommended Edits

- Recurate `data/normalized_yaml/bacterial/omiz_pat_medium_modified.yaml` as a nested recipe with aliquoted Solution A through L, Trace elements I through III, and Supplements 1 through 5 instead of one stock-flattened ingredient list.
- Preserve microliter and milliliter stock-addition rows at the final medium level, including the 1:1000 trace-element pre-dilutions and the final rabbit serum addition.
- Restore all distilled water basis rows and final "add up to 200 ml" semantics.
- Add `2-methylbutyric acid`, repair `D,L-lactic acid, sodium salt`, and remove the unsupported LB Medium constituent expansion.
- Prevent duplicate merger from summing unrelated same-label ingredients that occur in different stock-solution scopes.
- Regenerate `data/merge_yaml/merged/omiz_pat_medium_modified.yaml` after the normalized owner is repaired.

## Follow-up Checks

- Rerun open-schema, strict, reference, and term validation on the regenerated `data/merge_yaml/merged/omiz_pat_medium_modified.yaml`.
- Compare the regenerated topology against DSMZ Medium 1494 and MediaDive REST Medium 1494, checking that each stock solution, final aliquot, water row, N2CO2 filter step, and storage instruction is preserved in the correct scope.
- Recheck ingredient grounding for hydrate/salt terms and any stock-only solvent rows after the topology is repaired.

## Additional Notes

None found.
