# YAML Record Review: Cyanobacteria Medium BG11+ (TES buffered)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/cyanobacteria_medium_bg11_tes_buffered.yaml
- Started UTC: 2026-09-22T12:33:35Z
- Finished UTC: 2026-09-22T12:35:56Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001071 |
| Name | cyanobacteria_medium_bg11_tes_buffered |
| Source | DSMZ / MediaDive medium 1593a |
| Media term | mediadive.medium:1593a, DSMZ Medium 1593a |
| Generated record | data/merge_yaml/merged/cyanobacteria_medium_bg11_tes_buffered.yaml |
| Maintained medium input | data/normalized_yaml/bacterial/cyanobacteria_medium_bg11_tes_buffered.yaml |
| Shared solution input | data/normalized_yaml/bacterial/mediadive_5734_Trace_metal_mix.yaml |

This is the TES-buffered BG11+ variant with pH 8.0. It is a single-source
generated merge from the normalized MediaDive import for DSMZ medium 1593a.

## Validation

| Check | Result |
|---|---|
| LinkML open-schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/cyanobacteria_medium_bg11_tes_buffered.yaml` | Passed |
| Closed-schema validation, `python scripts/validate_strict.py data/merge_yaml/merged/cyanobacteria_medium_bg11_tes_buffered.yaml --out /private/tmp/cyanobacteria_medium_bg11_tes_buffered.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/cyanobacteria_medium_bg11_tes_buffered.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/cyanobacteria_medium_bg11_tes_buffered.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history validation | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML |

The file is schema-valid despite inherited stock-dilution errors.

## Identity and Grounding

The generated record correctly identifies MediaDive medium `1593a`,
"Cyanobacteria Medium BG11+ (TES buffered)"; live MediaDive JSON reports the
same DSMZ source, medium ID, fixed pH 8.0, and title. The top-level `ph_value:
8.0` and TES row agree with DSMZ Medium 1593a.

A gitignore-independent `rg --no-ignore --hidden` search for
`mediadive.medium:1593a`, `Cyanobacteria Medium BG11+ (TES buffered)`, and
`cyanobacteria_medium_bg11_tes_buffered` over `data/normalized_yaml`,
`data/raw`, and this generated file found one normalized 1593a source record
and one generated merge. The same search found no local raw DSMZ 1593a capture
under `data/raw`.

Mg(SO4) x 7 H2O is still ungrounded, and the NaNO3 row still uses a legacy
`mediaingredientmech_term` link.

## Evidence

DSMZ and MediaDive support 2.3 g TES and pH 8.0 in the final 1000 ml recipe.
The remaining parent rows inherit BG11+ stock additions:

| Component | Source addition | Generated record |
|---|---:|---:|
| TES | 2.3 g/L | 2.3 g/L |
| NaNO3 | 5 ml of 300 g/L stock = 1.5 g/L | 5 g/L |
| Mg(SO4) x 7 H2O | 10 ml of 7.5 g/L stock = 0.075 g/L | 10 g/L |
| CaCl2 x 2 H2O | 10 ml of 3.6 g/L stock = 0.036 g/L | 10 g/L |
| Na3-citrate x 2 H2O | 10 ml of 0.6 g/L stock = 0.006 g/L | 10 g/L |
| Na-EDTA x 2 H2O | 10 ml of 0.1 g/L stock = 0.001 g/L | 10 g/L |
| K2HPO4 x 3 H2O | BG11-Mix, 2 ml of a 20 g/L stock = 0.04 g/L | 2 g/L |
| Na2CO3 | BG11-Mix, 2 ml of a 10 g/L stock = 0.02 g/L | 2 g/L |
| Fe(NH4)citrate | BG11-Mix, 2 ml of a 3 g/L stock = 0.006 g/L | 1 g/L |
| Vitamin B12 | 1 ml of 0.02 g/L stock = 0.00002 g/L | 1 g/L |

Trace metal mix should be a nested stock added at 1 ml/L. The generated record
instead flattens H3BO3, MnCl2, ZnSO4, Na2MoO4, CuSO4, and Co(NO3)2 into the
final medium and appends the trace-stock "make up to 1000 ml" step as if it
were a final-medium step.

The DSMZ Medium 1593a PDF explicitly lists both Trace metal mix and BG11-Mix as
coming from medium 1592. MediaDive expands BG11-Mix to the three component rows
but does not preserve the stock as a named solution in the normalized parent.

## Completeness

- The generated record has no `references`, `source_data`, `target_organisms`,
  or `growth_metrics`. Empty organism and growth slots are acceptable for this
  DSMZ recipe; structured source provenance is missing.
- The pH 8.0 condition is represented.
- The BG11-Mix source stock boundary is missing, and the shared Trace metal mix
  stock is not linked structurally.
- No local raw DSMZ 1593a capture was found by the gitignore-independent search
  over `data/raw`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | BG11 stock additions were converted to raw `G_PER_L` values. | DSMZ 1593a lists 5 ml, 10 ml, 2 ml, and 1 ml stock additions; the generated record stores raw 5, 10, 2, and 1 values as final grams per liter for nitrate, mineral salts, BG11-Mix components, and vitamin B12. | `data/normalized_yaml/bacterial/cyanobacteria_medium_bg11_tes_buffered.yaml` and the MediaDive importer |
| major | Trace metal mix and BG11-Mix are flattened. | Source medium 1593a adds 1 ml/L Trace metal mix and 2 ml/L BG11-Mix from medium 1592; the generated record lists their constituents directly and carries the trace-stock make-up step at final-medium scope. | Normalized 1593a parent and MediaDive solution import logic |
| minor | Mg(SO4) x 7 H2O is ungrounded. | The generated row has no CHEBI or MediaIngredientMech term. | Normalized 1593a parent or MediaDive compound 2154 mapping |
| minor | NaNO3 still uses `mediaingredientmech_term`. | Sodium nitrate has a CHEBI term but retains `MediaIngredientMech:000171`. | Normalized 1593a parent |
| minor | Source provenance is free-text only. | The record has no structured DSMZ/MediaDive reference despite being imported from MediaDive 1593a. | Normalized 1593a parent |

## Recommended Edits

1. Preserve 2.3 g/L TES and pH 8.0.
2. Rebuild the BG11-derived mineral, BG11-Mix, NaNO3, and vitamin B12 rows as
   source stock additions or as correct final concentrations.
3. Link Trace metal mix and BG11-Mix to source-aligned SolutionRecipe records
   rather than flattening their ingredients.
4. Ground Mg(SO4) x 7 H2O, migrate the NaNO3 MediaIngredientMech link, and add
   structured MediaDive/DSMZ 1593a provenance.
5. Regenerate `data/merge_yaml/merged/cyanobacteria_medium_bg11_tes_buffered.yaml`
   after repairing the normalized input.

## Follow-up Checks

- Run schema, strict, reference, and term validation on the repaired 1593a
  normalized record and any touched stock solutions.
- Regenerate the merge and verify that TES remains 2.3 g/L and that nitrate is
  1.5 g/L or represented as 5 ml of 300 g/L stock.
- Verify BG11-Mix and Trace metal mix do not appear as unsupported top-level
  stock-strength ingredients.

## Additional Notes

- DSMZ 1593a is effectively BG11+ with TES and pH 8.0; the stock-repair work
  should stay aligned with the BG11+ and BG11- repairs to avoid three divergent
  definitions of the same BG11-Mix and Trace metal mix stocks.
