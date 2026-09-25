# YAML Record Review: ANAEROBIC ALKALINE GLUCOSE MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/anaerobic_alkaline_glucose_medium__bc3ee096.yaml
- Started UTC: 2026-09-21T12:07:28Z
- Finished UTC: 2026-09-21T12:10:03Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/anaerobic_alkaline_glucose_medium__bc3ee096.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:015394`
- Label: `ANAEROBIC ALKALINE GLUCOSE MEDIUM`
- Category: `specialized`
- Source identity: MediaDive `mediadive.medium:J1228`, source `JCM`, original JCM URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228`
- Generated status: generated merge record with fingerprint `bc3ee096a48f2841f9ad12cd1ed2ea323732f8629defffaebf098390ddeda399`
- Merge lineage: one source, `data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml`
- Maintained owner for future record edits: `data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml`; importer-level stock handling and any merge-collapse changes must be fixed in source transforms or merge rules, then the merge output must be regenerated

## Validation

- Open schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anaerobic_alkaline_glucose_medium__bc3ee096.yaml`
  - Result: passed
- Strict schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/anaerobic_alkaline_glucose_medium__bc3ee096.yaml --out /private/tmp/anaerobic_alkaline_glucose_medium__bc3ee096.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/anaerobic_alkaline_glucose_medium__bc3ee096.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 total checks
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/anaerobic_alkaline_glucose_medium__bc3ee096.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed
- Embedded curation history: Not checked. The documented `just validate-history` recipe validates standalone records under `history/`; I did not find a focused embedded `MediaRecipe.curation_history` validator for one merge file.

## Identity and Grounding

The generated merge carries the MediaDive source identity for JCM medium `J1228`, and the inspected MediaDive JSON agrees with the record on the source medium ID, medium name, pH `9.2`, JCM source tag, and JCM link. The JCM page itself is also medium 1228, `ANAEROBIC ALKALINE GLUCOSE MEDIUM`, so the source accession and high-level medium identity are not a sibling-source mixup.

The merge identity is still not canonical: `data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml` is the TOGO import for the same JCM URL and original JCM medium, but it remains a separate merged output with fingerprint `01194ff7f606e12c3a0351a655e7290e6b7dcf2114f709db450a05e67b966585`. A generated merge row whose only source is a duplicate source record is not a defensible canonical record for the corpus.

Most available primary ingredient terms are chemically plausible for the literal MediaDive names and passed the term validator. One ingredient, `Na2SeO4`, still has a legacy `mediaingredientmech_term: MediaIngredientMech:000198` value even though its primary `term` is `CHEBI:77775` and the curation history says the 2026-06-05 migration replaced legacy MIM identifiers with `mediaingredientmech_chebi_term` entries.

## Evidence

Supported:

- The MediaDive API record for `J1228` supports the imported source identity, pH `9.2`, and JCM source URL.
- JCM medium 1228 supports splitting the base medium into `Solution A` with `NaCl`, `Na2CO3`, `NaHCO3`, and 900 ml distilled water, and `Solution B` with `MgCl2 x 6 H2O`, `NH4Cl`, `KH2PO4`, yeast extract, glucose, 1 ml trace element solution, and 100 ml distilled water.
- JCM medium 1228 and MediaDive both support adding 10 ml of a filter-sterilized trace-vitamin stock under N2 after combining Solutions A and B.
- JCM and MediaDive both support the note that only JCM 32929 receives 10 ml of 10 percent peptone solution and 6 ml of 5 percent `Na2S x 9 H2O` solution per liter.

Unsupported or over-scoped:

- The top-level trace-element ingredients are the 1 L stock composition from MediaDive solution `4896`, but the medium uses only 1 ml of that stock. The record therefore overstates each trace metal by treating stock grams per liter as final-medium grams per liter.
- The top-level trace-vitamin ingredients are the 1 L stock composition from MediaDive solution `3861`, but the medium uses only 10 ml of that stock. The record likewise overstates the vitamin additions by treating stock grams per liter as final-medium grams per liter.
- `Peptone` at `10 G_PER_L` and `Na2S x 9 H2O` at `6 G_PER_L` came from milliliter additions of 10 percent and 5 percent stock solutions, not from 10 g/L and 6 g/L dry compounds in the base medium.
- The JCM 32929-specific peptone and sulfide additions are represented as unconditional top-level ingredients and an unconditional `AUTOCLAVE` preparation step.
- The JCM and MediaDive water rows, including 900 ml and 100 ml in the main recipe and 1 L rows in each stock solution, are absent.
- The preparation step parser turned section labels, blank stock boundaries, and a JCM strain-specific comment into executable `MIX`, `FILTER_STERILIZE`, and `AUTOCLAVE` steps.

## Completeness

Consequential gaps:

- No structured stock-solution relationship preserves the trace-element and trace-vitamin recipes as nested stocks.
- No structured conditional variant or note scopes the peptone and sulfide stocks to JCM 32929.
- No water entries preserve the main-solution final-volume boundaries or the two 1 L stock-solution recipes.
- No structured reference entry captures the JCM page or MediaDive source beyond the prose `notes` field.
- No preparation detail records the JCM default autoclave condition, 121 C for 15 min, attached to the two N2 autoclaving steps.

Correctly empty or not scored:

- `target_organisms`, `growth_metrics`, and variant links are empty. The inspected source pages are recipe sources, not primary growth evidence, and the JCM 32929 note is a conditional preparation comment rather than enough evidence for a target-organism growth claim.
- There is no need for a generic discussion item for every empty optional slot.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*anaerobic_alkaline_glucose_medium__bc3ee096.md' -print` found no prior report for this generated record before the report was written; `find` included ignored report files.
- `rg --no-ignore --hidden -F 'https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228' data/normalized_yaml data/merge_yaml` found the specialized MediaDive owner and merge plus the bacterial TOGO owner and merge, confirming the exact shared JCM source URL in the maintained normalized records and ignored generated merge records.

