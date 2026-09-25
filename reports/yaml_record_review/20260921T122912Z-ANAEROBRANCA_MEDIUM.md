# YAML Record Review: ANAEROBRANCA medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml
- Started UTC: 2026-09-21T12:28:00Z
- Finished UTC: 2026-09-21T12:29:12Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:006290`
- Label: `ANAEROBRANCA medium`
- Category: `bacterial`
- Source identity: displayed as KOMODO `komodo.medium:685`, copied from DSMZ/MediaDive medium `685`
- Generated status: generated merge record with fingerprint `3ee653a0f5066330321884a5317ae176f8a704eb9333c0abf1b914e7fedd9fa3`
- Merge lineage: two sources, `KOMODO_685_ANAEROBRANCA_medium` and `anaerobranca_medium`
- Maintained owners for future record edits: `data/normalized_yaml/bacterial/anaerobranca_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml`

## Validation

- Open schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml`
  - Result: passed; no issues found
- Strict schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml --out /private/tmp/ANAEROBRANCA_MEDIUM.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 total checks
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed
- Embedded curation history: Not checked. The documented `just validate-history` recipe validates standalone records under `history/`; I did not find a focused embedded `MediaRecipe.curation_history` validator for one merge file.

## Identity and Grounding

The generated record denotes DSMZ Medium 685 / Anaerobranca medium, but it is rooted on the KOMODO source duplicate `CultureMech:006290` rather than the maintained DSMZ/MediaDive parent `CultureMech:001822`. The KOMODO normalized child already points back to `data/normalized_yaml/bacterial/anaerobranca_medium.yaml` as a `SOURCE_DUPLICATE`, so the generated canonical identity should be regenerated from the DSMZ parent instead of exposing KOMODO `Aerobic: Yes` notes as the canonical source.

The inspected DSMZ PDF confirms `685: ANAEROBRANCA MEDIUM`, pH 8.5, 1000 ml distilled water, 5.00 ml Modified Wolin's mineral solution, 1.00 ml 10x Wolin vitamin solution, anoxic preparation, and post-autoclave additions of fumarate, vitamins, cysteine, and sulfide from sterile anoxic stock solutions.

The `NiCl2 x 6 H2O` row is incorrectly grounded to `CHEBI:34887` nickel dichloride, an anhydrous identity. The DSMZ mineral stock names nickel chloride hexahydrate, and hydrate count is identity-significant.

## Evidence

Supported:

- DSMZ 685 supports the title, pH 8.5, the listed base ingredients, 5.00 ml Modified Wolin's mineral solution, 1.00 ml 10x Wolin's vitamin solution, and the 1000 ml distilled-water row.
- The source supports Modified Wolin's mineral solution from medium 141, including nitrilotriacetic acid through a 1000 ml distilled-water row and pH adjustment to 7.0 after initial nitrilotriacetic acid dissolution at pH 6.5.
- The source supports Wolin's vitamin solution from medium 120, including biotin through `(DL)-alpha-Lipoic acid` and 1000 ml distilled water.
- The DSMZ normalized owner carries the source preparation faithfully: make the base anoxic under 100 percent N2, autoclave in anoxic Hungate-type tubes or serum vials, then add fumarate, vitamins, cysteine, and sulfide from sterile anoxic stock solutions.

Unsupported or over-scoped:

- The generated merge lost the DSMZ preparation steps by selecting the KOMODO source body, which has no preparation steps.
- The 5 ml Modified Wolin mineral stock rows are flattened at full stock concentration instead of being represented as a 5 ml stock addition.
- The 1 ml 10x Wolin vitamin rows are flattened at stock concentration and are 1000-fold stock units before considering their 1 ml final-medium addition.
- The generated record omits the 1000 ml main distilled-water row and the 1000 ml water rows from both stock solutions.
- The generated `Aerobic: Yes` KOMODO note conflicts with DSMZ's explicitly anoxic preparation.
- No structured source or evidence entry binds DSMZ Medium 685 to the imported formulation.

## Completeness

Consequential gaps:

- The generated canonical record has the KOMODO stable ID and source label instead of the DSMZ parent identity.
- The record has no `solutions` entries for Modified Wolin's mineral solution, Wolin's vitamin solution, fumarate stock, vitamin stock, cysteine stock, or sulfide stock.
- The DSMZ preparation protocol is missing from the generated merge.
- The main and stock water components are missing.
- The source PDF link appears only in the DSMZ normalized owner's `notes`; this generated KOMODO-rooted merge lacks structured `source_data` and `evidence`.

Correctly empty or not scored:

