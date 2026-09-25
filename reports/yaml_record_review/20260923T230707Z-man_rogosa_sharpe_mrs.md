# YAML Record Review: man_rogosa_sharpe_mrs

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/man_rogosa_sharpe_mrs.yaml
- Started UTC: 2026-09-23T23:07:07Z
- Finished UTC: 2026-09-23T23:07:07Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009475 |
| name | man_rogosa_sharpe_mrs |
| original_name | Man-Rogosa-Sharpe (MRS) |
| category | bacterial |
| medium_type | COMPLEX |
| composition_type | UNDEFINED |
| physical_state | LIQUID |
| source term | TOGO:M2949, Man-Rogosa-Sharpe (MRS) |
| generated path | data/merge_yaml/merged/man_rogosa_sharpe_mrs.yaml |
| maintained owner | data/normalized_yaml/bacterial/man_rogosa_sharpe_mrs.yaml |

The reviewed YAML is a derived merge artifact. Its terminal curation event reports a merge from the single normalized owner on fingerprint `7d1900c8bcf91e8b60f3c724722ddfece5f9e452cfa22cd211e38887f1648887`.

An ignored-file-inclusive exact search under `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:009475`, `TOGO:M2949`, and `M2949` found this normalized owner, this generated copy, and derived JSON indexes; no second YAML in those searched trees claimed the same exact CultureMech or TOGO identifier. An exact filename search under `data/normalized_yaml`, also including ignored files, found `man_rogosa_sharpe_mrs.yaml` plus the expected sibling records `man_rogosa_sharpe_mrs_broth.yaml` and `man_rogosa_sharpe_mrs_broth_difco.yaml`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/man_rogosa_sharpe_mrs.yaml` |
| Strict validator | Passed with 0 ERROR rows; `/private/tmp/man_rogosa_sharpe_mrs.strict.tsv` had the header row only |
| Reference validator | Passed structurally: 1 file validated, 0 reference checks, 0 failures |
| Term validator | Passed |
| Embedded history validation | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` lists in merged media records |

The equivalent focused validators were run directly against the generated `MediaRecipe` because the project-level `just` wrappers currently resolve the default Python 3.13 project environment before running.

## Identity and Grounding

The source identity is narrow and recoverable. TOGO M2949 names the medium `Man-Rogosa-Sharpe (MRS)` and represents the recipe as one liter of the commercial product `Man-Rogosa-Sharpe (MRS) (Beijing Land Bridge Technology Co., Ltd. CM187)`.

This record is not an internally specified MRS formula like TOGO M2906. TOGO M2949 does not enumerate peptone, beef extract, yeast extract, glucose, Tween 80, salts, citrate, or pH; it only states the Beijing Land Bridge product volume. Leaving that product as an unmapped literal ingredient is therefore more faithful than copying a sibling MRS formula into this record.

The generated copy is stale relative to the normalized owner:

| Claim | Generated merge | Current normalized owner |
|---|---|---|
| Product amount | `1 G_PER_L` | `1000 ML_PER_L` |
| Temperature | absent | `temperature_value: 37.0` |
| Source note | generic TOGO URL | TOGO M2949 summary including static cultivation and missing internal composition |
| Quality flags | absent | `ingredients_curated`, `has_unmapped_ingredients` |
| References | absent | `https://togomedium.org/medium/M2949` |
| Last source curation | absent | `RESOLVED_TOGO_LITERAL_PRODUCT_SCORE40_GRAPH` on 2026-09-07 |

## Evidence

TOGO M2949 supports:

- `TOGO:M2949` as the source accession for `Man-Rogosa-Sharpe (MRS)`.
- One liter of `Man-Rogosa-Sharpe (MRS) (Beijing Land Bridge Technology Co., Ltd. CM187)`.
- A source comment saying Lactobacillus bulgaricus was cultured in that MRS product at 37 C with no shaking.

TOGO M2949 does not support the generated record's `1 G_PER_L` amount. The source unit is liters, not grams, and the current normalized owner has already corrected that to `1000 ML_PER_L`.

No inspected source supports breaking this literal product into canonical MRS ingredients. The absence of a structured CHEBI or MediaIngredientMech term on the commercial MRS ingredient is expected until a curator identifies the exact vendor formula.

## Completeness

Missing or incomplete in the generated record:

- The generated copy does not include the September 2026 normalized curation that changed the commercial product from `1 G_PER_L` to `1000 ML_PER_L`.
- The generated copy does not include the TOGO-supported `temperature_value: 37.0`.
- The generated copy does not include the current normalized source reference, quality flags, or note that the source omits the product's internal composition.

Complete enough:

- No pH is present in TOGO M2949.
- No stock-solution references are needed; TOGO provides only the commercial product amount.
- No ingredient breakdown should be inferred from adjacent MRS records.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated merge is stale relative to its single normalized owner. | `data/normalized_yaml/bacterial/man_rogosa_sharpe_mrs.yaml` has a 2026-09-07 `RESOLVED_TOGO_LITERAL_PRODUCT_SCORE40_GRAPH` curation event, `1000 ML_PER_L`, `temperature_value: 37.0`, data-quality flags, and a TOGO reference; `data/merge_yaml/merged/man_rogosa_sharpe_mrs.yaml` still has the pre-repair `1 G_PER_L` import and an August 2026 merge event. | Regenerate `data/merge_yaml/merged/man_rogosa_sharpe_mrs.yaml` from `data/normalized_yaml/bacterial/man_rogosa_sharpe_mrs.yaml` |
| major | The generated copy represents a one-liter source product as a gram concentration. | TOGO M2949 lists `volume: 1`, `unit: L` for the Beijing Land Bridge MRS product. The generated YAML stores `value: '1'`, `unit: G_PER_L`; the normalized owner has already corrected this to `value: '1000'`, `unit: ML_PER_L`. | data/normalized_yaml/bacterial/man_rogosa_sharpe_mrs.yaml already contains the corrected value; regenerate the merge |

## Recommended Edits

1. Regenerate the merge output for `data/normalized_yaml/bacterial/man_rogosa_sharpe_mrs.yaml` so `data/merge_yaml/merged/man_rogosa_sharpe_mrs.yaml` carries the existing September 2026 normalized curation.
2. After regeneration, keep the commercial Beijing Land Bridge MRS product as an explicit unresolved/literal ingredient unless an inspected vendor source supplies its internal formula.
3. Use the TOGO M2949 comment as a growth-evidence lead only after inspecting its cited underlying publication or source row; the current TOGO payload alone does not identify a publication, DOI, PMID, or strain accession.

## Follow-up Checks

- Run the focused merge-freshness check or `just verify-merges` to prove the generated copy matches `data/normalized_yaml/bacterial/man_rogosa_sharpe_mrs.yaml`.
- Rerun the open schema, strict, reference, and term validators on the regenerated merged record.
- Re-fetch TOGO M2949 and confirm the regenerated record keeps the one-liter commercial product as `1000 ML_PER_L`, not `1 G_PER_L`.

## Additional Notes

None found.
