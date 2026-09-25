# YAML Record Review: EG Medium With 10% NaCl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/eg_medium_with_10_nacl.yaml
- Started UTC: 2026-09-22T23:32:00Z
- Finished UTC: 2026-09-22T23:37:49Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/eg_medium_with_10_nacl.yaml`
- Class: `MediaRecipe`
- ID: `CultureMech:009099`
- Name: `eg_medium_with_10_nacl`
- Original label: `EG Medium With 10% NaCl`
- Category: `bacterial`
- Medium term: `TOGO:M252`
- Generated status: generated merge record with fingerprint `c6c67bff85775ad152575e068ac88e99bedbc195b91ae19890bd8325ee75530f`
- Maintained source record: `data/normalized_yaml/bacterial/TOGO_M252_EG_Medium_With_10_NaCl.yaml`
- Repaired sibling record: `data/normalized_yaml/bacterial/eg_medium_with_10_nacl.yaml`

The current merged record is stale relative to the normalized corpus. The TOGO normalized owner has an August 20, 2026 MIM grounding for L-cystine that is absent from the August 6, 2026 merge product, and `find data/normalized_yaml -name '*TOGO_M252*' -o -name 'eg_medium_with_10_nacl.yaml'` found a separate direct JCM/MediaDive record, `CultureMech:002618`, repaired from the same TOGO M252 source on August 25, 2026.

## Validation

Focused validation did not catch the stale identity or formulation problems.

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/eg_medium_with_10_nacl.yaml` | Passed; `No issues found`. |
| Strict schema wrapper | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/eg_medium_with_10_nacl.yaml --out /private/tmp/eg_medium_with_10_nacl.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/eg_medium_with_10_nacl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks, all validations passed. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/eg_medium_with_10_nacl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with exit code 0 and no diagnostics. |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The source identity is TOGO M252, which is a TOGO snapshot of JCM medium `JCM_M260` with source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=260`. The live JCM URL now returns a `Nothing found` page, but MediaDive still resolves `J260` as `EG MEDIUM WITH 10% NaCl` from JCM and preserves the formulation instruction: use EG medium, add 100 g/L final NaCl, and omit horse blood.

The generated record should therefore represent the JCM J260 variant of EG medium, not a standalone TOGO expansion. That identity is already curated in `data/normalized_yaml/bacterial/eg_medium_with_10_nacl.yaml` as `CultureMech:002618` with `media_term: mediadive.medium:J260`; the reviewed merge output instead exposes the older TOGO record `CultureMech:009099` and no merged representation of the repaired JCM record. An ignored-independent `find data/merge_yaml/merged -maxdepth 1 -name '*eg_medium_with_10_nacl*'` found only `data/merge_yaml/merged/eg_medium_with_10_nacl.yaml`.

Grounding on the reviewed record is also stale: its maintained TOGO source gained a CHEBI term for `L--Cystine` on August 20, 2026, but the generated file still lacks that term because it predates the grounding update.

## Evidence

The TOGO API payload for M252 expands the inherited EG ingredient rows and adds 100 g/L NaCl. It also carries both relevant preparation comments: the base EG Medium 14 instruction for dissolving L-cystine in 50 ml of 1 N HCl, bringing the volume to 950 ml, adjusting pH to 7.6--7.8, autoclaving, cooling, and adding horse blood; then the JCM 260 instruction to use EG medium with 100 g/L final NaCl and omit horse blood.

The reviewed record keeps the base EG grams, keeps 100 g/L NaCl, and correctly omits the horse-blood ingredient. It loses the JCM 260 relationship, however, and its ingredient table incorrectly promotes two preparation liquids to final mass-concentration ingredients:

- `HCl`, which appears in TOGO only as `50 ml` of `1 N` acid for dissolving L-cystine, is represented as `50 G_PER_L`.
- `Distilled water`, which appears in TOGO as `950 ml` used before the final 50 ml horse-blood addition in the inherited EG recipe, is represented as `950 G_PER_L`.

The generated record also has no `preparation_steps`, so it drops both TOGO/JCM comments and leaves no machine-readable instruction to dissolve L-cystine in HCl, adjust pH, autoclave, cool, add NaCl as a final 100 g/L supplement to EG, or omit horse blood.

## Completeness

Consequential gaps remain:

- The generated corpus has only the stale TOGO variant for `eg_medium_with_10_nacl`, not the August 25 repaired direct JCM/MediaDive variant.
- No preparation steps remain in the generated TOGO variant.
- No pH survives from the inherited EG Medium 14 procedure.
- The record carries no discussion flag explaining that the original JCM 260 URL currently returns `Nothing found` and that TOGO M252/MediaDive J260 are being used to recover the unavailable formulation.

The absence check for a generated direct JCM sibling used `find`, which includes ignored files. No generated file other than `data/merge_yaml/merged/eg_medium_with_10_nacl.yaml` was found.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| blocker | The generated corpus exposes the stale TOGO record rather than the repaired direct JCM `eg_medium_with_10_nacl` identity. | `data/normalized_yaml/bacterial/eg_medium_with_10_nacl.yaml` recovered JCM J260 from TOGO M252 on August 25, 2026, but `data/merge_yaml/merged/eg_medium_with_10_nacl.yaml` is an August 6 TOGO-only merge for `CultureMech:009099`. | merge generation from `data/normalized_yaml/bacterial/eg_medium_with_10_nacl.yaml` and `data/normalized_yaml/bacterial/TOGO_M252_EG_Medium_With_10_NaCl.yaml` |
| major | The record turns inherited EG preparation liquids into final ingredients with gram-per-liter units. | TOGO M252 lists 50 ml of 1 N HCl and 950 ml distilled water as setup for the inherited EG medium procedure; the reviewed record lists `HCl` at `50 G_PER_L` and `Distilled water` at `950 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M252_EG_Medium_With_10_NaCl.yaml` or the TOGO import/recovery transform |
| major | All preparation evidence was dropped. | TOGO M252 carries the inherited EG preparation comment plus the JCM 260 "100 g/L final NaCl, omit horse blood" comment; `data/merge_yaml/merged/eg_medium_with_10_nacl.yaml` has no `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M252_EG_Medium_With_10_NaCl.yaml` |
| minor | The merge output is stale relative to its own maintained TOGO source. | The normalized TOGO record added a CHEBI grounding for `L--Cystine` on August 20, 2026; the August 6 merge output lacks it. | generated merge artifacts |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` from current normalized YAML so the repaired direct `data/normalized_yaml/bacterial/eg_medium_with_10_nacl.yaml` record participates in merge output.
2. Deduplicate or reconcile `data/normalized_yaml/bacterial/TOGO_M252_EG_Medium_With_10_NaCl.yaml` with `data/normalized_yaml/bacterial/eg_medium_with_10_nacl.yaml`; they denote the same JCM 260 medium through TOGO M252/MediaDive J260 and should not continue to publish as separate CultureMech IDs without an explicit relationship.
3. Remove final `HCl` and `Distilled water` mass ingredients from the TOGO-owned record, or represent the 50 ml 1 N HCl and 950 ml water only as preparation/solution context.
4. Restore preparation steps that preserve both inspected TOGO comments: inherited EG preparation through autoclaving, followed by the JCM 260-specific 100 g/L final NaCl and horse-blood omission.
5. Add a quality note or discussion explaining that the live JCM 260 URL is unavailable and that TOGO M252/MediaDive J260 preserve the source formulation.

## Follow-up Checks

1. Rerun the merge process and confirm with `find data/merge_yaml/merged -maxdepth 1 -name '*eg_medium_with_10_nacl*'` that the generated output contains exactly the intended reconciled JCM 260 record.
2. Rerun LinkML schema, strict schema, reference, and term validation on the regenerated file.
3. Reopen the TOGO M252 API payload and MediaDive `J260` response and manually verify that the regenerated ingredients model EG Medium 14 plus 100 g/L final NaCl, with horse blood omitted and no `HCl` or 950 ml water final-mass artifacts.
4. Manually verify that the unavailable JCM URL is documented without treating the live `Nothing found` page as evidence that JCM 260 never existed.

## Additional Notes

- The source discrepancy was checked directly: TOGO M252 and MediaDive J260 still resolve, while the embedded JCM `GRMD=260` URL no longer returns the recipe.
- Exact local discovery used `find`, which includes gitignored files, and found both the TOGO normalized record and the later repaired direct JCM normalized record.
