# YAML Record Review: Halorhabdus Segorensis Medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/halorhabdus_segorensis_medium__216a2588.yaml`
- Started UTC: 2026-09-23T11:11:39Z
- Finished UTC: 2026-09-23T11:13:45Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:007538` |
| Name | `halorhabdus_segorensis_medium` |
| Original name | `Halorhabdus Segorensis Medium` |
| Category | `archaea` |
| Physical state | `SOLID_AGAR` |
| Generated from | `data/normalized_yaml/archaea/TOGO_M1024_Halorhabdus_Segorensis_Medium.yaml` |
| Source accession | `TOGO:M1024` |
| Original source accession | `JCM_M973-2` |
| Merge fingerprint | `216a2588fd219e4804f48d223f15ff678e3ae106d71e322cec22e88457350af7` |

I reviewed the generated merged record, its normalized Togo owner, the Togo
`M1024` API payload, the live JCM `GRMD=973` page named by that payload, and
the secondary MediaDive `J973` REST payload.

I searched `data/normalized_yaml` and `data/merge_yaml` YAML files with
`rg --no-ignore --hidden` for `halorhabdus_segorensis_medium`,
`HALORHABDUS SEGORENSIS MEDIUM`, `TOGO:M1024`, `JCM_M973-2`, and
`GRMD=973`. Ignored files were included. That search found the reviewed
Togo `M1024` solid branch, a Togo `M1023` liquid sibling, a direct MediaDive
`J973` normalized import, their separate merged outputs, and the distinct
`HALORHABDUS SEGORENSIS S21 MEDIUM`; only the `M1024` solid branch feeds this
reviewed fingerprint.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halorhabdus_segorensis_medium__216a2588.yaml` exited 0 with no issues. |
| Strict schema | Passed: `python scripts/validate_strict.py data/merge_yaml/merged/halorhabdus_segorensis_medium__216a2588.yaml --out /private/tmp/halorhabdus_segorensis_medium_216a2588.strict.tsv --workers 1 --quiet` scanned one file and reported `total ERROR rows: 0`. |
| References | Passed with no checked references: `linkml-reference-validator validate data data/merge_yaml/merged/halorhabdus_segorensis_medium__216a2588.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported `Total checks: 0`. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/halorhabdus_segorensis_medium__216a2588.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 with no diagnostics. |
| Embedded history | Not checked: `just validate-history` validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries. |

The `just` validator entrypoints were not used because this checkout attempts
to resolve a Python 3.13 environment with `llvmlite==0.46.0`; the focused
validators above were run offline with Python 3.11 against the local uv cache.

## Identity and Grounding

The record denotes the Togo `M1024` solid branch of Halorhabdus segorensis
medium. The `SOLID_AGAR` state is supported because Togo `M1024` includes
20 g agar, while the sibling `M1023` Togo record is the liquid branch without
agar.

The Togo `M1024` API supports the generated NaCl, calcium chloride dihydrate,
magnesium chloride hexahydrate, KCl, soluble starch, agar, yeast extract
`BD-Difco`, and casamino acids `BD-Difco` ingredient identities and quantities.
It also supports the GMO role/property annotations embedded in the generated
`notes` fields.

The original JCM URL now returns no live formulation: fetching
`https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=973` returned a JCM page
with `Nothing found.` I therefore used the Togo `M1024` API as the direct
formulation source and MediaDive `J973` only as a consistency check for pH and
preparation comments that Togo also exposes.

## Evidence

Togo `M1024` lists these component rows under `main solution 1`:

| Component | Togo amount | Generated amount |
|---|---:|---:|
| `Distilled water` | 1000 ml | 1000 g/L |
| `NaCl` | 40.1 g | 40.1 g/L |
| `CaCl2 x 2 H2O` | 29.4 g | 29.4 g/L |
| `MgCl2 x 6 H2O` | 203 g | 203 g/L |
| `KCl` | 7.5 g | 7.5 g/L |
| `Soluble starch` | 2 g | 2 g/L |
| `agar` | 20 g | 20 g/L |
| `Yeast extract (BD-Difco)` | 1 g | 1 g/L |
| `Casamino acids (BD-Difco)` | 1 g | 1 g/L |

The salt, starch, agar, yeast extract, and casamino-acid amounts are supported.
The water row is dimensionally wrong: Togo reports `1000 ml`, but the generated
record stores that volume as `1000 G_PER_L`.

Togo `M1024` also carries a preparation comment with three consequential
instructions:

- dissolve `MgCl2 x 6 H2O` in distilled water and bring that solution to 500 ml;
- separately dissolve the remaining components in 500 ml distilled water and
  adjust to pH 7.0;
- for solid medium, add 20 g agar to the latter solution, autoclave both
  solutions separately, and combine them after autoclaving.

The generated record omits all of that text as structured preparation. It also
omits `ph_value: 7.0`, even though Togo's own comment and MediaDive `J973`
both preserve that value.

## Completeness

The generated record is not complete enough to reproduce Togo `M1024` because
it has no preparation steps, no pH, and no representation of the two 500 ml
solution boundaries.

No target organisms, growth evidence, incubation temperature, atmosphere, or
stock-solution references are present in the Togo `M1024` payload. The
corresponding empty optional fields in the generated record are not defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The Togo `1000 ml` distilled-water volume was imported as `1000 G_PER_L`. | Togo `M1024` reports `component_name: "Distilled water"`, `volume: 1000`, `unit: "ml"`. The generated record changes the unit to `G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1024_Halorhabdus_Segorensis_Medium.yaml` or the Togo import transform |
| Major | `ph_value: 7.0` is missing. | Togo's preparation comment instructs adjustment to pH 7.0, and MediaDive `J973` gives `min_pH: 7`, `max_pH: 7`. | `data/normalized_yaml/archaea/TOGO_M1024_Halorhabdus_Segorensis_Medium.yaml` or the Togo comment importer |
| Major | The split-solution preparation was dropped. | Togo `M1024` carries the full instruction to make a 500 ml `MgCl2 x 6 H2O` solution, make a second 500 ml solution, add 20 g agar to the second solution for the solid medium, autoclave both separately, and combine them after autoclaving. The generated record has no `preparation_steps`. | `data/normalized_yaml/archaea/TOGO_M1024_Halorhabdus_Segorensis_Medium.yaml` or the Togo comment importer |
| Minor | The stored original JCM URL is stale. | The record and Togo metadata both point to `GRMD=973`, but the live JCM page now reports no medium for that ID. | Togo source metadata, or a curator note if historical JCM URLs are retained intentionally |

## Recommended Edits

1. In the Togo import transform or
   `data/normalized_yaml/archaea/TOGO_M1024_Halorhabdus_Segorensis_Medium.yaml`,
   preserve `Distilled water` as the source's 1000 ml final-volume component
   instead of converting it to `1000 G_PER_L`.
2. Import the Togo preparation comment into ordered `preparation_steps` that
   preserve the two 500 ml solution scopes, pH 7.0 adjustment, agar addition to
   the non-MgCl2 solution, separate autoclaving, and post-autoclave combination.
3. Populate the top-level pH from the Togo comment as `ph_value: 7.0`.
4. Decide whether stale historical JCM URLs should remain only in free-text
   notes or get an explicit unresolved-source flag when the live JCM endpoint
   no longer serves the formula.
5. Regenerate merged recipes from the normalized Togo owner; do not patch
   `data/merge_yaml/merged/halorhabdus_segorensis_medium__216a2588.yaml`
   directly.

## Follow-up Checks

1. Run `just validate data/normalized_yaml/archaea/TOGO_M1024_Halorhabdus_Segorensis_Medium.yaml`
   after the normalized Togo record or importer is corrected.
2. Run `just validate-terms data/normalized_yaml/archaea/TOGO_M1024_Halorhabdus_Segorensis_Medium.yaml`
   to confirm the hydrated salts, soluble starch, agar, water, and BD-Difco
   undefined components still ground acceptably after regeneration.
3. Run `just verify-merges` to prove the corrected normalized Togo record
   regenerates the M1024 merged output.
4. Manually compare the regenerated record with the Togo `M1024` API comment
   and the MediaDive `J973` preparation text to confirm no step boundary was
   lost.

## Additional Notes

The separate direct MediaDive `J973` import keeps the same pH 7.0 and
preparation text in free text, but it represents the liquid base and says agar
is added for solid medium. It should remain a sibling branch, not be merged
silently with Togo `M1024` unless variant handling can preserve the liquid and
solid scopes explicitly.
