# YAML Record Review: METHYLOCYSTIS MEDIUM (NLS)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methylocystis_medium_nls.yaml
- Started UTC: 2026-09-24T05:35:37Z
- Finished UTC: 2026-09-24T05:36:43Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methylocystis_medium_nls.yaml`, a generated `MediaRecipe` for `CultureMech:001219` with `name: methylocystis_medium_nls`, `original_name: METHYLOCYSTIS MEDIUM (NLS)`, pH 7.0, and source grounding `mediadive.medium:1741`.

The record was merged from one normalized input:

- `data/normalized_yaml/bacterial/methylocystis_medium_nls.yaml`

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methylocystis_medium_nls.yaml` | Passed; exited 0 with no diagnostics. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methylocystis_medium_nls.yaml --out /private/tmp/methylocystis_medium_nls.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methylocystis_medium_nls.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methylocystis_medium_nls.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The DSMZ identity is correct. DSMZ/MediaDive medium 1741 is `METHYLOCYSTIS MEDIUM (NLS)`, a defined liquid medium with final pH 7.0.

The recipe structure is not correct. DSMZ 1741 is a five-stock assembly: 50 ml Solution A, 50 ml Solution B, 0.2 ml Solution C, 0.5 ml Solution D, and 10 ml filter-sterilized Solution E are brought to 1 L final volume. The generated YAML has no `solutions` entries and stores all Solution A-E constituents as final top-level ingredients.

## Evidence

Supported source claims:

- DSMZ/MediaDive 1741 supports the record's DSMZ identity, pH 7.0, final assembly volumes, methane headspace, 121 C autoclaving, and filter-sterile post-autoclave addition of Solution E.
- DSMZ/MediaDive 1741 support Solution A and Solution B as base stocks, Solution C as Acidic Trace Elements Solution, Solution D as Alkaline Trace Elements Solution, and Solution E as Wolfe's Vitamin Solution from medium 141.

Unsupported or over-scoped generated claims:

- MgSO4 x 7 H2O, KNO3, and CaCl2 x 2 H2O belong to Solution A, not the final medium at undiluted stock concentration.
- KH2PO4 and Na2HPO4 belong to Solution B.
- HCl through Ce(NO3)3 x 6 H2O belong to the 0.2 ml/L acidic trace stock.
- NaOH through Na2MoO4 x 2 H2O belong to the 0.5 ml/L alkaline trace stock.
- 4-Aminobenzoic Acid through Vitamin B12 belong to the 10 ml/L Wolfe vitamin stock.

## Completeness

The schema-optional evidence, discussions, growth, target organism, and solution arrays are empty; empty optional slots were not treated as defects.

Consequential gaps:

- Solution A, Solution B, Solution C, Solution D, and Solution E are absent as scoped stock additions.
- Distilled water rows from Solution C, Solution D, and Solution E are absent, and the final bring-up-to-1-L water context is only a preparation step.
- Solution A, Solution B, and Solution C preparation or heading text appears as final-medium steps 8 through 10.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Five DSMZ stock solutions were flattened into final-medium ingredients. | MediaDive 1741 adds 50 ml Solution A, 50 ml Solution B, 0.2 ml Solution C, 0.5 ml Solution D, and 10 ml Solution E. The YAML has no `solutions` array and stores all stock constituents as top-level ingredients. | `data/normalized_yaml/bacterial/methylocystis_medium_nls.yaml`; MediaDive importer. |
| Major | Stock concentrations are represented as final concentrations. | The final recipe uses ml amounts of Solution A-E, but the YAML gives their undiluted G_PER_L stock values as if added directly to the final liter. | `data/normalized_yaml/bacterial/methylocystis_medium_nls.yaml`; MediaDive importer. |
| Major | Explicit stock water rows were dropped. | DSMZ/MediaDive 1741 list 1000 ml distilled water in Solution C, Solution D, and Solution E. No Distilled water row is present in the YAML. | `data/normalized_yaml/bacterial/methylocystis_medium_nls.yaml`; MediaDive importer. |
| Minor | Stock preparation text lost its scope. | The Solution A/B dissolution instructions and the Solution C per-liter heading are emitted as final-medium steps 8-10. | `data/normalized_yaml/bacterial/methylocystis_medium_nls.yaml`; MediaDive importer. |

## Recommended Edits

1. Preserve Solution A-E as scoped stock additions with their MediaDive solution IDs.
2. Retain final assembly volumes of 50 ml, 50 ml, 0.2 ml, 0.5 ml, and 10 ml instead of promoting stock concentrations to final ingredients.
3. Restore explicit distilled-water rows for Solution C, Solution D, and Solution E.
4. Scope Solution A, Solution B, and Solution C preparation text to their stock recipes.
5. Regenerate `data/merge_yaml/merged/methylocystis_medium_nls.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated record.
- Diff the regenerated record against DSMZ/MediaDive 1741 and verify that no Solution A-E constituents are final top-level ingredients.
- Verify that Solution E remains a 10 ml post-autoclave filter-sterilized vitamin stock and that the methane headspace/autoclave steps remain in the final-medium preparation.

## Additional Notes

- Empty optional evidence and discussion fields were not treated as defects.
- Exact owner searches used `rg --no-ignore --hidden`, so ignored files were included when resolving `CultureMech:001219` and `data/normalized_yaml/bacterial/methylocystis_medium_nls.yaml`.
