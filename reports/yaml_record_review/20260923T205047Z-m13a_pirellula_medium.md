# YAML Record Review: M13a (PIRELLULA) medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/m13a_pirellula_medium.yaml`
- Started UTC: 2026-09-23T20:49:40Z
- Finished UTC: 2026-09-23T20:50:47Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/m13a_pirellula_medium.yaml`
- Canonical maintained owner: `data/normalized_yaml/bacterial/KOMODO_600a_M13a_PIRELLULA_medium.yaml`
- Additional maintained inputs: `data/normalized_yaml/bacterial/KOMODO_600_M14_PIRELLULA_MARINA_MEDIUM.yaml`, `data/normalized_yaml/bacterial/m13_3x_pirellula_medium.yaml`, `data/normalized_yaml/bacterial/m13a_pirellula_medium.yaml`
- CultureMech ID: `CultureMech:006088`
- Media term: `komodo.medium:600a`
- Merge fingerprint: `4174e34ca6b12c905184277859bf7432130e5c1768499f111e55dfe072e81761`
- Merge sources: `KOMODO_600_M14_PIRELLULA_MARINA_MEDIUM`, `KOMODO_600a_M13a_PIRELLULA_medium`, `m13_3x_pirellula_medium`, `m13a_pirellula_medium`
- Ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found all four maintained merge inputs, the generated four-source merge, generated indexes, and historical validation rows for the exact CultureMech and source identifiers.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows in `/private/tmp/m13a_pirellula_medium.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history` entries were not checked as standalone history records.

## Identity and Grounding

The generated record presents itself as KOMODO/DSMZ `600a`, M13a (PIRELLULA) medium, but its direct ingredient amounts and salts are a hybrid of other DSMZ variants. MediaDive REST confirms that DSMZ `600a`, DSMZ `600b`, and DSMZ `600` are distinct source records with different main recipes.

The generated four-source merge is therefore grounded to real sources but not to one coherent source recipe.

## Evidence

- MediaDive REST for `600a` identifies `M13a (PIRELLULA) MEDIUM`; its final liter has 0.25 g peptone, 0.25 g yeast extract, 0.25 g glucose, 10 ml vitamin solution, 20 ml Hutner's salts, 50 ml Tris-HCl buffer, 500 ml artificial seawater, and 420 ml distilled water.
- MediaDive REST for `600b` identifies `M13 (3x) PIRELLULA MEDIUM`; its main recipe has final volume 1050 ml, 0.75 g each of peptone, yeast extract, and glucose, 10 ml vitamin solution, 20 ml Hutner's salts, 50 ml Tris-HCl buffer, 250 ml artificial seawater, and 720 ml distilled water.
- MediaDive REST for `600` identifies `M14 (PIRELLULA MARINA) MEDIUM`; it omits peptone, uses 1 g each of yeast extract and glucose, uses 250 ml artificial seawater, and has a smaller vitamin stock than `600a` and `600b`.

## Completeness

The record is not complete as a curated M13a Pirellula representation. It flattens vitamin solution, Hutner's salts, `Metals 44`, and artificial seawater stock concentrations without applying their volumes in the final medium, and it merges three DSMZ variants whose source formulas differ before that flattening.

The record also lacks structured source references and target-organism grounding.

## Findings

1. The canonical `600a` record carries `600b` direct ingredient amounts. DSMZ `600a` has 0.25 g/L peptone, yeast extract, and glucose, but the generated KOMODO `600a` record stores `0.714286 G_PER_L` for all three, which matches the 0.75 g additions in DSMZ `600b` divided by its 1050 ml final volume.

2. The artificial-seawater stock is not diluted, and the wrong stock variant was propagated into the `600a` record. DSMZ `600a` adds 500 ml of a 1 L artificial-seawater stock whose MgCl2 x 6 H2O concentration is 4.98 g/L, while the generated record stores 10.64 g/L MgCl2 x 6 H2O from DSMZ `600b` directly as a final concentration. Every artificial-seawater salt in the generated record is therefore both variant-confused and missing the source volume factor.

3. Vitamin solution, Hutner's salts, and `Metals 44` were flattened without dilution. For DSMZ `600a`, vitamin ingredients require a 0.01 final factor, Hutner ingredients require a 0.02 final factor, and Metals ingredients require a nested 0.001 final factor. The YAML instead stores the 1 L stock values, including `0.599 G_PER_L` FeSO4 x 7 H2O from adding 0.099 g/L Hutner stock and 0.5 g/L Metals stock before either one is diluted.

4. DSMZ `600`, `600a`, and `600b` have been over-merged. The source recipes differ in direct carbon/nitrogen amounts, main-solution volume, artificial-seawater volume, artificial-seawater stock composition, and vitamin-stock composition. Treating `KOMODO_600_M14_PIRELLULA_MARINA_MEDIUM`, `KOMODO_600a_M13a_PIRELLULA_medium`, `m13_3x_pirellula_medium`, and `m13a_pirellula_medium` as source duplicates leaves one generated record that is not faithful to any DSMZ source.

5. The record has only a KOMODO `600a` `media_term`, while its source evidence includes DSMZ `600a`, DSMZ `600b`, and DSMZ `600`. Without structured source references and explicit variant identities, downstream users cannot tell which DSMZ PDF a value came from.

## Recommended Edits

- Split DSMZ `600`, `600a`, and `600b` into distinct maintained records unless a primary source proves one is a corrected duplicate of another.
- For DSMZ `600a`, restore the direct 0.25 g/L peptone, yeast extract, and glucose values; keep its 500 ml/L artificial-seawater addition; and compute final seawater, vitamin, Hutner, and Metals concentrations from the nested stock volumes.
- For DSMZ `600b`, keep the 1050 ml final volume arithmetic separate from the 1 L `600a` arithmetic.
- For DSMZ `600`, remove peptone and use its own 1 g yeast extract, 1 g glucose, 250 ml artificial seawater, and smaller vitamin stock.
- Regenerate merged YAML after the variants are split or correctly aliased, then rerun open schema, strict, reference, and term validation.

## Follow-up Checks

- Compare the KOMODO `600` and `600a` imports with their DSMZ counterparts to determine why both were enriched to the same 600b-like flattened composition.
- Re-run an ignored-inclusive exact search for `komodo.medium:600a`, `mediadive.medium:600a`, `mediadive.medium:600b`, and DSMZ `600` after curation to verify that the three variants no longer collapse to one fingerprint.
- Inspect DSMZ PDFs for `600`, `600a`, and `600b` if a discrepancy remains between MediaDive REST and the PDF formulas.

## Additional Notes

The generated record has no `preparation_steps`, even though the merged MediaDive `600a` and `600b` maintained inputs preserve seven steps from their nested stocks.
