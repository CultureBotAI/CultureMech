# YAML Record Review: marine_broth_with_0_5_methanol

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_broth_with_0_5_methanol.yaml
- Started UTC: 2026-09-23T23:51:56Z
- Finished UTC: 2026-09-23T23:54:09Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | data/merge_yaml/merged/marine_broth_with_0_5_methanol.yaml |
| Class | MediaRecipe |
| ID | CultureMech:008300 |
| Label | marine_broth_with_0_5_methanol |
| Source identity | TOGO:M1738, NBRC Medium 947, Marine Broth with 0.5% Methanol |
| Generation state | Generated four-source merge under data/merge_yaml/merged; repair data/normalized_yaml/bacterial/marine_broth_with_0_5_methanol.yaml, the other merged TOGO inputs, and merge_recipes.py rather than this file |

The generated record is the canonical merge output for TOGO M1738, but it also merges three distinct TOGO/NBRC Marine Broth dilution records: M1774, M2164, and M1916. Its visible formulation is also stale relative to the repaired September 2026 maintained M1738 input.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_broth_with_0_5_methanol.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_broth_with_0_5_methanol.yaml --out /private/tmp/marine_broth_with_0_5_methanol.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_broth_with_0_5_methanol.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_broth_with_0_5_methanol.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning |
| Embedded curation history | Not checked | `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries |

## Identity and Grounding

- CultureMech:008300, `marine_broth_with_0_5_methanol`, and TOGO M1738 agree on the intended source identity: NBRC Medium 947, `Marine Broth with 0.5% Methanol`.
- The generated `media_term` still points to TOGO M1738, but its `merged_from` list and `synonyms` incorrectly equate M1738 with `1_10_marine_broth_agar` from TOGO M1774, `1_2_marine_broth_agar` from TOGO M2164, and `1_5_marine_agar_broth` from TOGO M1916.
- TOGO M1738 and NBRC 947 list 37.4 g Bacto Marine Broth 2216 (Difco), 5 ml methanol, 15 g optional agar, and 1 L distilled water, with pH unadjusted and a note to sterilize methanol separately by filtration.
- The generated ingredient rows do not match TOGO M1738/NBRC 947: the record has 3.7 g/L Bacto Marine Broth 2216 from the 1/10 medium, keeps methanol as a 5 g/L empty `Unknown solution`, and misstates distilled water as 1 g/L.
- The maintained source input at data/normalized_yaml/bacterial/marine_broth_with_0_5_methanol.yaml was already repaired to 37.4 g/L Bacto Marine Broth 2216, 5 ml/L methanol, 15 g/L optional agar, and 1000 ml/L distilled water, with the filter-sterilization steps and M1738/NBRC 947 references preserved.

## Evidence

- TOGO M1738 preserves NBRC Medium 947 as the original source and points to NBRC `NO=947`; both sources list the same full-strength Marine Broth with 0.5% Methanol formulation.
- TOGO M1774 is a separate NBRC M990 record named `1/10 Marine Broth (Agar)` and lists 3.7 g Bacto Marine Broth 2216, 15 g optional agar, and 1 L distilled water. This supports the 3.7 g/L Bacto amount in the generated YAML only for M1774, not for M1738.
- The sibling inputs for TOGO M2164 and TOGO M1916 have separate CultureMech IDs, source accessions, labels, curation histories, and concentration-variant links; they should not be synonyms of M1738.
- Agar is source-supported only as an optional solidifying ingredient. The generated `physical_state: SOLID_AGAR` makes the whole M1738 recipe look obligatorily solid.
- No target organism, organism growth result, incubation condition, or primary literature growth claim is asserted by this generated record.

## Completeness

- The generated record is not a complete faithful M1738 projection until the false M1774/M2164/M1916 merge is split and the M1738-specific rows are regenerated from the repaired maintained input.
- The M1738 pH comment and methanol filter-sterilization instruction are missing from the generated record even though both are present in TOGO/NBRC and in the maintained M1738 YAML.
- The optional lack of target-organism entries is acceptable because the TOGO/NBRC recipe sources inspected here are formulation sources, not growth evidence.
- Exact gitignore-independent searches were run for `CultureMech:008300`, `marine_broth_with_0_5_methanol`, `TOGO:M1738`, `TOGO:M1774`, `TOGO:M2164`, `TOGO:M1916`, and the merge fingerprint across the scoped bacterial normalized YAML directory, this target merged YAML, and the TOGO, bacterial, and recipe index files with `--no-ignore --hidden`; the searches found the target input, the three incorrectly merged sibling inputs, and the expected index entries.
- An exact `find reports/yaml_record_review -maxdepth 1 -name '*-marine_broth_with_0_5_methanol.md' -print` search, which includes ignored files, found no pre-existing review report for this generated record before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The generated M1738 record falsely merges three different NBRC media into Marine Broth with 0.5% Methanol. | M1774, M2164, and M1916 have distinct TOGO/NBRC accessions, labels, source formulations, and CultureMech IDs, but the generated record lists them under `merged_from` and `synonyms` for M1738. | merge_recipes.py and the normalized TOGO records under data/normalized_yaml/bacterial |
| major | The generated formulation is stale relative to the repaired maintained M1738 input and authoritative sources. | TOGO M1738/NBRC 947 list 37.4 g Bacto Marine Broth 2216, 5 ml methanol, 15 g optional agar, and 1 L water; data/normalized_yaml/bacterial/marine_broth_with_0_5_methanol.yaml encodes those rows, but the generated merge still shows 3.7 g/L Bacto Marine Broth 2216, 1 g/L water, and a 5 g/L empty `Methanol*` solution. | data/merge_yaml generation after repair of merge_recipes.py |
| minor | Optional agar is represented as a required solid recipe state. | TOGO M1738 and NBRC 947 label agar as `if needed`, while the generated record sets top-level `physical_state: SOLID_AGAR`. | data/normalized_yaml/bacterial/marine_broth_with_0_5_methanol.yaml and the sibling TOGO Marine Broth dilution records |

## Recommended Edits

1. Tighten duplicate-merge identity checks so TOGO M1738 no longer merges with the M1774, M2164, or M1916 dilution records, then regenerate `data/merge_yaml/merged/`.
2. Confirm the regenerated M1738 output carries the already repaired maintained M1738 rows: 37.4 g/L Bacto Marine Broth 2216, 5 ml/L methanol, 15 g/L optional agar, 1000 ml/L distilled water, pH unadjusted, and the methanol filter-sterilization step.
3. Split the false `merged_from` and `synonyms` entries so M1774, M2164, and M1916 remain separate records or legitimate concentration variants rather than aliases of M1738.
4. Review the normalized TOGO Marine Broth dilution records for the same water-unit conversion residue and for optional agar being promoted to `SOLID_AGAR`.

## Follow-up Checks

- Re-run duplicate merging and confirm no generated record has the fingerprint `d5e67ebc3e43b20a2b5e584dc015360bd917a820d54848056a706b25e97739dd`.
- Diff the regenerated M1738 YAML against data/normalized_yaml/bacterial/marine_broth_with_0_5_methanol.yaml and verify that its ingredient amounts, pH note, references, and preparation steps survive generation.
- Run open schema, strict schema, reference, and term validation on the repaired normalized inputs and regenerated M1738 merged output.
- Inspect the regenerated TOGO M1774, M2164, and M1916 outputs to ensure they keep their own CultureMech IDs, source accessions, concentration-variant relationships, and non-methanol formulations.

## Additional Notes

- This review found a generated-layer defect over a maintained M1738 input that has already been directly repaired. Patching the generated YAML would hide the stale merge artifact without fixing the merge rule or the sibling false aliases.
