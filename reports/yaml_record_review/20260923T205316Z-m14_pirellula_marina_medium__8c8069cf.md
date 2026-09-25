# YAML Record Review: M14 (PIRELLULA MARINA) MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/m14_pirellula_marina_medium__8c8069cf.yaml`
- Started UTC: 2026-09-23T20:52:20Z
- Finished UTC: 2026-09-23T20:53:16Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/m14_pirellula_marina_medium__8c8069cf.yaml`
- Maintained owner: `data/normalized_yaml/bacterial/m14_pirellula_marina_medium.yaml`
- CultureMech ID: `CultureMech:001727`
- Media term: `mediadive.medium:600`
- Merge fingerprint: `8c8069cf5a97873d5f3791b6cdd613e20dfbbc9fec8e898809e8473a485f80ec`
- Merge sources: `m14_pirellula_marina_medium`
- Ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found the single direct MediaDive DSMZ `600` owner, generated indexes, the generated one-source merge, a KOMODO `600` record that also mentions `mediadive.medium:600`, and historical validation rows.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows in `/private/tmp/m14_pirellula_marina_medium__8c8069cf.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history` entries were not checked as standalone history records.

## Identity and Grounding

The record identifies MediaDive/DSMZ medium 600, `M14 (PIRELLULA MARINA) MEDIUM`. MediaDive REST confirms that DSMZ `600` has a main 1 L solution with 1 g yeast extract, 1 g glucose, 10 ml vitamin solution, 20 ml Hutner's salts, 50 ml Tris-HCl buffer, 250 ml artificial seawater, and 680 ml distilled water.

The generated recipe is a one-source merge of the direct MediaDive owner. A separate TOGO import of the same DSMZ Medium 600 page exists as `TOGO:M2346`, and the KOMODO `600` import also claims DSMZ Medium 600 but was merged into the M13a Pirellula cluster instead of this DSMZ `600` record.

## Evidence

- MediaDive REST for DSMZ `600` confirms the direct 1 g/L yeast extract and glucose additions.
- The same source confirms that the vitamin solution is a 1 L stock added at 10 ml/L.
- The artificial seawater recipe is a 1 L stock added at 250 ml/L.
- Hutner's salts is a 1 L stock added at 20 ml/L and contains 50 ml of a nested 1 L `Metals 44` stock.

## Completeness

The record captures DSMZ `600` compound names and milligram-to-gram conversions more faithfully than the TOGO import, but it still drops stock hierarchy. It lists stock-solution components at their 1 L stock concentrations, turns volume additions such as Tris-HCl buffer into mass concentrations, and loses explicit source references and target-organism grounding.

## Findings

1. The artificial-seawater stock is not diluted by its 250 ml/L addition. The YAML stores NaCl as `23.47 G_PER_L`, MgCl2 x 6 H2O as `10.64 G_PER_L`, Na2SO4 as `3.92 G_PER_L`, and all trace seawater salts at full 1 L stock concentration, even though their final contribution should be one quarter of those stock values.

2. The vitamin stock is not diluted by its 10 ml/L addition. The YAML stores Vitamin B12 as `0.0001 G_PER_L`, Biotin as `0.002 G_PER_L`, Nicotinamide as `0.009 G_PER_L`, and the 5 mg/L vitamins as `0.005 G_PER_L`; each should carry a 0.01 final factor if the recipe is flattened.

3. Hutner's salts and nested `Metals 44` were flattened before dilution. The final medium receives 20 ml/L of Hutner stock and 0.001 L/L of Metals stock, but the YAML stores Nitrilotriacetic acid as `10 G_PER_L`, MgSO4 x 7 H2O as `29.7 G_PER_L`, and Metals components such as ZnSO4 x 7 H2O as `1.095 G_PER_L`. The `FeSO4 x 7 H2O` row sums 0.099 g/L from Hutner and 0.5 g/L from Metals as `0.599 G_PER_L` instead of applying their separate 0.02 and 0.001 final factors.

4. The 50 ml Tris-HCl buffer addition is represented as `50 G_PER_L`, a mass concentration. It should remain a 0.1 M pH 7.5 buffer volume or be translated to a chemically meaningful final Tris concentration.

5. DSMZ Medium 600 is represented in three disconnected ways: this direct MediaDive owner, the TOGO `M2346` owner, and a KOMODO `600` owner that was imported with a 600b-like ingredient signature and then over-merged with DSMZ `600a` and `600b`. Those need reconciliation so one DSMZ `600` curation is exposed.

## Recommended Edits

- Preserve the 1 g/L yeast extract and 1 g/L glucose direct additions from DSMZ `600`.
- Recalculate flattened ingredients with the artificial-seawater 0.25 factor, vitamin 0.01 factor, Hutner 0.02 factor, and nested Metals 0.001 factor.
- Keep Tris-HCl buffer, artificial seawater, Hutner's salts, and Metals as solution additions when the schema can represent them.
- Reconcile this MediaDive DSMZ `600` owner with TOGO `M2346`, then review the KOMODO `600` import before deciding whether it should alias this record or be regenerated.
- Regenerate merged YAML and rerun open schema, strict, reference, and term validation.

## Follow-up Checks

- Compare the corrected direct MediaDive record with the DSMZ Medium 600 PDF, not only the MediaDive REST transcription.
- Re-run an ignored-inclusive exact search for `mediadive.medium:600`, `TOGO:M2346`, and `komodo.medium:600` after curation to confirm that DSMZ 600 has a coherent identity.
- Confirm final FeSO4 x 7 H2O after duplicate resolution because it has two stock sources with different dilution factors.

## Additional Notes

None found.
