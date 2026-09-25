# YAML Record Review: bacillus_racemilacticus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bacillus_racemilacticus_medium.yaml
- Started UTC: 2026-09-21T17:58:12Z
- Finished UTC: 2026-09-21T17:59:22Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:006760 |
| Generated record | data/merge_yaml/merged/bacillus_racemilacticus_medium.yaml |
| DSMZ owner | data/normalized_yaml/bacterial/bacillus_racemilacticus_medium.yaml |
| KOMODO owner | data/normalized_yaml/bacterial/KOMODO_8_BACILLUS_RACEMILACTICUS_medium.yaml |
| Label | BACILLUS "RACEMILACTICUS" medium |
| Source identity | KOMODO 8 / DSMZ Medium 8 |
| Merge state | Two-source SOURCE_DUPLICATE merge from DSMZ and KOMODO 8 |

The DSMZ and KOMODO normalized owners agree on the ingredient signature, so the
source-duplicate relationship is plausible. Future completeness fixes belong in
the normalized owners or merge overlay before regenerating this derived record.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bacillus_racemilacticus_medium.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/bacillus_racemilacticus_medium.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

The focused validators used the offline `uv --no-project` Python 3.11
workaround because direct project `just` validation currently fails during
Python 3.13 dependency resolution while building `llvmlite==0.46.0`.

## Identity and Grounding

- **Medium identity is correct.** KOMODO Medium 8 states DSMZ Medium 8
  provenance, and DSMZ Medium 8 is BACILLUS "RACEMILACTICUS" MEDIUM.
- **The duplicate merge is well grounded.** KOMODO 8 and the DSMZ owner agree on
  glucose, peptone, yeast extract, CaCO3, agar, pH, and solid agar state.
- **Displayed groundings are compatible with the source.** Glucose, CaCO3, and
  agar preserve their DSMZ ingredient identities; peptone and yeast extract are
  correctly left ungrounded as undefined components.

## Evidence

- DSMZ Medium 8 lists glucose 5.0 g, peptone 5.0 g, yeast extract 5.0 g, CaCO3
  5.0 g, agar 15.0 g, and distilled water 1000.0 ml.
- DSMZ Medium 8 instructs pH adjustment to 6.8.
- The generated record keeps every non-water ingredient amount and stores
  `ph_value: 6.8`.
- The generated record has no distilled-water row and no pH-adjustment
  `preparation_steps`.

## Completeness

- The final 1000 ml distilled-water row is missing.
- The pH 6.8 adjustment instruction is missing from the generated record and
  KOMODO owner.
- `target_organisms`, growth metrics, incubation temperature, and salinity are
  empty. The inspected DSMZ 8 PDF does not supply those claims, so I did not
  count them as defects.
- A gitignore-independent search of `reports/yaml_record_review` for the exact
  stem `bacillus_racemilacticus_medium` found no prior report before this file
  was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The final water row is absent. | DSMZ 8 lists `Distilled water 1000.0 ml`; neither the KOMODO owner nor the generated record has a water ingredient. | `data/normalized_yaml/bacterial/KOMODO_8_BACILLUS_RACEMILACTICUS_medium.yaml`; merge overlay, or both normalized owners for consistency. |
| Major | The pH-adjustment instruction was dropped in the generated canonical copy. | DSMZ 8 and `bacillus_racemilacticus_medium.yaml` include `Adjust pH to 6.8`; the generated KOMODO-canonical record has only `ph_value: 6.8` and no `preparation_steps`. | Merge overlay or `data/normalized_yaml/bacterial/KOMODO_8_BACILLUS_RACEMILACTICUS_medium.yaml`. |
| Minor | Source evidence is encoded only as notes and curation history. | DSMZ and KOMODO source IDs appear in free text and merge metadata, but there is no structured reference or evidence tying ingredient rows to DSMZ Medium 8 or KOMODO 8. | MediaDive/KOMODO importers or the two normalized owners. |

## Recommended Edits

1. Add the final 1000 ml distilled-water row from DSMZ 8.
2. Preserve the DSMZ 8 pH-adjustment preparation step when merging the DSMZ
   parent and KOMODO duplicate, either by enriching the KOMODO owner or by
   preferring the DSMZ parent for text fields.
3. Add structured source provenance for DSMZ Medium 8 and KOMODO Medium 8.
4. Regenerate merged products.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the repaired owners.
- Regenerate merges and verify `bacillus_racemilacticus_medium.yaml` has the
  1000 ml distilled-water row and pH adjustment step while keeping only one
  canonical DSMZ/KOMODO 8 record.
- Compare the regenerated record manually against DSMZ Medium 8.

## Additional Notes

- The exact prior-report search used `find` and `rg --no-ignore --hidden`, so
  ignored review reports were included.
