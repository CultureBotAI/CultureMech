# YAML Record Review: PFENNIG'S MEDIUM I WITH YEAST EXTRACT

- Repository: CultureMech
- Record: data/merge_yaml/merged/pfennigs_medium_i_with_yeast_extract.yaml
- Started UTC: 2026-09-24T20:53:57Z
- Finished UTC: 2026-09-24T20:53:57Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pfennigs_medium_i_with_yeast_extract.yaml`, the merged record for DSMZ medium 39 / PFENNIG'S MEDIUM I WITH YEAST EXTRACT.

The merged record is canonicalized to the bacterial KOMODO import `komodo.medium:39`, but it also absorbed a fungal direct-DSMZ import for the same DSMZ medium 39 source.

## Validation

- LinkML open validation: passed; no issues found.
- Strict schema validation: passed; `/private/tmp/pfennigs_medium_i_with_yeast_extract.strict.tsv` has one header row and zero error rows.
- Reference validation: passed; 1 file validated, 0 checks configured.
- Term validation: passed.
- Embedded curation history validation: Not checked; the available `just validate-history` target validates standalone `history/` records rather than `MediaRecipe.curation_history` blocks inside merged YAML.

## Identity and Grounding

The underlying medium identity is DSMZ medium 39. The direct DSMZ PDF defines it as DSMZ medium 28 plus 0.05% yeast extract, and the MediaDive REST record converts that supplement to 0.5 g/L.

The merged record has ambiguous source ownership. It lists `pfennigs_medium_i_with_yeast_extract` twice in `merged_from` because a bacterial KOMODO normalized source and a fungal direct-DSMZ normalized source share the same basename. The merged output consequently carries both `bacterial` and `fungal` categories while preserving only the KOMODO medium term.

The ingredient groundings again sit in the wrong scope: DSMZ 39 inherits the named-solution hierarchy of DSMZ medium 28, but the target flattens those stock-solution concentrations into final ingredients.

## Evidence

- Fetched the DSMZ Medium 39 PDF and confirmed its complete formula is "To medium 28 add 0.05% yeast extract."
- Fetched MediaDive medium 39 and confirmed it represents the formula as `Main sol. 28` plus 0.5 g/L yeast extract.
- Inspected `data/normalized_yaml/bacterial/pfennigs_medium_i_with_yeast_extract.yaml` and `data/normalized_yaml/fungal/pfennigs_medium_i_with_yeast_extract.yaml`; both describe the same DSMZ medium 39-derived formula with the same flattened concentrations.
- Compared the inherited DSMZ 28 stock structure against the target's flat ingredient array.

## Completeness

The target captures the DSMZ 39 yeast-extract supplement and several inherited DSMZ 28 preparation sentences. The target does not preserve the source recipe hierarchy from DSMZ 28, and it does not keep the direct DSMZ source ID as a distinct merged source identity.

Because the record is flattened, the source's Solution A water, bicarbonate stock water, resazurin stock water, heterotrophic salts stock water, vitamin B12 stock water, and sulfide stock water are all lost. Trace element solution SL-12 B is not represented as a stock addition under Pfennig's heterotrophic salts solution.

## Findings

- DSMZ medium 39 is a derivative of DSMZ medium 28, but the target stores stock concentrations from medium 28 as top-level final concentrations.
- Yeast extract from Solution A and the 0.5 g/L DSMZ 39 supplement were summed into one `1.043478 G_PER_L` row even though one amount belongs to Solution A and the other is the top-level DSMZ 39 addition.
- The 1.5% sulfide stock and 3% neutralized sulfide feed were summed into one `44.8148 G_PER_L` Na2S x 9 H2O row even though they are independent preparations.
- Trace element solution SL-12 B is absent as a nested stock addition.
- `merged_from` repeats the same basename twice and hides the fact that two different normalized files, one under `bacterial/` and one under `fungal/`, were collapsed.
- The first `curation_history` timestamp is malformed: `2026-01-27T01:15:02.fZ`.
- `Pyruvic acid sodium salt` still carries a legacy `mediaingredientmech_term` block instead of a CHEBI-keyed `mediaingredientmech_chebi_term`.

## Recommended Edits

- Represent DSMZ medium 39 as DSMZ medium 28 plus a 0.5 g/L yeast-extract supplement.
- Preserve DSMZ medium 28's nested named solutions instead of flattening their stock concentrations into DSMZ 39.
- Keep the Solution A yeast extract and the extra DSMZ 39 yeast extract in their correct scopes instead of summing them.
- Restore Trace element solution SL-12 B as a stock addition under Pfennig's heterotrophic salts solution.
- Resolve the bacterial/fungal duplicate source ownership so the merged record has unambiguous provenance and category assignment.
- Repair the malformed KOMODO curation timestamp.
- Replace the legacy `mediaingredientmech_term` on `Pyruvic acid sodium salt` with a CHEBI-keyed `mediaingredientmech_chebi_term` for `CHEBI:50144`.

## Follow-up Checks

- Re-run LinkML open validation, strict validation, reference validation, and term validation on the regenerated DSMZ 39 merged record.
- Verify the top-level DSMZ 39 addition is only 0.5 g/L yeast extract above medium 28.
- Confirm `merged_from` distinguishes any retained KOMODO and direct DSMZ sources by full normalized path or no longer needs both category-specific source files.
- Confirm no stock-only concentration from DSMZ medium 28 is exposed as a final top-level concentration.

## Additional Notes

Empty optional fields were not treated as defects. The review used DSMZ Medium 28 only because DSMZ Medium 39 is defined as a yeast-extract addition to medium 28.
