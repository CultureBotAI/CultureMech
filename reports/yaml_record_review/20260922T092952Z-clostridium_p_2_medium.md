# YAML Record Review: CLOSTRIDIUM (P-2) MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_p_2_medium.yaml`
- Started UTC: `2026-09-22T09:29:52Z`
- Finished UTC: `2026-09-22T09:30:04Z`
- Verdict: pass with minor issues

## Target

Generated bacterial `MediaRecipe` record `CultureMech:001816` for MediaDive medium `677`, DSMZ Medium 677 `CLOSTRIDIUM (P-2) MEDIUM`. The generated record merges the MediaDive source with KOMODO duplicate `p_2_medium.yaml` on merge fingerprint `23e78c6c1324e9cab458f86ada185080162731a50e55ba31d332205e7b63e219`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/clostridium_p_2_medium.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The DSMZ identity is correct. The record links to `mediadive.medium:677`, carries the DSMZ label, and merged the KOMODO `komodo.medium:677` duplicate rather than emitting it as a second generated record.

All defined chemical ingredients are grounded to appropriate CHEBI terms. Yeast extract is intentionally left ungrounded as an undefined component, and `Sodium resazurin` is represented as the correct final 0.0005 g/l contribution from 0.5 ml of 0.1% w/v source solution.

The only identity metadata issue is that `parent_media.path` points to the KOMODO duplicate `data/normalized_yaml/bacterial/p_2_medium.yaml`, while the generated canonical record itself is the direct DSMZ/MediaDive record.

## Evidence

The DSMZ Medium 677 PDF supports the complete formula in the generated record: K2HPO4 3 g/l, KH2PO4 2 g/l, NH4Cl 2 g/l, MgCl2 x 6 H2O 0.2 g/l, CaCl2 x 2 H2O 0.05 g/l, yeast extract 5 g/l, 0.5 ml 0.1% sodium resazurin, D-glucose 5 g/l, L-Cysteine HCl x H2O 0.5 g/l, Na2S x 9 H2O 0.5 g/l, and 1000 ml distilled water.

The DSMZ preparation paragraph also matches `preparation_steps[0]`: all ingredients except glucose, cysteine, and sulfide are dissolved first; the medium is sparged with 100% N2 for 30-45 min; dispensing and autoclaving happen under the same atmosphere; glucose, cysteine, and sulfide are added from sterile anoxic stock solutions; and pH is adjusted to 7.0-7.2 if necessary.

The ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found only the direct DSMZ source and its KOMODO duplicate for exact DSMZ Medium 677 identifiers and URLs; ignored files were included.

## Completeness

The record carries the source pH range and the substantive anoxic preparation steps.

Source water is not represented as a separate ingredient, which is consistent with the surrounding direct MediaDive normalized records and is not a defect by itself.

No target organism is listed.

## Findings

- Minor: `parent_media` identifies the duplicate KOMODO source as the parent even though the generated record's `media_term` is the direct DSMZ/MediaDive medium. The duplicate relationship is correct, but the parent direction is unintuitive.
- Minor: the source duplicate `p_2_medium.yaml` still has the inherited KOMODO note `Aerobic: Yes`, contrary to DSMZ's anoxic N2 preparation; that stale note does not surface in the generated record except through the synonym metadata.

## Recommended Edits

- Prefer the DSMZ/MediaDive source as the duplicate-group parent when regenerating merged metadata.
- Clean stale KOMODO aerobic annotations for DSMZ anaerobic media during duplicate import or merge normalization.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validators after any metadata regeneration.
- Confirm `p_2_medium` remains merged and no second generated DSMZ Medium 677 branch is emitted.
- Confirm resazurin remains a correctly diluted final concentration if source solution rows continue to be flattened.

## Additional Notes

No formula-level curation issues were found. Empty optional fields are not defects, and the flat formula is appropriate here because DSMZ Medium 677 does not define nested trace or vitamin stocks.
