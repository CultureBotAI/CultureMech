# YAML Record Review: DESULFOVIGRA ADIPICA

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovigra_adipica.yaml`
- Started UTC: 2026-09-22T21:06:17Z
- Finished UTC: 2026-09-22T21:06:17Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:006698` for `desulfovigra_adipica`, a KOMODO 868 placeholder for DSMZ Medium 868.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The target is grounded to `komodo.medium:868`, `DESULFOVIGRA ADIPICA`, with DSMZ 868 provenance in `notes`.

A gitignore-independent exact lookup found only this Desulfovigra adipica normalized source. MediaDive has no live record for DSMZ 868, and the stale generated `kg_microbe_match: mediadive.medium:634c` resolves to `RCM MEDIUM (N2/CO2)`, not to DSMZ 868.

## Evidence

The current normalized source has already been repaired from an archived DSMZ Medium 868 PDF. It lists Desulfovigra adipica as basal DSMZ Medium 503 supplemented per liter with 7.0 ml 10% Na2SO4, 10.0 ml 10% yeast extract, 1.0 ml trace element solution from DSMZ Medium 320, 50.0 ml 5% NaHCO3, 1.0 ml selenite-tungstate solution from DSMZ Medium 385, 10.0 ml vitamin solution from DSMZ Medium 141, 1.0 ml 10% propanol, and 17.0 ml 3% Na2S x 9H2O.

The repaired normalized record also carries pH 7.0-7.2, instructions to adjust with sterile anaerobic 5% Na2CO3 and feed the same amount of propanol again after growth starts, and a reference to the archived DSMZ 868 PDF.

## Completeness

The generated record is stale relative to the repaired normalized source. It has only a variable Na2CO3 placeholder that was extracted from old notes, no DSMZ 868 supplements, no stock additions, no preparation steps, no archived-DSMZ reference, and the stale `kg_microbe_match` that the September repair removed.

No source formula from the archived DSMZ record is represented in the generated output.

## Findings

- High: The generated target predates the September DSMZ 868 repair and omits every curated archived-DSMZ stock addition.
- High: The stale `kg_microbe_match: mediadive.medium:634c` still points at RCM Medium (N2/CO2), an unrelated MediaDive record.
- High: The only generated ingredient is variable Na2CO3 from old recipe notes; the repaired source uses sterile anaerobic 5% Na2CO3 only for pH adjustment after the DSMZ 503 basal medium is completed.
- Medium: The generated record omits the repaired pH-adjustment and propanol-feeding preparation steps.
- Medium: The generated record omits the archived DSMZ 868 reference.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/desulfovigra_adipica.yaml` from the repaired `data/normalized_yaml/bacterial/desulfovigra_adipica.yaml`.
- Confirm the regenerated output no longer contains `kg_microbe_match: mediadive.medium:634c` or a one-row variable Na2CO3 formula.
- Preserve the curated DSMZ 868 supplement list, preparation steps, and archived DSMZ reference through merge generation.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating merged YAML.
- Verify the regenerated record exposes basal DSMZ Medium 503 plus the eight archived DSMZ 868 supplement additions.
- Verify the regenerated preparation text keeps the pH 7.0-7.2 Na2CO3 adjustment and propanol-feeding instruction.

## Additional Notes

None found.