- `target_organisms`, `growth_metrics`, and variant links other than the KOMODO source duplicate are empty. DSMZ Medium 685 is a recipe source, not primary growth-performance evidence for a named Anaerobranca strain.
- `high_metal` and `high_ree` are empty and not scored for this review.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ANAEROBRANCA_MEDIUM.md' -print` found no prior report for this generated record before the report was written; `find` included ignored report files.
- `rg --no-ignore --hidden -n "ANAEROBRANCA_MEDIUM|ANAEROBRANCA MEDIUM|anaerobranca_medium|DSMZ Medium 921|mediadive.medium:921|komodo.medium:895" data . -g '*.yaml' -g '*.yml' -g '*.tsv' -g '*.csv' -g '*.json' -g '*.md' -g '*.py'` covered tracked and ignored YAML/TSV/CSV/JSON/Markdown/Python files under `data` and `.`. It found the DSMZ 685 parent, KOMODO 685 source duplicate, this generated merge, archived validation/source-duplicate review rows, generated ingredient output, and separate DSMZ/KOMODO 895 and DSMZ 921 records that do not duplicate this medium.

## Findings

- **Major - generated canonical identity is source-duplicate rooted.** The generated merge is rooted on KOMODO `CultureMech:006290` even though the normalized KOMODO 685 record is a `SOURCE_DUPLICATE` child of DSMZ `CultureMech:001822`. Future fix owner: merge selection or regeneration from `data/normalized_yaml/bacterial/anaerobranca_medium.yaml`.
- **Major - DSMZ stock solutions are flattened as direct ingredients.** Modified Wolin's mineral solution and 10x Wolin's vitamin solution are represented as undiluted direct `G_PER_L` rows, and water rows for both stocks are missing. Future fix owner: `data/normalized_yaml/bacterial/anaerobranca_medium.yaml`.
- **Major - generated preparation is missing.** The inspected DSMZ owner has an anoxic preparation protocol, but the generated KOMODO-rooted merge has no `preparation_steps`. Future fix owner: canonical merge selection or regenerated merge output.
- **Major - `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride.** The preferred term and DSMZ mineral stock specify nickel chloride hexahydrate, while the CHEBI term is `CHEBI:34887` `nickel dichloride`. Future fix owner: `data/normalized_yaml/bacterial/anaerobranca_medium.yaml` and the KOMODO copy if it retains this row.
- **Minor - source provenance is unstructured.** The DSMZ PDF is only a prose link in the DSMZ parent, while this generated merge exposes KOMODO notes and no evidence for the copied DSMZ composition. Future fix owner: `data/normalized_yaml/bacterial/anaerobranca_medium.yaml` and KOMODO-source notes as needed.

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/ANAEROBRANCA_MEDIUM.yaml` so DSMZ `CultureMech:001822` becomes canonical and KOMODO 685 remains only a source duplicate.
2. In `data/normalized_yaml/bacterial/anaerobranca_medium.yaml`, replace flattened Modified Wolin mineral and 10x Wolin vitamin rows with explicit solution references, retaining each stock composition and water row separately.
3. Keep fumarate, vitamins, cysteine, and sulfide scoped to their sterile anoxic stock-addition preparation boundaries instead of modeling every value as an undifferentiated direct ingredient.
4. Correct `NiCl2 x 6 H2O` to a hexahydrate CHEBI identity wherever this DSMZ 685 ingredient row is retained.
5. Add structured DSMZ Medium 685 provenance and narrow evidence snippets for the parent recipe, stock formulas, and preparation protocol.

## Follow-up Checks

- Rerun `just validate-schema` and `just validate-strict` on the DSMZ and KOMODO normalized owners.
- Rerun `just validate-terms` on both owners to confirm the nickel chloride hexahydrate correction.
- Rerun `just validate-references` if structured DSMZ evidence is added.
- Rerun `just validate-media-variant-links` to confirm the DSMZ parent and KOMODO source duplicate remain linked bidirectionally.
- Rerun `just verify-merges` or the narrow merge-regeneration check that proves the generated canonical record is fresh from the two maintained inputs.
- Manually re-open DSMZ Medium 685 after curation and verify all parent stock boundaries and post-autoclave additions against the PDF.

## Additional Notes

- The final-volume dilution over 1006 ml explains values such as `0.497018 G_PER_L` from 0.50 g `KH2PO4`; those base rows are dimensionally plausible as final concentrations even though water is omitted.
- I did not rerun `just validate-schema`, `just validate-strict`, or `just validate-terms` directly because the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails before reaching these focused validators. The no-project Python 3.11 commands above exercised the same record-level LinkML, strict, reference, and term validators without installing the project.
