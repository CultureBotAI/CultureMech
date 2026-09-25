# YAML Record Review: thermoplasma_medium__b7efc8b9

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoplasma_medium__b7efc8b9.yaml`
- Started UTC: 2026-09-25T10:34:00Z
- Finished UTC: 2026-09-25T10:39:00Z
- Verdict: needs curation

## Target

- Reviewed generated direct MediaDive/JCM merge record `CultureMech:002541`.
- Media term: `mediadive.medium:J180`, `THERMOPLASMA MEDIUM`.
- Merge sources: `picrophilus_medium.yaml`, `thermogymnomonas_medium.yaml`, and `thermoplasma_medium.yaml`.

## Validation

- Schema validation: passed with `linkml-validate`; no issues found.
- Strict validation: passed; `/private/tmp/thermoplasma_medium__b7efc8b9.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; 0 checks were configured for this record.
- Term validation: passed; exited 0 with no diagnostics.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- JCM Medium 180 is Thermoplasma Medium at pH 2.0 with yeast extract 1 g/L.
- JCM Medium 233 is Picrophilus Medium; it explicitly says to use Medium 180 with 2.0 g/L final yeast extract and pH 1.0.
- DSMZ Medium 1141 is Thermogymnomonas Medium at pH 3.0.
- An exact ignored-inclusive search found all three sources folded into this generated record and also found a separate KOMODO DSMZ 1141 generated record.

## Evidence

- `/private/tmp/jcm_180.html` and `/private/tmp/mediadive_J180.json` confirm the JCM 180 formula, pH 2.0, and the 10% yeast extract and glucose stock addition instruction.
- `/private/tmp/jcm_233.html` and `/private/tmp/mediadive_J233.json` confirm that Picrophilus Medium is a JCM 180 derivative with yeast extract raised to 2.0 g/L and pH lowered to 1.0.
- `/private/tmp/DSMZ_Medium1141.txt` and `/private/tmp/mediadive_1141.json` confirm that Thermogymnomonas Medium uses the same six main ingredients but pH 3.0.
- Local duplicate detection was rerun with `rg --no-ignore --hidden` against exact current source IDs and filenames, so ignored generated indexes were included.

## Completeness

- The JCM 180 ingredient list and pH 2.0 preparation step are represented.
- The Picrophilus and Thermogymnomonas source-specific pH values are not represented in variants.
- The Picrophilus 2.0 g/L yeast extract change is absent from the generated ingredient list.
- The merged record omits distilled water even though each direct MediaDive/JCM source carries a 1000 ml water basis where a full recipe is available.

## Findings

- The merge collapsed three biologically named records across different pH values and, for JCM 233, a different yeast-extract concentration.
- The source duplicate metadata points at `data/normalized_yaml/bacterial/picrophilus_medium.yaml` even though the observed Picrophilus source file is under `data/normalized_yaml/archaea/`.
- Thermogymnomonas DSMZ 1141 is present here as a synonym and still exists as a separate KOMODO-derived generated target.

## Recommended Edits

- Split Picrophilus Medium and Thermogymnomonas Medium out of the JCM 180 Thermoplasma Medium canonical record or model them as evidence-backed variants with their own pH and yeast-extract changes.
- Correct the stale Picrophilus parent path before regenerating merge outputs.
- Preserve source water rows when rebuilding direct JCM/DSMZ recipes.
- De-duplicate the direct DSMZ 1141 representation against KOMODO 1141 after the Thermogymnomonas record is separated from JCM 180.

## Follow-up Checks

- Rebuild the merge YAML and confirm JCM 180, JCM 233, and DSMZ 1141 no longer collapse solely because their basal salts overlap.
- Re-run schema, strict, reference, and term validation on the regenerated targets.
- Re-run exact ignored-inclusive searches for `mediadive.medium:J180`, `mediadive.medium:J233`, and `mediadive.medium:1141`.

## Additional Notes

None found.
