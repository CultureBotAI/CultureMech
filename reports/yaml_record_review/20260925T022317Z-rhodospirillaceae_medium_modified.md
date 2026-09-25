# YAML Record Review: rhodospirillaceae_medium_modified

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rhodospirillaceae_medium_modified.yaml`
- Started UTC: 2026-09-25T02:23:16Z
- Finished UTC: 2026-09-25T02:23:25Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:004707` for KOMODO Medium 27 / `komodo.medium:27`, merged from KOMODO 27, DSMZ 27, DSMZ 26, KOMODO 26, and many KOMODO DSM 27 strain records.

## Validation

- Open schema validation: passed; exited 0 with no diagnostics.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

KOMODO 27 explicitly cites DSMZ Medium 27, and `data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml` is the corresponding direct `mediadive.medium:27` owner. An exact ignored-inclusive search for `komodo.medium:27`, `mediadive.medium:27`, and `DSMZ_Medium27.pdf` found the expected direct DSMZ, KOMODO, and DSMZ Medium 44 delegating records under the relevant data trees.

KOMODO 26 and DSMZ 26 are not source duplicates of Medium 27. Medium 26 is the acid Rhodospirillaceae recipe with pH 5.7 and 0.2 g/L yeast extract; Medium 27 has pH 6.8 and 0.3 g/L yeast extract.

## Evidence

The DSMZ 27 PDF and MediaDive 27 list a final recipe with 0.30 g yeast extract, 1 g disodium succinate, 0.50 g ammonium acetate, 5 ml 0.1% Fe(III) citrate solution, 0.50 g KH2PO4, 0.40 g MgSO4 x 7H2O, 0.40 g NaCl, 0.40 g NH4Cl, 0.05 g CaCl2 x 2H2O, 0.40 ml vitamin B12 stock, 1.00 ml Trace element solution SL-6, 0.30 g L-cysteine HCl, 0.50 ml 0.1% resazurin, and 1000 ml distilled water. SL-6 is a separate stock with seven salts and 1000 ml distilled water. DSMZ 27 also specifies pH 6.8, boiling under nitrogen, dispensing into 10 ml tubes under nitrogen, autoclaving at 121 C for 15 min, sterile-syringe handling, and light incubation with a tungsten lamp.

The maintained KOMODO 27 and direct DSMZ 27 owners already have the repaired 10-row final recipe, Fe(III) citrate, vitamin B12, SL-6, and resazurin stock solutions, final distilled water, and structured preparation steps. The generated target is stale: it still emits 19 flattened ingredients, uses 0.2 g/L yeast extract, leaves the Fe(III) citrate, vitamin B12, resazurin, and SL-6 stock components in the final recipe, omits distilled water, and omits all preparation steps.

## Completeness

The current generated record is missing all stock boundaries and final water from the repaired upstream owners. It also merges Medium 26 into Medium 27 rather than preserving acid Medium 26 as a separate pH/composition variant.

Empty optional literature and organism fields are not defects.

## Findings

- Major: `data/merge_yaml/merged/rhodospirillaceae_medium_modified.yaml` is stale relative to `data/normalized_yaml/bacterial/KOMODO_27_RHODOSPIRILLACEAE_medium_modified.yaml` and `data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml`. It drops the repaired stock topology and final water and restores the old flattened SL-6, vitamin B12, Fe(III) citrate, and resazurin representation.
- Major: the generated target retains 0.2 g/L yeast extract from acid DSMZ/KOMODO Medium 26, but DSMZ Medium 27 lists 0.3 g/L.
- Major: acid Medium 26 is falsely merged into the Medium 27 duplicate set. DSMZ/MediaDive 26 reports pH 5.7 and a 20 min autoclave under anoxic 100% N2 conditions, while DSMZ/MediaDive 27 reports pH 6.8 and a different 15 min nitrogen-bubbled preparation.
- Major: `data/merge_yaml/merged/rhodospirillaceae_medium_modified.yaml` omits the DSMZ 27 preparation steps now present in the maintained DSMZ and KOMODO 27 owners.

## Recommended Edits

- Remove `data/normalized_yaml/bacterial/KOMODO_26_ACID_RHODOSPIRILLACEAE_medium.yaml` and `data/normalized_yaml/bacterial/acid_rhodospirillaceae_medium.yaml` from the Medium 27 source-duplicate set; keep Medium 26 as a distinct acid variant.
- Regenerate `data/merge_yaml/merged` from the already-repaired Medium 27 owners so the generated target preserves final distilled water, four stock solutions, 0.3 g/L yeast extract, and the structured preparation steps.
- Confirm the KOMODO DSM 27 strain-specific records remain duplicates only where they do not introduce strain-specific modifications.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation for regenerated Medium 27 and Medium 26 records.
- Confirm regenerated Medium 27 has the 10 final ingredients and four stock solutions from the maintained DSMZ owner.
- Confirm acid Medium 26 is no longer listed in `synonyms` or `merged_from` for Medium 27.

## Additional Notes

The direct source-duplicate relationship between KOMODO 27 and DSMZ 27 is correct; the generated record has not caught up to that repaired owner pair.
