# YAML Record Review: pes_provasoli_s_enriched_seawater_medium_7_psu_at_25_c

- Repository: CultureMech
- Record: data/merge_yaml/merged/pes_provasoli_s_enriched_seawater_medium_7_psu_at_25_c.yaml
- Started UTC: 2026-09-24T20:33:18Z
- Finished UTC: 2026-09-24T20:33:18Z
- Verdict: needs curation

## Target

Generated bacterial MediaRecipe `CultureMech:001163`, `pes_provasoli_s_enriched_seawater_medium_7_psu_at_25_c`, merged from `data/normalized_yaml/bacterial/pes_provasoli_s_enriched_seawater_medium_7_psu_at_25_c.yaml` and `data/normalized_yaml/bacterial/cyanobacteria_medium_mcl.yaml`.

The record represents DSMZ / MediaDive medium 1680a, PES - Provasoli's Enriched Seawater-Medium at 7 PSU, merged with DSMZ / MediaDive medium 1680, Cyanobacteria Medium MCL. It currently has 33 g/L Artificial Sea Salt plus MCL trace metals, MCL nitrogen/phosphate/chelator components, and MCL vitamin components flattened as top-level ingredients.

## Validation

- Open LinkML validation: Passed with no issues.
- Strict validator: Passed; `/private/tmp/pes_provasoli_s_enriched_seawater_medium_7_psu_at_25_c.strict.tsv` was header-only, so there were 0 strict errors.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The generated merge is not a true source duplicate. MediaDive 1680a is the 7 PSU-at-25 C PES variant with 8.2 g/L Artificial Sea Salt, whereas MediaDive 1680 is Cyanobacteria Medium MCL with 33 g/L Artificial Sea Salt and a description that ties it to 28 PSU at 25 C.

An exact ignored-inclusive search found only the two MediaDive owners for `mediadive.medium:1680a` and `mediadive.medium:1680`, plus their one generated merged record.

## Evidence

MediaDive 1680a and MediaDive 1680 have the same MCL stock additions: 5 ml MCL Stock Solution A, 5 ml MCL Stock Solution B, and 1 ml MCL Vitamin Stock Solution added to a 1 L final medium.

They differ in the artificial sea-salt component. MediaDive 1680a lists 8.2 g Artificial Sea Salt in the 1 L final medium; MediaDive 1680 lists 33 g. The generated record selected the 1680a identity but the 1680 sea-salt concentration.

Each MCL stock has its own make-up volume and subrecipe. The stock rows in the source are volume additions from ingredient stock solutions, such as 5 ml of a 1.92 g/L CoSO4 x 7 H2O solution into 500 ml MCL Stock Solution A, and 160 uL of a 1.0 g/L Vitamin B12 solution into 100 ml MCL Vitamin Stock Solution. They are not gram-per-liter final-medium components.

## Completeness

The generated record preserves the MediaDive source IDs, preparation text, and many component labels, but it loses all stock-solution boundaries.

The merge also collapses two salinity variants into one generated recipe, causing the 7 PSU record to contain the 28 PSU artificial sea-salt concentration.

## Findings

1. Needs curation: MediaDive 1680a and 1680 are salinity variants, not exact source duplicates. The generated 1680a record carries 33 g/L Artificial Sea Salt from medium 1680 instead of the 8.2 g/L specified by medium 1680a.
2. Needs curation: MCL Stock Solution A, MCL Stock Solution B, and MCL Vitamin Stock Solution are flattened into top-level final-medium ingredients. The final medium should contain three stock-solution additions, not the individual trace-metal, nitrogen/phosphate/chelator, and vitamin rows.
3. Needs curation: stock subrecipe volumes are encoded as grams per liter. The 100 ml metal and nutrient rows and the 160 uL / 800 uL vitamin rows are volumes drawn from more concentrated stock solutions, not 100 g/L, 160 g/L, or 800 g/L components.
4. Needs curation: the 500 ml, 500 ml, and 100 ml MCL stock make-up scopes are represented only as free-text preparation steps, so their water and stock identities are not structurally attached to populated `solutions`.
5. Needs curation: legacy `mediaingredientmech_term` fields remain on NaNO3 and Thiamine even though both rows are already grounded to CHEBI terms.

## Recommended Edits

1. Split DSMZ / MediaDive 1680a back out from DSMZ / MediaDive 1680, or model them explicitly as salinity-specific variants rather than exact source duplicates.
2. Keep each final medium to its sea-salt amount plus MCL Stock Solution A, MCL Stock Solution B, and MCL Vitamin Stock Solution volume additions.
3. Move the three MCL stock recipes into populated `solutions` with their source make-up volumes and the correct volume additions from their ingredient stock solutions.
4. Convert or otherwise preserve the `uL` vitamin additions without interpreting them as grams per liter.
5. Refresh stale legacy MediaIngredientMech fields on NaNO3 and Thiamine after the stock rows are repaired.

## Follow-up Checks

1. Re-run open, strict, reference, and term validation on the repaired maintained owners and regenerated merged records.
2. Repeat an exact ignored-inclusive search for `mediadive.medium:1680a`, `mediadive.medium:1680`, `CultureMech:001163`, and `cyanobacteria_medium_mcl` to verify only the intended salinity-variant relationship remains.

## Additional Notes

The exact ignored-inclusive duplicate search covered `data`, `src`, and `scripts` for `mediadive.medium:1680a`, `mediadive.medium:1680`, `CultureMech:001163`, `cyanobacteria_medium_mcl`, and `pes_provasoli_s_enriched_seawater_medium_7_psu_at_25_c`.
