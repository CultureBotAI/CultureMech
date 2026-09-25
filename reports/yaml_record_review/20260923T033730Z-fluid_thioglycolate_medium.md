# YAML Record Review: fluid_thioglycolate_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/fluid_thioglycolate_medium.yaml
- Started UTC: 2026-09-23T03:36:39Z
- Finished UTC: 2026-09-23T03:37:30Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:004176` / `fluid_thioglycolate_medium`, the KOMODO Medium 153 record enriched from DSMZ Medium 153.
- Cross-checked the generated record against the DSMZ Medium 153 PDF and the MediaDive REST payload for medium 153.
- Compared the generated merge with its normalized source at `data/normalized_yaml/bacterial/fluid_thioglycolate_medium.yaml`.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass; 0 total ERROR rows in `/private/tmp/fluid_thioglycolate_medium.strict.tsv`.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- The KOMODO-to-DSMZ identity is coherent: `komodo.medium:153`, the note that this is DSMZ Medium 153, and the ingredient set all map to DSMZ THIOGLYCOLATE MEDIUM (MERCK 108190).
- `Trypticase` is incorrectly grounded to `CHEBI:78018` / dodecylphosphocholine. Trypticase is a complex casein digest and should not use that small-molecule CHEBI term.
- `Trypticase` also retains a legacy `MediaIngredientMech:000263` mirror instead of an id-safe CHEBI mirror.
- Yeast extract is ungrounded; that is acceptable as a complex ingredient.
- The derived `Na2CO3` pH-adjuster row is grounded to sodium carbonate, but it is not a recipe-table ingredient in DSMZ 153.

## Evidence

- DSMZ 153 and MediaDive 153 both assert Trypticase 15 g/L, L-Cystine 0.5 g/L, Glucose 2 g/L, Yeast extract 5 g/L, NaCl 2.5 g/L, Na-thioglycolate 0.5 g/L, 0.5 ml/L of 0.1% Sodium resazurin, optional Agar 15 g/L for solid medium, and Distilled water 1 L.
- The generated record preserves those final ingredient amounts, including 0.0005 g/L Sodium resazurin and optional Agar 15 g/L.
- DSMZ and MediaDive include a preparation step that dissolves ingredients, sparges with 100% N2, adjusts pH to 7.1 with 5% Na2CO3 if necessary, dispenses under the same gas atmosphere, and autoclaves.
- The generated record has `ph_value: 7.1` and a variable Na2CO3 ingredient extracted from the note, but no `preparation_steps` entry.
- DSMZ marks agar as optional for solid medium; the generated record always materializes agar and sets `physical_state: SOLID_AGAR`, so it represents only the solid variant of an optional fluid/solid source.

## Completeness

- The source ingredient table is present except for Distilled water, which is intentionally not materialized.
- The source pH value is present.
- The DSMZ preparation step is absent.

## Findings

- Needs curation: Trypticase is wrongly grounded to dodecylphosphocholine and still carries a legacy MediaIngredientMech mirror.
- Needs curation: the DSMZ 153 preparation step is missing despite carrying essential anoxic sparging, pH adjustment, dispensing, and autoclave instructions.
- Needs curation: optional agar has been promoted into an unconditional `SOLID_AGAR` record; curation should either confirm this generated record intentionally models the solid variant or split a fluid record from the optional agar variant.
- Minor issue: Trypticase's BBL source attribute and Sodium resazurin's 0.1% w/v source attribute are not retained.
- Minor issue: the KOMODO import's first embedded curation-history timestamp is malformed as `2026-01-27T01:15:02.fZ`.

## Recommended Edits

- Remove the erroneous `CHEBI:78018` grounding from Trypticase and keep it ungrounded or map it to a complex-ingredient class if an exact Trypticase mapping exists.
- Add the DSMZ preparation step covering N2 sparging, optional Na2CO3 pH adjustment, anoxic dispensing, and autoclaving.
- Decide whether DSMZ 153 should be modeled as a broth recipe plus an agar variant or as the current solid agar recipe with the agar row explicitly marked optional.
- Preserve the BBL and 0.1% w/v source attributes in `preferred_term` or `notes`.

## Follow-up Checks

- After curation, rerun open-schema, strict, reference, and term validation on the generated KOMODO 153 YAML.
- Confirm no row maps Trypticase to `CHEBI:78018`.
- Confirm `ph_value: 7.1` and the 0.0005 g/L Sodium resazurin conversion are preserved.
- Confirm embedded curation-history timestamps are parseable after regeneration.

## Additional Notes

- No nested-stock or unit-conversion defect was found in the DSMZ 153 ingredient amounts.
