# YAML Record Review: azotobacter_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml
- Started UTC: 2026-09-21T17:06:53Z
- Finished UTC: 2026-09-21T17:11:06Z
- Verdict: needs curation

## Target

| Field | Observed |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:005190 |
| name | azotobacter_medium |
| original_name | AZOTOBACTER MEDIUM |
| category | bacterial |
| media_term | KOMODO Medium 3, komodo.medium:3 |
| generated status | Generated merge artifact in data/merge_yaml/merged |
| maintained owners | data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml; data/normalized_yaml/bacterial/azotobacter_medium.yaml; data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml |

The target is the generated merge for `KOMODO_3_AZOTOBACTER_MEDIUM`,
`azotobacter_medium`, and `medium_3_modified_for_dsm_44106`, with merge fingerprint
`3762de72a3f7a77aa967501b92a3f50bf8ca9049914cfd321152490da41b62e3`.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml` completed with no errors. |
| Strict validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml --out /private/tmp/AZOTOBACTER_MEDIUM.strict.tsv --workers 1 --quiet` completed with no errors. |
| Reference validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 checks. |
| Term validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` completed with no errors, aside from a non-fatal `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused embedded `MediaRecipe.curation_history` validator for one merge record. |
| Direct `just` validators | Not checked: the project-level `uv` environment currently fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13, with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project LinkML validator workaround above exercised the target schema, strict, reference, and term checks. |

## Identity and Grounding

- The base record identity is supported. DSMZ Medium 3 is `AZOTOBACTER MEDIUM`,
  reports pH 7.3, and the KOMODO Medium 3 page points to DSMZ Medium 3 with the same
  medium name and pH value.
- KOMODO `3_44106` is a separate live KOMODO entry named `MEDIUM 3 MODIFIED FOR
  DSM 44106`; its detail page also points to DSMZ Medium 3, exposes the same chemical
  set, and has `PH Info: null`.
- The `medium_3_modified_for_dsm_44106` child is related, but its exact
  `SOURCE_DUPLICATE` status remains incompletely supported: the only inspected live
  detail page names it as modified for a strain and does not describe what the
  modification is.
- The generated target's `medium_type: DEFINED` and `composition_type: DEFINED` are
  consistent with the inspected DSMZ formulation.

## Evidence

Supported by inspected source text:

- DSMZ Medium 3 lists Glucose 5.00 g, Mannitol 5.00 g,
  CaCl2 x 2 H2O 0.10 g, MgSO4 x 7 H2O 0.10 g,
  Na2MoO4 x 2 H2O 5.00 mg, K2HPO4 0.90 g, KH2PO4 0.10 g,
  FeSO4 x 7 H2O 0.01 g, CaCO3 5.00 g, Agar 15.00 g,
  Distilled water 950.00 ml, and a pH adjustment to 7.3.
- DSMZ Medium 3 instructs that glucose and mannitol are sterilized separately in
  50 ml H2O and added after autoclaving; it also describes CaCO3 as a buffer that
  settles before agar plates set and later forms clearing zones below acid-producing
  colonies.
- The generated target correctly converts the DSMZ molybdate row to
  `0.005 G_PER_L`, and the direct ingredient identities agree with DSMZ Medium 3.
- KOMODO pages for base Medium 3 and modified Medium 3_44106 both expose the same
  metabolite set with an H2O row and per-liter gram amounts scaled over the 950 ml
  DSMZ base.

Unsupported or stale in the generated target:

- The target has no `Distilled water` row even though DSMZ Medium 3 lists 950.00 ml
  and KOMODO exposes H2O as a metabolite.
- The target has no `preparation_steps` even though the DSMZ normalized source owner
  preserves the pH adjustment, glucose/mannitol separate sterilization, post-autoclave
  addition, and CaCO3 handling notes.
- `medium_3_modified_for_dsm_44106` is merged as a `SOURCE_DUPLICATE` even though the
  live KOMODO source names it as a modified strain-specific medium and does not expose
  any explicit modification text in the inspected detail page.

