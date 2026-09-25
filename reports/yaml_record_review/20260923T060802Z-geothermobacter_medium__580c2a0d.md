# YAML Record Review: geothermobacter_medium__580c2a0d

- Repository: CultureMech
- Record: data/merge_yaml/merged/geothermobacter_medium__580c2a0d.yaml
- Started UTC: 2026-09-23T06:06:37Z
- Finished UTC: 2026-09-23T06:08:02Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:006942` merges the KOMODO 981 and DSMZ/MediaDive 981 imports for DSMZ 981, `GEOTHERMOBACTER MEDIUM`.

The merge combines `data/normalized_yaml/bacterial/KOMODO_981_GEOTHERMOBACTER_medium.yaml` with parent `data/normalized_yaml/bacterial/geothermobacter_medium.yaml`. An ignored-file-inclusive exact search for `komodo.medium:981`, `mediadive.medium:981`, and `KOMODO_981_GEOTHERMOBACTER` found those two maintained inputs, generated `data/merge_yaml/merged/geothermobacter_medium__580c2a0d.yaml`, and source indexes.

## Validation

`linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/geothermobacter_medium__580c2a0d.yaml` passed.

`scripts/validate_strict.py data/merge_yaml/merged/geothermobacter_medium__580c2a0d.yaml --workers 1 --quiet` exited 0; `/private/tmp/geothermobacter_medium_580c2a0d.strict.tsv` contained only the header row.

`linkml-reference-validator validate data data/merge_yaml/merged/geothermobacter_medium__580c2a0d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` passed with 0 checks.

`linkml-term-validator validate-data data/merge_yaml/merged/geothermobacter_medium__580c2a0d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `komodo.medium:981` row correctly points at DSMZ Medium 981, and the merge's `SOURCE_DUPLICATE` relationship to `mediadive.medium:981` is justified because both normalized parents have the same ingredient and concentration signature.

The record denotes DSMZ 981, not the separate JCM 1192 Geothermobacter recipe reviewed in `geothermobacter_medium__23e4cbc2`.

Most basal ingredient groundings match the DSMZ strings. `NiCl2 x 6 H2O` from Trace element solution SL-10 is grounded to anhydrous nickel dichloride, and `KNO3` still has a legacy `mediaingredientmech_term: MediaIngredientMech:000170` alongside its CHEBI grounding.

## Evidence

The DSMZ Medium 981 PDF lists NaCl, MgCl2 x 6H2O, MgSO4 x 7H2O, CaCl2 x 2H2O, KCl, KH2PO4, ammonium sulfate, NaBr, SrCl2 x 6H2O, KNO3, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, Na2CO3, yeast extract, DL-malic acid, 1 ml Wolin's vitamin solution (10x), L-cysteine HCl x H2O, and 1000 ml distilled water.

The same DSMZ PDF defines each 1 L stock: Trace element solution SL-10 from medium 320, Selenite-tungstate solution from medium 385, and Wolin's vitamin solution (10x) from medium 120. MediaDive 981 preserves those three as separate solution recipes with 1 ml additions into `Main sol. 981`.

The generated merge preserves the main DSMZ anoxic preparation instruction and pH 6.2, and it preserves the Trace element solution SL-10 instruction to dissolve FeCl2 in HCl before making up to 1000 ml.

## Completeness

The main 1000 ml distilled-water row is absent.

Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x) are absent as 1 ml solution additions. Their internal stock rows are flattened at stock strength into final-medium ingredients.

The 990 ml water in Trace element solution SL-10 and the 1000 ml waters in Selenite-tungstate solution and Wolin's vitamin solution (10x) are absent.

Empty growth-evidence, variant, discussion, and publication slots are acceptable for this imported DSMZ recipe.

## Findings

- Major: The 1 ml Trace element solution SL-10 addition was flattened at 1 L stock strength; generated final HCl 2.5 g/L, FeCl2 x 4 H2O 1.5 g/L, ZnCl2 0.07 g/L, and the other trace rows are about 1000-fold too high.
- Major: The 1 ml Selenite-tungstate solution addition was flattened at 1 L stock strength, adding unsupported final NaOH 0.5 g/L, Na2SeO3 x 5H2O 0.003 g/L, and Na2WO4 x 2H2O 0.004 g/L rows.
- Major: The 1 ml Wolin's vitamin solution (10x) addition was flattened at 1 L stock strength, so each vitamin row is about 1000-fold too high for the final medium.
- Major: DSMZ water rows are dropped from the main medium and from all three stock solutions, erasing the stock boundaries needed to interpret the concentrations.
- Major: The KOMODO source note says `Aerobic: Yes`, but DSMZ 981 describes anoxic sparging, anoxic Hungate-type tubes or serum vials, and sterile anoxic stock additions.
- Minor: `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride.
- Minor: `KNO3` still has the stale legacy `MediaIngredientMech:000170` link.
- Minor: The KOMODO import contributes a malformed embedded curation timestamp, `2026-01-27T01:15:03.fZ`.

## Recommended Edits

- Preserve Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x) as 1 ml stock additions in `data/normalized_yaml/bacterial/geothermobacter_medium.yaml`.
- Keep the three 1 L DSMZ stock recipes as separate subrecipes, or compute documented final concentrations from the 1 ml additions while retaining the source stock boundary.
- Preserve the 1000 ml main distilled-water row and the stock-solution water rows as formulation context.
- Remove or correct the KOMODO `Aerobic: Yes` note when linking KOMODO 981 to DSMZ 981.
- Re-ground hydrated nickel chloride and remove the stale KNO3 legacy MediaIngredientMech link.
- Normalize the malformed KOMODO curation timestamp only through a guarded curation-history cleanup.

## Follow-up Checks

- Regenerate the merged record and confirm there are no direct final HCl, FeCl2, SL-10 trace-metal, selenite-tungstate, or Wolin vitamin rows at stock strength.
- Confirm the regenerated recipe keeps exactly three 1 ml stock-solution additions plus the DSMZ anoxic preparation instruction.
- Re-run LinkML, strict, reference, and term validation on the regenerated generated YAML.
- Re-run an ignored-file-inclusive exact search for `komodo.medium:981` and `mediadive.medium:981` to confirm only the maintained KOMODO and DSMZ source rows feed the regenerated merge.

## Additional Notes

The exact local source search used `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged`, so ignored generated records and index files were included.
