# YAML Record Review: DESULFOVIBRIO MEDIUM (CHOLINE)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_medium_choline.yaml`
- Started UTC: 2026-09-22T20:43:47Z
- Finished UTC: 2026-09-22T20:44:46Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:001776` for `desulfovibrio_medium_choline`, a MediaDive import of DSMZ Medium 63c.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, exit 0 with a header-only TSV and 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The record is grounded to `mediadive.medium:63c`, `DESULFOVIBRIO MEDIUM (CHOLINE)`, with the DSMZ Medium 63c PDF URL preserved in `notes`.

A gitignore-independent exact duplicate check found `data/normalized_yaml/bacterial/desulfovibrio_medium_choline.yaml` plus `data/normalized_yaml/bacterial/KOMODO_272_DESULFOVIBRIO_medium_choline.yaml`. The KOMODO 272 file is a stale DSMZ-source duplicate that is now linked to DSMZ Medium 63c in normalized YAML, but the generated target predates those September 2026 repairs.

## Evidence

MediaDive 63c represents the final 1 liter medium as 980 ml Solution A, 10 ml Solution B, and 10 ml Solution C.

Solution A contains the phosphate, ammonium, sulfate, calcium, magnesium, choline chloride, yeast extract, 0.5 ml 0.1% w/v sodium resazurin, and 980 ml water. Solution B contains 0.5 g ferrous sulfate heptahydrate in 10 ml water. Solution C contains 0.1 g sodium thioglycolate and 0.1 g ascorbic acid in 10 ml water.

## Completeness

The generated record preserves the pH range and the long DSMZ preparation text for boiling Solution A under nitrogen, adding Solutions B and C, adjusting pH, dispensing under nitrogen, and autoclaving.

It is stale and chemically incomplete relative to the repaired normalized source. It lacks the 1000 ml/L total water row, has one unsplit preparation paragraph instead of ordered steps, and lists Solution B and Solution C compounds at stock concentrations instead of final-medium amounts.

## Findings

- High: Solution B was flattened at stock strength. The generated target lists `FeSO4 x 7 H2O` as 50 G/L even though DSMZ 63c adds 0.5 g in the 10 ml Solution B used to make 1 liter final medium; the repaired normalized record stores 0.50 G/L.
- High: Solution C was flattened at stock strength. Sodium thioglycolate and ascorbic acid are listed as 10 G/L, but each should be 0.10 G/L in the final 1 liter medium.
- Medium: Solution A ingredients were scaled to their 980 ml stock volume in generated output, yielding values such as K2HPO4 0.510204 G/L and choline chloride 5.10204 G/L; the repaired normalized record stores their final 1 liter amounts.
- Medium: The 980 ml, 10 ml, and 10 ml water contributions are absent from the generated record.
- Medium: The KOMODO 272 source duplicate is already linked in normalized YAML but absent from this generated output.

## Recommended Edits

- Regenerate `data/merge_yaml/merged` from the current `data/normalized_yaml/bacterial/desulfovibrio_medium_choline.yaml` so the September 2026 DSMZ 63c final-concentration repair reaches generated output.
- Confirm the regenerated target uses 0.50 G/L ferrous sulfate, 0.10 G/L sodium thioglycolate, 0.10 G/L ascorbic acid, and 1000 ML/L total water.
- Confirm `KOMODO_272_DESULFOVIBRIO_medium_choline.yaml` remains linked as a source duplicate of DSMZ 63c after regeneration.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Compare the regenerated ingredients against MediaDive 63c and the repaired normalized source rather than the stale August merged artifact.
- Confirm the generated preparation steps are split into the seven curated steps from the normalized source.

## Additional Notes

None found.
