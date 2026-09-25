# YAML Record Review: Complete pleuropneumonia-like organism (PPLO) medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/complete_pleuropneumonia_like_organism_pplo_medium.yaml`
- Started UTC: 2026-09-22T11:22:00Z
- Finished UTC: 2026-09-22T11:24:12Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009427`
- Normalized source: `data/normalized_yaml/bacterial/complete_pleuropneumonia_like_organism_pplo_medium.yaml`
- Source identity: TOGO M2891, `Complete pleuropneumonia-like organism (PPLO) medium`
- Current generated merge: one source recipe, `complete_pleuropneumonia_like_organism_pplo_medium`

## Validation

- Open schema validation: pass.
- Strict validation: pass.
- Reference validation: pass with 0 checks.
- Term validation: pass.
- Embedded `curation_history`: not checked by the standalone history validator.

## Identity and Grounding

- TOGO M2891 lists one liter of PPLO medium and 5% CO2.
- The same source comment records cultivation at 37 C in 5% CO2 for approximately 48 h.
- A gitignore-independent search over `data` found no additional TOGO M2891 or `CultureMech:009427` YAML records.
- The normalized owner was repaired on September 10, 2026, but this August 6 generated record predates that repair.

## Evidence

- TOGO API checked: `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2891`.
- Local normalized owner checked: `data/normalized_yaml/bacterial/complete_pleuropneumonia_like_organism_pplo_medium.yaml`.

## Completeness

- The bacterial category, complex undefined type, and liquid physical state are appropriate.
- The record intentionally uses PPLO medium as an opaque base.
- The generated artifact is missing the repaired 37 C condition and the exact 5% CO2 atmosphere.

## Findings

1. `PPLO medium` is generated as `1 G_PER_L`, but TOGO encodes one liter of base medium; the repaired normalized owner now records `1000 ML_PER_L`.
2. `CO2` is generated with a default `VARIABLE` concentration, but TOGO explicitly lists 5% CO2; the repaired normalized owner now records `5 PERCENT_V_V`.
3. The generated record omits the source-supported 37 C cultivation condition and approximately 48 h incubation note that the repaired normalized owner preserves.

## Recommended Edits

1. Regenerate from `data/normalized_yaml/bacterial/complete_pleuropneumonia_like_organism_pplo_medium.yaml`.
2. Confirm the generated record keeps PPLO medium at `1000 ML_PER_L`, CO2 at `5 PERCENT_V_V`, and the 37 C condition.
3. Preserve the TOGO M2891 URL in a `references` entry after regeneration.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Re-query TOGO M2891 and verify that no numeric condition was lost from the repaired output.

## Additional Notes

- No source-catalogue duplicate or variant relationship was found.
- The direct normalized owner already contains the evidence-backed fix.
