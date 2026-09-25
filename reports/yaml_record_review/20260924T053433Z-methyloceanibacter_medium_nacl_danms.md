# YAML Record Review: METHYLOCEANIBACTER MEDIUM (NaCl-dANMS)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methyloceanibacter_medium_nacl_danms.yaml
- Started UTC: 2026-09-24T05:33:28Z
- Finished UTC: 2026-09-24T05:34:33Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methyloceanibacter_medium_nacl_danms.yaml`, a generated `MediaRecipe` for `CultureMech:001092` with `name: methyloceanibacter_medium_nacl_danms`, `original_name: METHYLOCEANIBACTER MEDIUM (NaCl-dANMS)`, pH 7.8, and source grounding `mediadive.medium:1610`.

The record was merged from one normalized input:

- `data/normalized_yaml/bacterial/methyloceanibacter_medium_nacl_danms.yaml`

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methyloceanibacter_medium_nacl_danms.yaml` | Passed; exited 0. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methyloceanibacter_medium_nacl_danms.yaml --out /private/tmp/methyloceanibacter_medium_nacl_danms.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methyloceanibacter_medium_nacl_danms.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methyloceanibacter_medium_nacl_danms.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The medium identity is correct. DSMZ/MediaDive medium 1610 is `METHYLOCEANIBACTER MEDIUM (NaCl-dANMS)`, a defined liquid medium with pH 7.8.

The formulation graph is not correct. DSMZ 1610 is prepared from nine numbered stock solutions plus Trace element solution and post-autoclave methanol. The record has no `solutions` array, stores the stock recipes as if they were final-medium ingredients, and leaves final preparation steps that refer to `solution 1` through `solution 9` even though those named solutions no longer exist in the record.

## Evidence

Supported source claims:

- DSMZ/MediaDive 1610 supports the DSMZ identity, pH 7.8, filter-sterilized post-autoclave methanol, Solution 1 through Solution 9 additions, 1 ml Trace element solution, and the pH/autoclave preparation steps.
- DSMZ/MediaDive 1610 supports the Trace element solution and Solution 1 recipes, including their preparation or storage notes.
- MediaDive preserves the 10 mM CuSO4 x 5 H2O stock as solution 5750; the DSMZ PDF heading also names CuSO4 x 5 H2O although the inspected PDF body text appears to repeat KH2PO4 in that row.

Unsupported or over-scoped generated claims:

- EDTA through Na2MoO4 x 2 H2O are Trace element solution constituents, not top-level final ingredients.
- MgSO4 x 6 H2O and CaCl2 x 2 H2O belong to Solution 1; Fe(III)-EDTA belongs to Solution 2; KH2PO4 belongs to Solution 3; CuSO4 x 5 H2O belongs to Solution 4; NaCl belongs to Solution 5; NH4Cl belongs to Solution 6; KNO3 belongs to Solution 7; HEPES belongs to Solution 8; and the lanthanide chlorides belong to Solution 9.
- The final medium uses measured volumes of each stock, so stock G_PER_L concentrations are not final-medium G_PER_L concentrations.
- Preparation step 10 is a Trace element solution storage instruction, and step 11 is Solution 1 preparation, but both are emitted at final-medium level.

## Completeness

The schema-optional evidence, discussions, growth, target organism, and solution arrays are empty; evidence, discussion, and growth omissions are not defects by themselves.

Consequential gaps:

- Solution 1 through Solution 9 and Trace element solution are all absent as scoped stocks.
- Every 1000 ml stock water row is absent, and the final-medium distilled-water context is only implicit in the first preparation step.
- The record does not make post-autoclave methanol distinguishable from autoclaved stock additions except through free text.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Ten DSMZ stocks were flattened into top-level final ingredients. | MediaDive 1610 defines Trace element solution plus Solutions 1-9 and adds measured ml amounts of each to the final medium. The YAML has no `solutions` array and stores every stock child in `ingredients`. | `data/normalized_yaml/bacterial/methyloceanibacter_medium_nacl_danms.yaml`; MediaDive importer. |
| Major | Stock concentrations are presented as final concentrations. | The final medium uses 20 ml Solution 1, 0.4 ml Solution 2, 10 ml Solution 3, 0.1 ml Solution 4, 100 ml Solution 5, 20 ml each of Solutions 6 and 7, 50 ml Solution 8, 1 ml Solution 9, and 1 ml Trace element solution. The YAML stores only the undiluted stock G_PER_L ingredient values. | `data/normalized_yaml/bacterial/methyloceanibacter_medium_nacl_danms.yaml`; MediaDive importer. |
| Major | Stock water rows were dropped. | DSMZ/MediaDive 1610 list 1000 ml distilled water in every stock recipe. The YAML has no Distilled water row. | `data/normalized_yaml/bacterial/methyloceanibacter_medium_nacl_danms.yaml`; MediaDive importer. |
| Minor | Two stock-specific instructions are scoped to the final medium. | The 4 C dark-storage instruction belongs to Trace element solution, and the 700 ml dissolution instruction belongs to Solution 1. The YAML appends both after final-medium methanol addition. | `data/normalized_yaml/bacterial/methyloceanibacter_medium_nacl_danms.yaml`; MediaDive importer. |

## Recommended Edits

1. Preserve Trace element solution and Solutions 1-9 as scoped stock additions with their MediaDive solution IDs.
2. Preserve the final assembly volumes for each numbered stock instead of promoting stock G_PER_L concentrations to final ingredients.
3. Restore the 1000 ml stock water rows.
4. Scope the Trace element storage instruction and Solution 1 dissolution instruction to their owning stock recipes.
5. Regenerate `data/merge_yaml/merged/methyloceanibacter_medium_nacl_danms.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated record.
- Diff the regenerated record against DSMZ/MediaDive 1610 and verify that all nine numbered solutions plus Trace element solution appear exactly once as final assembly stocks.
- Verify that the preparation text still describes the 20/100/50/20/20/10/1/0.4/0.1 ml stock-addition sequence and the 10 ml post-autoclave methanol addition.
- Inspect DSMZ solution 4 versus MediaDive solution 5750 and preserve the likely CuSO4 x 5 H2O correction explicitly if the DSMZ PDF body text remains inconsistent with its heading.

## Additional Notes

- Empty optional evidence and discussion fields were not treated as defects.
- Exact owner searches used `rg --no-ignore --hidden`, so ignored files were included when resolving `CultureMech:001092` and `data/normalized_yaml/bacterial/methyloceanibacter_medium_nacl_danms.yaml`.
