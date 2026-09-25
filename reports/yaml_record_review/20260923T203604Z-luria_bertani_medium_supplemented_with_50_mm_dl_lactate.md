# YAML Record Review: Luria-Bertani Medium Supplemented With 50 mM DL-Lactate

- Repository: CultureMech
- Record: `data/merge_yaml/merged/luria_bertani_medium_supplemented_with_50_mm_dl_lactate.yaml`
- Started UTC: `2026-09-23T20:35:07Z`
- Finished UTC: `2026-09-23T20:36:04Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:008836`
- `name`: `luria_bertani_medium_supplemented_with_50_mm_dl_lactate`
- `original_name`: `Luria-Bertani medium supplemented with 50 mM DL-lactate`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `TOGO:M2248`
- `merge_fingerprint`: `5bbcf12f9b37dcb97028e77831a620a733096876ebae9223864dec08bb049f67`
- `merged_from`: `luria_bertani_medium_supplemented_with_50_mm_dl_lactate`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/luria_bertani_medium_supplemented_with_50_mm_dl_lactate.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:008836`, `TOGO:M2248`, `M2248`, `luria_bertani_medium_supplemented_with_50_mm_dl_lactate`, and the merge fingerprint found the maintained TOGO M2248 owner and this generated record.
- TOGO M2248 identifies the source as `Luria-Bertani medium supplemented with 50 mM DL-lactate`.
- TOGO M2248 lists 50 mM DL-lactate, a 1 L Luria-Bertani base, NaOH solution, and a decomposed Luria-Bertani subcomponent with 1 L distilled water, 5 g yeast extract, 10 g NaCl, and 10 g tryptone.
- The TOGO source comments say the Luria-Bertani basal medium is adjusted to pH 7.5 with NaOH and supplemented with 50 mM DL-lactate.

## Evidence

- The generated `DL-lactate` row preserves the source value of 50 `MILLIMOLAR`.
- The source's 5 g yeast extract, 10 g NaCl, and 10 g tryptone rows are present near the bottom of the generated ingredient list.
- The generated record also adds inferred LB Miller rows of 5 g/L yeast extract, 10 g/L sodium chloride, and 10 g/L tryptone above the source rows.
- The source's 1 L distilled-water solvent row is emitted as 1 `G_PER_L`.
- The source pH 7.5 endpoint is not represented.

## Completeness

- The lactate supplement and three LB base constituents are present.
- The LB base constituents are duplicated.
- The NaOH pH adjuster is preserved only as an empty `Unknown solution` with variable concentration.
- The DL-lactate row is not ontology-grounded.
- The source organisms and temperatures from the TOGO comments are not represented as structured target or growth-condition metadata.
- The generated record has no structured `references`.

## Findings

1. The generated recipe duplicates the LB base.
   - Evidence: TOGO M2248 already provides 5 g yeast extract, 10 g NaCl, and 10 g tryptone under its `Luria-Bertani medium` subcomponent; the generated record also infers 5 g/L yeast extract, 10 g/L sodium chloride, and 10 g/L tryptone from the external Laboratory Notes page.
   - Impact: downstream consumers can interpret the generated recipe as containing twice the intended LB nutrient and salt amounts.

2. The pH 7.5 adjustment is incomplete.
   - Evidence: TOGO comments state that the basal medium is adjusted to pH 7.5 with NaOH, but the generated record has no `ph_value` and only an empty `Unknown solution` entry for NaOH.
   - Impact: the medium no longer carries its final pH and cannot specify the adjustment reagent usefully.

3. The source solvent row has the wrong dimension.
   - Evidence: TOGO lists 1 L distilled water in the LB subcomponent; the generated record stores `Distilled water` as 1 `G_PER_L`.
   - Impact: a final-volume row is represented as a mass concentration.

4. The DL-lactate supplement is not grounded.
   - Evidence: the distinctive `DL-lactate` row has role/property notes but no `term` or `mediaingredientmech_chebi_term`.
   - Impact: lactate-supplemented LB cannot be retrieved reliably by ChEBI or MediaIngredientMech identifiers.

## Recommended Edits

1. Remove the inferred Laboratory Notes LB rows when TOGO already supplies the LB base composition.
2. Preserve pH 7.5 as `ph_value` and replace the empty `Unknown solution` with a real NaOH pH-adjustment step.
3. Represent the 1 L distilled-water source row as final volume, not 1 `G_PER_L`.
4. Add a ChEBI grounding for DL-lactate.
5. Add structured references for TOGO M2248 and for any external source used to interpret the LB base.

## Follow-up Checks

- Re-fetch TOGO M2248 and confirm the regenerated record has one 10 g/L tryptone row, one 5 g/L yeast-extract row, one 10 g/L NaCl row, 50 mM DL-lactate, and pH 7.5.
- Re-run open schema, strict schema, reference, and term validation on the rebuilt record.
- Run an ignored-inclusive exact search for `TOGO:M2248` and `luria_bertani_medium_supplemented_with_50_mm_dl_lactate` to confirm no duplicate TOGO M2248 owner was introduced.

## Additional Notes

- Exact duplicate checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.