## Findings

| ID | Severity | Finding | Maintained owner |
| --- | --- | --- | --- |
| F1 | blocker | The generated corpus contains this MediaDive/JCM 1228 merge as a separate canonical output even though the TOGO M1320 bacterial record points to the same JCM medium 1228 URL. The two source records should normalize to a source-faithful shape that can merge or be explicitly modeled as duplicate source imports. | `data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml`, `data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml`, and the merge/import normalization rules |
| F2 | major | The importer flattened MediaDive solution `4896` into undiluted top-level trace-element concentrations even though JCM adds only 1 ml of that stock to the main recipe. | `data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml` and the MediaDive import rule that inlines child solutions |
| F3 | major | The importer flattened MediaDive solution `3861` into undiluted top-level trace-vitamin concentrations even though JCM adds only 10 ml of that stock to the main recipe. | `data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml` and the MediaDive import rule that inlines child solutions |
| F4 | major | The 10 ml 10 percent peptone solution and 6 ml 5 percent `Na2S x 9 H2O` solution are represented as unconditional `10 G_PER_L` and `6 G_PER_L` ingredients rather than conditional JCM 32929 stock additions. | `data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml` and the MediaDive importer |
| F5 | major | All water rows and solution boundaries are missing, including 900 ml for Solution A, 100 ml for Solution B, and 1 L water rows for the two stock recipes. | `data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml` and the MediaDive importer |
| F6 | major | Preparation parsing emitted headings and a strain-specific comment as steps, did not attach the 121 C for 15 min JCM default to the autoclave actions, and does not preserve which components belong to Solution A, Solution B, trace elements, and trace vitamins. | `data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml` and the MediaDive step importer |
| F7 | minor | The JCM and MediaDive sources are present only in `notes`/`curation_history`, with no structured `references` entry available for future evidence validation. | `data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml` |
| F8 | minor | `Na2SeO4` still carries `mediaingredientmech_term: MediaIngredientMech:000198` instead of `mediaingredientmech_chebi_term` despite the migration history claiming all legacy links were replaced. | `data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml` or the MIM legacy migration |

## Recommended Edits

1. In the specialized normalized owner, restore the JCM/MediaDive recipe hierarchy: Solution A, Solution B, a 1 ml trace-element stock addition, and a 10 ml trace-vitamin stock addition with the stock recipes kept under stock-solution boundaries.
2. Model the 10 percent peptone and 5 percent `Na2S x 9 H2O` additions as JCM 32929-specific conditional additions instead of default dry-compound ingredients.
3. Restore water rows to the main solution and both stock recipes so volume and dilution arithmetic are auditable.
4. Replace the label/comment preparation rows with structured steps that mix and autoclave Solutions A and B under N2, anaerobically combine them, adjust or verify final pH 9.2, add filter-sterilized trace vitamins stored under N2, and separately describe the JCM 32929 condition.
5. Add structured source references for the MediaDive import and JCM source URL, with evidence attached no broader than the source-derived formulation and preparation claims.
6. Finish migrating `Na2SeO4` from `mediaingredientmech_term` to `mediaingredientmech_chebi_term`.
7. Regenerate `data/merge_yaml/merged/*.yaml` and verify this MediaDive record and the TOGO M1320 record now collapse to one canonical generated record or are explicitly reconciled by the intended duplicate-source rule.

## Follow-up Checks

- Re-run open schema, strict schema, reference validation, and term validation on `data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml`.
- Re-run the same focused validators on the regenerated `data/merge_yaml/merged/anaerobic_alkaline_glucose_medium__bc3ee096.yaml`, or on its replacement canonical merge if the corrected fingerprint changes.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration to prove normalized source edits are faithfully reflected in `data/merge_yaml/merged`.
- Manually compare the regenerated record against MediaDive `J1228` and JCM medium 1228, checking that stock additions stay diluted, JCM 32929 additions are conditional, and all four water rows survive.
- Repeat the exact JCM URL search with `rg --no-ignore --hidden -F` over `data/normalized_yaml` and `data/merge_yaml` to confirm the two JCM 1228 imports no longer produce contradictory generated merge records.

## Additional Notes

- Direct `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` were not used for this report because the project `uv` environment attempted to build `llvmlite==0.46.0` under Python 3.13 and failed before target-specific validation. The no-project Python 3.11 commands above were used as focused equivalents.
- The inspected generated merge and normalized owner are identical through the source-owned fields; the generated record only adds the `merge_recipes.py` curation event, `merge_fingerprint`, and `merged_from`.
- The record has no `references` block, so the reference validator had zero reference checks to perform.
