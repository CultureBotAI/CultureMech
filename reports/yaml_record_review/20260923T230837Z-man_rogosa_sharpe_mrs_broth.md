# YAML Record Review: man_rogosa_sharpe_mrs_broth

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/man_rogosa_sharpe_mrs_broth.yaml
- Started UTC: 2026-09-23T23:08:37Z
- Finished UTC: 2026-09-23T23:08:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009069 |
| name | man_rogosa_sharpe_mrs_broth |
| original_name | Man-Rogosa-Sharpe (MRS) broth |
| category | bacterial |
| medium_type | COMPLEX |
| composition_type | UNDEFINED |
| physical_state | LIQUID |
| source term | TOGO:M2495, Man-Rogosa-Sharpe (MRS) broth |
| generated path | data/merge_yaml/merged/man_rogosa_sharpe_mrs_broth.yaml |
| maintained owner | data/normalized_yaml/bacterial/TOGO_M2495_Man-Rogosa-Sharpe_MRS_broth.yaml |

The reviewed YAML is a derived merge artifact. Its `merged_from` value names the exact normalized owner `TOGO_M2495_Man-Rogosa-Sharpe_MRS_broth`, and the terminal curation event reports an August 2026 merge on fingerprint `aceef0e03f8017d423ea401f32c0e6bb6fae6c650304dfb675931f355cbb22f0`.

An ignored-file-inclusive exact search under `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:009069`, `TOGO:M2495`, and `M2495` found this normalized owner, this generated copy, and derived JSON indexes; no second YAML in those searched trees claimed the same exact CultureMech or TOGO identifier.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/man_rogosa_sharpe_mrs_broth.yaml` |
| Strict validator | Passed with 0 ERROR rows; `/private/tmp/man_rogosa_sharpe_mrs_broth.strict.tsv` had the header row only |
| Reference validator | Passed structurally: 1 file validated, 0 reference checks, 0 failures |
| Term validator | Passed |
| Embedded history validation | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` lists in merged media records |

The equivalent focused validators were run directly against the generated `MediaRecipe` because the project-level `just` wrappers currently resolve the default Python 3.13 project environment before running.

## Identity and Grounding

The generated record has the correct medium identity, stable ID, TOGO accession, and category for the M2495 Biokar Diagnostic MRS broth import.

TOGO M2495 does not expose a component-level broth formulation. It represents the source recipe as one liter of `Man-Rogosa-Sharpe (MRS) broth (Biokar Diagnostic, Beauvais, France)`, with TOGO GMO term `GMO_002113` labelled `MRS broth (Solabia, Biokar diagnostics)`. Keeping this commercial product as an unmapped literal component is faithful; importing peptone, beef extract, glucose, salts, citrate, or Tween 80 from another MRS recipe would overstate the inspected source.

The generated merge is stale relative to its owner:

| Claim | Generated merge | Current normalized owner |
|---|---|---|
| Product amount | `1 G_PER_L` | `1000 ML_PER_L` |
| Temperature | absent | `temperature_value: 37.0` |
| Source note | generic TOGO URL | TOGO M2495 anaerobic Gaspak H2+CO2, 37 C, 24 h summary |
| Preparation steps | absent | use one liter of product; grow anaerobically for 24 h at 37 C |
| Quality flags | absent | `ingredients_curated`, `has_unmapped_ingredients` |
| References | absent | `https://togomedium.org/medium/M2495` |
| Last source curation | absent | `RESOLVED_TOGO_MRS_2XYT_SCORE40` on 2026-09-08 |

## Evidence

TOGO M2495 supports the MRS broth identity, the Biokar Diagnostic commercial product label, and a one-liter source amount. It also supports anaerobic Gaspak H2+CO2 incubation for 24 h at 37 C as source context.

TOGO M2495 does not support the generated record's `1 G_PER_L` amount. The inspected source row uses `volume: 1`, `unit: L`, and the maintained normalized owner has already corrected that to `1000 ML_PER_L`.

The source does not provide a DOI, PMID, strain identifier, pH, storage rule, or internal product composition.

## Completeness

Missing or incomplete in the generated record:

- The generated copy does not include the September 2026 correction from `1 G_PER_L` to `1000 ML_PER_L`.
- The generated copy omits the source-supported 37 C value and the anaerobic Gaspak H2+CO2, 24 h preparation/incubation context.
- The generated copy omits the normalized quality flags and TOGO reference that mark the commercial broth as intentionally opaque and unmapped.

Complete enough:

- No pH field is required; TOGO M2495 does not report one.
- No stock-solution references are needed; TOGO M2495 lists the commercial broth product directly.
- No CHEBI or MediaIngredientMech grounding is expected for the complete commercial MRS broth product.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated merge is stale relative to its single normalized owner. | `data/normalized_yaml/bacterial/TOGO_M2495_Man-Rogosa-Sharpe_MRS_broth.yaml` has a 2026-09-08 `RESOLVED_TOGO_MRS_2XYT_SCORE40` curation event, `1000 ML_PER_L`, `temperature_value: 37.0`, anaerobic 24 h preparation context, quality flags, and a TOGO reference; the generated YAML still has the pre-repair `1 G_PER_L` import and an August 2026 merge event. | Regenerate `data/merge_yaml/merged/man_rogosa_sharpe_mrs_broth.yaml` from `data/normalized_yaml/bacterial/TOGO_M2495_Man-Rogosa-Sharpe_MRS_broth.yaml` |
| major | The generated copy represents a one-liter source product as a gram concentration. | TOGO M2495 lists `volume: 1`, `unit: L` for `Man-Rogosa-Sharpe (MRS) broth (Biokar Diagnostic, Beauvais, France)`. The generated YAML stores `value: '1'`, `unit: G_PER_L`; the normalized owner has already corrected this to `value: '1000'`, `unit: ML_PER_L`. | data/normalized_yaml/bacterial/TOGO_M2495_Man-Rogosa-Sharpe_MRS_broth.yaml already contains the corrected value; regenerate the merge |

## Recommended Edits

1. Regenerate the merge output for `data/normalized_yaml/bacterial/TOGO_M2495_Man-Rogosa-Sharpe_MRS_broth.yaml` so `data/merge_yaml/merged/man_rogosa_sharpe_mrs_broth.yaml` carries the existing September 2026 normalized curation.
2. Preserve the Biokar Diagnostic MRS broth as an explicit unmapped commercial-product component until an inspected product sheet or primary source provides its internal formula.
3. If the anaerobic Lactobacillus growth claim is later structured as target-organism evidence, inspect the underlying source before adding a taxon, strain, DOI, PMID, or growth metric.

## Follow-up Checks

- Run the focused merge-freshness check or `just verify-merges` to prove the generated copy matches `data/normalized_yaml/bacterial/TOGO_M2495_Man-Rogosa-Sharpe_MRS_broth.yaml`.
- Rerun the open schema, strict, reference, and term validators on the regenerated merged record.
- Re-fetch TOGO M2495 and confirm the regenerated record keeps the one-liter commercial product as `1000 ML_PER_L`, not `1 G_PER_L`.

## Additional Notes

None found.
