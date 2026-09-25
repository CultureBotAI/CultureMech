# YAML Record Review: Luria Bertani (LB) Medium (Buffered MOPS)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/luria_bertani_lb_medium_buffered_mops.yaml`
- Started UTC: `2026-09-23T20:33:55Z`
- Finished UTC: `2026-09-23T20:35:06Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:009075`
- `name`: `luria_bertani_lb_medium_buffered_mops`
- `original_name`: `Luria Bertani (LB) medium (buffered MOPS)`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `TOGO:M2501`
- `merge_fingerprint`: `51250b79535f0fac2abd7dae19b21b39e2d8df69e129e506364b0ba0854ef17f`
- `merged_from`: `luria_bertani_lb_medium_buffered_mops`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/luria_bertani_lb_medium_buffered_mops.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:009075`, `TOGO:M2501`, `M2501`, `luria_bertani_lb_medium_buffered_mops`, and the merge fingerprint found the maintained TOGO M2501 owner and this generated record.
- TOGO M2501 identifies the source as `Luria Bertani (LB) medium (buffered MOPS)`.
- TOGO M2501 lists 50 mM `3-[N-morpho- lino] propanesulfonic acid (MOPS)`, 1 L `Luria Bertani (LB) medium`, and pH 6.8.
- The `kg_microbe_match: mediadive.medium:74` field resolves to DSMZ Medium 74, `THERMUS THERMOPHILUS MEDIUM`, not LB or MOPS-buffered LB.
- An ignored-inclusive exact search for `kg_microbe_match: mediadive.medium:74` shows the same automated match on many unrelated records, so it is not an identity signal for this target.

## Evidence

- The generated MOPS row preserves the source value as 50 `MILLIMOLAR`.
- The generated record expands the 1 L `Luria Bertani (LB) medium` source component into 10 g/L tryptone, 5 g/L yeast extract, and 10 g/L sodium chloride.
- The TOGO source pH 6.8 is absent from the generated record.
- The MOPS ingredient has no ChEBI or MediaIngredientMech grounding.
- The generated record cites a Laboratory Notes recipe URL for the LB expansion while describing it as product-specification research.

## Completeness

- The MOPS buffer row and inferred LB Miller base are present.
- The pH value that makes the MOPS-buffered variant distinct is missing.
- The TOGO source has no explicit source publication or original media URL.
- The generated record has no structured `references`.
- The generated record has no preparation steps for making buffered LB or adjusting to pH 6.8.

## Findings

1. The pH 6.8 specification was dropped.
   - Evidence: TOGO M2501 has `ph: "6.8"` and its comment says MOPS buffered LB to pH 6.8; the generated record has no `ph_value` and no preparation step mentioning pH.
   - Impact: the generated recipe loses the pH condition that defines why MOPS is added.

2. The KG-Microbe match points to an unrelated DSMZ recipe.
   - Evidence: the generated `kg_microbe_match` is `mediadive.medium:74`, whose MediaDive REST record is `THERMUS THERMOPHILUS MEDIUM` with yeast extract, Proteose peptone no. 3, and NaCl.
   - Impact: downstream identity reconciliation can connect MOPS-buffered LB to a different DSMZ medium.

3. The LB base expansion is weakly sourced.
   - Evidence: TOGO represents the base as 1 L prepared LB; the generated record expands it to Miller-style tryptone, yeast extract, and sodium chloride via a Laboratory Notes recipe page while claiming product-specification provenance.
   - Impact: the final base may be plausible, but the expanded composition is not supported by a source-quality product specification or a curated LB parent link.

4. MOPS is not ontology-grounded.
   - Evidence: the 50 mM MOPS row has source role and property notes but no `term` or `mediaingredientmech_chebi_term`.
   - Impact: the distinctive buffer for this medium cannot be queried by ChEBI or MediaIngredientMech ID.

## Recommended Edits

1. Preserve TOGO M2501 pH 6.8 as `ph_value` and as a pH-adjustment step if preparation logic supports it.
2. Remove or recompute `kg_microbe_match: mediadive.medium:74`; DSMZ Medium 74 is unrelated to this medium.
3. Ground MOPS to a ChEBI term and refresh the MediaIngredientMech grounding if available.
4. Replace the Laboratory Notes LB expansion with a curated LB parent record or stable LB Miller product specification.
5. Add structured references for TOGO M2501 and for the source used to decompose the prepared LB component.

## Follow-up Checks

- Re-fetch TOGO M2501 and confirm regenerated output keeps 50 mM MOPS and pH 6.8.
- Re-run open schema, strict schema, reference, and term validation on the rebuilt record.
- Run an ignored-inclusive exact search for `kg_microbe_match: mediadive.medium:74` after KG-Microbe reconciliation to confirm it no longer appears on unrelated LB-style records.

## Additional Notes

- Exact duplicate and KG-Microbe match checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.
