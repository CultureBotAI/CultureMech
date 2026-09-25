# YAML Record Review: desulfotomaculum_14_5_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/desulfotomaculum_14_5_medium.yaml
- Started UTC: 2026-09-22T20:11:57Z
- Finished UTC: 2026-09-22T20:14:15Z
- Verdict: needs curation

## Target

Generated MediaRecipe `CultureMech:001774`, `desulfotomaculum_14_5_medium`, from DSMZ/MediaDive medium 63a.

The generated record carries `media_term.id` `mediadive.medium:63a` and merges six source records that locally share the same ingredient and concentration signature.

## Validation

- LinkML open validation: passed.
- Strict validation: passed with 0 error rows.
- LinkML reference validation: passed with 0 checks.
- LinkML term validation: passed.
- Embedded history validation: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged records.

## Identity and Grounding

The lead MediaDive identity is DSMZ 63a, `DESULFOTOMACULUM (14.5) MEDIUM`.

The merge groups DSMZ 63a with five KOMODO-style source duplicates, including records for DSMZ 63-derived media and `medium_for_d_indonesiensis`. That grouping was made from the flattened ingredient/concentration signature and should be rechecked after DSMZ 63a is rebuilt as three nested solutions.

## Evidence

The MediaDive 63a payload represents the medium as a 1000 ml main solution composed only of 980 ml `Solution A`, 10 ml `Solution B`, and 10 ml `Solution C`.

`Solution A` contains the phosphate, ammonium, sulfate, calcium, magnesium, acetate, pyruvate, yeast extract, resazurin, and 980 ml water formula. `Solution B` is a 10 ml FeSO4 stock at 50 g/L. `Solution C` is a 10 ml stock containing 10 g/L sodium thioglycolate and 10 g/L ascorbic acid.

The generated record has no `solutions` block and emits the Solution B and C stock concentrations as top-level final-medium ingredients.

## Completeness

The target preserves the DSMZ 63a identity, pH range, base Solution A compounds, and preparation text.

It omits the explicit 980 ml, 10 ml, and 10 ml solution additions, drops all distilled-water rows, and flattens Solutions B and C into the final ingredient list. The generated values `FeSO4 x 7 H2O = 50`, `Na-thioglycolate = 10`, and `Ascorbic acid = 10` `G_PER_L` are stock strengths, not final concentrations after adding 10 ml of each stock to the main medium.

## Findings

1. **Solution B and Solution C were flattened into top-level stock concentrations.**

   FeSO4 x 7 H2O, sodium thioglycolate, and ascorbic acid belong to separate 10 ml stocks. Their concentrations are off by the 100-fold dilution that would be implied when 10 ml stock is used in a 1000 ml final medium.

2. **The three-solution assembly is absent.**

   The source main solution contains only 980 ml Solution A, 10 ml Solution B, and 10 ml Solution C. The generated record instead emits one flat `ingredients` array and cannot express which ingredients are boiled under N2 as Solution A versus added later as B and C.

3. **Distilled water was dropped from every source solution.**

   Solution A, B, and C all contain source water rows. None of them are represented in the generated record, so solution volumes are not recoverable from the YAML.

4. **Duplicate merge provenance depends on a distorted formula.**

   The six-record merge may be correct, but it was decided after the DSMZ 63a A/B/C structure had been flattened. The provider equivalence should be re-evaluated using structured solutions so strain-specific DSMZ 63 variants are not collapsed only because the import lost context.

## Recommended Edits

Rebuild the DSMZ 63a MediaDive import with explicit `Solution A`, `Solution B`, and `Solution C` records and a main recipe that adds them at 980 ml, 10 ml, and 10 ml.

Move FeSO4 into Solution B and sodium thioglycolate plus ascorbic acid into Solution C; do not leave their stock concentrations in the final top-level ingredient list.

Preserve the water rows in the appropriate subsolutions.

After structured regeneration, re-run duplicate detection on the six merged source records and keep only source-level true duplicates in this canonical record.

## Follow-up Checks

Compare the regenerated output against MediaDive 63a and confirm that the main solution contains three solution additions and no direct FeSO4, sodium thioglycolate, or ascorbic acid rows.

Inspect each KOMODO DSMZ 63 derivative in the merge to confirm it is genuinely equivalent to DSMZ 63a.

Run the focused LinkML open, strict, reference, and term validators on the regenerated record.

## Additional Notes

No source YAML was edited during this review. Exact local searches for `desulfotomaculum_14_5_medium` included ignored files.
