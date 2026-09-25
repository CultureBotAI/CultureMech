# YAML Record Review: Cyanobacteria Medium BA+50+B+N/2

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/cyanobacteria_medium_ba_50_b_n_2.yaml
- Started UTC: 2026-09-22T12:25:15Z
- Finished UTC: 2026-09-22T12:28:22Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001160 |
| Name | cyanobacteria_medium_ba_50_b_n_2 |
| Source | DSMZ / MediaDive medium 1678 |
| Media term | mediadive.medium:1678, DSMZ Medium 1678 |
| Generated record | data/merge_yaml/merged/cyanobacteria_medium_ba_50_b_n_2.yaml |
| Maintained medium input | data/normalized_yaml/bacterial/cyanobacteria_medium_ba_50_b_n_2.yaml |

The generated record is a single-source merge from the normalized DSMZ /
MediaDive 1678 record. The row identity is correct, but the source T-Trace
Metal Mix was only partially nested in the normalized input and was flattened
again in the generated output.

## Validation

| Check | Result |
|---|---|
| LinkML open-schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/cyanobacteria_medium_ba_50_b_n_2.yaml` | Passed |
| Closed-schema validation, `python scripts/validate_strict.py data/merge_yaml/merged/cyanobacteria_medium_ba_50_b_n_2.yaml --out /private/tmp/cyanobacteria_medium_ba_50_b_n_2.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/cyanobacteria_medium_ba_50_b_n_2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/cyanobacteria_medium_ba_50_b_n_2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history validation | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML |

Shape validation passes, including the ungrounded Mg(SO4) row and the flattened
trace-stock constituents.

## Identity and Grounding

The generated and normalized records both identify DSMZ / MediaDive medium 1678
"Cyanobacteria Medium BA+50+B+N/2". Live MediaDive JSON for
`/download/medium/1678/json` gives the same ID, name, DSMZ source, and direct
DSMZ Medium 1678 PDF link.

A gitignore-independent `rg --no-ignore --hidden` search for
`cyanobacteria_medium_ba_50_b_n_2`, `Cyanobacteria Medium BA+50+B+N/2`,
`mediadive.medium:1678`, and `DSMZ Medium 1678` over `data/normalized_yaml`,
`data/raw`, and this generated file found one normalized MediaRecipe and one
generated merge. The search found no local raw DSMZ 1678 capture under
`data/raw`.

The Mg(SO4) x 7 H2O row is still ungrounded and carries no
MediaIngredientMech cross-link. The NaNO3 row has a correct CHEBI primary term
but retains the deprecated `mediaingredientmech_term` link.

## Evidence

The final main-solution concentrations in the generated record match
MediaDive's calculated `g_l` fields and DSMZ Medium 1678 for these rows:

| Row | Supported final amount |
|---|---:|
| NaCl | 33.3 g/L |
| MgCl2 x 6 H2O | 3.3 g/L |
| KCl | 3.3 g/L |
| Mg(SO4) x 7 H2O | 3.3 g/L |
| CaCl2 x 2 H2O | 3.3 g/L |
| Na3-citrate x 2 H2O | 0.00498 g/L |
| Na2-EDTA x 2 H2O | 0.00083 g/L |
| NaNO3 | 0.6225 g/L |
| K2HPO4 x 3 H2O | 0.0332 g/L |
| NaHCO3 | 0.180075 g/L |
| Fe(NH4)citrate | 0.0048 g/L |
| NH4Cl | 0.02675 g/L |
| Vitamin B12 | 0.00002 g/L |

The trace mix is not supported at final-medium scope. MediaDive medium 1678
adds `T-Trace Metal Mix` solution `5774` at 1 ml/L; DSMZ prints the same
1 ml/L trace-stock addition. The generated record lists ZnSO4, MnCl2, H3BO3,
Na2MoO4, CuSO4, and Co(NO3)2 as top-level final-medium ingredients and appends
the trace stock's make-up step as final preparation step 3.

The normalized input has a partial local `T-Trace Metal Mix` solution containing
MnCl2, H3BO3, and CuSO4, but ZnSO4, Na2MoO4, and Co(NO3)2 remain top-level
ingredients. The generated merge flattened even that partial local stock, so no
structured trace-solution boundary remains in the reviewed file.

