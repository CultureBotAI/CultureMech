# YAML Record Review: BACILLUS PASTEURII MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACILLUS_PASTEURII_MEDIUM.yaml
- Started UTC: 2026-09-21T17:55:54Z
- Finished UTC: 2026-09-21T17:57:56Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:004777 |
| Generated record | data/merge_yaml/merged/BACILLUS_PASTEURII_MEDIUM.yaml |
| DSMZ owner | data/normalized_yaml/bacterial/bacillus_pasteurii_medium.yaml |
| KOMODO owner | data/normalized_yaml/bacterial/KOMODO_2_BACILLUS_PASTEURII_medium.yaml |
| Label | BACILLUS PASTEURII MEDIUM |
| Source identity | KOMODO 2 / DSMZ Medium 2 |
| Merge state | Two-source merge from DSMZ and KOMODO Medium 2 |

The generated target merges a KOMODO copy of DSMZ Medium 2 with a MediaDive
DSMZ Medium 2 record. Future fixes belong in the normalized owners or merge
overlay before regenerating this derived record.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACILLUS_PASTEURII_MEDIUM.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/BACILLUS_PASTEURII_MEDIUM.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

The focused validators used the offline `uv --no-project` Python 3.11
workaround because direct project `just` validation currently fails during
Python 3.13 dependency resolution while building `llvmlite==0.46.0`.

## Identity and Grounding

- **Medium identity is correct.** KOMODO Medium 2 explicitly maps to DSMZ Medium
  2, BACILLUS PASTEURII MEDIUM.
- **The displayed ingredient identities are compatible with DSMZ 2 plus its
  parent DSMZ 1.** DSMZ 2 adds 20 g/L urea to Medium 1; Medium 1 supplies
  peptone 5 g/L, meat extract 3 g/L, and 15 g/L agar when agar is needed.
- **Parent-medium context was lost.** DSMZ 2 is defined as a modification of
  Medium 1, but the generated record has only the flattened rows and not the
  water or instructions inherited from Medium 1 and DSMZ 2.

## Evidence

- DSMZ Medium 2 says to add 20 g/L urea to Medium 1 before autoclaving, not to
  adjust pH because heat-degraded urea raises pH to about 8, and to add
  10 mg/L MnSO4 x H2O for sporulation enhancement.
- DSMZ Medium 1 lists peptone 5.0 g, meat extract 3.0 g, agar if necessary
  15.0 g, and distilled water 1000.0 ml, with pH adjusted to 7.0 before the
  DSMZ 2 urea modification.
- The generated record contains the urea, peptone, meat extract, and agar
  amounts and stores `ph_value: 8.0`.
- The generated record has no water row and no preparation text.

## Completeness

- The Medium 1 distilled-water row is missing.
- The Medium 2 preparation instruction to add urea before autoclaving and not
  manually adjust pH is missing.
- The optional 10 mg/L MnSO4 x H2O sporulation enhancement note is missing.
- `target_organisms`, growth metrics, incubation temperature, and salinity are
  empty. The inspected DSMZ PDFs do not supply those claims, so I did not count
  them as defects.
- A gitignore-independent search of `reports/yaml_record_review` for
  `BACILLUS_PASTEURII_MEDIUM` and `BACILLUS PASTEURII MEDIUM` found no prior
  report before this file was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The parent Medium 1 water row is absent. | DSMZ 2 modifies Medium 1, and Medium 1 includes `Distilled water 1000.0 ml`; neither the KOMODO owner nor the generated merge has a water ingredient. | `data/normalized_yaml/bacterial/KOMODO_2_BACILLUS_PASTEURII_medium.yaml`; merge overlay, or both owners for consistency. |
| Major | DSMZ preparation context was dropped in the KOMODO-canonical merge. | DSMZ 2 explains that urea is added before autoclaving and drives pH to about 8; the DSMZ owner retains this note, while the generated KOMODO-canonical record has no `preparation_steps`. | Merge overlay or `data/normalized_yaml/bacterial/KOMODO_2_BACILLUS_PASTEURII_medium.yaml`. |
| Major | The source sporulation enhancement is missing. | DSMZ 2 says 10 mg/L MnSO4 x H2O can be added for sporulation enhancement; the generated record has no conditional additive or preparation note for MnSO4. | Both normalized owners or DSMZ/KOMODO importers. |
| Minor | Source evidence is encoded only as notes and merge metadata. | DSMZ and KOMODO source IDs appear in free text and curation history, but there is no structured reference or evidence tying ingredient rows to DSMZ Medium 2, DSMZ Medium 1, or KOMODO 2. | MediaDive/KOMODO importers or the two normalized owners. |

## Recommended Edits

1. Add the distilled-water row inherited from DSMZ Medium 1.
2. Preserve the DSMZ Medium 2 urea/autoclave/pH instruction when merging the
   DSMZ parent and KOMODO duplicate, either by enriching the KOMODO owner or by
   preferring the DSMZ parent for text fields.
3. Encode the optional MnSO4 x H2O sporulation enhancement as a preparation note
   or conditional additive instead of dropping it.
4. Add structured source provenance for DSMZ Medium 2, inherited DSMZ Medium 1,
   and KOMODO Medium 2.
5. Regenerate merged products.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the repaired owners.
- Regenerate merges and verify `BACILLUS_PASTEURII_MEDIUM.yaml` has the 1000 ml
  inherited water row and DSMZ 2 preparation text while keeping the
  source-supported 20 g/L urea and pH 8.
- Compare the regenerated record manually against DSMZ Medium 2 and Medium 1.

## Additional Notes

- The exact prior-report search used `find` and `rg --no-ignore --hidden`, so
  ignored review reports were included.
