# YAML Record Review: BACTO MIDDLEBROOK 7H9 BROTH

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACTO_MIDDLEBROOK_7H9_BROTH.yaml
- Started UTC: 2026-09-21T18:27:15Z
- Finished UTC: 2026-09-21T18:27:15Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002016 |
| Name | bacto_middlebrook_7h9_broth |
| Original name | BACTO MIDDLEBROOK 7H9 BROTH |
| Maintained input | data/normalized_yaml/bacterial/bacto_middlebrook_7h9_broth.yaml |
| Primary checked source | DSMZ Medium 857 PDF |
| Generated status | Generated merge under data/merge_yaml/merged from one normalized input |

This record is DSMZ Medium 857, Bacto Middlebrook 7H9 Broth with 100 ml ADC Enrichment added aseptically after autoclaving.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACTO_MIDDLEBROOK_7H9_BROTH.yaml` | Passed: `No issues found` |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BACTO_MIDDLEBROOK_7H9_BROTH.yaml --out /private/tmp/BACTO_MIDDLEBROOK_7H9_BROTH.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 ERROR rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BACTO_MIDDLEBROOK_7H9_BROTH.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BACTO_MIDDLEBROOK_7H9_BROTH.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented; `just validate-history` targets standalone `history/` files. |

The repository `just` validators were not used for this target because the project environment currently fails while syncing the Python 3.13 dependency set. The equivalent no-project validators above ran against the checked-in schema and target file.

## Identity and Grounding

The DSMZ Medium 857 identity and pH range are correct, and the first twelve ingredient rows match the Bacto Middlebrook 7H9 dehydrated-powder formula listed by DSMZ.

The maintained record then diverges from the source:

- The top-level `notes` and the Tryptone, Yeast extract, and Sodium chloride rows were enriched with LB Miller commercial-product metadata and an unrelated laboratorynotes.com URL. DSMZ 857 does not cite LB Miller and does not contain 10 g/L tryptone, 5 g/L yeast extract, or 10 g/L sodium chloride as ADC ingredients.
- DSMZ defines ADC Enrichment as a separate 100 ml addition. The record flattens only Dextrose and Catalase, omits Albumin Fraction V, Bovine and ADC water, and inflates the ADC values tenfold.
- The source `Catalase (Beef)` ingredient has been shortened to generic `Catalase`, losing the source's supplied material label.

## Evidence

DSMZ supports these Bacto Middlebrook 7H9 powder rows as grams per liter of final solution: 0.5 ammonium sulfate, 1.0 monopotassium phosphate, 2.5 disodium phosphate, 0.1 sodium citrate, 0.05 magnesium sulfate, 0.0005 calcium chloride, 0.001 zinc sulfate, 0.001 copper sulfate, 0.5 L-glutamic acid, 0.04 ferric ammonium citrate, 0.001 pyridoxine, and 0.0005 biotin. Their sum is approximately the 4.7 g/L powder amount stated by DSMZ.

DSMZ supports a 100 ml ADC Enrichment addition containing 5 g Albumin Fraction V, Bovine, 2 g Dextrose, 0.0003 g Catalase (Beef), and 100 ml distilled water. Because the whole 100 ml enrichment is added to one liter of final medium, the current 20 g/L Dextrose and 0.003 g/L Catalase rows are 10-fold too high.

DSMZ also supports 900 ml distilled and deionized water with 2 ml glycerol before autoclaving, cooling to 50-55 C, and aseptic addition of 100 ml ADC Enrichment. The preparation prose retains this instruction, but the ingredient structure omits both the 900 ml water and the 2 ml glycerol.

## Completeness

- Albumin Fraction V, Bovine is missing from the ADC Enrichment.
- The record has no 100 ml water row for ADC Enrichment and no 900 ml distilled/deionized water row for the base medium.
- Glycerol at 2 ml/L is missing.
- The ADC Enrichment boundary is absent; its dextrose and catalase rows are mixed with the powder formula and unrelated LB rows.
- Empty organism, strain, growth-evidence, variant, and publication-reference fields are not automatically defective because the inspected DSMZ source is a medium protocol.

A gitignore-independent search of `reports/yaml_record_review` for `BACTO_MIDDLEBROOK_7H9_BROTH|bacto_middlebrook_7h9_broth|Middlebrook_7H9` found no existing report for this target before this report was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Unrelated LB Miller metadata and ingredients were grafted onto the 7H9 record. | The record has LB Medium supplier notes and 10 g/L Tryptone, 5 g/L Yeast extract, and 10 g/L Sodium chloride rows. DSMZ Medium 857 does not contain those rows. | data/normalized_yaml/bacterial/bacto_middlebrook_7h9_broth.yaml and the commercial-product enrichment that produced the LB rows |
| Major | ADC Enrichment is incomplete and inflated. | DSMZ lists Albumin Fraction V, Bovine 5 g, Dextrose 2 g, Catalase (Beef) 0.0003 g, and 100 ml water for ADC Enrichment; the record lacks albumin and water and stores Dextrose 20 g/L and Catalase 0.003 g/L. | DSMZ import of nested ADC Enrichment |
| Major | Required water and glycerol for the base medium are missing. | DSMZ says to suspend the 7H9 powder in 900 ml distilled/deionized water containing 2 ml glycerol before autoclaving. Neither appears as an ingredient row. | data/normalized_yaml/bacterial/bacto_middlebrook_7h9_broth.yaml |
| Major | The ADC Enrichment stock boundary is absent. | DSMZ scopes albumin, dextrose, catalase, and 100 ml water under `ADC Enrichment`, then adds the stock aseptically after cooling. The record flattens dextrose and catalase into the parent list. | DSMZ import of nested enrichment solutions |
| Minor | Catalase lost its source-specific material label. | DSMZ says `Catalase (Beef)`; the YAML says only `Catalase`. The exact beef catalase term is unresolved locally, so the source label should be preserved even if grounding stays unresolved. | DSMZ import normalization |

## Recommended Edits

1. Remove the LB Miller note plus the unsupported 10 g/L Tryptone, 5 g/L Yeast extract, and 10 g/L Sodium chloride rows from the Middlebrook 7H9 record.
2. Represent ADC Enrichment as a separate 100 ml post-autoclave addition containing 5 g Albumin Fraction V, Bovine, 2 g Dextrose, 0.0003 g Catalase (Beef), and 100 ml distilled water.
3. Fix the ADC arithmetic so final Dextrose is 2 g/L and final beef catalase is 0.0003 g/L if the stock is flattened.
4. Add 900 ml distilled/deionized water and 2 ml glycerol to the base-medium preparation.
5. Preserve the source label `Catalase (Beef)` and leave it explicitly ungrounded unless an exact packaged mapping is added.
6. Regenerate `data/merge_yaml/merged/BACTO_MIDDLEBROOK_7H9_BROTH.yaml` and generated pages from the corrected normalized record.

## Follow-up Checks

- Rerun the open-schema, strict, reference, and term validators on the edited normalized input and regenerated merge.
- Rerun `just verify-merges` and `just audit-merge-freshness` after regeneration to prove the one-source generated record is fresh.
- Search exactly for `LB Medium` in the corrected Middlebrook 7H9 YAML to ensure the unrelated LB enrichment was removed.
- Manually compare the regenerated record against DSMZ 857 to confirm the powder formula totals 4.7 g/L, the ADC Enrichment is present at 100 ml/L, and dextrose/catalase were not multiplied by 10.

## Additional Notes

- A broader ignored-inclusive search for the LB note found the phrase in many other normalized and generated records; this report only establishes that it is unsupported in `bacto_middlebrook_7h9_broth`.
- The exact ignored-inclusive pre-report search covered `reports/yaml_record_review`; no prior report for this target was present.
- Catalase has a generic `NCIT:C61062` mapping in the packaged label index, but this review did not find an exact packaged row for DSMZ's `Catalase (Beef)`.
