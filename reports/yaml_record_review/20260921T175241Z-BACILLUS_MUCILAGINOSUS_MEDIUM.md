# YAML Record Review: BACILLUS MUCILAGINOSUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACILLUS_MUCILAGINOSUS_MEDIUM.yaml
- Started UTC: 2026-09-21T17:51:42Z
- Finished UTC: 2026-09-21T17:52:41Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:004062 |
| Generated record | data/merge_yaml/merged/BACILLUS_MUCILAGINOSUS_MEDIUM.yaml |
| DSMZ owner | data/normalized_yaml/bacterial/bacillus_mucilaginosus_medium.yaml |
| KOMODO owner | data/normalized_yaml/bacterial/KOMODO_1307_BACILLUS_MUCILAGINOSUS_MEDIUM.yaml |
| Label | BACILLUS MUCILAGINOSUS MEDIUM |
| Source identity | KOMODO 1307 / DSMZ Medium 1307 |
| Merge state | Two-source SOURCE_DUPLICATE merge from DSMZ and KOMODO 1307 |

The DSMZ and KOMODO normalized owners have the same ingredient signature, so
the source-duplicate relationship is plausible. Future completeness fixes
belong in the normalized owners or merge overlay before regenerating this
derived record.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACILLUS_MUCILAGINOSUS_MEDIUM.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/BACILLUS_MUCILAGINOSUS_MEDIUM.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

The focused validators used the offline `uv --no-project` Python 3.11
workaround because direct project `just` validation currently fails during
Python 3.13 dependency resolution while building `llvmlite==0.46.0`.

## Identity and Grounding

- **Medium identity is correct.** The record's label, `media_term`, DSMZ 1307
  note on the KOMODO owner, and parent DSMZ record all point to DSMZ Medium
  1307, BACILLUS MUCILAGINOSUS MEDIUM.
- **The duplicate merge is well grounded.** KOMODO 1307 explicitly cites DSMZ
  1307, and the two normalized owners agree on physical state, pH, ingredient
  names, and concentrations.
- **Chemical groundings are compatible with the DSMZ labels.** Sucrose, K2HPO4,
  MgSO4 x 7 H2O, CaCO3, and agar all use terms that preserve the source
  identities.

## Evidence

- DSMZ Medium 1307 lists sucrose 10.0 g, K2HPO4 1.0 g, MgSO4 x 7 H2O 0.2 g,
  CaCO3 5.0 g, agar 15.0 g, and distilled water made up to 1000.0 ml.
- DSMZ Medium 1307 instructs adjusting pH to 7.6 and autoclaving at 121 C for
  15 minutes.
- The generated record keeps the five non-water ingredient rows and `ph_value:
  7.6`, but it has no distilled-water row and no `preparation_steps`.
- The DSMZ normalized owner already has the pH/autoclave preparation step; the
  KOMODO normalized owner does not, and the generated canonical record selected
  the leaner KOMODO copy as `CultureMech:004062`.

## Completeness

- The final `Distilled water make up to 1000.0 ml` row is missing.
- The 121 C for 15 minutes autoclave instruction is missing from the generated
  record and the KOMODO owner.
- `target_organisms`, growth metrics, incubation temperature, and salinity are
  empty. The inspected DSMZ 1307 PDF does not supply those claims, so I did not
  count them as defects.
- A gitignore-independent search of `reports/yaml_record_review` for
  `BACILLUS_MUCILAGINOSUS_MEDIUM` and `BACILLUS MUCILAGINOSUS MEDIUM` found no
  prior report before this file was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The final water row is absent. | DSMZ 1307 says to make the medium up to 1000.0 ml with distilled water; neither the KOMODO owner nor the generated record has a water ingredient. | `data/normalized_yaml/bacterial/KOMODO_1307_BACILLUS_MUCILAGINOSUS_MEDIUM.yaml`; merge overlay, or both normalized owners for consistency. |
| Major | The autoclave instruction was dropped in the generated canonical copy. | DSMZ 1307 and `bacillus_mucilaginosus_medium.yaml` include autoclaving at 121 C for 15 minutes, but the generated KOMODO-canonical record has no `preparation_steps`. | Merge overlay or `data/normalized_yaml/bacterial/KOMODO_1307_BACILLUS_MUCILAGINOSUS_MEDIUM.yaml`. |
| Minor | Source evidence is encoded only as notes and curation history. | DSMZ and KOMODO source IDs appear in free text and merge metadata, but there is no structured reference or evidence tying ingredient rows to DSMZ Medium 1307 or KOMODO 1307. | MediaDive/KOMODO importers or the two normalized owners. |

## Recommended Edits

1. Add the final 1000 ml distilled-water row from DSMZ 1307.
2. Preserve the DSMZ 1307 pH/autoclave preparation step when merging the DSMZ
   parent and KOMODO duplicate, either by enriching the KOMODO owner or by
   preferring the DSMZ parent for text fields.
3. Add structured source provenance for DSMZ Medium 1307 and KOMODO 1307.
4. Regenerate merged products.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the repaired owners.
- Regenerate merges and verify `BACILLUS_MUCILAGINOSUS_MEDIUM.yaml` has the
  1000 ml water row and the 121 C autoclave instruction while keeping only one
  canonical DSMZ/KOMODO 1307 record.
- Compare the regenerated record manually against DSMZ Medium 1307.

## Additional Notes

- The exact prior-report search used `find` and `rg --no-ignore --hidden`, so
  ignored review reports were included.
