# YAML Record Review: ANAEROCELLA MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROCELLA_MEDIUM.yaml
- Started UTC: 2026-09-21T12:29:20Z
- Finished UTC: 2026-09-21T12:30:25Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/ANAEROCELLA_MEDIUM.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:000745`
- Label: `ANAEROCELLA MEDIUM`
- Category: `bacterial`
- Source identity: MediaDive `mediadive.medium:1281`, source `DSMZ`, DSMZ medium `1281`
- Generated status: generated merge record with fingerprint `2b89dff2302e63d11ad749eaf2117675accf1b26485d3ba967a77f29ef44892b`
- Merge lineage: one source, `anaerocella_medium`
- Maintained owner for future record edits: `data/normalized_yaml/bacterial/anaerocella_medium.yaml`

## Validation

- Open schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROCELLA_MEDIUM.yaml`
  - Result: passed; no issues found
- Strict schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROCELLA_MEDIUM.yaml --out /private/tmp/ANAEROCELLA_MEDIUM.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROCELLA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 total checks
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROCELLA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed
- Embedded curation history: Not checked. The documented `just validate-history` recipe validates standalone records under `history/`; I did not find a focused embedded `MediaRecipe.curation_history` validator for one merge file.

## Identity and Grounding

The record correctly denotes DSMZ/MediaDive medium 1281. The inspected DSMZ PDF is `1281. ANAEROCELLA MEDIUM`, matching the generated `media_term`, source accession, and PDF link.

The `Trypticase` grounding is wrong: it points at `CHEBI:78018` dodecylphosphocholine even though the source row is a commercial BBL Trypticase peptone. That complex digest should not be grounded to a pure zwitterionic detergent. The generated record also still has a legacy `mediaingredientmech_term` on Trypticase instead of the CHEBI-keyed `mediaingredientmech_chebi_term` used on ordinary grounded rows.

The available CHEBI identities for glucose, cellobiose, maltose, starch, cysteine hydrochloride hydrate, resazurin, sodium carbonate, agar, phosphate salts, ammonium sulfate, sodium chloride, magnesium sulfate heptahydrate, calcium chloride dihydrate, and the vitamin labels are plausible for the source strings.

## Evidence

Supported:

- DSMZ 1281 supports 10.0 g Trypticase, 5.0 g yeast extract, 0.25 g each glucose/cellobiose/maltose/soluble starch, 0.30 g cysteine-HCl hydrate, 1.0 mg resazurin, 1000 ml distilled water, 1.0 ml vitamin solution, and 2.5 ml 8 percent `Na2CO3` solution.
- DSMZ 1281 supports 75 ml Salt Solution I and 75 ml Salt Solution II additions, with their own 1000 ml distilled-water stock recipes.
- DSMZ 1281 supports adding 15.0 g/L agar only for solid medium.
- DSMZ 1281 supports boiling under N2 for 10 min, cooling, adjusting to pH 7.3, autoclaving for 20 min at 121 C, and adding sterile anoxic `#` solutions after autoclaving.

Unsupported or over-scoped:

- The generated record omits the 1000 ml main distilled-water row and both salt-stock 1000 ml distilled-water rows.
- Salt Solution I and II are flattened at full stock concentration, so rows such as `K2HPO4 6 G_PER_L`, `(NH4)2SO4 12 G_PER_L`, `NaCl 12 G_PER_L`, `MgSO4 x 7 H2O 1.2 G_PER_L`, and `CaCl2 x 2 H2O 1.2 G_PER_L` are not diluted by their 75 ml additions.
- The vitamin solution is still flattened in this generated merge. The maintained normalized owner moved only vitamin B12, nicotinic acid, pyridoxine hydrochloride, and thiamine-HCl dihydrate under `solutions` on 2026-08-07; p-aminobenzoic acid, D-(+)-biotin, and calcium pantothenate remain direct rows at stock concentration in the normalized file.
- The 2.5 ml 8 percent Na2CO3 addition is numerically represented as `0.2 G_PER_L`, but its sterile anoxic stock boundary is lost.
- `physical_state: SOLID_AGAR` and the direct 15 g/L agar row over-scope an optional solid-medium instruction onto the whole medium.
- No structured source or evidence entry binds DSMZ Medium 1281 to the imported formulation.

## Completeness

Consequential gaps:

- The generated merge is stale relative to `data/normalized_yaml/bacterial/anaerocella_medium.yaml`: it was generated before `apply_cocktail_nesting.py` moved four vitamin rows into a 1 ml/L `Vitamin solution`.
- Even the maintained normalized owner still has three direct vitamin-stock rows that should be nested under the same vitamin solution.
- The record has no `solutions` entries for Salt Solution I, Salt Solution II, or the Na2CO3 stock.
- The main and stock water components are missing.
- The agar instruction is not scoped as an optional solid-medium variant.
- The source PDF link appears only in `notes`; the record lacks structured `source_data` and `evidence`.

