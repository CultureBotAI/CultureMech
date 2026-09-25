# YAML Record Review: ANAEROBRANCA GOTTSCHALKII medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROBRANCA_GOTTSCHALKII_MEDIUM.yaml
- Started UTC: 2026-09-21T12:26:35Z
- Finished UTC: 2026-09-21T12:27:50Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/ANAEROBRANCA_GOTTSCHALKII_MEDIUM.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:006750`
- Label: `ANAEROBRANCA GOTTSCHALKII medium`
- Category: `bacterial`
- Source identity: displayed as KOMODO `komodo.medium:895`, copied from DSMZ/MediaDive medium `895`
- Generated status: generated merge record with fingerprint `78cacc45f7436b5c5eb81eccc8a495e3073a430a95c386c43571020912db8b72`
- Merge lineage: four sources, `KOMODO_895_ANAEROBRANCA_GOTTSCHALKII_medium`, `anaerobranca_gottschalkii_medium`, `for_dsm_14826`, and `for_dsm_14828`
- Maintained owners for future record edits: `data/normalized_yaml/bacterial/anaerobranca_gottschalkii_medium.yaml`, `data/normalized_yaml/bacterial/KOMODO_895_ANAEROBRANCA_GOTTSCHALKII_medium.yaml`, `data/normalized_yaml/bacterial/for_dsm_14826.yaml`, and `data/normalized_yaml/bacterial/for_dsm_14828.yaml`

## Validation

- Open schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROBRANCA_GOTTSCHALKII_MEDIUM.yaml`
  - Result: passed; no issues found
- Strict schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROBRANCA_GOTTSCHALKII_MEDIUM.yaml --out /private/tmp/ANAEROBRANCA_GOTTSCHALKII_MEDIUM.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROBRANCA_GOTTSCHALKII_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 total checks
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROBRANCA_GOTTSCHALKII_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed
- Embedded curation history: Not checked. The documented `just validate-history` recipe validates standalone records under `history/`; I did not find a focused embedded `MediaRecipe.curation_history` validator for one merge file.

## Identity and Grounding

This generated record is a stale canonicalization of DSMZ Medium 895. The merge body is rooted on the KOMODO-derived child `CultureMech:006750`, but the maintained normalized graph was repaired on 2026-09-13 so DSMZ/MediaDive `CultureMech:002058` is the parent, KOMODO 895 is an exact `SOURCE_DUPLICATE`, and KOMODO 895.1/895.2 are `STRAIN_SPECIFIC_VARIANT` children for DSM 14826 and DSM 14828.

The inspected DSMZ PDF confirms that the parent identity is `895: ANAEROBRANCA GOTTSCHALKII MEDIUM`, with final pH 9.3 to 9.5 and final volume 1013 ml. The direct final concentrations for the first base rows match DSMZ after dividing by 1013 ml, but Modified Wolin's mineral solution, Wolin's vitamin solution, an FeSO4 stock, starch, and carbonate are stock additions in the source and not all should be flattened as independent dry final-medium rows.

The `NiCl2 x 6 H2O` row is incorrectly grounded to `CHEBI:34887` nickel dichloride, an anhydrous identity. The DSMZ mineral stock names nickel chloride hexahydrate, and hydrate count is identity-significant.

## Evidence

Supported:

- DSMZ 895 supports the title, final pH 9.3 to 9.5, final volume 1013 ml, the 1000 ml distilled-water basis, the listed base salts through starch, 10.00 ml Modified Wolin's mineral solution, and 1.00 ml Wolin's vitamin solution.
- The source supports the two stock formulas: Modified Wolin's mineral solution from medium 141 and 10x Wolin's vitamin solution from medium 120.
- The source supports the preparation text in the DSMZ normalized owner: dissolve all ingredients except cysteine, carbonate, starch, and vitamins; sparge with 100 percent N2 for 30 to 45 min; add cysteine; adjust pH to 7.5; dispense under 100 percent N2; autoclave; add sterile anoxic starch/vitamin and carbonate stocks; filter-sterilize the vitamins; adjust the complete medium to pH 9.3 to 9.5 if necessary.
- DSMZ 895 supports strain-specific variants: for DSM 14826, omit starch, raise tryptone to 2.00 g/L, and supplement 4.00 g/L `Na2S2O3 x 5 H2O`; for DSM 14828 and DSM 119686, omit starch, add 5.00 g/L D-glucose, raise tryptone to 2.00 g/L, and adjust the completed medium to pH 9.0.