## Completeness

- Source provenance is sufficient to recover base DSMZ Medium 3 and KOMODO MediaInfo
  pages for IDs `3` and `3_44106`.
- Empty organism and growth-metric slots are acceptable for this source recipe. DSMZ
  Medium 3 and the inspected KOMODO pages establish formulations, not a growth claim
  for a named strain.
- The generated record's standalone `references` slot is empty; source pointers live
  in `media_term`, `notes`, and source-owner relationships.
- Exact gitignore-independent search covered `reports/yaml_record_review` for an
  existing `AZOTOBACTER_MEDIUM.md` report and found no prior report for this exact
  generated record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The 950 ml water base is missing. | DSMZ Medium 3 lists 950.00 ml Distilled water, and both inspected KOMODO detail pages expose H2O. The generated target and all three normalized owners omit a water ingredient row. | `data/normalized_yaml/bacterial/azotobacter_medium.yaml`, the two KOMODO-derived normalized owners, or the DSMZ-to-KOMODO composition enrichment path. |
| Major | The generated merge drops source-supported preparation details. | The DSMZ owner has pH and separate glucose/mannitol sterilization steps from the DSMZ PDF. The generated target has no `preparation_steps`, and `RecipeMerger` merges only ingredients, categories, synonyms, and merge provenance from noncanonical duplicates. | `src/culturemech/merge/merger.py`, then regenerate `data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml`. |
| Major | The modified-for-DSM-44106 child is flattened into the base Azotobacter medium without enough source support for exact duplication. | KOMODO `3_44106` is named `MEDIUM 3 MODIFIED FOR DSM 44106` and has `PH Info: null`; the normalized child inherits DSMZ pH 7.3 and the exact base DSMZ ingredient amounts, then the merge layer labels it `SOURCE_DUPLICATE`. The inspected KOMODO pages show the same chemical set but not the missing modification semantics. | `data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml` and the KOMODO DSMZ-modified import/enrichment path. |

No blocker or minor findings found.

## Recommended Edits

1. Add the missing DSMZ water row to `data/normalized_yaml/bacterial/azotobacter_medium.yaml`
   as `950.0 ML_PER_L` or an equivalent supported volume representation.
2. Add or intentionally map the KOMODO H2O rows for
   `data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml` and
   `data/normalized_yaml/bacterial/medium_3_modified_for_dsm_44106.yaml`.
3. Teach `RecipeMerger` to preserve unique source-supported `preparation_steps` when an
   ingredient-fingerprint merge selects a canonical recipe that lacks them.
4. Revisit `medium_3_modified_for_dsm_44106` against a source that explains the
   DSM 44106 modification; either encode the missing strain-specific difference or
   record a data-quality flag that KOMODO exposes it as a modified medium whose
   modification could not be recovered from the live detail page.
5. Regenerate `data/merge_yaml/merged/AZOTOBACTER_MEDIUM.yaml` from corrected
   normalized and merge inputs.

## Follow-up Checks

- `just validate-strict data/normalized_yaml/bacterial/azotobacter_medium.yaml` after
  adding the missing distilled-water volume.
- `just validate-terms data/normalized_yaml/bacterial/azotobacter_medium.yaml` after
  grounding the water row to CHEBI:15377.
- A focused `RecipeMerger` unit test showing that a KOMODO/DSMZ source-duplicate merge
  keeps preparation steps present only on the DSMZ owner.
- A targeted manual recheck of KOMODO `3_44106` or an alternate KOMODO export that can
  recover any hidden DSM 44106 modification.
- `just verify-merges` after regenerating the merge layer.

## Additional Notes

- The live KOMODO MediaInfo pages report gram amounts per liter and divide the DSMZ
  listed grams by 0.95, so their 5.26 g glucose/mannitol and 15.79 g agar values are
  a normalized KOMODO representation of DSMZ's 950 ml basal recipe rather than
  independent source amounts to copy over the DSMZ PDF rows.
- `linkml-reference-validator` performed zero checks because this generated record has
  no `references` block.
