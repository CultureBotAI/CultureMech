# YAML Record Review: Halosarcina Pallida Medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/halosarcina_pallida_medium__02a05db9.yaml`
- Started UTC: 2026-09-23T11:26:41Z
- Finished UTC: 2026-09-23T11:27:46Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:010063` |
| Name | `halosarcina_pallida_medium` |
| Original name | `Halosarcina Pallida Medium` |
| Category | `archaea` |
| Physical state | `SOLID_AGAR` |
| Generated from | `data/normalized_yaml/archaea/TOGO_M660_Halosarcina_Pallida_Medium.yaml` |
| Source accession | `TOGO:M660` |
| Original source accession | `JCM_M645-2` |
| Original source URL | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=645` |
| Merge fingerprint | `02a05db964e09c41d753d5e0eb49784ac2a0acd913bc9e466bb4c8374acf8658` |

I reviewed the generated merged record, its normalized Togo owner, the Togo
`M660` API payload, the live JCM 645 page, and the direct curated JCM 645
normalized sibling.

I searched `data/normalized_yaml` and `data/merge_yaml` YAML files with
`rg --no-ignore --hidden` for `halosarcina_pallida_medium`,
`HALOSARCINA PALLIDA MEDIUM`, `Halosarcina Pallida`, and `pallida`. Ignored
files were included. The search found the reviewed Togo `M660` solid branch,
the Togo `M659` liquid branch, the direct curated JCM 645 branch that is merged
with `halobacteria_hmd_medium`, and unrelated Isosphaera pallida records; only
`TOGO_M660_Halosarcina_Pallida_Medium.yaml` feeds this reviewed fingerprint.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halosarcina_pallida_medium__02a05db9.yaml` reported `No issues found`. |
| Strict schema | Passed: `python scripts/validate_strict.py data/merge_yaml/merged/halosarcina_pallida_medium__02a05db9.yaml --out /private/tmp/halosarcina_pallida_medium_02a05db9.strict.tsv --workers 1 --quiet` scanned one file and reported `total ERROR rows: 0`. |
| References | Passed with no checked references: `linkml-reference-validator validate data data/merge_yaml/merged/halosarcina_pallida_medium__02a05db9.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported `Total checks: 0`. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/halosarcina_pallida_medium__02a05db9.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries. |

The `just` validator entrypoints were not used because this checkout attempts
to resolve a Python 3.13 environment with `llvmlite==0.46.0`; the focused
validators above were run offline with Python 3.11 against the local uv cache.

## Identity and Grounding

The record is the Togo `M660` solid variant of JCM 645
`HALOSARCINA PALLIDA MEDIUM`. Togo `M659` represents the liquid branch without
agar; Togo `M660` carries the same source medium with the 20 g/L agar solid
option materialized.

The generated salts, yeast extract, casamino acids with `BD-Difco`, and agar
rows match Togo `M660` and JCM 645. The hydrated chloride preferred terms for
`CaCl2 x 2 H2O` and `MgCl2 x 6 H2O` preserve the supplied forms.

## Evidence

JCM 645 lists 180 g NaCl, 20 g `MgCl2 x 6 H2O`, 5 g K2SO4, 0.1 g
`CaCl2 x 2 H2O`, 0.5 g NH4Cl, 0.05 g KH2PO4, 0.1 g yeast extract, and 5 g
`Casamino acids (BD-Difco)` in 1 L final volume, followed by pH 6.5 adjustment
and autoclaving. It then says solid medium is prepared by adding 20 g/L agar.

Togo `M660` preserves those ingredient amounts and includes the solid agar row,
but its `Distilled water` component is `volume: 1`, `unit: "L"`. The generated
record imports that as `1 G_PER_L`, which is not dimensionally equivalent to
bringing the recipe to 1 L final volume.

Togo `M660` also keeps two comments: add components to distilled water, bring
volume to 1.0 L, adjust pH to 6.5, autoclave, and add 20 g/L agar for solid
medium. The generated record has neither `ph_value` nor `preparation_steps`.

## Completeness

The record is missing pH 6.5 and the autoclaving preparation sequence. The
water row is present but has the wrong unit and amount.

No target organisms, growth evidence, incubation temperature, atmosphere, or
stock-solution references are present in the Togo `M660` payload. The
corresponding empty optional fields are not defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The 1 L water/final-volume row was imported as `1 G_PER_L`. | Togo `M660` reports `Distilled water`, `volume: 1`, `unit: "L"`; JCM says to bring volume to 1.0 L. | `data/normalized_yaml/archaea/TOGO_M660_Halosarcina_Pallida_Medium.yaml` or the Togo water-unit importer |
| Major | pH and preparation were dropped. | Togo and JCM instruct pH 6.5 adjustment and autoclaving; the generated record has no `ph_value` or `preparation_steps`. | `data/normalized_yaml/archaea/TOGO_M660_Halosarcina_Pallida_Medium.yaml` or the Togo comment importer |

## Recommended Edits

1. In `data/normalized_yaml/archaea/TOGO_M660_Halosarcina_Pallida_Medium.yaml`
   or the Togo importer, represent distilled water as a 1 L final-volume
   component instead of `1 G_PER_L`.
2. Import the Togo comments as structured preparation: bring to 1 L, adjust pH
   to 6.5, autoclave, and include the 20 g/L agar solid branch.
3. Populate `ph_value: 6.5` on the solid branch.
4. Regenerate merged recipes from the corrected normalized owner; do not patch
   `data/merge_yaml/merged/halosarcina_pallida_medium__02a05db9.yaml`
   directly.

## Follow-up Checks

1. Run `just validate data/normalized_yaml/archaea/TOGO_M660_Halosarcina_Pallida_Medium.yaml`
   after the normalized Togo record or importer is corrected.
2. Run `just validate-terms data/normalized_yaml/archaea/TOGO_M660_Halosarcina_Pallida_Medium.yaml`
   to confirm hydrated chloride and casamino-acid grounding remain acceptable.
3. Run `just verify-merges` to prove the generated Togo M660 branch regenerates
   from the corrected normalized source.
4. Manually compare the regenerated record with Togo `M660`, Togo `M659`, and
   JCM 645 to confirm the solid and liquid branches remain distinct.

## Additional Notes

The direct curated JCM 645 record already models this medium as a concentration
variant of Halobacteria HMD medium. That curated branch is separate from Togo
`M660` and should remain the authority for the direct JCM import.
