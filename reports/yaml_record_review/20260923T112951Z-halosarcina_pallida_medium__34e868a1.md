# YAML Record Review: HALOSARCINA PALLIDA MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/halosarcina_pallida_medium__34e868a1.yaml`
- Started UTC: 2026-09-23T11:28:50Z
- Finished UTC: 2026-09-23T11:29:51Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:002991` |
| Name | `halosarcina_pallida_medium` |
| Original name | `HALOSARCINA PALLIDA MEDIUM` |
| Category | `archaea` |
| Physical state | `LIQUID` |
| pH | `6.5` |
| Generated from | `data/normalized_yaml/archaea/halosarcina_pallida_medium.yaml` and `data/normalized_yaml/archaea/halobacteria_hmd_medium.yaml` |
| Source accession | `mediadive.medium:J645` |
| Parent source accession | `mediadive.medium:J878` |
| Source URL | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=645` |
| Merge fingerprint | `34e868a11550f0e6f5ac4052cdff2902421903a6b8d3d5da39a48e21066faf9e` |

I reviewed the generated merged record, both normalized owners named in
`merged_from`, the live JCM 645 and JCM 878 pages, and the MediaDive `J645`
REST payload.

I searched `data/normalized_yaml/archaea` and `data/merge_yaml/merged` YAML
files with `rg --no-ignore --hidden` for `mediadive.medium:J645`,
`JCM Medium J645`, `jcm_grmd?GRMD=645`, `GRMD=645`,
`HALOSARCINA PALLIDA MEDIUM`, `halosarcina_pallida_medium`, and
`halobacteria_hmd_medium`. Ignored files were included. The search found the
curated direct JCM 645 branch, the JCM 878 Halobacteria HMD parent, Togo liquid
and solid branches for both media, and their generated outputs.

I also used `find data/normalized_yaml -name halobacteria_hmd_medium.yaml`,
which includes ignored files by default. It found only
`data/normalized_yaml/archaea/halobacteria_hmd_medium.yaml`, so the
`data/normalized_yaml/bacterial/halobacteria_hmd_medium.yaml` path embedded in
`parent_media.path` is stale.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halosarcina_pallida_medium__34e868a1.yaml` reported `No issues found`. |
| Strict schema | Passed: `python scripts/validate_strict.py data/merge_yaml/merged/halosarcina_pallida_medium__34e868a1.yaml --out /private/tmp/halosarcina_pallida_medium_34e868a1.strict.tsv --workers 1 --quiet` scanned one file and reported `total ERROR rows: 0`. |
| References | Passed with no checked references: `linkml-reference-validator validate data data/merge_yaml/merged/halosarcina_pallida_medium__34e868a1.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported `Total checks: 0`. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/halosarcina_pallida_medium__34e868a1.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 with no diagnostics. |
| Embedded history | Not checked: `just validate-history` validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries. |

The `just` validator entrypoints were not used because this checkout attempts
to resolve a Python 3.13 environment with `llvmlite==0.46.0`; the focused
validators above were run offline with Python 3.11 against the local uv cache.

## Identity and Grounding

The primary identity is JCM 645 `HALOSARCINA PALLIDA MEDIUM`, but the generated
record was merged with JCM 878 `HALOBACTERIA HMD MEDIUM`. Those are explicitly
modeled as a `CONCENTRATION_VARIANT` parent/child pair in the normalized files,
not as duplicate formulations.

The merge imported parent-only values into the child. JCM 645 has 0.5 g NH4Cl,
5 g `Casamino acids (BD-Difco)`, and anhydrous K2SO4. JCM 878 has 0.1 g NH4Cl,
0.5 g `Casamino acids (BD-Difco)`, and `K2SO4 x 7 H2O`; those parent values
are what the generated Halosarcina record now shows.

## Evidence

The JCM 645 and MediaDive `J645` sources agree that Halosarcina pallida medium
contains these child-specific rows:

