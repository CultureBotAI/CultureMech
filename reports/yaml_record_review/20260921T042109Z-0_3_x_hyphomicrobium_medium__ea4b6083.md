# YAML Record Review: TOGO M1158 0.3 x Hyphomicrobium Medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/0_3_x_hyphomicrobium_medium__ea4b6083.yaml`
- Started UTC: 2026-09-21T04:20:52Z
- Finished UTC: 2026-09-21T04:21:09Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/0_3_x_hyphomicrobium_medium__ea4b6083.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007681` |
| Name | `0_3_x_hyphomicrobium_medium` |
| Label | `0.3 x Hyphomicrobium Medium` |
| Source | TOGO Medium M1158, originally JCM Medium 1088 |
| Generated? | Yes; single-source merge from `data/normalized_yaml/bacterial/TOGO_M1158_0.3_x_Hyphomicrobium_Medium.yaml` |

Future corrections belong in
`data/normalized_yaml/bacterial/TOGO_M1158_0.3_x_Hyphomicrobium_Medium.yaml` or
the TOGO import transform, followed by merge regeneration.

## Validation

| Check | Result |
|---|---|
| Documented `just validate-*` validators | Not rerun for this fourth report: in the same checkout, the documented project `uv` path fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13. |
| No-project LinkML schema fallback | Passed: `linkml-validate` reported `No issues found`. |
| No-project strict-schema fallback | Passed: 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| No-project reference fallback | Passed: 1 file validated, 0 reference checks, all validations passed. |
| No-project term fallback | Passed: `linkml-term-validator` reported `Validation passed`. |
| History validation | Not checked: this review did not create a `history/*.yaml` record. |

## Identity and Grounding

The record correctly identifies TOGO M1158 and its upstream JCM 1088 medium.
TOGO M1158, JCM 1088, and MediaDive J1088 agree that the recipe is
`0.3 x Hyphomicrobium Medium`.

The main gram rows are in the right numeric range when interpreted as a
1 L recipe:

| Ingredient | Generated value | TOGO value |
|---|---:|---:|
| `MgSO4-7H2O` | 0.07 g/L | 0.07 g/L |
| `K2HPO4` | 0.85 g/L | 0.85 g/L |
| `(NH4)2SO4` | 0.2 g/L | 0.2 g/L |
| `NaH2PO4` | 0.75 g/L | 0.75 g/L |
| `Agar` | 15 g/L | 15 g/L |

The trace-vitamin and Visniac stock boundaries are wrong or incomplete.

## Evidence

The inspected sources were:

- live TOGO `gmdb_medium_by_gmid?gm_id=M1158` response;
- live TOGO `gmdb_medium_by_gmid?gm_id=M925` response;
- live JCM `GRMD=1088` HTML;
- live MediaDive REST response for `J1088`.

TOGO M1158 lists 1 L distilled water, basal salts, 2 ml methanol, 15 g agar,
1 ml `Visniac trace elements (see Medium [M925])`, and 2 ml `Trace vitamins
(see below)`. Its trace-vitamin subcomponent is a separate 500 ml stock. The
generated record flattened that 500 ml stock into top-level ingredient rows and
also kept a top-level empty `Trace vitamins (see below)` row at `2 G_PER_L`.

The `Visniac trace elements` entry is closer: it remains a `solutions` entry
with empty composition and a cross-reference to M925. That cross-reference is
too coarse for direct use because TOGO M925 is a complete Hyphomicrobium medium
with its own 500 ml `Visniac trace elements` subcomponent.

## Completeness

The record is missing enough source structure to make the final formulation
ambiguous:

- the trace-vitamin stock is both flattened and represented as an empty 2 g/L
  top-level row;
- the Visniac trace-element stock is empty rather than nested or linked to the
  M925 sub-solution;
- source water is merged from unrelated main and vitamin-stock volumes into
  one 501 g/L row;
- 2 ml methanol is represented as 2 g/L;
- the post-autoclave, filter-sterilized vitamin/methanol addition is omitted.

No target-organism or growth-evidence claims are present.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The 500 ml trace-vitamin stock was flattened into final top-level vitamin rows and the 2 ml/L stock addition was retained as `Trace vitamins (see below)` at `2 G_PER_L`. | TOGO M1158 and JCM 1088 make the vitamins a 500 ml stock added at 2 ml/L. | `data/normalized_yaml/bacterial/TOGO_M1158_0.3_x_Hyphomicrobium_Medium.yaml` |
| Major | The Visniac trace elements stock is an empty `G_PER_L` solution with only a broad M925 cross-reference. | TOGO M1158 adds 1 ml of Visniac trace elements; TOGO M925 contains the 500 ml Visniac trace element subcomponent that should own Ca, Fe, Mn, Co, Zn, Cu, molybdate, and EDTA rows. | `data/normalized_yaml/bacterial/TOGO_M1158_0.3_x_Hyphomicrobium_Medium.yaml` plus `data/normalized_yaml/bacterial/TOGO_M925_Hyphomicrobium_Medium.yaml` |
| Major | `Distilled water` is `501 G_PER_L`, summing 1 L final-medium water with 500 ml trace-vitamin stock water. | TOGO M1158 separates 1 L main solution water from 500 ml trace-vitamin stock water. | TOGO import / solution migration for `data/normalized_yaml/bacterial/TOGO_M1158_0.3_x_Hyphomicrobium_Medium.yaml` |
| Major | 2 ml/L methanol was converted to `2 G_PER_L`. | TOGO/JCM/MediaDive all list methanol as 2 ml. | `data/normalized_yaml/bacterial/TOGO_M1158_0.3_x_Hyphomicrobium_Medium.yaml` |
| Major | The only preparation step was omitted. | TOGO/JCM/MediaDive all state that trace vitamins and methanol are added aseptically after autoclaving, with the vitamins filter-sterilized. | `data/normalized_yaml/bacterial/TOGO_M1158_0.3_x_Hyphomicrobium_Medium.yaml` |

## Recommended Edits

1. Model the trace-vitamin block as a 500 ml stock solution added at 2 ml/L;
   remove its flattened top-level vitamin rows and the empty `2 G_PER_L`
   ingredient.
2. Link or inline the M925 `Visniac trace elements` 500 ml subcomponent as a
   1 ml/L stock addition without importing M925's complete main medium.
3. Split main-medium distilled water from stock water and stop summing them.
4. Represent methanol as 2 ml/L or another supported volume unit.
5. Restore the post-autoclave, filter-sterilized trace-vitamins/methanol step.
6. Regenerate the merged corpus and indexes.

## Follow-up Checks

- Run schema, strict, term, and reference validation on the normalized M1158
  source after the stock repair.
- Manually compare M1158 against both TOGO and JCM to ensure the M925 reference
  resolves to only the Visniac trace elements stock.
- Run `just merge-recipes`, `just verify-merges`, and
  `just audit-merge-freshness`.

## Additional Notes

This is a single-source merge. Its source identity is valid, but the imported
representation conflates final medium, local trace-vitamin stock, and
cross-referenced trace-element stock quantities.
