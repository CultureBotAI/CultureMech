# YAML Record Review: Brain Heart Infusion + 2% NaCl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_2_nacl.yaml
- Started UTC: 2026-09-21T23:30:21Z
- Finished UTC: 2026-09-21T23:31:47Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008546 |
| Label | Brain Heart Infusion + 2% NaCl |
| Primary source | TOGO:M1965, wrapping NBRC_M1243 |
| Generated status | Generated merge of four normalized TOGO records |
| Merge fingerprint | 7f2ed13ceaece22351080426ee85921d70b89280ca13054fd513287793e20035 |

The reviewed file is a derived merge record. The four maintained sources named
in `merged_from` are:

| Maintained source | Source accession | TOGO formulation |
|---|---|---|
| `data/normalized_yaml/bacterial/brain_heart_infusion_2_nacl.yaml` | TOGO:M1965 / NBRC_M1243 | 1 L distilled water, 20 g NaCl, 15 g agar if needed, 37 g Bacto Brain Heart Infusion |
| `data/normalized_yaml/bacterial/1_10_brain_heart_infusion_medium_bhi.yaml` | TOGO:M2070 / NBRC_M1377 | 1 L distilled water, 15 g agar if needed, 3.7 g Bacto Brain Heart Infusion |
| `data/normalized_yaml/bacterial/1_5_brain_heart_infusion.yaml` | TOGO:M1897 / NBRC_M1154 | 1 L distilled water, 15 g agar if needed, 7.4 g Bacto Brain Heart Infusion |
| `data/normalized_yaml/bacterial/brain_heart_infusion.yaml` | TOGO:M1473 / NBRC_M253 | 1 L distilled water, 15 g agar if needed, 37 g Bacto Brain Heart Infusion |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_2_nacl.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_2_nacl.yaml --out /private/tmp/brain_heart_infusion_2_nacl.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_2_nacl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_2_nacl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- The generated top-level identity points to TOGO:M1965, Brain Heart Infusion +
  2% NaCl, originally NBRC_M1243.
- The `synonyms` and `merged_from` blocks make TOGO:M2070, TOGO:M1897, and
  TOGO:M1473 look equivalent to the M1965 2% NaCl recipe, but their inspected
  TOGO API payloads give different Bacto Brain Heart Infusion masses and only
  M1965 contains the 20 g NaCl supplement.
- A gitignore-independent search for the target IDs, source accessions,
  slugs, and merge fingerprint across `data`, `src`, `scripts`, `docs`,
  `.claude`, and `justfile` found the four direct TOGO owners and also found
  `data/normalized_yaml/bacterial/NBRC_1245.yaml`, which separately represents
  NBRC Medium 1243 with `id: CultureMech:007466`.
- The generated merge inherits a Bacto Brain Heart Infusion premix expansion,
  but the TOGO source rows identify only `Bacto Brain Heart Infusion (Difco)`
  with gram amounts. They do not identify calf-brain, beef-heart, proteose
  peptone, dextrose, sodium chloride, or disodium phosphate rows directly.

## Evidence

The TOGO API confirms four different source recipes:

| TOGO ID | Source title | Bacto BHI | Added NaCl | Agar |
|---|---:|---:|---:|---:|
| M1965 | Brain Heart Infusion + 2% NaCl | 37 g/L | 20 g/L | 15 g/L if needed |
| M2070 | 1/10 Brain Heart Infusion medium (BHI) | 3.7 g/L | 0 | 15 g/L if needed |
| M1897 | 1/5 Brain Heart Infusion | 7.4 g/L | 0 | 15 g/L if needed |
| M1473 | Brain Heart Infusion | 37 g/L | 0 | 15 g/L if needed |

The cited MicrobeNotes page is not the TOGO/NBRC source and is not a BD/Difco
product specification. It lists a generic BHI Agar ingredient table with HM
infusion powder and BHI powder plus proteose peptone, dextrose, sodium
chloride, disodium phosphate, and agar; it does not support the record's
replacement of TOGO's opaque Bacto BHI row with `Calf brains` and `Beef heart`
VARIABLE rows, nor does it support using the same full-strength expansion for
the 1/10 and 1/5 BHI recipes.

## Completeness

- Consequential gap: the actual TOGO component `Bacto Brain Heart Infusion
  (Difco)` is absent from all four maintained TOGO owners.
- Consequential gap: the source-specific 3.7 g/L and 7.4 g/L Bacto BHI
  dilutions are absent from the 1/10 and 1/5 owners.
- Consequential gap: `data/normalized_yaml/bacterial/NBRC_1245.yaml` and the
  TOGO:M1965 owner both represent NBRC Medium 1243 under different
  CultureMech IDs.