Unsupported or over-scoped:

- The generated record omits the 1000 ml main distilled-water row and the 1000 ml water rows from both stock solutions.
- The Modified Wolin mineral stock rows are flattened at stock concentration. This adds whole stock amounts such as `3.0 G_PER_L` `MgSO4 x 7 H2O`, `1.0 G_PER_L` NaCl, `0.1 G_PER_L` FeSO4, and `0.1 G_PER_L` CaCl2 directly into the final medium instead of scoping them to a 10 ml/L stock addition.
- The 10x Wolin vitamin rows are flattened at stock concentration and are 1000-fold stock units before considering the 1 ml into 1013 ml dilution.
- The generated merge lost the DSMZ preparation steps by selecting the KOMODO source body, which has no preparation steps.
- The generated `Aerobic: Yes` KOMODO note conflicts with DSMZ's explicitly anoxic preparation under N2 or N2/CO2.
- KOMODO 895.1 and 895.2 are not exact source duplicates of the parent recipe; DSMZ describes them as strain-specific variants with starch, tryptone, thiosulfate, glucose, or pH changes.
- No structured source or evidence entry binds DSMZ Medium 895 to the imported formulation.

## Completeness

Consequential gaps:

- Generated `variant_children` and `variant_relationship` are stale relative to the September topology repair in all four normalized owners.
- The generated canonical record has the KOMODO stable ID and source label instead of the repaired DSMZ parent identity.
- The record has no `solutions` entries for Modified Wolin's mineral solution, Wolin's vitamin solution, FeSO4 solution, carbonate stock, or sterile anoxic starch/vitamin additions.
- The DSMZ preparation protocol is missing from the generated merge.
- The main and stock water components are missing.
- The source PDF link appears only in the DSMZ normalized owner's `notes`; this generated KOMODO-rooted merge lacks structured `source_data` and `evidence`.

Correctly empty or not scored:

- `target_organisms` and `growth_metrics` are empty. DSMZ Medium 895 is a recipe source, not primary growth-performance evidence for Anaerobranca gottschalkii.
- `high_metal` and `high_ree` are empty and not scored for this review.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ANAEROBRANCA_GOTTSCHALKII_MEDIUM.md' -print` found no prior report for this generated record before the report was written; `find` included ignored report files.
- `rg --no-ignore --hidden -n "ANAEROBRANCA_GOTTSCHALKII_MEDIUM|Anaerobranca Gottschalkii|ANAEROBRANCA GOTTSCHALKII|anaerobranca_gottschalkii" data . -g '*.yaml' -g '*.yml' -g '*.tsv' -g '*.csv' -g '*.md' -g '*.py'` covered tracked and ignored YAML/TSV/CSV/Markdown/Python files under `data` and `.`. It found the DSMZ parent, KOMODO 895 child, two KOMODO strain-specific children, this generated merge, generated ingredient output, archived source-duplicate review rows, archived validation TSVs, and no second generated `ANAEROBRANCA_GOTTSCHALKII_MEDIUM` record.
- The same ignored-file search found `data/import_tracking/reports/merged_duplicates.tsv` rows that already identify the same summed `MgSO4 x 7 H2O`, `CaCl2 x 2 H2O`, `NaCl`, and `FeSO4 x 7 H2O` rows as differing merged parts requiring source review.

## Findings

