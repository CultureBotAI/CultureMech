# YAML Record Review: ANAEROBIC TYEG MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml
- Started UTC: 2026-09-21T12:22:10Z
- Finished UTC: 2026-09-21T12:24:47Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:015413`
- Label: `ANAEROBIC TYEG MEDIUM`
- Category: `specialized`
- Source identity: MediaDive `mediadive.medium:J684`, source `JCM`, JCM medium `684`
- Generated status: generated merge record with fingerprint `d304fc335b934369241d96fa18746653cdd8c88762886f0deaf26b8044ab7cb3`
- Merge lineage: one source, `anaerobic_tyeg_medium`
- Maintained owner for future record edits: `data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml`

## Validation

- Open schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml`
  - Result: passed; no issues found
- Strict schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml --out /private/tmp/ANAEROBIC_TYEG_MEDIUM.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 total checks
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed
- Embedded curation history: Not checked. The documented `just validate-history` recipe validates standalone records under `history/`; I did not find a focused embedded `MediaRecipe.curation_history` validator for one merge file.

## Identity and Grounding

The record correctly denotes JCM medium 684. The inspected JCM page is numbered `684` and titled `ANAEROBIC TYEG MEDIUM`, matching the imported `original_name`, `media_term`, source accession, and JCM link.

The available direct ingredient grounding is mostly consistent with the stated chemical forms where the source lists dry salts or explicit hydrates: `KH2PO4`, `K2HPO4`, `NaCl`, `MgCl2 x 6 H2O`, `NH4Cl`, `FeSO4 x 7 H2O`, glucose, resazurin, `Na2S x 9 H2O`, nitrilotriacetic acid, `FeCl2 x 4 H2O`, `MnCl2 x 4 H2O`, `CoCl2 x 6 H2O`, `CaCl2 x 2 H2O`, `ZnCl2`, `CuCl2`, `H3BO3`, `Na2MoO4 x 2 H2O`, `Na2SeO3 x 5 H2O`, and the trace-vitamin compounds all point at plausible CHEBI identities for the JCM labels. `Tryptone` and `Yeast extract` remain unresolved mixtures, which is preferable to forcing narrow CHEBI chemicals.

The record-level `ph_value: 6.5` is incorrectly grounded. JCM 684 adjusts the complete medium to pH 7.5 before boiling, cooling under N2, dispensing, sealing, and autoclaving; pH 6.5 applies only to the separate trace-mineral solution made from nitrilotriacetic acid and minerals.

## Evidence

Supported:

- JCM 684 supports the root identity, source label, liquid complex formulation, the main mineral/base ingredient labels, 2.0 g/L each of tryptone, yeast extract, and glucose on the source recipe's nominal basis, 1.0 mg resazurin, and a 1.0 L distilled-water row.
- JCM 684 supports 9.0 ml trace-mineral stock and 10.0 ml trace-vitamin stock additions, a 5.0 ul addition of 10 percent `FeSO4 x 7 H2O` solution, and an 8.0 ml addition of 5 percent `Na2S x 9 H2O` solution before inoculation.
- JCM 684 supports the trace-mineral stock contents from nitrilotriacetic acid through distilled water and instructs the curator to dissolve nitrilotriacetic acid first, adjust that stock to pH 6.5 with KOH, then add the minerals.
- JCM medium 197 supports the trace-vitamin stock recipe referenced by JCM 684, including biotin, folic acid, pyridoxine HCl, thiamine HCl, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, lipoic acid, and 1.0 L distilled water.

Unsupported or over-scoped:

- The trace-mineral and trace-vitamin stock formulas are flattened into direct final-medium `ingredients`, so their stock concentrations are carried over without dilution by 9.0 ml/L or 10.0 ml/L.
- The 8.0 ml `Na2S x 9 H2O` stock addition is represented as `8 G_PER_L` of dry `Na2S x 9 H2O`; the source amount is a volume of a 5 percent stock.
- The 5.0 ul `FeSO4 x 7 H2O` stock addition is represented as `5 G_PER_L` of dry `FeSO4 x 7 H2O`; the source amount is a microliter-scale addition of a 10 percent stock.
- The trace-mineral stock's `NaCl 1.0 g` row is added to the final direct `NaCl` row as another whole `1.0 G_PER_L`, producing `1.876339 G_PER_L`; this should remain inside the 9.0 ml stock addition or be diluted before any final-concentration projection.
- The main 1.0 L distilled-water row and both stock 1.0 L distilled-water rows are missing.
- The `ph_value: 6.5` root claim is imported from the trace-mineral stock and contradicts the JCM 684 complete-medium instruction to adjust to pH 7.5.
- The JCM `Tryptone (BD-Difco)` qualifier is dropped.
- No structured source or evidence entry binds the JCM 684 and JCM 197 pages to the generated formulation.

## Completeness

Consequential gaps:

- The record has no `solutions` entries for the 9.0 ml trace-mineral stock, 10.0 ml trace-vitamin stock, 5.0 ul 10 percent `FeSO4 x 7 H2O` stock, or 8.0 ml 5 percent `Na2S x 9 H2O` stock.
- The medium has only one direct ingredient layer, so a consumer cannot distinguish final-medium concentrations from stock-solution concentrations.
- The stock-specific pH and preparation text are modeled as top-level medium fields and steps.
- The importer link appears only in `notes`; the record lacks structured `source_data` and `evidence`.

Correctly empty or not scored:

