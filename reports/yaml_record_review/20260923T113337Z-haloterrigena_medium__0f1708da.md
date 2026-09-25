# YAML Record Review: HALOTERRIGENA MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/haloterrigena_medium__0f1708da.yaml`
- Started UTC: 2026-09-23T11:32:34Z
- Finished UTC: 2026-09-23T11:33:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:000853` |
| Name | `haloterrigena_medium` |
| Original name | `HALOTERRIGENA MEDIUM` |
| Category | `archaea` |
| Physical state | `SOLID_AGAR` |
| pH | `7.2` |
| Generated from | `data/normalized_yaml/archaea/haloterrigena_medium.yaml` |
| Source accession | `mediadive.medium:1392` |
| Source PDF | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1392.pdf` |
| Merge fingerprint | `0f1708da1863def430d3399dd24d01b7bf58f4c085c5f794b85a8286b51b4119` |

I reviewed the generated merged record, its direct MediaDive/DSMZ normalized
owner, the DSMZ Medium 1392 PDF, and the MediaDive 1392 REST payload.

I searched `data/normalized_yaml` and `data/merge_yaml` YAML files with
`rg --no-ignore --hidden` for `mediadive.medium:1392`, `DSMZ Medium 1392`,
`DSMZ_Medium1392`, `HALOTERRIGENA MEDIUM`, and `haloterrigena_medium`. Ignored
files were included. The search found this direct DSMZ 1392 branch, a Togo
`M1858` sibling, and their generated outputs; only `haloterrigena_medium.yaml`
feeds this reviewed fingerprint.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/haloterrigena_medium__0f1708da.yaml` reported `No issues found`. |
| Strict schema | Passed: `python scripts/validate_strict.py data/merge_yaml/merged/haloterrigena_medium__0f1708da.yaml --out /private/tmp/haloterrigena_medium_0f1708da.strict.tsv --workers 1 --quiet` exited 0 and wrote a header-only TSV. |
| References | Passed with no checked references: `linkml-reference-validator validate data data/merge_yaml/merged/haloterrigena_medium__0f1708da.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported `Total checks: 0`. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/haloterrigena_medium__0f1708da.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries. |

The `just` validator entrypoints were not used because this checkout attempts
to resolve a Python 3.13 environment with `llvmlite==0.46.0`; the focused
validators above were run offline with Python 3.11 against the local uv cache.

## Identity and Grounding

The record correctly identifies DSMZ Medium 1392, `HALOTERRIGENA MEDIUM`, and
preserves pH 7.2. The NaCl, magnesium sulfate, KCl, trisodium citrate, KNO3,
calcium chloride, and agar quantities match the DSMZ and MediaDive rows.

The top-level `SOLID_AGAR` state is too narrow because DSMZ says the medium may
be solidified by adding 20 g/L agar. KNO3 still carries a legacy
`mediaingredientmech_term` field despite having a CHEBI primary term.

## Evidence

The current DSMZ 1392 PDF and MediaDive 1392 both list `Casamino acids` twice
at 5 g each, followed by 240 g NaCl, 10 g `MgSO4 x 7 H2O`, 5 g KCl, 3 g
trisodium citrate, 1 g KNO3, 0.2 g `CaCl2 x 2 H2O`, and 1000 ml distilled
water. The generated cleanup merged those two casamino-acid rows into a single
10 g/L row.

The source duplicate is consequential: if the first DSMZ `Casmino Acid` row is
a typographic duplicate, the generated value is doubled; if both rows are
intentional, the generated sum is arithmetically right but should retain a
discussion that the current DSMZ PDF repeats the component.

DSMZ's preparation instruction is to adjust to pH 7.2 and sterilize by
autoclaving. The generated record keeps the text but uses `action: MIX`.

## Completeness

The generated record omits the 1000 ml distilled-water component and does not
split the liquid base from the optional 20 g/L agar solid branch.

No target organisms, growth evidence, incubation temperature, atmosphere, or
stock-solution references are present in the MediaDive 1392 payload. The
corresponding empty optional fields are not defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The liquid base and conditional solid option are collapsed into one `SOLID_AGAR` record. | DSMZ says the medium may be solidified by adding 20 g/L agar; MediaDive marks the agar row with `condition: "for solid medium"`. | `data/normalized_yaml/archaea/haloterrigena_medium.yaml` or a variant-aware MediaDive import rule |
| Major | The 1000 ml water component is missing. | DSMZ and MediaDive both list 1000 ml distilled water in the mineral salts solution. | `data/normalized_yaml/archaea/haloterrigena_medium.yaml` or the MediaDive importer |
| Major | A duplicate casamino-acid source row was silently collapsed to 10 g/L without retaining the source ambiguity. | DSMZ 1392 repeats the 5 g Casamino acids row, and the generated curation history records `Merged 1 duplicate ingredient(s)`. | `data/normalized_yaml/archaea/haloterrigena_medium.yaml` and duplicate-ingredient cleanup |
| Minor | The preparation action is too generic. | The source says to adjust pH and sterilize by autoclaving; the generated step is `action: MIX`. | `data/normalized_yaml/archaea/haloterrigena_medium.yaml` or the MediaDive preparation importer |
| Minor | The KNO3 ingredient still uses the legacy MIM slot. | The generated row has `term: CHEBI:63043` but still stores `mediaingredientmech_term: MediaIngredientMech:000170`. | MIM/CHEBI migration or the normalized record |

## Recommended Edits

1. In `data/normalized_yaml/archaea/haloterrigena_medium.yaml` or the MediaDive
   importer, preserve the liquid base and the 20 g/L agar solid option as
   explicit variants rather than setting the whole record to `SOLID_AGAR`.
2. Restore the 1000 ml distilled-water row.
3. Add an explicit quality flag or discussion for the duplicate 5 g
   casamino-acid rows in the current DSMZ 1392 source before deciding whether
   the curated concentration should be 5 g/L or 10 g/L.
4. Represent the preparation as pH adjustment followed by autoclaving.
5. Refresh KNO3 to an id-safe `mediaingredientmech_chebi_term`.
6. Regenerate merged recipes from the corrected normalized owner; do not patch
   `data/merge_yaml/merged/haloterrigena_medium__0f1708da.yaml` directly.

## Follow-up Checks

1. Run `just validate data/normalized_yaml/archaea/haloterrigena_medium.yaml`
   after the normalized DSMZ 1392 record or importer is corrected.
2. Run `just validate-terms data/normalized_yaml/archaea/haloterrigena_medium.yaml`
   to confirm KNO3 uses the refreshed MIM/CHEBI field.
3. Run `just validate-media-variant-links` if the optional agar branch is
   represented as a variant.
4. Run `just verify-merges` to prove the generated DSMZ 1392 branch regenerates
   from the corrected normalized source.

## Additional Notes

The Togo `M1858` sibling is a separate import of the same DSMZ medium and
should be reviewed independently.
