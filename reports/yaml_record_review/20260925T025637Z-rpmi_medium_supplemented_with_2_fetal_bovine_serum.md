# YAML Record Review: rpmi_medium_supplemented_with_2_fetal_bovine_serum

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/rpmi_medium_supplemented_with_2_fetal_bovine_serum.yaml
- Started UTC: 2026-09-25T02:54:50Z
- Finished UTC: 2026-09-25T02:56:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Generated file | `data/merge_yaml/merged/rpmi_medium_supplemented_with_2_fetal_bovine_serum.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009482` |
| Name | `rpmi_medium_supplemented_with_2_fetal_bovine_serum` |
| Original name | `RPMI medium (supplemented with 2% fetal bovine serum)` |
| Category | `bacterial` |
| Media term | `TOGO Medium M2958` / `TOGO:M2958` |
| Immediate maintained input | `data/normalized_yaml/bacterial/rpmi_medium_supplemented_with_2_fetal_bovine_serum.yaml` |
| Merge fingerprint | `188494b646a8fef9472f90257540e2318fde17cfab6f8d43cdc03c7acdcac0e2` |
| Merged from | `rpmi_medium_supplemented_with_2_fetal_bovine_serum` |

The generated file is the single-source merge of TOGO M2958.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/rpmi_medium_supplemented_with_2_fetal_bovine_serum.yaml` exited 0 and reported `No issues found`. |
| Strict schema | Passed: `scripts/validate_strict.py data/merge_yaml/merged/rpmi_medium_supplemented_with_2_fetal_bovine_serum.yaml --out /private/tmp/rpmi_medium_supplemented_with_2_fetal_bovine_serum.strict.tsv --workers 1 --quiet` scanned 1 file and reported 0 error rows. |
| Reference validation | Passed: `linkml-reference-validator validate data data/merge_yaml/merged/rpmi_medium_supplemented_with_2_fetal_bovine_serum.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` validated 1 file and reported 0 checks. |
| Term validation | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/rpmi_medium_supplemented_with_2_fetal_bovine_serum.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after the known `eutils/pkg_resources` warning. |
| Embedded curation history | Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks embedded in merged YAML. |

## Identity and Grounding

- TOGO M2958 supports the record label `RPMI medium (supplemented with 2% fetal bovine serum)`.
- The source ingredients are the two TOGO components: `fetal bovine serum` at `2 %` and `RPMI medium (Invitrogen, Carlsbad, CA)` at `1 L`.
- The TOGO comment says *Coxiella burnetii* was propagated in African green monkey kidney Vero fibroblasts grown in this RPMI/FBS medium or in embryonated hen's eggs. It does not say the RPMI/FBS recipe is a standalone bacterial culture medium.
- An exact ignored-file search for `CultureMech:009482`, `TOGO:M2958`, `M2958`, `rpmi_medium_supplemented_with_2_fetal_bovine_serum`, and `RPMI medium` found this generated merge, its maintained normalized input, the TOGO source index, and related archive/report rows; ignored files were included.

## Evidence

### Supported

- The current maintained input correctly reflects TOGO M2958's literal component graph: 2% fetal bovine serum and 1 L RPMI medium from Invitrogen.
- Leaving `RPMI medium (Invitrogen, Carlsbad, CA)` unmapped to CHEBI is appropriate; the TOGO record itself maps it to a GMO product concept, not an exact ChEBI chemical identity.

### Unsupported Or Over-scoped

- The generated file is stale and has wrong units. It still publishes `fetal bovine serum` as `2 PERCENT_W_V` and the RPMI base as `1 G_PER_L`, but the maintained source was repaired to `2 PERCENT_V_V` and `1000 ML_PER_L`.
- `applications: Microbial cultivation` is over-scoped for the inspected source text. TOGO M2958 came from a Vero-fibroblast propagation paragraph for an intracellular bacterium, not from a protocol claiming this medium directly cultivates bacteria.
- `category: bacterial` is source-derived from the curated organism context, but the recipe itself is a mammalian host-cell medium. The category needs an explicit CultureMech decision rather than defaulting silently to bacterial media.

## Completeness

- The generated record lacks the structured `references` and `data_quality_flags` present in `data/normalized_yaml/bacterial/rpmi_medium_supplemented_with_2_fetal_bovine_serum.yaml` after the September 2026 repair.
- The record has no preparation steps. That absence is not a defect: TOGO M2958's component graph does not supply any preparation procedure.
- `target_organisms` and growth metrics are empty. They should stay empty unless a curator adds source-scoped evidence distinguishing Vero host-cell growth from *Coxiella burnetii* propagation in that host system.

## Findings

### Blocker

None found.

### Major

1. **The generated merge is stale relative to the maintained TOGO repair.** The maintained source has a 2026-09-07 `repair_togo_literal_products_score40.py` event that changed fetal bovine serum to `2 PERCENT_V_V`, RPMI medium to `1000 ML_PER_L`, and added a structured reference. The August generated merge still publishes pre-repair `PERCENT_W_V` and `1 G_PER_L` values.

2. **The source context is a host-cell propagation medium, not directly a bacterial medium formulation.** TOGO M2958 was extracted from a paragraph where Vero fibroblasts were grown in RPMI/FBS and used to propagate *C. burnetii*. Filing the record as ordinary `bacterial` / `Microbial cultivation` overstates what the inspected text supports.

### Minor

None found.

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/rpmi_medium_supplemented_with_2_fetal_bovine_serum.yaml` from `data/normalized_yaml/bacterial/rpmi_medium_supplemented_with_2_fetal_bovine_serum.yaml` so the September TOGO literal-product unit repair reaches the generated layer.

2. Review the category and application policy for mammalian host-cell media extracted from intracellular bacterial propagation contexts, and either move/reclassify this source record or add a concrete quality flag/discussion that prevents it from being read as a direct bacterial growth recipe.

3. Keep `RPMI medium (Invitrogen, Carlsbad, CA)` as an unresolved or product-level ingredient unless a curator can map it to an exact source-supported medium term; do not force a CHEBI chemical grounding.

## Follow-up Checks

- Run `just audit-merge-freshness` after regenerating merged YAML.
- Run focused open-schema, strict, reference, and term validation on the regenerated merge.
- Re-fetch TOGO M2958 and confirm the regenerated ingredient list keeps fetal bovine serum at 2% and RPMI medium at 1 L / 1000 ml without converting either to grams.
- Manually re-check the source comment before adding any target-organism or growth-metric evidence; Vero fibroblast culture and *C. burnetii* propagation should remain separately scoped.

## Additional Notes

- The initial TOGO fetch failed inside the sandbox with DNS resolution error `curl: (6) Could not resolve host: togomedium.org`; an approved `curl -L` retry outside the sandbox retrieved the M2958 API response.
- The source search used `rg --no-ignore --hidden`; ignored files were included.
- `data/merge_yaml/merged/rpmi_medium_supplemented_with_2_fetal_bovine_serum.yaml` is generated output. Future source edits belong in `data/normalized_yaml/bacterial/rpmi_medium_supplemented_with_2_fetal_bovine_serum.yaml` or the TOGO import/repair logic.
