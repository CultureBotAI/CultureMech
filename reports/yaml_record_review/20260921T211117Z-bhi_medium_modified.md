# YAML Record Review: bhi_medium_modified

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bhi_medium_modified.yaml
- Started UTC: 2026-09-21T21:08:31Z
- Finished UTC: 2026-09-21T21:11:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001315 |
| Name | bhi_medium_modified |
| Original name | BHI MEDIUM (modified) |
| Category | bacterial |
| Source identity | DSMZ Medium 215a, `mediadive.medium:215a` |
| Reviewed artifact | `data/merge_yaml/merged/bhi_medium_modified.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/bhi_medium_modified.yaml` |
| Generated state | Derived single-source merge from `merged_from: [bhi_medium_modified]`, `merge_fingerprint: 7ed839815b2cc2a034a3f76cc1ff5266f8cd597780dd0378ed37f9ea7095929c` |

`data/culturemech_id_registry.tsv` maps `CultureMech:001315` to
`data/normalized_yaml/bacterial/bhi_medium_modified.yaml`.

The inspected MediaDive REST record for 215a and the inspected DSMZ Medium
215a PDF both define BHI Medium (modified) as 37 g/L Brain heart infusion, 10
mg/L erythromycin, and 1000 ml distilled water.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bhi_medium_modified.yaml` | Passed; no issues emitted |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bhi_medium_modified.yaml --out /private/tmp/bhi_medium_modified.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 ERROR rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bhi_medium_modified.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file, 0 reference checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bhi_medium_modified.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded-`MediaRecipe.curation_history` validator is documented for one merge record; `just validate-history` targets standalone records under `history/` |

The direct `just validate-*` wrappers were not rerun for this record because
this checkout currently fails before target-specific validation while building
`llvmlite==0.46.0` under Python 3.13. The no-project commands above exercise
the same narrow validators under Python 3.11 from a cache outside the project
environment.

## Identity and Grounding

- **Record identity is coherent.** `CultureMech:001315`, the record label, and
  `mediadive.medium:215a` all identify DSMZ Medium 215a, BHI MEDIUM
  (modified).
- **The erythromycin row is supported.** DSMZ lists 10 mg/L and MediaDive lists
  10 mg, `g_l: 0.01`, for the one-liter main solution.
- **Brain Heart Infusion is missing as an aggregate.** DSMZ and MediaDive list
  37 g/L Brain heart infusion, but the generated record expands that opaque
  aggregate into Calf brains, Beef heart, Proteose peptone, Dextrose, Sodium
  chloride, and Disodium phosphate rows from a secondary MicrobeNotes page.
- **The final-volume water row is missing.** DSMZ and MediaDive both list 1000
  ml distilled water; the generated medium has no Distilled water ingredient.

## Evidence

| Claim | Review |
|---|---|
| DSMZ 215a / BHI MEDIUM (modified) identity | Supported by MediaDive REST and the DSMZ PDF. |
| Erythromycin at 10 mg/L | Supported by MediaDive REST and the DSMZ PDF; the generated `0.01 G_PER_L` value is the same concentration. |
| Six expanded BHI constituents | Unsupported by DSMZ 215a and by the MediaDive REST recipe. The source lists a 37 g/L Brain heart infusion aggregate. |
| Missing distilled water | Unsupported omission; the source recipe includes 1000 ml distilled water. |

## Completeness

- Empty pH and preparation-step slots are acceptable because the inspected
  DSMZ 215a PDF and MediaDive REST payload do not specify pH or preparation
  steps for this medium.
- Empty organism and growth slots are acceptable because the inspected DSMZ
  and MediaDive recipe records do not assert growth outcomes.
- The reviewed merge has only a free-text DSMZ PDF URL in `notes`; it has no
  structured `references` entries for the PDF or MediaDive REST URL.
- The Mediadive-derived source solution
  `data/normalized_yaml/bacterial/mediadive_470_Main_sol_215a.yaml` has the
  right three-row formula, but its imported Distilled water row is encoded as
  `1000 PERCENT_V_V` instead of 1000 ml.
- A gitignore-independent search with `rg --no-ignore --hidden` over `data`
  and `reports/yaml_record_review` for `CultureMech:001315`,
  `mediadive.medium:215a`, `bhi_medium_modified`, and the merge fingerprint
  found the expected normalized owner, generated merge, generated indexes,
  duplicate KOMODO 215a owner, and import-tracking references. A `find` search
  over the ignored `reports/yaml_record_review` directory found no
  pre-existing `*-bhi_medium_modified.md` report before this one was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated medium replaces the source's 37 g/L Brain heart infusion aggregate with six unsupported BHI subcomponents. | The inspected DSMZ 215a PDF and MediaDive 215a REST payload list Brain heart infusion as one 37 g/L ingredient. | `data/normalized_yaml/bacterial/bhi_medium_modified.yaml` |
| major | The source's 1000 ml distilled-water row is missing from the medium. | DSMZ 215a and MediaDive 215a both include Distilled water as the final row of the one-liter recipe. | `data/normalized_yaml/bacterial/bhi_medium_modified.yaml` |
| minor | Structured source references are absent. | The DSMZ PDF URL is present only in the free-text `notes`, and the MediaDive REST endpoint is not recorded. | `data/normalized_yaml/bacterial/bhi_medium_modified.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/bhi_medium_modified.yaml`, replace the
   Calf brains, Beef heart, Proteose peptone, Dextrose, Sodium chloride, and
   Disodium phosphate rows with one 37 g/L Brain heart infusion row grounded
   to `mediadive.compound:186`.
2. Add the source 1000 ml Distilled water row grounded to
   `mediadive.compound:4`; retain the supported 0.01 g/L Erythromycin row.
3. Add structured references for
   `https://mediadive.dsmz.de/rest/medium/215a` and
   `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215a.pdf`.
4. Regenerate `data/merge_yaml/merged/bhi_medium_modified.yaml` and generated
   media pages from the corrected normalized owner.

## Follow-up Checks

- Rerun schema, strict, term, and reference validation on the corrected
  normalized owner and on the regenerated merge.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Manually compare the regenerated merge against DSMZ 215a and MediaDive
  `/rest/medium/215a` to confirm that it has exactly 37 g/L Brain heart
  infusion, 0.01 g/L Erythromycin, and 1000 ml Distilled water.

## Additional Notes

None found.