- `target_organisms`, `growth_metrics`, and variant links are empty. JCM 684 is a recipe source, not primary growth-performance evidence.
- `high_metal` and `high_ree` are empty and not scored for this review.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ANAEROBIC_TYEG_MEDIUM.md' -print` found no prior report for this generated record before the report was written; `find` included ignored report files.
- `rg --no-ignore --hidden -n "ANAEROBIC_TYEG_MEDIUM|Anaerobic TYEG|TYEG" data . -g '*.yaml' -g '*.yml' -g '*.tsv' -g '*.csv' -g '*.md' -g '*.py'` covered tracked and ignored YAML/TSV/CSV/Markdown/Python files under `data` and `.`. It found the single normalized owner, this single generated merge, generated indexes, the media-content manifest, and archived validation TSVs; it did not find an adjacent duplicate TYEG merge record.
- `rg --no-ignore --hidden -n "J684|jcm_grmd\?GRMD=684|CultureMech:015413|anaerobic_tyeg_medium" data/raw_yaml data/raw data/normalized_yaml data/merge_yaml -g '*.yaml' -g '*.yml' -g '*.tsv' -g '*.csv' -g '*.json' -g '*.md'` included ignored files in those layers. `data/raw_yaml` is absent in this checkout and `data/raw/mediadive*` contains only README files, so the maintained YAML and generated index files were the only local J684 records found.

## Findings

- **Major - stock additions are flattened as final dry ingredients.** The generated record places `Na2S x 9 H2O`, trace minerals, and trace vitamins directly in `ingredients` even though JCM 684 specifies stock additions of 9.0 ml trace minerals, 10.0 ml trace vitamins, 5.0 ul 10 percent ferrous sulfate, and 8.0 ml 5 percent sulfide. Future fix owner: `data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml`, with any reusable MediaDive/JCM stock-boundary repair in the importer that produced the normalized record.
- **Major - multiple amounts use stock or volume numbers as `G_PER_L` final concentrations.** `FeSO4 x 7 H2O` is recorded as `5 G_PER_L` from a 5.0 ul 10 percent stock addition, `Na2S x 9 H2O` is recorded as `8 G_PER_L` from an 8.0 ml 5 percent stock addition, and the trace-mineral `NaCl` is merged into direct final `NaCl` as an undiluted extra `1.0 G_PER_L`. Future fix owner: `data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml`.
- **Major - the root pH is the trace-mineral stock pH.** The complete JCM 684 medium is adjusted to pH 7.5 before boiling and autoclaving, while the pH 6.5 instruction belongs to the trace-mineral stock only. Future fix owner: `data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml`.
- **Major - solution waters and stock composition boundaries are missing.** JCM 684 has distilled water rows for the main medium and trace-mineral solution, and the JCM 197 trace-vitamin stock has its own 1.0 L distilled-water row; none survive into the generated record as water components or stock solution definitions. Future fix owner: `data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml`.
- **Minor - source qualifiers and source references are thin.** The JCM `Tryptone (BD-Difco)` qualifier is dropped, and the JCM source pages are represented only by prose `notes` rather than structured source or evidence entries. Future fix owner: `data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml`.

## Recommended Edits

1. In `data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml`, replace the flattened trace-mineral and trace-vitamin direct ingredient rows with explicit stock-solution references and compositions. Preserve the 9.0 ml and 10.0 ml addition amounts from JCM 684.
2. Model the 5.0 ul 10 percent `FeSO4 x 7 H2O` solution and 8.0 ml 5 percent `Na2S x 9 H2O` solution as stock additions instead of direct dry `G_PER_L` ingredients.
3. Move `ph_value: 6.5` and the nitrilotriacetic-acid/KOH preparation text onto the trace-mineral stock, then represent the complete medium's pH 7.5 adjustment as a top-level preparation condition.
4. Add the main 1.0 L distilled-water row and the stock-solution water rows at the appropriate nesting level.
5. Add structured source provenance for JCM 684 and the linked JCM 197 trace-vitamin recipe; retain short evidence snippets on the narrowest stock or preparation claims if the schema path supports them.
6. Preserve `BD-Difco` as a supplier note on tryptone if the maintained ingredient shape has a suitable slot; otherwise record the unresolved qualifier in the row notes.
7. Regenerate `data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml` from the normalized owner instead of hand-editing this generated file.

## Follow-up Checks

- Rerun `just validate-schema data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml` and `just validate-strict data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml`.
- Rerun `just validate-terms data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml` to confirm all retained CHEBI links, including explicit hydrate forms, still validate.
- Rerun `just validate-references data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml` if structured JCM evidence is added.
- Rerun `just verify-merges` or the narrow merge-regeneration check that proves `data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml` is fresh from `data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml`.
- Manually re-open JCM 684 and JCM 197 after curation to verify that every stock solution, pH condition, water row, and post-autoclave addition is still scoped to the same formulation segment as the source page.

## Additional Notes

- `data/normalized_yaml/bacterial/mediadive_4584_Main_sol_J684.yaml` contains MediaDive's intermediate `Main sol. J684` solution with `Original volume: 1027 mL`, but the generated medium does not reference it as a solution and it also stores the `Na2S x 9 H2O` 8.0 ml stock addition as a `PERCENT_V_V` row inside the main solution.
- I did not rerun `just validate-schema`, `just validate-strict`, or `just validate-terms` directly because the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails before reaching these focused validators. The no-project Python 3.11 commands above exercised the same record-level LinkML, strict, reference, and term validators without installing the project.
