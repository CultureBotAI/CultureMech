# YAML Record Review: METHYLOFERULA STELLATA MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methyloferula_stellata_medium__4fc16e2e.yaml
- Started UTC: 2026-09-24T05:36:44Z
- Finished UTC: 2026-09-24T05:37:55Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methyloferula_stellata_medium__4fc16e2e.yaml`, a generated `MediaRecipe` for `CultureMech:000779` with `name: methyloferula_stellata_medium`, `original_name: METHYLOFERULA STELLATA MEDIUM`, pH 5.0-5.8, and source grounding `mediadive.medium:1322`.

The record was merged from one normalized input:

- `data/normalized_yaml/bacterial/methyloferula_stellata_medium.yaml`

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methyloferula_stellata_medium__4fc16e2e.yaml` | Passed; exited 0 with no diagnostics. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methyloferula_stellata_medium__4fc16e2e.yaml --out /private/tmp/methyloferula_stellata_medium__4fc16e2e.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methyloferula_stellata_medium__4fc16e2e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methyloferula_stellata_medium__4fc16e2e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The DSMZ identity is correct. DSMZ/MediaDive medium 1322 is `METHYLOFERULA STELLATA MEDIUM`, a defined liquid medium with final pH 5.0-5.8.

The stock structure is not correct. DSMZ 1322 adds 3 ml FeEDTA solution and 1 ml Trace elements to a final main medium. The generated record has no `solutions` entries, flattens both stock recipes, sums their FeSO4 x 7 H2O rows, and represents both stock concentrations as if they were final concentrations.

## Evidence

Supported source claims:

- DSMZ/MediaDive 1322 supports the record's DSMZ identity, pH 5.0-5.8, direct KH2PO4, ammonium sulfate, MgSO4 x 7 H2O, CaCl2 x 2 H2O, NaCl, methanol, and distilled-water rows.
- DSMZ/MediaDive 1322 supports 3 ml FeEDTA solution and 1 ml Trace elements as stock additions.
- DSMZ/MediaDive 1322 supports preparing the medium without methanol in closed vessels, adding 10 ml/L filter-sterilized methanol after cooling to about 30 C, pH adjustment with H3PO4, and shaking incubation.

Unsupported or over-scoped generated claims:

- EDTA through Na2MoO4 are Trace elements constituents, not final top-level ingredients.
- Na2-EDTA and the 1.54 g/L FeSO4 x 7 H2O row are FeEDTA solution constituents, not final top-level ingredients.
- The generated 3.54 G_PER_L FeSO4 x 7 H2O row is the sum of 2.0 g/L from Trace elements and 1.54 g/L from FeEDTA solution.

## Completeness

The schema-optional evidence, discussions, growth, target organism, and solution arrays are empty; evidence, discussion, and growth omissions are not defects by themselves.

Consequential gaps:

- FeEDTA solution 2649 and Trace elements 2648 are absent as scoped 3 ml and 1 ml stock additions.
- The 1000 ml final-medium water row and both stock water rows are absent.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | FeEDTA solution and Trace elements were flattened into final-medium ingredients. | DSMZ 1322 adds 3 ml FeEDTA solution and 1 ml Trace elements. The YAML has no `solutions` array and stores all stock children as top-level ingredients. | `data/normalized_yaml/bacterial/methyloferula_stellata_medium.yaml`; MediaDive importer. |
| Major | Duplicate cleanup merged FeSO4 across two stocks. | The source has 2.0 g/L FeSO4 x 7 H2O in Trace elements and 1.54 g/L in FeEDTA solution. The YAML sums them into one 3.54 G_PER_L ingredient. | `data/normalized_yaml/bacterial/methyloferula_stellata_medium.yaml`; duplicate cleanup. |
| Major | Source water rows were dropped. | DSMZ 1322 has a 1000 ml final-medium water row plus 1000 ml water rows in Trace elements and FeEDTA solution. The YAML has no Distilled water row. | `data/normalized_yaml/bacterial/methyloferula_stellata_medium.yaml`; MediaDive importer. |

## Recommended Edits

1. Preserve FeEDTA solution 2649 and Trace elements 2648 as scoped stock additions at 3 ml and 1 ml.
2. Keep the two FeSO4 x 7 H2O stock rows separate.
3. Restore the final-medium and stock distilled-water rows.
4. Regenerate `data/merge_yaml/merged/methyloferula_stellata_medium__4fc16e2e.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated record.
- Diff the regenerated record against DSMZ/MediaDive 1322 and verify that FeEDTA solution and Trace elements child rows are not emitted as final top-level ingredients.
- Verify that FeSO4 x 7 H2O remains scoped separately in FeEDTA solution and Trace elements.

## Additional Notes

- Empty optional evidence and discussion fields were not treated as defects.
- Exact owner searches used `rg --no-ignore --hidden`, so ignored files were included when resolving `CultureMech:000779` and `data/normalized_yaml/bacterial/methyloferula_stellata_medium.yaml`.