Correctly empty or not scored:

- `target_organisms`, `growth_metrics`, and variant links are empty. DSMZ Medium 1281 is a recipe source, not primary growth-performance evidence.
- `high_metal` and `high_ree` are empty and not scored for this review.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ANAEROCELLA_MEDIUM.md' -print` found no prior report for this generated record before the report was written; `find` included ignored report files.
- `rg --no-ignore --hidden -n "ANAEROCELLA_MEDIUM|ANAEROCELLA MEDIUM|Anaerocella|anaerocella" data . -g '*.yaml' -g '*.yml' -g '*.tsv' -g '*.csv' -g '*.json' -g '*.md' -g '*.py'` covered tracked and ignored YAML/TSV/CSV/JSON/Markdown/Python files under `data` and `.`. It found the single normalized owner, this single generated merge, generated indexes and ingredient outputs, archived validation rows, import-tracking priority output, and no adjacent duplicate generated record for this medium.

## Findings

- **Major - two DSMZ salt stocks are flattened as direct ingredients.** Salt Solution I and Salt Solution II are 75 ml stock additions, but the generated record stores their component concentrations directly as final-medium `G_PER_L` rows and omits both stock water rows. Future fix owner: `data/normalized_yaml/bacterial/anaerocella_medium.yaml`.
- **Major - the vitamin stock nesting is stale and incomplete.** The generated merge predates the normalized 2026-08-07 partial nesting of four vitamin rows, and the normalized owner still leaves p-aminobenzoic acid, D-(+)-biotin, and calcium pantothenate as direct stock-strength rows. Future fix owner: `data/normalized_yaml/bacterial/anaerocella_medium.yaml`, followed by merge regeneration.
- **Major - `Trypticase` is grounded to an unrelated CHEBI term.** The row points at dodecylphosphocholine, not a peptone or Trypticase mixture. Future fix owner: `data/normalized_yaml/bacterial/anaerocella_medium.yaml`.
- **Major - optional agar is promoted to the root physical state.** DSMZ adds 15.0 g/L agar only for solid medium, but the generated record marks the entire recipe as `SOLID_AGAR` and always includes the agar ingredient. Future fix owner: `data/normalized_yaml/bacterial/anaerocella_medium.yaml`.
- **Minor - source provenance is unstructured.** The DSMZ PDF link is present only in prose `notes`, and there is no evidence object for the source formulation. Future fix owner: `data/normalized_yaml/bacterial/anaerocella_medium.yaml`.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/anaerocella_medium.yaml`, add explicit Salt Solution I and Salt Solution II solution references with 75 ml/L additions, stock compositions, and stock water rows.
2. Move the remaining p-aminobenzoic acid, D-(+)-biotin, and calcium pantothenate rows into the existing 1 ml/L `Vitamin solution`, verify the already nested vitamin rows, and regenerate the merge.
3. Keep the 2.5 ml 8 percent Na2CO3 addition as a sterile anoxic stock addition rather than only its final `0.2 G_PER_L` carbonate equivalent.
4. Remove the erroneous `CHEBI:78018` grounding from `Trypticase` and leave it unresolved or point it at the packaged MIM mixture identity if a supported non-CHEBI target exists.
5. Recast the 15 g/L agar as an optional solid-medium variant or conditional additive and avoid marking the whole record `SOLID_AGAR`.
6. Add structured DSMZ Medium 1281 provenance and narrow evidence snippets for the main formula, stock formulas, and preparation protocol.

## Follow-up Checks

- Rerun `just validate-schema data/normalized_yaml/bacterial/anaerocella_medium.yaml` and `just validate-strict data/normalized_yaml/bacterial/anaerocella_medium.yaml`.
- Rerun `just validate-terms data/normalized_yaml/bacterial/anaerocella_medium.yaml` after removing the Trypticase misgrounding.
- Rerun `just validate-references data/normalized_yaml/bacterial/anaerocella_medium.yaml` if structured DSMZ evidence is added.
- Rerun `just verify-merges` or the narrow merge-regeneration check that proves `data/merge_yaml/merged/ANAEROCELLA_MEDIUM.yaml` is fresh from `data/normalized_yaml/bacterial/anaerocella_medium.yaml`.
- Manually re-open DSMZ Medium 1281 after curation and verify both salt stocks, all seven vitamin rows, the carbonate stock, the water rows, and the optional agar instruction against the PDF.

## Additional Notes

- I did not rerun `just validate-schema`, `just validate-strict`, or `just validate-terms` directly because the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails before reaching these focused validators. The no-project Python 3.11 commands above exercised the same record-level LinkML, strict, reference, and term validators without installing the project.
