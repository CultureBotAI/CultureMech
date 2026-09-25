# YAML Record Review: BYG Medium (for Acidiphilium multivorum)

- Repository: CultureMech
- Record: data/merge_yaml/merged/byg_medium_for_acidiphilium_multivorum.yaml
- Started UTC: 2026-09-22T01:26:09Z
- Finished UTC: 2026-09-22T01:27:20Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:008199`, `byg_medium_for_acidiphilium_multivorum`, `BYG Medium (for Acidiphilium multivorum)`.
- Merge lineage: one source recipe on fingerprint `f08bb61117aca48b617fcfe2e72a65e240f6dc8a01df8487915ce0dfef4140a7`.
- Authoritative owner: `data/normalized_yaml/bacterial/byg_medium_for_acidiphilium_multivorum.yaml`.
- Claimed source identity: TOGO Medium `M1643` over NBRC medium `846`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The target identity is correct: TOGO `M1643` and NBRC `846` are both `BYG Medium (for Acidiphilium multivorum)`.
- The active normalized owner and generated merge differ only in the distilled-water value: the owner has `500.0 G_PER_L` with `Collapsed 2 identical duplicates: 500.0, 500.0`, while the generated merge is stale and still carries `1000.0 G_PER_L` with `Merged 2 duplicates: 500.0, 500.0`.
- `MgSO4.7H2O`, `KH2PO4`, `KCl`, ammonium sulfate, calcium nitrate tetrahydrate, sulfuric acid, glucose, and water are grounded to source-compatible ChEBI identities.
- `Agar (if needed)` is ungrounded even though the source row is an exact agar ingredient in Solution B.

## Evidence

- Live TOGO `M1643` and NBRC medium `846` were checked and agree on the formulation and source identity.
- The source defines the medium as 500 ml Solution A plus 500 ml Solution B.
- Solution A contains 500 ml distilled water, 0.5 g `MgSO4.7H2O`, 0.1 g yeast extract, 0.5 g `KH2PO4`, 0.1 g `KCl`, 2 g `(NH4)2SO4`, and 0.01 g `Ca(NO3)2.4H2O`; the pH is adjusted to 3.5 with 1 N `H2SO4`.
- Solution B contains 500 ml distilled water, 1 g glucose, and 20 g agar if needed.
- The NBRC/TOGO comment says the agar solid BYG medium contains 2% agar and that Solutions A and B are autoclaved separately and combined before solidification at 50-60 C to avoid agar and glucose hydrolysis during low-pH autoclaving.

## Completeness

- The generated record retains all source-listed chemicals somewhere in the recipe, but the top-level recipe, solution structure, and preparation semantics are incomplete.
- The Solution A/Solution B boundaries are consequential because the source autoclaves them separately and combines them after sterilization.
- The record has no structured TOGO or NBRC `references` entry even though the source metadata are known.

## Findings

- The generated merge has empty `Solution A*` and `Solution B**` stubs with `500 G_PER_L` concentrations and `Unknown solution` names; their member ingredients are flattened into top-level final-ingredient rows.
- Distilled water is represented as one top-level `1000.0 G_PER_L` row, while the repaired owner still represents it as one top-level `500.0 G_PER_L` duplicate-collapse artifact; the source instead has separate 500 ml water rows inside Solution A and Solution B.
- The 1 N sulfuric-acid pH adjustment is modeled as a variable final ingredient, but the source uses sulfuric acid only to adjust Solution A to pH 3.5.
- The final generated record is missing the pH 3.5 condition and the instruction to autoclave Solutions A and B separately, then combine them before solidification at 50-60 C.
- Optional agar is modeled as an unconditional 20 g/L ingredient and the generated record is classified as `SOLID_AGAR`; the source has an `Agar (if needed)` row, so the broth/base record versus agar variant boundary still needs an explicit modeling decision.

## Recommended Edits

- Curate the authoritative normalized owner, not `data/merge_yaml/merged/byg_medium_for_acidiphilium_multivorum.yaml`.
- Rebuild Solution A and Solution B as actual stock/subrecipe nodes with their NBRC volumes and member ingredients instead of final top-level rows.
- Move sulfuric acid to a pH-adjustment/preparation role for Solution A and add the pH 3.5 target.
- Add the NBRC preparation note for separate autoclaving and 50-60 C combination.
- Ground agar to the exact compatible ontology term and decide whether `Agar (if needed)` belongs on this recipe, a separate solid variant, or an optional-ingredient flag.
- Add structured TOGO `M1643` and NBRC `846` references so the free-text `notes` field is no longer the only provenance path.
- Regenerate the merge after the normalized owner is corrected and verify that the fingerprint no longer yields flattened Solution A/B ingredients.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized owner.
- Re-run the merge builder and compare the regenerated merge against TOGO/NBRC to ensure the two 500 ml water rows are scoped to their respective solutions.
- Search generated pages for this ID after regeneration to ensure pH 3.5, the separate-autoclave instruction, and the optional agar semantics render correctly.

## Additional Notes

- A gitignore-independent search for `CultureMech:008199`, `TOGO:M1643`, `NBRC_M846`, `byg_medium_for_acidiphilium_multivorum`, and the merge fingerprint across normalized YAML, generated merged YAML, registries, reports, and import reports found only the expected active owner, generated merge, registry/catalog rows, import rows, and stale archive references to the old TOGO import path.
- The active normalized owner was already repaired by `repair_merged_duplicates.py` on 2026-09-02 for the generated 1000 g/L water summation, but the more consequential lost Solution A/Solution B structure remains.
