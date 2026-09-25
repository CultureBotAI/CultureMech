# YAML Record Review: METHERMICOCCUS (METHANOGEN) MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methermicoccus_methanogen_medium.yaml
- Started UTC: 2026-09-24T05:29:45Z
- Finished UTC: 2026-09-24T05:30:54Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methermicoccus_methanogen_medium.yaml`, a generated `MediaRecipe` for `CultureMech:000246` with `name: methermicoccus_methanogen_medium`, `original_name: METHERMICOCCUS (METHANOGEN) MEDIUM`, pH 6.0-6.5, and source grounding `mediadive.medium:1084`.

The record was merged from two normalized duplicate inputs:

- `data/normalized_yaml/archaea/methermicoccus_methanogen_medium.yaml`
- `data/normalized_yaml/archaea/methermicoccus_medium.yaml`

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methermicoccus_methanogen_medium.yaml` | Passed; exited 0 with no diagnostics. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methermicoccus_methanogen_medium.yaml --out /private/tmp/methermicoccus_methanogen_medium.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methermicoccus_methanogen_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methermicoccus_methanogen_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The DSMZ identity is correct. DSMZ/MediaDive medium 1084 is `METHERMICOCCUS (METHANOGEN) MEDIUM`, a complex liquid archaeal medium with final pH 6.0-6.5.

The stock structure is not correct. DSMZ 1084 adds 5 ml Sludge fluid from DSMZ medium 119 to a 1021 ml final medium; the generated record has no `solutions` entry for Sludge fluid, sums Sludge fluid yeast extract with final-medium yeast extract, promotes sludge to a final ingredient, and scopes the Sludge fluid preparation as a final-medium step.

## Evidence

Supported source claims:

- DSMZ/MediaDive 1084 supports the record's DSMZ identity, complex liquid classification, final pH 6.0-6.5, and direct final-medium rows for KCl, NH4Cl, K2HPO4, NaCl, MgCl2 x 6 H2O, yeast extract, sodium resazurin, Na2CO3, methanol, 2-mercaptoethanesulfonate, L-cysteine HCl x H2O, Na2S x 9 H2O, and distilled water.
- DSMZ/MediaDive 1084 supports the anaerobic preparation text for sparging with 80% N2 and 20% CO2, dispensing under the same gas atmosphere, autoclaving, and adding sludge fluid, methanol, coenzyme M, cysteine, sulfide, and carbonate from sterile stocks.
- DSMZ/MediaDive solution 208 supports Sludge fluid as a separate stock made from 4 g yeast extract plus 1000 ml anaerobic-digester sludge.

Unsupported or over-scoped generated claims:

- The record's 5.95886 G_PER_L Yeast extract row is the sum of 1.95886 G_PER_L final-medium yeast extract and 4 G_PER_L Sludge fluid yeast extract; those are different recipe scopes.
- The 1000 ml sludge used to make Sludge fluid is not a 1000 G_PER_L final-medium ingredient.
- The Sludge fluid incubation, centrifugation, autoclaving, storage, and dark-storage instructions belong to the stock solution, not to final-medium preparation.

## Completeness

The schema-optional evidence, discussions, growth, target organism, and solution arrays are empty; evidence, discussion, and growth omissions are not defects by themselves.

Consequential gaps:

- Sludge fluid solution 208 is absent as a scoped 5 ml stock addition.
- The main 1000 ml distilled-water row is absent.
- The final record does not distinguish the DSMZ source from the KOMODO duplicate's inherited DSMZ composition, and the KOMODO normalized duplicate still says `Aerobic: Yes` despite representing an anaerobic methanogen medium.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Sludge fluid was flattened into top-level ingredients. | DSMZ/MediaDive 1084 adds 5 ml Sludge fluid and defines that stock separately. The generated YAML has no Sludge fluid solution and emits Sludge as a final ingredient. | Both normalized duplicate inputs; MediaDive importer and KOMODO DSMZ enrichment. |
| Major | Duplicate cleanup merged yeast extract across stock scopes. | DSMZ 1084 has 2 g yeast extract in the final medium and 4 g yeast extract in 1 L Sludge fluid. The YAML stores a single 5.95886 G_PER_L row. | Both normalized duplicate inputs; duplicate cleanup. |
| Major | Source water was dropped. | DSMZ 1084 lists 1000 ml distilled water in the final medium. The YAML has no Distilled water ingredient. | Both normalized duplicate inputs; MediaDive importer and KOMODO DSMZ enrichment. |
| Minor | Sludge fluid preparation lost its stock scope. | MediaDive solution 208 owns the sludge gassing, 37 C incubation, centrifugation, autoclaving, and 8-12 C storage instructions. The YAML stores them as final-medium `preparation_steps` step 2. | `data/normalized_yaml/archaea/methermicoccus_methanogen_medium.yaml`; MediaDive importer. |
| Minor | KOMODO duplicate metadata is inconsistent with DSMZ 1084. | The source duplicate `methermicoccus_medium.yaml` is enriched from DSMZ medium 1084 but its provenance note says `Aerobic: Yes`, while DSMZ 1084 is prepared under N2/CO2 and sterile anoxic stocks. | `data/normalized_yaml/archaea/methermicoccus_medium.yaml`; KOMODO DSMZ enrichment. |

## Recommended Edits

1. Preserve Sludge fluid as a 5 ml scoped stock addition sourced from MediaDive solution 208.
2. Keep the 2 g final-medium yeast extract row separate from the 4 g Sludge fluid yeast extract row.
3. Restore the 1000 ml final-medium water row.
4. Scope the Sludge fluid preparation and storage step to Sludge fluid.
5. Correct or drop the KOMODO `Aerobic: Yes` note when enriching KOMODO duplicates from DSMZ anaerobic media.
6. Regenerate `data/merge_yaml/merged/methermicoccus_methanogen_medium.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated record.
- Diff the regenerated record against DSMZ/MediaDive 1084 and verify that Sludge fluid remains a 5 ml solution reference with its own sludge and yeast-extract recipe.
- Verify that Yeast extract appears in the final medium and Sludge fluid as two scoped rows rather than one summed top-level ingredient.
- Search ignored and generated files for the exact `Aerobic: Yes` string in `methermicoccus_medium` and confirm it is gone or only present in archived reports.

## Additional Notes

- Empty optional evidence and discussion fields were not treated as defects.
- Exact owner searches used `rg --no-ignore --hidden`, so ignored files were included when resolving `CultureMech:000246`, `CultureMech:003736`, and the two normalized owner files.
