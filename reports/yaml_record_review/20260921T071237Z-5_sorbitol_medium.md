# YAML Record Review: 5_sorbitol_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/5_sorbitol_medium.yaml
- Started UTC: 2026-09-21T07:11:51Z
- Finished UTC: 2026-09-21T07:12:37Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/5_sorbitol_medium.yaml`.
- Stable identifier: `CultureMech:001757`.
- Source identity asserted by the record: DSMZ / MediaDive `626`, `5% SORBITOL MEDIUM`.
- The generated record was merged from one owner, `5_sorbitol_medium.yaml`, on fingerprint `a64c0871cf82886170cfa1626fb081e459ac60f41e86adff55e8ee6ab008dc0c`.
- Current authoritative owner: `data/normalized_yaml/bacterial/5_sorbitol_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/5_sorbitol_medium.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/5_sorbitol_medium.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/5_sorbitol_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/5_sorbitol_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- The DSMZ / MediaDive identity is coherent: `mediadive.medium:626`, the original name, the linked DSMZ PDF, the BacMedia text rendering, and the extracted PDF all identify medium 626 as `5% SORBITOL MEDIUM`.
- A gitignore-independent exact search with a digit boundary for `mediadive.medium:626` found the direct DSMZ owner and generated record, plus the KOMODO medium 626 owner and generated record whose notes explicitly say it was enriched from DSMZ medium 626.
- A gitignore-independent exact search with a digit boundary for `komodo.medium:626` found only the KOMODO duplicate owner and generated record.

## Evidence

- DSMZ Medium 626 lists 50 g D-sorbitol, 10 g yeast extract, 10 g peptone, 15 g agar, and 1000 ml distilled water.
- The DSMZ PDF and BacMedia text both state that the final medium should be adjusted to pH 6.0 with HCl.
- The generated target has the four non-solvent rows at the source masses per litre, records `ph_value: 6.0`, and keeps HCl as a preparation instruction rather than as a variable ingredient.

## Completeness

- The direct DSMZ target is complete at the ingredient level for non-solvent rows and final pH.
- Distilled water is omitted from the direct target, which is acceptable as a solvent omission here because the source uses it only to make the medium up to 1 L.
- The record does not carry a structured `references` entry for the DSMZ PDF, but the PDF URL is present in `notes`.

## Findings

- BLOCKER: DSMZ Medium 626 is represented by two separate active generated records: this direct DSMZ / MediaDive import and the KOMODO 626 record at `data/merge_yaml/merged/5_sorbitol_medium__c395a410.yaml`. They contain the same DSMZ formulation but carry separate CultureMech IDs and fingerprints.
- MAJOR: the KOMODO-side duplicate includes a variable HCl ingredient for pH adjustment. HCl is correctly modeled as a pH-adjustment instruction in this direct DSMZ target.
- MINOR: source provenance is note-only; the DSMZ PDF URL should be promoted to a structured reference or source slot.

## Recommended Edits

- Reconcile `data/normalized_yaml/bacterial/5_sorbitol_medium.yaml` with `data/normalized_yaml/bacterial/KOMODO_626_5_SORBITOL_medium.yaml` so one canonical DSMZ Medium 626 recipe is generated.
- Preserve both `mediadive.medium:626` and `komodo.medium:626` as source identities or cross-references.
- Preserve the direct DSMZ treatment of HCl as a pH adjustment rather than keeping the KOMODO variable ingredient row.
- Add a structured reference for the linked DSMZ Medium 626 PDF.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after duplicate reconciliation.
- Confirm that only one active generated record remains for DSMZ Medium 626.
- Confirm that no `HCl` ingredient with `VARIABLE` concentration remains in the canonical 5% Sorbitol Medium record.

## Additional Notes

- This generated target is source-faithful on recipe chemistry; its failure is the active duplicate for the same DSMZ medium.
