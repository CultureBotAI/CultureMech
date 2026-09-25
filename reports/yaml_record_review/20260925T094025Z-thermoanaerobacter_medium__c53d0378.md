# YAML Record Review: THERMOANAEROBACTER MEDIUM
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoanaerobacter_medium__c53d0378.yaml`
- Started UTC: `2026-09-25T09:40:25Z`
- Finished UTC: `2026-09-25T09:41:35Z`
- Verdict: pass with minor issues

## Target
Generated bacterial recipe `CultureMech:001750`, `thermoanaerobacter_medium`, with medium term `mediadive.medium:61` and label `THERMOANAEROBACTER MEDIUM`.

It merges the MediaDive DSMZ 61 source `thermoanaerobacter_medium` with KOMODO aliases `clostridium_thermohydrosulfuricum_medium` and `for_dsm_8686_and_dsm_8690`.

## Validation
- LinkML schema validation: passed; `linkml-validate` reported `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file with 0 files containing errors and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` reported `Validation passed`.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The record is correctly grounded to DSMZ Medium 61, `THERMOANAEROBACTER MEDIUM`, and the two KOMODO aliases are plausible DSMZ 61 source-equivalent records.

The same DSMZ 61 PDF is also represented by TOGO source `TOGO:M2541`, emitted separately as `data/merge_yaml/merged/THERMOANAEROBACTER_MEDIUM.yaml`.

The reviewed target branch has correct CHEBI groundings for the defined salts and carbon source, including sucrose, sodium sulfite, and sodium thiosulfate pentahydrate.

## Evidence
DSMZ Medium 61 and MediaDive medium 61 specify a single main solution containing Tryptone, yeast extract, sodium resazurin, FeSO4 x 7 H2O, sucrose, Na2SO3, Na2S2O3 x 5 H2O, and distilled water.

The generated MediaDive/KOMODO record preserves that ingredient set, quantities, pH range, and anoxic preparation step, including the source instruction to add ferrous sulfate before dispensing and sucrose, sulfite, and thiosulfate from filtered anoxic stock solutions after autoclaving.

Exact source-identity search found a TOGO M2541 branch for the same DSMZ 61 PDF. That TOGO branch should not be merged as-is: its generated record has `Na2SeO3 x 5 H2O` at `0.08 G_PER_L` where DSMZ and MediaDive specify `Na2S2O3 x 5 H2O`.

## Completeness
The target MediaDive/KOMODO branch contains the complete DSMZ 61 base recipe and preparation text visible in MediaDive and the DSMZ PDF.

The separate TOGO M2541 branch drops the structured preparation step and should be corrected before it is merged into the canonical DSMZ 61 identity.

## Findings
1. Minor issue: TOGO M2541 remains split from this MediaDive/KOMODO DSMZ 61 identity.
2. Minor issue: the unmerged TOGO M2541 branch has a thiosulfate-to-selenite substitution that must be fixed before source-identity merging.

## Recommended Edits
1. Correct `TOGO_M2541_Thermoanaerobacter_Medium` in `data/normalized_yaml`, not the generated TOGO branch, so the DSMZ thiosulfate ingredient is `Na2S2O3 x 5 H2O`.
2. Preserve the filtered anoxic sucrose, sulfite, and thiosulfate stock-addition preparation semantics in the TOGO source.
3. Merge `TOGO:M2541` with `mediadive.medium:61`, `komodo.medium:61`, and `komodo.medium:61.1` only after the TOGO chemistry is fixed.

## Follow-up Checks
After the TOGO correction and merge regeneration, re-run schema, strict, reference, and term validation.

Run an exact duplicate search with ignored files included for `TOGO:M2541`, `mediadive.medium:61`, `komodo.medium:61`, `komodo.medium:61.1`, and `DSMZ_Medium61.pdf` and confirm that DSMZ 61 regenerates as one canonical output whose sulfur rows are `Na2SO3` and `Na2S2O3 x 5 H2O`, not selenite.

## Additional Notes
Exact duplicate-source searches included ignored files.
