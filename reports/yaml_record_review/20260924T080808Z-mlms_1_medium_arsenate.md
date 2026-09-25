# YAML Record Review: mlms_1_medium_arsenate

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mlms_1_medium_arsenate.yaml
- Started UTC: 2026-09-24T08:08:08Z
- Finished UTC: 2026-09-24T08:08:08Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/mlms_1_medium_arsenate.yaml`
- Class: `MediaRecipe`
- Record ID: `CultureMech:002150`
- Label: `mlms_1_medium_arsenate`
- Original label: `MLMS-1 MEDIUM (ARSENATE)`
- Source grounding: `mediadive.medium:968b`, labelled `MLMS-1 MEDIUM (ARSENATE)`
- Category: `bacterial`
- Generated status: generated merged record with `merge_fingerprint: a1fa2695edf68583fe49d6e88a382d00d8e823d4a25bc51ec52b8bbe16a91e34`
- Maintained owners for future edits: `data/normalized_yaml/bacterial/mlms_1_medium_arsenate.yaml`, plus merged sibling sources `data/normalized_yaml/bacterial/mlms_1_medium.yaml` and `data/normalized_yaml/bacterial/bacillus_selenitireducens_medium.yaml`

## Validation

- Open schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mlms_1_medium_arsenate.yaml`
  - Result: passed with `No issues found`.
- Strict schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mlms_1_medium_arsenate.yaml --out /private/tmp/mlms_1_medium_arsenate.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows. `/private/tmp/mlms_1_medium_arsenate.strict.tsv` has 1 line, the header only.
- LinkML reference validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mlms_1_medium_arsenate.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 reference checks, all validations passed.
- Term validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mlms_1_medium_arsenate.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed.
- Embedded history validation:
  - Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated merged YAML.

## Identity and Grounding

- The generated record identity matches DSMZ/MediaDive `968b`: the inspected MediaDive REST payload names `id: 968b`, `name: MLMS-1 MEDIUM (ARSENATE)`, `source: DSMZ`, fixed pH 9.8, and the DSMZ 968b PDF URL.
- The inspected DSMZ PDF for medium 968b supports the same arsenate formula, including 3.10 g Na2HAsO4 x 7 H2O, 0.82 g Na2S x 9 H2O, and 1 ml each of Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x).
- The generated record is a three-source merge of `bacillus_selenitireducens_medium`, `mlms_1_medium`, and `mlms_1_medium_arsenate`. An exact gitignore-independent search with `rg --no-ignore --hidden` over `data/normalized_yaml` and this generated target found all three normalized source owners and the generated `merged_from` entries.
- The generated ingredient list has no stock-solution boundaries. An exact `rg --no-ignore --hidden` search for `^solutions:`, `Trace element solution SL-10`, `Selenite-tungstate`, `Wolin`, `solution_id: 595`, `solution_id: 777`, and `solution_id: 5980` across `data/merge_yaml/merged/mlms_1_medium_arsenate.yaml` and `data/normalized_yaml/bacterial/mlms_1_medium_arsenate.yaml` returned no matches, with ignored files included by the search.

## Evidence

- The source identity, main 968b recipe, pH 9.8 target, stock-solution additions, anoxic handling instructions, and SL-10 preparation instruction are supported by the inspected MediaDive `rest/medium/968b` payload and the rendered DSMZ 968b PDF text.
- MediaDive main solution 1993 and the DSMZ PDF both include `1 ml` Trace element solution SL-10; MediaDive models that stock as solution 595 with 10 ml 25% HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and water made up to 1000 ml.
- MediaDive main solution 1993 and the DSMZ PDF both include `1 ml` Selenite-tungstate solution; MediaDive models that stock as solution 777 with NaOH, Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, and water made up to 1000 ml.
- MediaDive main solution 1993 and the DSMZ PDF both include `1 ml` Wolin's vitamin solution (10x); MediaDive models that stock as solution 5980 with ten vitamins in 1000 ml.
- The generated record flattens the one-liter SL-10, Selenite-tungstate, and Wolin's vitamin stock formulas directly into final-medium ingredients. For example, the source adds 1 ml of the 10x vitamin stock to the 1003 ml main recipe, but the generated record stores the stock's 20 mg/L biotin as `0.02 G_PER_L` in the final medium.
- The source explicitly supplies `NiCl2 x 6 H2O`, but the generated row grounds that hydrated salt to `CHEBI:34887` with label `nickel dichloride`; that ontology link does not preserve the supplied hexahydrate form.

