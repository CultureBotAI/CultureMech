# YAML Record Review: Brain Heart Infusion Agar With 2% NaCl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_agar_with_2_nacl.yaml
- Started UTC: 2026-09-21T23:40:03Z
- Finished UTC: 2026-09-21T23:40:53Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009128 |
| Label | Brain Heart Infusion Agar With 2% NaCl |
| Primary source | TOGO:M255 / JCM_M263 |
| Generated status | Generated merge of two normalized TOGO records |
| Merge fingerprint | 848f9bc3f74e5aeedf3b08373ace3a1d5d62e90841cf7f233ea1b910f30f20ee |

The reviewed file is a derived merge record. Its maintained inputs are
`data/normalized_yaml/bacterial/TOGO_M255_Brain_Heart_Infusion_Agar_With_2_NaCl.yaml`
for TOGO:M255 and `data/normalized_yaml/bacterial/TOGO_M21_Brain_Heart_Infusion_Agar.yaml`
for TOGO:M21.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_agar_with_2_nacl.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_agar_with_2_nacl.yaml --out /private/tmp/brain_heart_infusion_agar_with_2_nacl.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_agar_with_2_nacl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_agar_with_2_nacl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- TOGO:M255 resolves to Brain Heart Infusion Agar With 2% NaCl, originally
  JCM_M263.
- TOGO:M21 resolves to plain Brain Heart Infusion Agar, originally JCM_M28.
- The generated record incorrectly lists TOGO:M21 as a synonym of the M255 2%
  NaCl recipe.
- A corrected gitignore-independent search for digit-bounded `TOGO:M255` and
  `TOGO:M21`, both normalized owner filenames, both CultureMech IDs, and the
  merge fingerprint across `data`, `src`, `scripts`, `docs`, `.claude`, and
  `justfile` found the two normalized owners, the generated merge, a
  TOGO:M2425 source-duplicate link to M21, and generated indexes.

## Evidence

The TOGO M255 payload lists 1 L distilled water, 20 g NaCl, 15 g agar, and 37 g
Brain heart infusion broth (BD-Difco). The TOGO M21 payload lists the same 1 L
water, 15 g agar, and 37 g Bacto BHI row, but it has no 20 g NaCl supplement.

The inspected source payloads support two related but distinct formulas, not a
single duplicate recipe. They also list `Distilled water` as 1 L, not 1 g/L.

## Completeness

- Consequential gap: the 20 g NaCl supplement is the defining distinction
  between M255 and M21, but the generated merge collapses both.
- Consequential gap: both normalized owners carry `Distilled water` as
  `1 G_PER_L`.
- Consequential gap: both normalized owners replace the source's opaque
  37 g Bacto BHI row with inferred full-strength constituents and a
  MicrobeNotes URL that is not the JCM source.
- Empty target-organism and growth-evidence slots are acceptable for
  source-only JCM/TOGO formulations.
- A target-specific `find` under `reports/yaml_record_review` found no prior
  `brain_heart_infusion_agar_with_2_nacl` report, so this report did not
  overwrite an earlier review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | Plain BHI Agar TOGO:M21 is merged into the BHI Agar With 2% NaCl TOGO:M255 record. This makes a no-extra-salt formula a synonym of a formula with 20 g/L extra NaCl. | TOGO M255 contains a 20 g NaCl row; TOGO M21 does not. | Merge ownership across `data/normalized_yaml/bacterial/TOGO_M255_Brain_Heart_Infusion_Agar_With_2_NaCl.yaml` and `data/normalized_yaml/bacterial/TOGO_M21_Brain_Heart_Infusion_Agar.yaml` |
| Major | Distilled water is encoded as `1 G_PER_L` in both normalized owners. | TOGO M255 and M21 both list `Distilled water` with `volume: 1` and `unit: L`. | `data/normalized_yaml/bacterial/TOGO_M255_Brain_Heart_Infusion_Agar_With_2_NaCl.yaml`; `data/normalized_yaml/bacterial/TOGO_M21_Brain_Heart_Infusion_Agar.yaml` |
| Major | Both JCM/TOGO owners expand an opaque `Brain heart infusion broth (BD-Difco)` premix into inferred commercial constituents. The source supports a 37 g premix row, not direct calf-brain, beef-heart, proteose-peptone, dextrose, sodium-chloride, and disodium-phosphate rows. | TOGO M255 and M21 both list one 37 g Bacto BHI row. | The two normalized TOGO owners; likely also the TOGO/BHI premix expansion importer |
| Minor | The generated merge is stale before the September 2026 source-duplicate link between TOGO:M21 and TOGO:M2425. | `TOGO_M21_Brain_Heart_Infusion_Agar.yaml` now records `TOGO_M2425_Brain_Heart_Infusion_Agar.yaml` as a `SOURCE_DUPLICATE` child, but the generated merge predates that curation event. | Regenerate derived merges after correcting the normalized inputs |

## Recommended Edits

1. Repair the merge inputs or fingerprinting so TOGO:M255 and TOGO:M21 do not
   collapse into one generated record.
2. Restore M255 and M21 to their TOGO-supported opaque 37 g Bacto BHI row plus
   1 L distilled water and 15 g agar.
3. Preserve the 20 g NaCl supplement only on M255.
4. Change distilled-water units from `G_PER_L` to a liter-scale volume in both
   normalized owners.
5. Regenerate merged records after the authoritative normalized records or the
   importer that populates them are corrected.

## Follow-up Checks

- Rerun `just validate` on the corrected M255 and M21 normalized owners.
- Regenerate merges and confirm M255 and M21 land in distinct generated
  records with distinct fingerprints.
- Rerun `just verify-merges` and `just audit-merge-freshness`.
- Rerun focused LinkML, strict, reference, and term validation on the
  regenerated M255 and M21 records.

## Additional Notes

- The first search for `TOGO:M21` was intentionally corrected with a
  digit-bounded gitignore-independent search because a bare `TOGO:M21` pattern
  also matches unrelated source IDs such as `TOGO:M2103`.
- Optional empty growth-evidence and preparation slots were not treated as
  defects.