- Empty target-organism and growth-evidence slots are acceptable here; the
  inspected TOGO payloads have no growth rows.
- A target-specific `find` under `reports/yaml_record_review` found no prior
  `brain_heart_infusion_2_nacl` report, so this report did not overwrite an
  earlier review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | Four non-equivalent TOGO/NBRC recipes are merged into one generated record. The generated M1965 record lists M2070 1/10 BHI, M1897 1/5 BHI, and M1473 full-strength BHI as synonyms even though their source formulations differ. | The TOGO payloads list Bacto BHI at 37 g/L plus 20 g/L added NaCl for M1965, 3.7 g/L for M2070, 7.4 g/L for M1897, and 37 g/L with no added NaCl for M1473. | Merge ownership across `data/normalized_yaml/bacterial/brain_heart_infusion_2_nacl.yaml`, `data/normalized_yaml/bacterial/1_10_brain_heart_infusion_medium_bhi.yaml`, `data/normalized_yaml/bacterial/1_5_brain_heart_infusion.yaml`, and `data/normalized_yaml/bacterial/brain_heart_infusion.yaml` |
| Major | All four TOGO owners expand an opaque `Bacto Brain Heart Infusion (Difco)` premix into the same unscaled full-strength inferred constituents. This erases the 1/10 and 1/5 dilutions and gives the source rows ingredient identities that TOGO does not assert. | TOGO supplies one Bacto BHI row per recipe. The 1/10 and 1/5 records still contain `Proteose peptone 10.0 G_PER_L`, `Dextrose 2.0 G_PER_L`, `Sodium chloride 5.0 G_PER_L`, and `Disodium phosphate 2.5 G_PER_L`, the same as the full-strength owners. | The four `data/normalized_yaml/bacterial/*brain_heart_infusion*.yaml` owners listed in the target table; likely also the TOGO/BHI premix expansion importer |
| Major | Distilled water is encoded as `1 G_PER_L` in every merged TOGO owner. | All four TOGO payloads list `Distilled water` with `volume: 1` and `unit: L`, not 1 g/L. | The four normalized TOGO owners listed in the target table |
| Major | NBRC Medium 1243 is represented twice in the normalized corpus, once as TOGO:M1965 and once as `nbrc.medium:1243` in `NBRC_1245.yaml`, with different IDs and merge destinations. | M1965 wraps `original_media_id: NBRC_M1243`; `NBRC_1245.yaml` has `media_term.id: nbrc.medium:1243` and `id: CultureMech:007466`. | `data/normalized_yaml/bacterial/brain_heart_infusion_2_nacl.yaml` and `data/normalized_yaml/bacterial/NBRC_1245.yaml` |
| Minor | `Agar (if needed)` is ungrounded in the M1965/M2070/M1897/M1473 owners and the generated record. | The source TOGO row has GMO_001007 with label `Agar`, but the normalized rows have no CHEBI term or MIM CHEBI link. | The four normalized TOGO owners listed in the target table |

## Recommended Edits

1. Repair the merge inputs or fingerprinting so M1965, M2070, M1897, and M1473
   do not collapse into one generated record.
2. Restore the four normalized TOGO owners to the TOGO-supported opaque Bacto
   Brain Heart Infusion masses: 37 g/L for M1965, 3.7 g/L for M2070, 7.4 g/L
   for M1897, and 37 g/L for M1473.
3. Preserve the 20 g/L external NaCl supplement only on the M1965 / NBRC_M1243
   record.
4. Reconcile `data/normalized_yaml/bacterial/NBRC_1245.yaml` with the TOGO:M1965
   owner so NBRC Medium 1243 has one canonical maintained representation or an
   explicit cross-source relationship.
5. Change the distilled-water units from `G_PER_L` to a liter-scale volume in
   each TOGO owner.
6. Ground `Agar (if needed)` to `CHEBI:2509` / agar and refresh the
   MediaIngredientMech CHEBI link.

## Follow-up Checks

- Rerun `just validate` on each corrected normalized owner.
- Regenerate merges, then confirm M1965, M2070, M1897, and M1473 land in
  separate generated records with separate fingerprints.
- Rerun `just verify-merges` and `just audit-merge-freshness`.
- Rerun focused LinkML, strict, reference, and term validation on the generated
  M1965, M2070, M1897, and M1473 records after regeneration.
- Repeat an exact gitignore-independent search for `NBRC_M1243`,
  `nbrc.medium:1243`, and `TOGO:M1965` to prove the NBRC Medium 1243 duplicate
  has been reconciled.

## Additional Notes

- The target-specific duplicate search used `rg --no-ignore --hidden`, so
  ignored files under the searched project paths were included.
- Optional empty growth-evidence and preparation slots were not treated as
  defects.
