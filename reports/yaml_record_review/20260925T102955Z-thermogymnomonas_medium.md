# YAML Record Review: thermogymnomonas_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermogymnomonas_medium.yaml`
- Started UTC: 2026-09-25T10:24:00Z
- Finished UTC: 2026-09-25T10:29:55Z
- Verdict: needs curation

## Target

- Reviewed generated KOMODO/DSMZ 1141 merge record `CultureMech:003851`.
- Media term: `komodo.medium:1141`, `THERMOGYMNOMONAS medium`.
- Source claims in the record point to KOMODO ModelSEED ID 1141 and DSMZ Medium 1141 via `mediadive.medium:1141`.

## Validation

- Schema validation: passed with `linkml-validate`; no issues found.
- Strict validation: passed; `/private/tmp/thermogymnomonas_medium.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; 0 checks were configured for this record.
- Term validation: passed; only the known `eutils`/`pkg_resources` deprecation warning was emitted.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- DSMZ Medium 1141 and the MediaDive REST record agree on the identity `THERMOGYMNOMONAS MEDIUM`.
- The generated KOMODO record has the same DSMZ 1141 ingredient signature as the source: ammonium sulfate 0.2 g/L, KH2PO4 3 g/L, MgSO4 x 7 H2O 0.5 g/L, CaCl2 x 2 H2O 0.25 g/L, yeast extract 1 g/L, and glucose 10 g/L.
- An exact ignored-inclusive search found a separate direct MediaDive normalized record at `data/normalized_yaml/archaea/thermogymnomonas_medium.yaml`; that direct record was merged into `data/merge_yaml/merged/thermoplasma_medium__b7efc8b9.yaml` through the `thermogymnomonas_medium` synonym with `mediadive.medium:1141`.

## Evidence

- `/private/tmp/DSMZ_Medium1141.txt` extracted from the DSMZ Medium 1141 PDF lists the six main ingredients and the pH-3.0 adjustment with 10 N H2SO4.
- `/private/tmp/mediadive_1141.json` mirrors the same six main ingredients at the same concentrations and exposes the same preparation instruction.
- Local duplicate detection was run with `rg --no-ignore --hidden` against `data/normalized_yaml` and `data/merge_yaml/merged`, so ignored generated indexes were included in the source-ID search.

## Completeness

- The ingredient list is source-consistent for the DSMZ main solution.
- The generated KOMODO record represents the pH adjustment as a variable H2SO4 ingredient but does not preserve the DSMZ preparation instruction to adjust to pH 3.0 and autoclave yeast extract and glucose separately as 10% solutions.
- Water is absent in this generated KOMODO record, while the direct MediaDive import records distilled water as 1000 ml.

## Findings

- Duplicate source import: the same DSMZ 1141 source appears both as this KOMODO-derived merge and as a direct MediaDive-derived `thermogymnomonas_medium` source inside `thermoplasma_medium__b7efc8b9.yaml`. These should not remain as two generated recipes for the same underlying source.
- Preparation loss: the KOMODO-derived target lacks the DSMZ preparation step that the direct MediaDive import preserves.

## Recommended Edits

- Fix the normalized input and/or merge logic so KOMODO 1141 and direct MediaDive DSMZ 1141 fold into one canonical DSMZ 1141 representation instead of separate generated records.
- Prefer the direct MediaDive DSMZ 1141 preparation text when building the canonical record, and retain H2SO4 only as a pH-adjustment condition rather than as a quantified basal ingredient.
- After normalizing the duplicate, regenerate the merged YAML instead of hand-editing `data/merge_yaml/merged/thermogymnomonas_medium.yaml`.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated DSMZ 1141 merge target.
- Re-run the exact ignored-inclusive duplicate search for `mediadive.medium:1141` and `KOMODO_1141_THERMOGYMNOMONAS_medium` to confirm there is only one generated DSMZ 1141 recipe.
- Confirm the preparation step survives regeneration.

## Additional Notes

None found.
