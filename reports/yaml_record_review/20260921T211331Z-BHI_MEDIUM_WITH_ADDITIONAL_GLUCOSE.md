# YAML Record Review: bhi_medium_with_additional_glucose

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BHI_MEDIUM_WITH_ADDITIONAL_GLUCOSE.yaml
- Started UTC: 2026-09-21T21:12:02Z
- Finished UTC: 2026-09-21T21:13:31Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001316 |
| Name | bhi_medium_with_additional_glucose |
| Original name | BHI MEDIUM WITH ADDITIONAL GLUCOSE |
| Category | bacterial |
| Source identity | DSMZ Medium 215b, `mediadive.medium:215b` |
| Reviewed artifact | `data/merge_yaml/merged/BHI_MEDIUM_WITH_ADDITIONAL_GLUCOSE.yaml` |
| Primary maintained owner | `data/normalized_yaml/bacterial/bhi_medium_with_additional_glucose.yaml` |
| Generated state | Derived 33-source merge from `merged_from` entries including DSMZ 215, 215a, 215b, 215c, BHI broth, BHI agar, BHI with 5% NaCl, strain-specific 215/215b/215c variants, and TOGO/JCM/NBRC BHI records; `merge_fingerprint: c9f479eb46e904ba5f4f951ddac3fa23ee2c06f09ce437f640c578c867514d28` |

`data/culturemech_id_registry.tsv` maps `CultureMech:001316` to
`data/normalized_yaml/bacterial/bhi_medium_with_additional_glucose.yaml`.

