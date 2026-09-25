# YAML Record Review: nsc3_medium_with_acetate

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/nsc3_medium_with_acetate.yaml
- Started UTC: 2026-09-24T17:59:21Z
- Finished UTC: 2026-09-24T18:00:52Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| CultureMech ID | CultureMech:000705 |
| Name | nsc3_medium_with_acetate |
| Original name | NSC3-MEDIUM WITH ACETATE |
| Category | bacterial |
| Media term | mediadive.medium:1246 / NSC3-MEDIUM WITH ACETATE |
| Generated path | data/merge_yaml/merged/nsc3_medium_with_acetate.yaml |
| Maintained source | data/normalized_yaml/bacterial/nsc3_medium_with_acetate.yaml |
| Merge fingerprint | 0d6400cd5f9564b2ac829e124498b95bf0cd823688dec17fd729a1455d144016 |
| Merged from | nsc3_medium_with_acetate |

This is a generated merged recipe from a single MediaDive/DSMZ import. Future corrections belong in the maintained MediaDive-normalized source, followed by merged-record regeneration.

## Validation

| Check | Result |
| --- | --- |
| Open schema validation with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/nsc3_medium_with_acetate.yaml` | Passed; exited 0 with no diagnostics. |
| Strict validation with `scripts/validate_strict.py data/merge_yaml/merged/nsc3_medium_with_acetate.yaml --out /private/tmp/nsc3_medium_with_acetate.strict.tsv --workers 1 --quiet` | Passed; the TSV contained only the header line. |
| Reference validation with `linkml-reference-validator validate data data/merge_yaml/merged/nsc3_medium_with_acetate.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 total checks and no failures. |
| Term validation with `linkml-term-validator validate-data data/merge_yaml/merged/nsc3_medium_with_acetate.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented history validator validates standalone `history/` entries, not embedded generated `MediaRecipe.curation_history`. |

## Identity and Grounding

The record has the correct DSMZ/MediaDive identity for DSMZ Medium 1246, `NSC3-MEDIUM WITH ACETATE`. Its bacterial category, defined composition, solid agar state, 8.5-9.0 pH range, source PDF link, and base medium label agree with the DSMZ 1246 source.

An ignored-file-inclusive search for `mediadive.medium:1246`, `DSMZ Medium 1246`, `NSC3-MEDIUM WITH ACETATE`, and `nsc3_medium_with_acetate` across `data/normalized_yaml` and `data/merge_yaml/merged` found only the maintained MediaDive source, its index entries, and this generated record. I found no stranded TOGO/JCM/NBRC mirror for this source in those generated or normalized files.

## Evidence

The generated rows for Na2S x 9 H2O, NH4Cl, K2HPO4, NaHCO3, NaCl, Na-acetate, agar, and the pH-adjustment step are supported by DSMZ 1246 Solution A.

The generated EDTA, FeSO4 x 7 H2O, ZnSO4 x 7 H2O, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O rows are not supported as final per-liter ingredients at the recorded concentrations. The DSMZ PDF and MediaDive JSON put 1 ml Trace element solution SL-4 in Solution A; SL-4 is a separate stock with 0.50 g EDTA, 0.20 g FeSO4 x 7 H2O, 100 ml Trace element solution SL-6, and water to 1000 ml; SL-6 is another nested stock with the zinc, manganese, boron, cobalt, copper, nickel, and molybdate salts in 1000 ml water.

## Completeness

The top-level base medium is otherwise complete for the DSMZ formula: all Solution A salts, acetate, agar, source pH range, and the pre-autoclave pH instruction are present.

The trace-element stock hierarchy is missing. The generated record should contain a 1 ml/L Trace element solution SL-4 addition with nested EDTA, ferrous sulfate heptahydrate, 100 ml/L Trace element solution SL-6, and water, and SL-6 should own the trace-metal salts instead of exposing them as top-level final medium ingredients.

Empty target-organism and citation slots are acceptable for this provider medium. The imported DSMZ formula does not provide strain-specific target-organism evidence.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| Major | The MediaDive/DSMZ import flattens nested Trace element solutions SL-4 and SL-6 into final top-level ingredients at stock concentrations. | DSMZ 1246 adds 1 ml Trace element solution SL-4 to Solution A, while SL-4 and SL-6 are separate one-liter stock recipes. The generated record stores EDTA, FeSO4 x 7 H2O, ZnSO4 x 7 H2O, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O directly as `G_PER_L` medium ingredients. | MediaDive import normalization for `data/normalized_yaml/bacterial/nsc3_medium_with_acetate.yaml`, then merged-record regeneration. |

## Recommended Edits

1. Update the MediaDive/DSMZ normalization that generated `data/normalized_yaml/bacterial/nsc3_medium_with_acetate.yaml` so DSMZ 1246 retains a 1 ml/L Trace element solution SL-4 addition in Solution A.
2. Model Trace element solution SL-4 as its own nested stock containing EDTA, FeSO4 x 7 H2O, 100 ml/L Trace element solution SL-6, and water to 1000 ml.
3. Model Trace element solution SL-6 as a nested stock that owns the zinc, manganese, boron, cobalt, copper, nickel, and molybdate salts currently flattened into the recipe top level.

## Follow-up Checks

1. Regenerate normalized and merged YAML, then verify the regenerated NSC3 acetate record has only Solution A ingredients at the top level and keeps SL-4/SL-6 inside the solution tree.
2. Run the focused open schema, strict, reference, and term validators on `data/merge_yaml/merged/nsc3_medium_with_acetate.yaml`.
3. Search with ignored files included for `mediadive.medium:1246` and `NSC3-MEDIUM WITH ACETATE` to confirm no duplicate generated record was introduced.

## Additional Notes

None found.
