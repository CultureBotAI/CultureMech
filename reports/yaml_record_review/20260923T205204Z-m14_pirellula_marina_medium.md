# YAML Record Review: M14 (Pirellula Marina) Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/m14_pirellula_marina_medium.yaml`
- Started UTC: 2026-09-23T20:51:10Z
- Finished UTC: 2026-09-23T20:52:04Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/m14_pirellula_marina_medium.yaml`
- Maintained owner: `data/normalized_yaml/bacterial/TOGO_M2346_M14_Pirellula_Marina_Medium.yaml`
- CultureMech ID: `CultureMech:008932`
- Media term: `TOGO:M2346`
- Merge fingerprint: `a3f59027cf38e167bb0a5bf8e5e5488bba2b0abd8dd346862b002642013bb437`
- Merge sources: `TOGO_M2346_M14_Pirellula_Marina_Medium`
- Ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found the single maintained TOGO owner, generated indexes, the generated one-source merge, and historical validation rows for the exact CultureMech and TOGO identifiers.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows in `/private/tmp/m14_pirellula_marina_medium.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history` entries were not checked as standalone history records.

## Identity and Grounding

The record identifies TOGO `M2346`, `M14 (Pirellula Marina) Medium`, which TOGO links to the DSMZ Medium 600 PDF. MediaDive's DSMZ `600` representation confirms the same M14 source formula: a main 1 L solution with 1 g yeast extract, 1 g glucose, 10 ml vitamin solution, 20 ml Hutner's salts, 50 ml Tris-HCl buffer, 250 ml artificial seawater, and 680 ml distilled water.

The generated recipe is a one-source merge of the TOGO owner, so the defects are already present in `data/normalized_yaml/bacterial/TOGO_M2346_M14_Pirellula_Marina_Medium.yaml`.

## Evidence

- TOGO API record `M2346` reports a DSMZ Medium 600 source URL and separates the formula into main solution, vitamin solution, artificial sea water, Hutner's basal salts, and `Metals 44`.
- TOGO stores artificial-seawater trace salts such as H3BO3, KCl, NaHCO3, NaF, KBr, and SrCl2 with `unit: mg` in the source payload, not grams.
- TOGO stores Hutner and Metals trace entries such as 9.25 mg ammonium molybdate, 99 mg FeSO4 x 7 H2O, 500 mg FeSO4 x 7 H2O, 1095 mg ZnSO4 x 7 H2O, and 250 mg Na-EDTA in nested 1 L stocks.
- MediaDive REST for DSMZ `600` confirms that M14 omits peptone, uses the smaller 600-series vitamin stock, and adds the artificial-seawater stock at 250 ml/L.

## Completeness

The record captures the source hierarchy only superficially. It preserves some main-solution names, but solution volumes are represented as gram-per-liter mass concentrations; 1 L stock waters are collapsed into a nonsensical `4630.0 G_PER_L` water ingredient; milligram trace salts are recorded as grams; and nested vitamin, Hutner, Metals, and artificial-seawater stocks are not diluted into the final liter.

The record also lacks structured source references and target-organism grounding.

## Findings

1. Source milligram quantities were converted to gram-per-liter values without dividing by 1000. Examples from artificial seawater alone include H3BO3 `26 G_PER_L` instead of a 0.026 g/L stock value, KCl `664 G_PER_L` instead of 0.664 g/L stock, NaHCO3 `192 G_PER_L` instead of 0.192 g/L stock, NaF `3 G_PER_L` instead of 0.003 g/L stock, KBr `96 G_PER_L` instead of 0.096 g/L stock, and SrCl2 `24 G_PER_L` instead of 0.024 g/L stock.

2. The 250 ml artificial-seawater addition was not applied. Even gram-scale stock entries such as NaCl, MgCl2 x 6 H2O, Na2SO4, and CaCl2 are copied at their 1 L stock concentrations instead of one-quarter final concentrations.

3. Vitamin, Hutner, and Metals stocks were flattened without nested dilution. The vitamin stock is added at 10 ml/L, Hutner's salts at 20 ml/L, and `Metals 44` at 50 ml per liter of Hutner stock; the YAML stores the undiluted stock masses directly. The `FeSO4 x 7 H2O` row is especially wrong because it sums 99 mg and 500 mg as `599.0 G_PER_L` before applying either the 0.02 Hutner or 0.001 Metals final factors.

4. Stock solutions are represented as mass ingredients. The main solution contains `Hutner's basal salts`, `Artifical sea water`, and Tris-HCl buffer as volume additions, but the YAML stores them as `20 G_PER_L`, `250 G_PER_L`, and `50 G_PER_L`. It also leaves escaped `\"Metals 44\"` as a `50 G_PER_L` ingredient.

5. The ammonium molybdate formula is corrupted as `(NH4)6MoO7O24 x 4 H2O`; the DSMZ/MediaDive source uses `(NH4)6Mo7O24 x 4 H2O`. The generated formula should not keep the TOGO parsing artifact.

## Recommended Edits

- Reimport `TOGO:M2346` or curate `data/normalized_yaml/bacterial/TOGO_M2346_M14_Pirellula_Marina_Medium.yaml` from DSMZ Medium 600 with nested stock solutions intact.
- Convert all milligram quantities to g/L stock concentrations before calculating final concentrations.
- Apply the final volume factors: 0.25 for artificial seawater, 0.01 for vitamin solution, 0.02 for Hutner's salts, and 0.001 for the nested Metals ingredients.
- Keep Tris-HCl buffer, artificial seawater, Hutner's salts, and Metals as solution additions rather than mass ingredients when the schema supports it.
- Correct the ammonium molybdate formula spelling while grounding it to a hydrate-specific term if one is available.
- Regenerate merged YAML and rerun open schema, strict, reference, and term validation.

## Follow-up Checks

- Compare the corrected TOGO M14 record against the DSMZ `600` MediaDive REST payload before release.
- Search ignored files exactly for `TOGO:M2346` after regeneration to confirm the one-source owner remains unique.
- Review the separate KOMODO `600` owner before deciding whether it should alias this TOGO record or remain quarantined until its DSMZ enrichment is fixed.

## Additional Notes

The generated `mediaingredientmech_chebi_term` for `MgSO4 x 7 H2O` still points to generic magnesium sulfate while `term` points to magnesium sulfate heptahydrate. Fixing the concentrations is higher priority, but that stale linked term should be cleaned up in the same curation pass.