| Ingredient | JCM 645 amount | Generated amount |
|---|---:|---:|
| `K2SO4` | 5 g | 5 g/L as `K2SO4 x 7 H2O` |
| `NH4Cl` | 0.5 g | 0.1 g/L |
| `Casamino acids (BD-Difco)` | 5 g | 0.5 g/L |

The generated `variant_modifications` text correctly says the child raises
NH4Cl from 0.1 to 0.5 g/L, raises casamino acids from 0.5 to 5 g/L, and changes
pH from 7.1 to 6.5. The generated ingredients contradict that text because the
merge used the parent concentrations.

JCM 645 also instructs the recipe to add components to distilled water and bring
the volume to 1.0 L. The curated normalized child and generated merge both keep
that instruction as text but have no structured water ingredient.

## Completeness

The source gives a 20 g/L agar solid option. The reviewed record is the liquid
base and keeps that agar option only as free-text preparation; this is
acceptable if the existing variant metadata stays liquid-base scoped and the
solid branch is not asserted as an unconditional ingredient.

No target organisms, growth evidence, incubation temperature, atmosphere, or
stock-solution references are present in the direct JCM 645 payload. The
corresponding empty optional fields are not defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `merge_recipes.py` merged a concentration-variant parent into its child and changed child ingredient values. | The generated Halosarcina record lists both `halobacteria_hmd_medium` and `halosarcina_pallida_medium` in `merged_from`; JCM 645 child values for NH4Cl, casamino acids, and K2SO4 were overwritten by JCM 878 parent values. | merge grouping/rules plus the normalized `parent_media`/`variant_children` metadata |
| Major | `parent_media.path` points to a non-existent category path. | A gitignore-independent `find` found `data/normalized_yaml/archaea/halobacteria_hmd_medium.yaml`; the record points to `data/normalized_yaml/bacterial/halobacteria_hmd_medium.yaml`. | `data/normalized_yaml/archaea/halosarcina_pallida_medium.yaml` |
| Major | The 1 L final-volume water component is missing. | JCM 645 says to bring the medium to 1.0 L with distilled water, but the generated record has no water row. | `data/normalized_yaml/archaea/halosarcina_pallida_medium.yaml` or the MediaDive importer |
| Minor | The `Casamino acids` row loses its `BD-Difco` qualifier. | JCM 645 and MediaDive `J645` both qualify casamino acids as `BD-Difco`; the generated row is unqualified. | `data/normalized_yaml/archaea/halosarcina_pallida_medium.yaml` or the MediaDive ingredient importer |

## Recommended Edits

1. Adjust merge logic so `CONCENTRATION_VARIANT` parent/child records do not
   merge into one canonical recipe when their explicit variant axes change
   ingredient amounts or pH.
2. Regenerate the Halosarcina child with JCM 645 values: 0.5 g/L NH4Cl, 5 g/L
   `Casamino acids (BD-Difco)`, and source-form `K2SO4`.
3. Fix `parent_media.path` in
   `data/normalized_yaml/archaea/halosarcina_pallida_medium.yaml` to point at
   `data/normalized_yaml/archaea/halobacteria_hmd_medium.yaml`.
4. Add structured 1 L distilled-water final volume to the direct child.
5. Preserve the `BD-Difco` qualifier on casamino acids.
6. Regenerate merged recipes after the normalized owner and merge rule are
   corrected; do not patch
   `data/merge_yaml/merged/halosarcina_pallida_medium__34e868a1.yaml`
   directly.

## Follow-up Checks

1. Run `just validate data/normalized_yaml/archaea/halosarcina_pallida_medium.yaml`
   after the child metadata is corrected.
2. Run `just verify-merges` and confirm the regenerated output keeps JCM 645
   and JCM 878 in separate fingerprints.
3. Run `just validate-media-variant-links` to ensure the corrected
   parent/child paths resolve.
4. Manually compare regenerated Halosarcina and Halobacteria HMD records
   against JCM 645 and JCM 878 to confirm only shared values are shared.

## Additional Notes

The Togo `M659` and `M660` records are separate mechanical imports from JCM
645 and should remain outside this direct curated JCM 645/Halobacteria HMD
variant merge.