DSMZ and MediaDive disagree on Cu/Co stock strengths inside T-Trace Metal Mix:
the DSMZ PDF prints 0.8 g/100 ml CuSO4 and 0.5 g/100 ml Co(NO3)2 stock
solutions, while the MediaDive text and JSON exports render those as 0.08 g/L
and 0.05 g/L. A curation fix should resolve that factor-100 conflict instead
of preserving the current raw `10` concentration for copper or final 0.005 g/L
for cobalt.

## Completeness

- The generated record has no structured `references`, `source_data`,
  `target_organisms`, or `growth_metrics`. Empty organism and growth slots are
  acceptable for this database recipe; source retrieval details should be added
  to structured provenance, not only to free-text `notes`.
- There is no source-owned normalized SolutionRecipe for MediaDive solution
  `5774`; a gitignore-independent search for the medium-specific record name
  and source ID found only the parent 1678 record. The only T-Trace Metal Mix
  representation is embedded and partial.
- The source Distilled water row from MediaDive is absent from the generated
  ingredient list, but the final-volume preparation step covers it.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | T-Trace Metal Mix was flattened into final-medium ingredients. | Source medium 1678 adds 1 ml/L of solution `5774`; the generated YAML lists ZnSO4, MnCl2, H3BO3, Na2MoO4, CuSO4, and Co(NO3)2 directly as final ingredients and appends the stock make-up step to final-medium preparation. | `data/normalized_yaml/bacterial/cyanobacteria_medium_ba_50_b_n_2.yaml` and merge logic for local `solutions` entries |
| major | The normalized local trace mix is incomplete and has unresolved Cu/Co stock arithmetic. | The local `solutions` block moved only MnCl2, H3BO3, and CuSO4; ZnSO4, Na2MoO4, and Co(NO3)2 remain top-level. DSMZ and MediaDive disagree on Cu/Co stock strengths, while CultureMech stores raw or over-flattened values. | `data/normalized_yaml/bacterial/cyanobacteria_medium_ba_50_b_n_2.yaml` |
| minor | Mg(SO4) x 7 H2O is ungrounded. | The ingredient row has no CHEBI or MediaIngredientMech mapping. | Normalized source or MediaDive compound 2154 mapping |
| minor | NaNO3 still uses the deprecated `mediaingredientmech_term` field. | Sodium nitrate has a valid CHEBI primary term but keeps `MediaIngredientMech:000171` as a legacy cross-link. | `data/normalized_yaml/bacterial/cyanobacteria_medium_ba_50_b_n_2.yaml` |
| minor | Source provenance is free-text only. | The DSMZ Medium 1678 PDF URL is in `notes`, but not in a structured `references` or `source_data` block. | `data/normalized_yaml/bacterial/cyanobacteria_medium_ba_50_b_n_2.yaml` |

## Recommended Edits

1. Preserve a complete T-Trace Metal Mix nested solution for MediaDive solution
   `5774` and link the 1678 parent to it at 1 ml/L.
2. Resolve the DSMZ vs MediaDive Cu/Co stock-strength discrepancy in that stock
   instead of treating the raw 10 ml additions as grams per liter.
3. Keep the supported final concentrations for the parent main-solution rows;
   they already match MediaDive's calculated final `g_l` values.
4. Ground Mg(SO4) x 7 H2O to the exact magnesium sulfate heptahydrate term if
   the source spelling can be normalized safely.
5. Migrate NaNO3 to a CHEBI-keyed MediaIngredientMech link and add structured
   DSMZ/MediaDive 1678 provenance.
6. Regenerate `data/merge_yaml/merged/cyanobacteria_medium_ba_50_b_n_2.yaml`
   after repairing the maintained input.

## Follow-up Checks

- Run open-schema, strict, reference, and term validation on the repaired
  normalized 1678 record and any extracted T-Trace Metal Mix SolutionRecipe.
- Regenerate the merge and verify that ZnSO4, MnCl2, H3BO3, Na2MoO4, CuSO4,
  and Co(NO3)2 do not appear as top-level final-medium ingredients.
- Compare the regenerated parent rows against MediaDive
  `/download/medium/1678/json`, and compare the Cu/Co stock interpretation
  against both MediaDive and the current DSMZ Medium 1678 PDF.

## Additional Notes

- `mediadive_5734_Trace_metal_mix.yaml` is not the source-owned stock for this
  medium; DSMZ 1678 uses MediaDive solution `5774`, whose Cu and Co source
  stock strengths are printed differently from solution `5734`.