## Completeness

- The direct base-salt, arsenate, sulfide, resazurin, carbonate, and hydrogencarbonate amounts are preserved with MediaDive's 1003 ml normalization.
- The preparation prose preserves the main anoxic sparging, carbonate and hydrogencarbonate timing, pH 9.8 adjustment, anoxic dispensing, autoclaving, filtered vitamin addition, and post-autoclave arsenate and sulfide addition instructions.
- The record is materially incomplete for three 1 ml stock additions: Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x) are flattened at stock strength instead of represented as 1 ml solution rows.
- Empty optional organism, source-data, and discussion fields are not defects for this generated import. The inspected DSMZ and MediaDive entries support the recipe but do not attach a specific growth observation that should have produced a `target_organisms` claim here.

## Findings

1. **major - three 1 ml stock solutions were flattened at stock strength**
   - Evidence: DSMZ 968b and MediaDive main solution 1993 use `1 ml` each of Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x). The generated record has no `solutions` field and stores every SL-10, Selenite-tungstate, and vitamin stock component as a final-medium ingredient at its 1000 ml stock concentration.
   - Maintained owner: `data/normalized_yaml/bacterial/mlms_1_medium_arsenate.yaml`, the KOMODO sibling sources that merged with it, and the importer or merger code that flattened MediaDive stock solutions.
2. **major - a hydrate-specific stock ingredient is grounded to a non-hydrate CHEBI term**
   - Evidence: `NiCl2 x 6 H2O` is grounded to `CHEBI:34887`, `nickel dichloride`, for both `term` and `mediaingredientmech_chebi_term`.
   - Maintained owner: `data/normalized_yaml/bacterial/mlms_1_medium_arsenate.yaml` and the MediaDive chemical mapping used by enrichment.

## Recommended Edits

1. Rework the MediaDive and KOMODO source normalization so DSMZ 968b preserves 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, and 1 ml Wolin's vitamin solution (10x) as stock additions instead of direct final-medium ingredient rows.
2. Keep the SL-10 preparation instruction scoped to the SL-10 solution rather than relying on a second top-level `DISSOLVE` step after flattening.
3. Re-enrich `NiCl2 x 6 H2O` against a hydrate-specific chemical term, or leave the term unresolved until the exact hydrate is available instead of grounding the hexahydrate row to generic nickel dichloride.
4. Regenerate `data/merge_yaml/merged/mlms_1_medium_arsenate.yaml` after the normalized source and any importer fixes land; do not patch the generated merged file directly.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the regenerated `data/merge_yaml/merged/mlms_1_medium_arsenate.yaml`.
- Inspect the regenerated YAML for explicit 1 ml stock additions corresponding to MediaDive solution IDs 595, 777, and 5980 or their DSMZ names.
- Confirm that SL-10, Selenite-tungstate, and Wolin's vitamin components no longer appear as top-level final-medium ingredients at full stock strength.
- Re-run exact ignored-inclusive `rg --no-ignore --hidden` checks for `Trace element solution SL-10`, `Selenite-tungstate`, `Wolin`, and `NiCl2 x 6 H2O` against the maintained normalized owners and regenerated merge output.

## Additional Notes

- The generated three-source merge appears intended to group DSMZ 968b with KOMODO/ModelSEED aliases for the same arsenate formula. After stock-solution boundaries are preserved, compare the regenerated fingerprints to ensure only truly identical source records remain merged.