The inspected MediaDive REST record for 215b and the inspected DSMZ Medium
215b PDF both define BHI Medium With Additional Glucose as 37 g/L Brain heart
infusion (Difco), 5 g/L glucose, and 1000 ml distilled water.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BHI_MEDIUM_WITH_ADDITIONAL_GLUCOSE.yaml` | Passed; no issues emitted |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BHI_MEDIUM_WITH_ADDITIONAL_GLUCOSE.yaml --out /private/tmp/BHI_MEDIUM_WITH_ADDITIONAL_GLUCOSE.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 ERROR rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BHI_MEDIUM_WITH_ADDITIONAL_GLUCOSE.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file, 0 reference checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BHI_MEDIUM_WITH_ADDITIONAL_GLUCOSE.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded-`MediaRecipe.curation_history` validator is documented for one merge record; `just validate-history` targets standalone records under `history/` |

The direct `just validate-*` wrappers were not rerun for this record because
this checkout currently fails before target-specific validation while building
`llvmlite==0.46.0` under Python 3.13. The no-project commands above exercise
the same narrow validators under Python 3.11 from a cache outside the project
environment.

## Identity and Grounding

- **The canonical ID resolves to DSMZ 215b.** `CultureMech:001316`,
  `mediadive.medium:215b`, and the record label all identify BHI MEDIUM WITH
  ADDITIONAL GLUCOSE.
- **The added 5 g/L glucose row is supported.** DSMZ and MediaDive list 5 g
  glucose in the one-liter 215b recipe.
- **Brain Heart Infusion is missing as an aggregate.** DSMZ and MediaDive list
  37 g/L Brain heart infusion, but the generated record expands that opaque
  aggregate into six BHI subcomponents from a secondary MicrobeNotes page.
- **The final-volume water row is missing.** DSMZ and MediaDive both list 1000
  ml distilled water; the generated medium has no Distilled water ingredient.
- **The generated synonym and `merged_from` set is over-broad and stale.** The
  current generated merge still links source-distinct BHI records, including
  BHI Medium 215a with erythromycin, BHI Medium 215c for strict anaerobes, BHI
  agar, BHI with 5% NaCl, and strain-specific derivatives, as duplicates of
  DSMZ 215b. The KOMODO 215c parent has already been repaired upstream into a
  source duplicate of DSMZ 215c and no longer belongs in this 215b merge.

## Evidence

| Claim | Review |
|---|---|
| DSMZ 215b / BHI MEDIUM WITH ADDITIONAL GLUCOSE | Supported by MediaDive REST and the DSMZ PDF. |
| 5 g/L glucose | Supported by MediaDive REST and the DSMZ PDF. |
| Six expanded BHI constituents | Unsupported by DSMZ 215b and by the MediaDive REST recipe. The source lists a 37 g/L Brain heart infusion aggregate. |
| Missing distilled water | Unsupported omission; the source recipe includes 1000 ml distilled water. |
| The 33 `merged_from` records are duplicates | Unsupported. Local parents named BHI MEDIUM, BHI MEDIUM (modified), BHI MEDIUM FOR STRICT ANAEROBES, BHI agar, BHI broth, and BRAIN HEART INFUSION WITH 5% NaCl carry distinct source IDs, source formulations, supplements, or physical states. |

## Completeness

- Empty pH and preparation-step slots are acceptable for the DSMZ 215b base
  recipe because the inspected DSMZ 215b PDF and MediaDive REST payload do not
  specify pH or preparation steps.
- Empty organism and growth slots are acceptable because the inspected DSMZ
  and MediaDive recipe records do not assert growth outcomes.
- The reviewed merge has only a free-text DSMZ PDF URL in `notes`; it has no
  structured `references` entries for the PDF or MediaDive REST URL.
- The Mediadive-derived source solution
  `data/normalized_yaml/bacterial/mediadive_471_Main_sol_215b.yaml` has the
  right three-row formula, but its imported Distilled water row is encoded as
  `1000 PERCENT_V_V` instead of 1000 ml.
- A gitignore-independent search with `rg --no-ignore --hidden` over `data`
  and `reports/yaml_record_review` for `CultureMech:001316`,
  `mediadive.medium:215b`, `bhi_medium_with_additional_glucose`, and the merge
  fingerprint found the expected normalized owner, generated merge, generated
  indexes, duplicate KOMODO 215b owner, the KOMODO DSM 41834 derivative, and
  import-tracking references. A `find` search over the ignored
  `reports/yaml_record_review` directory found no pre-existing
  `*-BHI_MEDIUM_WITH_ADDITIONAL_GLUCOSE.md` report before this one was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated medium replaces the source's 37 g/L Brain heart infusion aggregate with six unsupported BHI subcomponents. | The inspected DSMZ 215b PDF and MediaDive 215b REST payload list Brain heart infusion (Difco) as one 37 g/L ingredient. | `data/normalized_yaml/bacterial/bhi_medium_with_additional_glucose.yaml` |
| major | The source's 1000 ml distilled-water row is missing from the medium. | DSMZ 215b and MediaDive 215b both include Distilled water as the final row of the one-liter recipe. | `data/normalized_yaml/bacterial/bhi_medium_with_additional_glucose.yaml` |
| major | The generated merge conflates non-duplicate BHI records under DSMZ 215b. | The `merged_from` list names 33 parents spanning base BHI, erythromycin-modified 215a, glucose-supplemented 215b, strict-anaerobe 215c, BHI agar, high-NaCl BHI, and strain-specific variants; at least the current KOMODO 215c parent has been repaired into a distinct strict-anaerobe recipe. | Correct the BHI-family normalized records that still collapse to this fingerprint, then rerun `src/culturemech/merge/merge_recipes.py`; if corrected BHI records still collapse, refine `src/culturemech/merge/` to respect source identity, physical state, or curated variant relationships. |
| minor | Structured source references are absent. | The DSMZ PDF URL is present only in the free-text `notes`, and the MediaDive REST endpoint is not recorded. | `data/normalized_yaml/bacterial/bhi_medium_with_additional_glucose.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/bhi_medium_with_additional_glucose.yaml`,
   replace the Calf brains, Beef heart, Proteose peptone, Dextrose, Sodium
   chloride, and Disodium phosphate rows with one 37 g/L Brain heart infusion
   row grounded to `mediadive.compound:186`.
2. Add the source 1000 ml Distilled water row grounded to
   `mediadive.compound:4`; retain the supported 5 g/L Glucose row.
3. Apply the same DSMZ 215b formulation fix, with its own curation history, to
   `data/normalized_yaml/bacterial/KOMODO_215b_BHI_medium_WITH_ADDITIONAL_GLUCOSE.yaml`
   or model it as a source duplicate of the DSMZ 215b owner.
4. Remove source-distinct records from the generated DSMZ 215b merge by
   repairing the remaining BHI-family normalized owners and regenerating
   `data/merge_yaml/merged/`.
5. Add structured references for
   `https://mediadive.dsmz.de/rest/medium/215b` and
   `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215b.pdf`.

## Follow-up Checks

- Rerun schema, strict, term, and reference validation on the corrected
  normalized owner and on the regenerated merge.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Manually compare the regenerated DSMZ 215b merge against MediaDive
  `/rest/medium/215b` and confirm it has exactly Brain heart infusion at
  37 g/L, Glucose at 5 g/L, and 1000 ml Distilled water.
- Confirm that regenerated BHI 215a, 215b, 215c, BHI agar, BHI with 5% NaCl,
  and strain-specific BHI derivatives are represented as separate records or
  explicit variants instead of synonyms of DSMZ 215b.

## Additional Notes

None found.
