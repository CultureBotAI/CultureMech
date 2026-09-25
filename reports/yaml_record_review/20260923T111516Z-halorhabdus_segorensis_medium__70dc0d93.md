# YAML Record Review: HALORHABDUS SEGORENSIS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/halorhabdus_segorensis_medium__70dc0d93.yaml`
- Started UTC: 2026-09-23T11:14:50Z
- Finished UTC: 2026-09-23T11:15:16Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:003322` |
| Name | `halorhabdus_segorensis_medium` |
| Original name | `HALORHABDUS SEGORENSIS MEDIUM` |
| Category | `archaea` |
| Physical state | `LIQUID` |
| pH | `7.0` |
| Generated from | `data/normalized_yaml/archaea/halorhabdus_segorensis_medium.yaml` |
| Source accession | `mediadive.medium:J973` |
| Source URL | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=973` |
| Merge fingerprint | `70dc0d931a6de801ac303740c4dd696fda7dc82ea97b607db5f9283791e8bd58` |

I reviewed the generated merged record, its direct MediaDive/JCM normalized
owner, the MediaDive `J973` REST payload, the live JCM `GRMD=973` page, and
the sibling Togo `M1023` and `M1024` normalized records.

I searched `data/normalized_yaml/archaea` and `data/merge_yaml/merged` YAML
files with `rg --no-ignore --hidden` for `mediadive.medium:J973`,
`JCM Medium J973`, `jcm_grmd?GRMD=973`, `GRMD=973`,
`HALORHABDUS SEGORENSIS MEDIUM`, and `halorhabdus_segorensis_medium`. Ignored
files were included. The search found the direct MediaDive `J973` owner under
review, Togo `M1023` and `M1024` siblings from the same historical JCM page,
and their separate generated outputs; only `halorhabdus_segorensis_medium.yaml`
feeds this reviewed fingerprint.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halorhabdus_segorensis_medium__70dc0d93.yaml` exited 0 with no diagnostics. |
| Strict schema | Passed: `python scripts/validate_strict.py data/merge_yaml/merged/halorhabdus_segorensis_medium__70dc0d93.yaml --out /private/tmp/halorhabdus_segorensis_medium_70dc0d93.strict.tsv --workers 1 --quiet` exited 0 and wrote a header-only TSV. |
| References | Passed with no checked references: `linkml-reference-validator validate data data/merge_yaml/merged/halorhabdus_segorensis_medium__70dc0d93.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported `Total checks: 0`. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/halorhabdus_segorensis_medium__70dc0d93.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries. |

The `just` validator entrypoints were not used because this checkout attempts
to resolve a Python 3.13 environment with `llvmlite==0.46.0`; the focused
validators above were run offline with Python 3.11 against the local uv cache.

## Identity and Grounding

The record is the direct MediaDive import of JCM medium `J973`, and MediaDive
still reports the JCM medium name `HALORHABDUS SEGORENSIS MEDIUM`, pH 7.0, and
JCM source identity for that accession.

The live JCM URL currently returns no formulation for `GRMD=973`; it displays
`Nothing found.` The MediaDive `J973` payload therefore served as the inspected
source for the exact direct branch, with Togo `M1023` and `M1024` only checked
as source-family siblings.

## Evidence

The generated record correctly preserves the direct MediaDive `J973` pH and
base salts:

| Ingredient | MediaDive amount | Generated amount |
|---|---:|---:|
| `NaCl` | 40.1 g | 40.1 g/L |
| `MgCl2 x 6 H2O` | 203 g | 203 g/L |
| `CaCl2 x 2 H2O` | 29.4 g | 29.4 g/L |
| `KCl` | 7.5 g | 7.5 g/L |
| `Yeast extract` | 1 g | 1 g/L |
| `Casamino acids` | 1 g | 1 g/L |
| `Starch` | 2 g | 2 g/L |

The MediaDive payload qualifies `Yeast extract` and `Casamino acids` with
`BD-Difco` attributes and qualifies `Starch` as soluble. The generated record
drops all three qualifiers.

MediaDive also carries the preparation paragraph: dissolve `MgCl2 x 6 H2O` in
distilled water to 500 ml, separately dissolve the remaining components in
500 ml distilled water and adjust to pH 7.0, add 20 g agar to that latter
solution for solid medium, autoclave the two solutions separately, and combine
them after autoclaving. The generated record keeps that paragraph, but it
stores it as one `AUTOCLAVE` action rather than representing the water, two
solution scopes, pH adjustment, conditional agar branch, separate autoclaving,
and final combination.

