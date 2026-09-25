# YAML Record Review: man_rogosa_sharpe_mrs_broth

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/man_rogosa_sharpe_mrs_broth__613cdd32.yaml
- Started UTC: 2026-09-23T23:09:35Z
- Finished UTC: 2026-09-23T23:09:35Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009057 |
| name | man_rogosa_sharpe_mrs_broth |
| original_name | Man-Rogosa-Sharpe (MRS) broth |
| category | bacterial |
| medium_type | COMPLEX |
| composition_type | UNDEFINED |
| physical_state | LIQUID |
| source term | TOGO:M2484, Man-Rogosa-Sharpe (MRS) broth |
| generated path | data/merge_yaml/merged/man_rogosa_sharpe_mrs_broth__613cdd32.yaml |
| maintained owner | data/normalized_yaml/bacterial/man_rogosa_sharpe_mrs_broth.yaml |

The reviewed YAML is a derived merge artifact. Its `merged_from` value names `man_rogosa_sharpe_mrs_broth`, and the terminal curation event reports an August 2026 merge on fingerprint `613cdd322b60d55de97154293f5b40452531dfd6c6636040790d7d03fb7a15c1`.

An ignored-file-inclusive exact search under `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:009057`, `TOGO:M2484`, and `M2484` found this normalized owner, this generated copy, and derived JSON indexes; no second YAML in those searched trees claimed the same exact CultureMech or TOGO identifier.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/man_rogosa_sharpe_mrs_broth__613cdd32.yaml` |
| Strict validator | Passed with 0 ERROR rows; `/private/tmp/man_rogosa_sharpe_mrs_broth__613cdd32.strict.tsv` had the header row only |
| Reference validator | Passed structurally: 1 file validated, 0 reference checks, 0 failures |
| Term validator | Passed |
| Embedded history validation | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` lists in merged media records |

The equivalent focused validators were run directly against the generated `MediaRecipe` because the project-level `just` wrappers currently resolve the default Python 3.13 project environment before running.

## Identity and Grounding

The generated record has the correct stable ID, label, category, and TOGO source accession for M2484. The hash suffix on the filename is justified by the other `Man-Rogosa-Sharpe (MRS) broth` TOGO records that normalize to the same stem but carry different source accessions.

TOGO M2484 represents the source recipe as one liter of `Man-Rogosa-Sharpe (MRS) broth` with GMO term `GMO_002109` labelled `MRS broth`. It does not enumerate the MRS components. The current normalized owner correctly keeps the product as an explicit unmapped ingredient instead of borrowing an internal formula from a sibling MRS record.

The generated copy is stale relative to the owner:

| Claim | Generated merge | Current normalized owner |
|---|---|---|
| Product amount | `1 G_PER_L` | `1000 ML_PER_L` |
| Source note | generic TOGO URL | TOGO M2484 one-liter opaque-product summary |
| Quality flags | absent | `ingredients_curated`, `has_unmapped_ingredients` |
| References | absent | `https://togomedium.org/medium/M2484` |
| Last source curation | absent | `RESOLVED_TOGO_PRODUCT_SCORE40_GRAPH` on 2026-09-07 |

## Evidence

TOGO M2484 supports the MRS broth identity and the one-liter `Man-Rogosa-Sharpe (MRS) broth` component. The TOGO comment mentions Lactobacillus piscium MKFS47 only as source context for DNA isolation from cells grown in MRS broth; it does not provide a pH, incubation temperature, stock-solution boundary, vendor formula, DOI, or PMID in the inspected payload.

TOGO M2484 does not support the generated record's `1 G_PER_L` amount. The inspected source row uses `volume: 1`, `unit: L`, and the maintained normalized owner has already corrected that to `1000 ML_PER_L`.

## Completeness

Missing or incomplete in the generated record:

- The generated copy does not include the September 2026 correction from `1 G_PER_L` to `1000 ML_PER_L`.
- The generated copy omits the normalized note, quality flags, and TOGO reference that make the commercial broth's intentionally opaque representation explicit.

Complete enough:

- No pH or temperature field is required from TOGO M2484.
- No stock-solution references are needed; TOGO M2484 lists the MRS broth product directly.
- No CHEBI or MediaIngredientMech term should be forced for the complete MRS broth product without vendor-composition evidence.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated merge is stale relative to its single normalized owner. | `data/normalized_yaml/bacterial/man_rogosa_sharpe_mrs_broth.yaml` has a 2026-09-07 `RESOLVED_TOGO_PRODUCT_SCORE40_GRAPH` curation event, `1000 ML_PER_L`, quality flags, and a TOGO reference; the generated YAML still has the pre-repair `1 G_PER_L` import and an August 2026 merge event. | Regenerate `data/merge_yaml/merged/man_rogosa_sharpe_mrs_broth__613cdd32.yaml` from `data/normalized_yaml/bacterial/man_rogosa_sharpe_mrs_broth.yaml` |
| major | The generated copy represents a one-liter source product as a gram concentration. | TOGO M2484 lists `volume: 1`, `unit: L` for `Man-Rogosa-Sharpe (MRS) broth`. The generated YAML stores `value: '1'`, `unit: G_PER_L`; the normalized owner has already corrected this to `value: '1000'`, `unit: ML_PER_L`. | data/normalized_yaml/bacterial/man_rogosa_sharpe_mrs_broth.yaml already contains the corrected value; regenerate the merge |

## Recommended Edits

1. Regenerate the merge output for `data/normalized_yaml/bacterial/man_rogosa_sharpe_mrs_broth.yaml` so `data/merge_yaml/merged/man_rogosa_sharpe_mrs_broth__613cdd32.yaml` carries the existing September 2026 normalized curation.
2. Preserve the complete MRS broth product as an explicit unmapped component until an inspected vendor sheet or publication supplies an internal formula for this exact source.
3. Use the Lactobacillus piscium MKFS47 comment as a growth-evidence lead only after inspecting the underlying paper and confirming taxon, strain, conditions, and citation details.

## Follow-up Checks

- Run the focused merge-freshness check or `just verify-merges` to prove the generated copy matches `data/normalized_yaml/bacterial/man_rogosa_sharpe_mrs_broth.yaml`.
- Rerun the open schema, strict, reference, and term validators on the regenerated merged record.
- Re-fetch TOGO M2484 and confirm the regenerated record keeps the one-liter commercial product as `1000 ML_PER_L`, not `1 G_PER_L`.

## Additional Notes

None found.
