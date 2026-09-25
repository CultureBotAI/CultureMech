# YAML Record Review: BACTO MARINE BROTH WITH NA-ACETATE

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bacto_marine_broth_with_na_acetate.yaml
- Started UTC: 2026-09-21T18:25:52Z
- Finished UTC: 2026-09-21T18:25:52Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:015339 |
| Name | bacto_marine_broth_with_na_acetate |
| Original name | BACTO MARINE BROTH WITH NA-ACETATE |
| Maintained input | data/normalized_yaml/specialized/bacto_marine_broth_with_na_acetate.yaml |
| Primary checked source | DSMZ Medium 1354 PDF |
| Generated status | Generated merge under data/merge_yaml/merged from one normalized input |

This record is the DSMZ Medium 1354 Marine Broth 2216 formulation with 10 g/L sodium acetate.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bacto_marine_broth_with_na_acetate.yaml` | Passed: `No issues found` |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bacto_marine_broth_with_na_acetate.yaml --out /private/tmp/bacto_marine_broth_with_na_acetate.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 ERROR rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bacto_marine_broth_with_na_acetate.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bacto_marine_broth_with_na_acetate.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented; `just validate-history` targets standalone `history/` files. |

The repository `just` validators were not used for this target because the project environment currently fails while syncing the Python 3.13 dependency set. The equivalent no-project validators above ran against the checked-in schema and target file.

## Identity and Grounding

The ID, label, source accession, category, pH range, and 10 g/L sodium-acetate supplement agree with DSMZ Medium 1354. The six trace salts that were milligram rows in DSMZ were already correctly converted to g/L in this DSMZ-derived normalized record.

The physical-state identity is too narrow. DSMZ gives a broth recipe and then states that the medium may be solidified with 15 g/L agar. The current record sets `physical_state: SOLID_AGAR` and always includes 15 g/L agar, which makes the optional solid form look mandatory.

Grounding is incomplete for the complex nutrients even though exact local mappings are present. The packaged label index maps `Bacto peptone` to `MICRO:0000178` and maps yeast-extract labels, including `Bacto yeast extract`, to `FOODON:03315426`.

## Evidence

DSMZ Medium 1354 supports these direct grams-per-liter amounts: 5 g Bacto peptone, 1 g Bacto yeast extract, 0.10 g Fe(III) citrate, 19.45 g NaCl, 5.90 g anhydrous MgCl2, 3.24 g Na2SO4, 1.80 g CaCl2, 0.55 g KCl, 0.16 g NaHCO3, 0.08 g KBr, 10 g sodium acetate, and 1000 ml distilled water.

DSMZ supports the trace salts only as milligram quantities: 34 mg SrCl2, 22 mg H3BO3, 4 mg Na-silicate, 2.40 mg NaF, 1.60 mg `(NH4)NO3`, and 8 mg Na2HPO4. The generated record correctly represents these as 0.034, 0.022, 0.004, 0.0024, 0.0016, and 0.008 g/L.

The pH range 6.8-8.5 is supported. The generated `preparation_steps` row also preserves DSMZ's commercial Difco Marine Broth 2216 note and the optional 15 g/L agar note.

## Completeness

- DSMZ includes 1000 ml distilled water; the generated record omits it.
- DSMZ explicitly says `Bacto yeast extract`, while the generated row is only `Yeast extract`.
- The optional agar statement is represented as a required ingredient and record-level solid physical state.
- Empty organism, strain, growth-evidence, variant, and publication-reference fields are not automatically defects because the inspected DSMZ source is a medium protocol.

A gitignore-independent search of `reports/yaml_record_review` for `bacto_marine_broth_with_na_acetate|Bacto_Marine_Broth_with_Na_Acetate|Na_Acetate` found no existing report for this target before this report was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Optional agar was promoted to a mandatory solid formulation. | DSMZ 1354 describes agar as optional solidification, but the YAML sets `physical_state: SOLID_AGAR` and includes 15 g/L agar as a top-level ingredient. | data/normalized_yaml/specialized/bacto_marine_broth_with_na_acetate.yaml |
| Major | Distilled water is missing. | DSMZ lists 1000 ml distilled water and the generated ingredient list has no water row. | data/normalized_yaml/specialized/bacto_marine_broth_with_na_acetate.yaml |
| Major | Bacto peptone and yeast extract are missing exact available groundings. | The packaged label index maps exact `Bacto peptone` to `MICRO:0000178` and maps `Bacto yeast extract`/`Yeast extract` to `FOODON:03315426`; both generated rows are ungrounded. | Ingredient grounding in the normalized record |
| Minor | The yeast-extract row lost the supplied Bacto qualifier. | DSMZ lists Bacto yeast extract, while the YAML `preferred_term` is only Yeast extract. | DSMZ import normalization |
| Minor | The source anhydrous MgCl2 form is not preserved in `preferred_term`. | DSMZ says `MgCl2 (anhydrous)`; the YAML uses generic `MgCl2`, though its CHEBI grounding is anhydrous magnesium dichloride. | DSMZ import normalization |

## Recommended Edits

1. Model the base recipe as liquid and move 15 g/L agar into an optional solid-medium variant or another source-supported representation of optional solidification.
2. Add the 1000 ml distilled-water row from DSMZ.
3. Link Bacto peptone and Bacto yeast extract/Yeast extract to their exact packaged label-index terms.
4. Preserve the source label `Bacto yeast extract` unless there is a documented normalization rule that intentionally erases the Bacto product qualifier.
5. Preserve `MgCl2 (anhydrous)` as the supplied source text while keeping exact anhydrous magnesium chloride grounding.
6. Regenerate `data/merge_yaml/merged/bacto_marine_broth_with_na_acetate.yaml` and generated pages from the corrected normalized record.

## Follow-up Checks

- Rerun the open-schema, strict, reference, and term validators on the edited normalized input and regenerated merge.
- Rerun `just verify-merges` and `just audit-merge-freshness` after regeneration to prove the one-source generated record is fresh.
- Manually compare the regenerated record against DSMZ 1354 to confirm the six milligram salts remain converted exactly once.
- Inspect the rendered page to confirm the agar option is visibly optional and does not imply that every use of DSMZ 1354 contains agar.

## Additional Notes

- This record already avoids the TOGO milligram-to-gram error seen in several TOGO Marine Broth imports.
- The exact ignored-inclusive pre-report search covered `reports/yaml_record_review`; no prior report for this target was present.
- No target-organism claims were present to review.
