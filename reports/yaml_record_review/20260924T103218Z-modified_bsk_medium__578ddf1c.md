# YAML Record Review: MODIFIED BSK MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_bsk_medium__578ddf1c.yaml
- Started UTC: 2026-09-24T10:32:18Z
- Finished UTC: 2026-09-24T10:32:18Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_bsk_medium__578ddf1c.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:003244` |
| Name | `modified_bsk_medium` |
| Original name | `MODIFIED BSK MEDIUM` |
| Category | `bacterial` |
| Medium source | JCM / MediaDive `J896` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_bsk_medium.yaml` |
| Generated status | Generated copy of a MediaDive/JCM normalized record with a wrong source volume |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_bsk_medium__578ddf1c.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_bsk_medium__578ddf1c.yaml --out /private/tmp/modified_bsk_medium__578ddf1c.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_bsk_medium__578ddf1c.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_bsk_medium__578ddf1c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_bsk_medium__578ddf1c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The medium identity is coherent: `CultureMech:003244`, `mediadive.medium:J896`, the label, the stored JCM URL, and pH 7.2 identify JCM Medium 896, MODIFIED BSK MEDIUM.

An exact `find data/normalized_yaml -name modified_bsk_medium.yaml` search, which covers ignored files, found one maintained owner at `data/normalized_yaml/bacterial/modified_bsk_medium.yaml`.

## Evidence

JCM `GRMD=896` is still live. MediaDive `J896` matches the JCM ingredient amounts but encodes the main solution as 40 ml, which is the rabbit-serum amount, even though the source says to fill the recipe to 584 ml with distilled water.

| Source claim | Record representation | Review |
| --- | --- | --- |
| JCM lists gram amounts for HEPES, Trisodium citrate x 2 H2O, glucose, sodium pyruvate, N-acetyl-D-glucosamine, NaHCO3, MEM alpha Modification, TC Yeastolate, Probumin Universal Grade, and Neopeptone, then instructs filling up to 584 ml with distilled water. | The generated record divides those gram amounts by 40 ml and stores the resulting values as grams per liter; HEPES is `75 G_PER_L` from 3 g / 40 ml. | Wrong final-volume basis inherited from MediaDive. |
| JCM adds 40 ml sterile non-hemolyzed young rabbit serum. | The record stores `Rabbit serum` as `40 G_PER_L`. | Unsupported unit and volume representation. |
| JCM uses specific products: MEM alpha Modification from BioWest, TC Yeastolate from BD-Difco, Probumin Universal Grade from Millipore, Neopeptone from BD-Difco, and Pel-Freez rabbit serum code No. 31125. | The record drops all supplier/product attributes except the generic preferred labels for MEM alpha Modification, Yeast extract, Probumin Universal Grade, Neopeptone, and Rabbit serum. | Unsupported loss of source specificity. |
| JCM instructs pH 7.2 adjustment with NaOH, filling to 584 ml with distilled water, and filter sterilization with a 0.22 um PES filter. | The preparation step preserves the actions but contains mojibake in the filter size and there is no structured distilled-water row. | Partial; water is missing and the filter note is corrupted. |
| The source specifies Trisodium citrate x 2 H2O. | The row is grounded to generic `sodium citrate`. | Hydrate-specific source label is not preserved in grounding. |

## Completeness

The generated record is incomplete because the distilled-water fill volume is unstructured and the final concentrations are calculated from the wrong 40 ml volume instead of the 584 ml final volume. It is also incomplete for complex source products whose vendor or formulation qualifier distinguishes them from a generic ingredient label.

Empty target-organism and growth-evidence fields were not treated as defects. JCM 896 and MediaDive `J896` are medium formulation pages, not growth-evidence pages.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Ingredient concentrations were calculated from a 40 ml volume instead of the 584 ml final volume. | JCM says to fill up to 584 ml; MediaDive `J896` stores `volume: 40`, and the generated row values, for example `75 G_PER_L` HEPES from 3 g, use that incorrect volume. | `data/normalized_yaml/bacterial/modified_bsk_medium.yaml`; MediaDive volume import or manual J896 repair. |
| major | Rabbit serum is modeled as grams per liter instead of a 40 ml volume. | JCM lists 40 ml rabbit serum; the record has `40 G_PER_L`. | `data/normalized_yaml/bacterial/modified_bsk_medium.yaml`; MediaDive volume import. |
| major | The distilled-water fill volume is absent. | The source says to fill up to 584 ml with distilled water; there is no water ingredient. | `data/normalized_yaml/bacterial/modified_bsk_medium.yaml`; MediaDive water import. |
| major | Several complex ingredient labels lost source-specific product detail. | JCM specifies TC Yeastolate, MEM alpha Modification from BioWest, Probumin Universal Grade from Millipore, Neopeptone from BD-Difco, and a Pel-Freez rabbit-serum product; the generated rows are generic or omit the vendor attributes. | `data/normalized_yaml/bacterial/modified_bsk_medium.yaml`; MediaDive attribute import. |
| minor | The filter size is mojibake in the preparation step. | JCM specifies a 0.22 um PES filter; the generated description has replacement-character mojibake where `u` should be. | `data/normalized_yaml/bacterial/modified_bsk_medium.yaml`; text encoding. |
| minor | Trisodium citrate x 2 H2O is grounded generically. | The source specifies a dihydrate; the record uses `CHEBI:53258` / `sodium citrate`. | `data/normalized_yaml/bacterial/modified_bsk_medium.yaml`; CHEBI grounding. |

## Recommended Edits

1. Re-curate `data/normalized_yaml/bacterial/modified_bsk_medium.yaml` against the JCM page instead of the MediaDive `volume: 40` conversion; calculate ingredient concentrations against 584 ml or preserve source masses with the 584 ml final volume.
2. Model 40 ml rabbit serum as a volume addition, not `40 G_PER_L`.
3. Add the distilled-water fill volume as structured water.
4. Preserve source-specific product labels and vendor attributes for TC Yeastolate, MEM alpha Modification, Probumin Universal Grade, Neopeptone, and Rabbit serum.
5. Repair the filter-sterilization step text to `0.22 um`.
6. Re-ground Trisodium citrate x 2 H2O to a hydrate-specific term or leave it ungrounded until an exact term is available.
7. Regenerate `data/merge_yaml/merged/modified_bsk_medium__578ddf1c.yaml` after the normalized owner is corrected.

## Follow-up Checks

1. Run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/modified_bsk_medium.yaml`.
2. Regenerate `data/merge_yaml/merged/modified_bsk_medium__578ddf1c.yaml` and re-run the same validators on the generated record.
3. Manually compare the regenerated record against JCM `GRMD=896`, checking the 584 ml final volume, 40 ml rabbit-serum addition, pH 7.2, product labels, filter size, and supplier annotations.

## Additional Notes

The JCM `GRMD=896` page still resolves. The MediaDive REST record for `J896` also resolves but appears to expose the source recipe with `volume: 40`, which does not match the JCM fill-to-584-ml instruction.

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