- **Major - generated canonical identity and topology are stale.** The merge is rooted on KOMODO `CultureMech:006750` and marks `for_dsm_14826` / `for_dsm_14828` as `SOURCE_DUPLICATE`, but the maintained September repair re-rooted KOMODO 895 under DSMZ Medium 895 and marked the two `for_dsm_*` records as `STRAIN_SPECIFIC_VARIANT`. Future fix owner: regenerate from `data/normalized_yaml/bacterial/anaerobranca_gottschalkii_medium.yaml` plus the three KOMODO children.
- **Major - DSMZ stock solutions are flattened as direct ingredients.** Modified Wolin's mineral solution and 10x Wolin's vitamin solution are represented as undiluted direct `G_PER_L` rows, and their rows are merged with base-medium salts when names collide. Future fix owner: `data/normalized_yaml/bacterial/anaerobranca_gottschalkii_medium.yaml`.
- **Major - generated preparation is missing.** The inspected DSMZ owner has an anoxic preparation protocol, but the generated KOMODO-rooted merge has no `preparation_steps`. Future fix owner: canonical merge selection or regeneration after the September topology repair.
- **Major - `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride.** The preferred term and DSMZ mineral stock specify nickel chloride hexahydrate, while the CHEBI term is `CHEBI:34887` `nickel dichloride`. Future fix owner: `data/normalized_yaml/bacterial/anaerobranca_gottschalkii_medium.yaml` and any copied KOMODO children retaining the row.
- **Major - strain-specific variants still carry the base formulation.** DSMZ 895 specifies starch omissions, higher tryptone, extra thiosulfate or glucose, and pH 9.0 for the DSM 14826/14828 variants, but the normalized `for_dsm_14826.yaml` and `for_dsm_14828.yaml` files still carry the unmodified 35-ingredient base signature. Future fix owner: `data/normalized_yaml/bacterial/for_dsm_14826.yaml` and `data/normalized_yaml/bacterial/for_dsm_14828.yaml`.
- **Minor - source provenance is unstructured.** The DSMZ PDF is only a prose link in the DSMZ parent, while this generated merge exposes KOMODO notes and no evidence for the copied DSMZ composition. Future fix owner: `data/normalized_yaml/bacterial/anaerobranca_gottschalkii_medium.yaml` and KOMODO-source notes as needed.

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/ANAEROBRANCA_GOTTSCHALKII_MEDIUM.yaml` from the September topology repair so DSMZ `CultureMech:002058` becomes the canonical parent and KOMODO 895 remains only a source duplicate.
2. In `data/normalized_yaml/bacterial/anaerobranca_gottschalkii_medium.yaml`, replace flattened Modified Wolin mineral and 10x Wolin vitamin rows with explicit solution references, retaining each stock composition and water row separately.
3. Keep FeSO4, carbonate, starch, and vitamins scoped to their stock-addition preparation boundaries instead of modeling every value as a direct dry ingredient.
4. Correct `NiCl2 x 6 H2O` to a hexahydrate CHEBI identity wherever this DSMZ 895 ingredient row is retained.
5. Apply the DSMZ-documented DSM 14826 and DSM 14828/DSM 119686 modifications to `for_dsm_14826.yaml` and `for_dsm_14828.yaml`.
6. Add structured DSMZ Medium 895 provenance and narrow evidence snippets for the parent recipe, stock formulas, preparation protocol, and strain-specific variant notes.

## Follow-up Checks

- Rerun `just validate-schema` and `just validate-strict` on all four normalized owners.
- Rerun `just validate-terms` on the same files to confirm the nickel chloride hexahydrate correction.
- Rerun `just validate-references` if structured DSMZ evidence is added.
- Rerun `just validate-media-variant-links` to confirm the DSMZ parent, KOMODO source duplicate, and strain-specific children remain linked bidirectionally.
- Rerun `just verify-merges` or the narrow merge-regeneration check that proves the generated canonical record is fresh from the four maintained inputs.
- Manually re-open DSMZ Medium 895 after curation and verify the parent stock boundaries plus both DSM-specific variant paragraphs against the PDF.

## Additional Notes

- The final-volume dilution of 1013 ml explains values such as `0.987167 G_PER_L` from 1.00 g `(NH4)2SO4`; those base rows are dimensionally plausible as final concentrations even though water is omitted.
- I did not rerun `just validate-schema`, `just validate-strict`, or `just validate-terms` directly because the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails before reaching these focused validators. The no-project Python 3.11 commands above exercised the same record-level LinkML, strict, reference, and term validators without installing the project.
