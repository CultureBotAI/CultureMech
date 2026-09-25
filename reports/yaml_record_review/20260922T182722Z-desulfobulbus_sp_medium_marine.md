# YAML Record Review: desulfobulbus_sp_medium_marine

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfobulbus_sp_medium_marine.yaml`
- Started UTC: 2026-09-22T18:27:22Z
- Finished UTC: 2026-09-22T18:27:22Z
- Verdict: needs curation

## Target

Generated specialized `desulfobulbus_sp_medium_marine` record for DSMZ Medium 195b.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The canonical record is grounded to MediaDive/DSMZ medium 195b, `DESULFOBULBUS SP. MEDIUM (MARINE)`.

The generated record merged 19 sources into this DSMZ 195b-labeled recipe, including `desulfobacter_sp_medium`, `desulfobulbus_sp_medium_freshwater`, `for_dsm_15576_and_dsm_16219`, `for_dsm_4661`, many `medium_195_modified_for_dsm_*` records, and `desulfobulbus_sp_medium_marine`.

An exact ignored-file search found no TOGO same-name duplicate for this record. TOGO M2530 in the local indexes is `Desulfovibrio Postgate Medium`, not this marine Desulfobulbus recipe.

The live DSMZ 195b recipe is defined, but this generated record also carries source names from bacterial variants in addition to the canonical specialized record.

## Evidence

MediaDive 195b describes a five-solution final medium: 952 ml Solution A, 30 ml Solution B, 10 ml Solution C, 1 ml Solution D, and 10 ml Solution E.

The generated basal rows match the contents of Solution A scaled by the 952 ml solution volume: Na2SO4, KH2PO4, NH4Cl, NaCl, MgCl2 x 6 H2O, KCl, CaCl2 x 2 H2O, and Sodium resazurin match the live 195b structure.

The generated record has no `solutions` array. Instead, Solution B Na2CO3 is present as the 50 g/L stock concentration, Solution C Na-propionate is present as the 150 g/L stock concentration, Solution E Na2S x 9 H2O is present as the 40 g/L stock concentration, and Selenite-tungstate, SL-10, and Wolin vitamin stock formulas are all flattened into top-level final-medium ingredients.

The preparation text from the live 195b source survived, including the 7.1-7.4 final pH, anaerobic gassing and autoclave conditions, filter-sterilized vitamin stock, ordered solution additions, optional sodium dithionite note, and transfer inoculum.

The SL-10 preparation step also survived but is detached from an SL-10 stock record.

## Completeness

The record preserves source pH and preparation prose, but it has lost the main Solution A-E mixture and the nested SL-10, Selenite-tungstate, and Wolin vitamin stock scopes.

Because the merge used a flattened fingerprint, the 19-source merge needs a source-level audit after repair. Strain-specific or DSM 195-derived variants can collapse to the same top-level ingredient fingerprint when all stock scopes are already flattened.

## Findings

- Major issue: the MediaDive/DSMZ 195b Solution A-E structure is absent.
- Major issue: Solution B, Solution C, and Solution E contents are flattened as final concentrations instead of represented as 30 ml, 10 ml, and 10 ml stock additions.
- Major issue: Selenite-tungstate, SL-10, and Wolin vitamin stock formulas are flattened into the top-level ingredient list.
- Major issue: the SL-10 preparation step is detached from the SL-10 formula it describes.
- Major issue: the 19-source merge was computed over a flattened, scope-losing representation and should be re-audited after structural repair.
- Minor issue: no water rows are retained for any of the nested stock solutions because the stock solutions themselves are absent.

## Recommended Edits

- Rebuild the normalized DSMZ 195b record from the MediaDive REST solution tree with an explicit final 952/30/10/1/10 ml Solution A-E mixture.
- Nest Selenite-tungstate, SL-10, and Wolin vitamin formulas under their own `solutions` blocks, preserving local water rows.
- Keep Na2CO3, Na-propionate, and Na2S x 9 H2O inside their Solution B, C, and E stocks instead of as final-medium ingredients.
- Attach the FeCl2/HCl dissolution step to Trace element solution SL-10.
- Recompute fingerprints only after solution scope is part of the structural comparison, then re-evaluate all 19 merged sources.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after restructuring the record.
- Confirm final concentrations for carbonate, propionate, and sulfide are derived from their stock addition volumes.
- Confirm DSMZ 194 freshwater and DSMZ 195b marine records do not collapse unless their scoped solution trees truly match.
- Confirm all `medium_195_modified_for_dsm_*` synonyms still belong in the canonical record after source-specific modifications are represented.

## Additional Notes

MediaDive REST medium 195b was reachable during review.