## Completeness

The record is missing the two 500 ml distilled-water scopes described by the
source preparation. It is also missing the source's 20 g agar solid branch; the
current `LIQUID` record keeps the agar instruction only as unstructured text
inside one preparation string.

No target organisms, growth evidence, incubation temperature, atmosphere, or
stock-solution references are present in the MediaDive `J973` source payload.
The corresponding empty optional fields are not defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record omits the two 500 ml distilled-water scopes. | MediaDive's preparation text says to dissolve `MgCl2 x 6 H2O` in distilled water and bring volume to 500 ml, then separately dissolve the remaining components in 500 ml distilled water. No water entry or structured solution boundary appears in the generated record. | `data/normalized_yaml/archaea/halorhabdus_segorensis_medium.yaml` or the MediaDive preparation importer |
| Major | The source's solid-medium agar branch is not represented as an ingredient or variant. | MediaDive says to add 20 g agar to the second solution for preparation of solid medium. The generated record is `LIQUID` and has no agar ingredient or linked solid variant. | `data/normalized_yaml/archaea/halorhabdus_segorensis_medium.yaml` or a variant-aware MediaDive import rule |
| Major | The preparation paragraph is collapsed to one broad `AUTOCLAVE` action. | The source distinguishes dissolution of two 500 ml solutions, pH adjustment, conditional agar addition, separate autoclaving, and post-autoclave combination. The generated record has one step whose action is only `AUTOCLAVE`. | `data/normalized_yaml/archaea/halorhabdus_segorensis_medium.yaml` or the MediaDive preparation importer |
| Minor | Three source ingredient qualifiers were dropped. | MediaDive has `attribute: "BD-Difco"` for yeast extract and casamino acids, and `attribute: "soluble"` for starch. The generated ingredient labels are unqualified. | `data/normalized_yaml/archaea/halorhabdus_segorensis_medium.yaml` or the MediaDive ingredient importer |
| Minor | The stored JCM URL is stale. | The record points to `GRMD=973`, but the live JCM page now reports no medium for that ID. | `data/normalized_yaml/archaea/halorhabdus_segorensis_medium.yaml` or a curator note if stale JCM links are kept as historical provenance |

## Recommended Edits

1. In `data/normalized_yaml/archaea/halorhabdus_segorensis_medium.yaml` or the
   MediaDive importer, represent the two 500 ml water scopes from the JCM
   preparation text.
2. Split the liquid base and 20 g agar solid branch into explicit variant
   structure or separate linked normalized records so the conditional agar
   instruction is no longer trapped in free text.
3. Split the preparation paragraph into ordered steps for making the MgCl2
   solution, making the remaining-component solution, adjusting pH 7.0,
   adding agar only for the solid branch, separately autoclaving both
   solutions, and combining them after autoclaving.
4. Preserve `BD-Difco` on yeast extract and casamino acids and preserve the
   soluble qualifier on starch.
5. Decide whether the dead live JCM link needs an explicit quality flag or
   whether the MediaDive `J973` accession is sufficient provenance.
6. Regenerate merged recipes from the normalized owner; do not patch
   `data/merge_yaml/merged/halorhabdus_segorensis_medium__70dc0d93.yaml`
   directly.

## Follow-up Checks

1. Run `just validate data/normalized_yaml/archaea/halorhabdus_segorensis_medium.yaml`
   after the normalized record or importer is corrected.
2. Run `just validate-terms data/normalized_yaml/archaea/halorhabdus_segorensis_medium.yaml`
   to confirm the hydrated salts, soluble starch, and BD-Difco undefined
   components still ground acceptably.
3. Run `just verify-merges` to prove the generated
   `halorhabdus_segorensis_medium__70dc0d93.yaml` record can be recreated from
   the maintained normalized owner.
4. Manually compare the regenerated preparation steps against MediaDive `J973`
   and the Togo `M1023`/`M1024` siblings to ensure the liquid and solid scopes
   remain distinct.

## Additional Notes

The Togo `M1024` solid sibling materializes the 20 g agar branch, while the
Togo `M1023` sibling materializes the liquid branch. Their presence supports
treating the MediaDive `for preparation of solid medium` sentence as a variant
boundary instead of as a single unconditional liquid-medium instruction.
