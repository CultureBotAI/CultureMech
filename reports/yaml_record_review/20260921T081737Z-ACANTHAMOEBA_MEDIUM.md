# YAML Record Review: ACANTHAMOEBA MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml
- Started UTC: 2026-09-21T08:16:13Z
- Finished UTC: 2026-09-21T08:17:37Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml`.
- Stable identifier: `CultureMech:000970`.
- Source identity asserted by the record: DSMZ Medium 1500, `ACANTHAMOEBA MEDIUM`, via MediaDive `mediadive.medium:1500`.
- The generated record was merged from one owner, `acanthamoeba_medium`, on fingerprint `7fb543da8fea7c0d4a9c959b6fdf75e9129da5d8d128f2d113b8ea2c8b77fb4c`.
- Current authoritative owner: `data/normalized_yaml/bacterial/acanthamoeba_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- The record identity is coherent: MediaDive `1500` and the linked DSMZ `DSMZ_Medium1500.pdf` both identify the source as `ACANTHAMOEBA MEDIUM`.
- A gitignore-independent exact search for `mediadive.medium:1500`, `DSMZ Medium 1500`, and `DSMZ_Medium1500.pdf` found only this normalized owner, its generated merge, and expected source-index rows.
- The generated merge is complete relative to its current normalized owner; it differs only by merge metadata.
- The exact same DSMZ PDF contains three different formula contexts: Trypticase Soy Broth with Yeast Extract for maintenance, Peptone-yeast-glucose medium as an alternative maintenance medium, and Sucrose-Phosphate-Glutamate buffer for freezer storage.
- The current record flattens all three contexts into one recipe and loses the `OR` relationship between TSY and PYG.

## Evidence

- DSMZ specifies TSY as `Trypticase Soy Broth 30 g`, `Yeast extract 10 g`, and `Distilled water 1000 ml`, adjusted to pH 7.3 and autoclaved at 121 C.
- DSMZ separately specifies PYG with proteose peptone, glucose, yeast extract, sodium citrate dihydrate, MgSO4.7H2O, Na2HPO4.7H2O, KH2PO4, Fe(NH4)2(SO4)2.6H2O, and water, adjusted to pH 6.5 and autoclaved at 110 C or filter-sterilized.
- DSMZ separately specifies Sucrose-Phosphate-Glutamate buffer with sucrose, KH2PO4, Na2HPO4.2H2O, glutamic acid, and water for storage of bacteria released from host cells at -80 C.
- The target sums yeast extract across TSY and PYG to `12.0 G_PER_L` and KH2PO4 across PYG and SPG to `0.8600000000000001 G_PER_L`, although those ingredients belong to separate alternative media or storage buffer sections.
- The target replaces DSMZ's 30 g/L Trypticase Soy Broth line with researched TSB/TSA subcomponents, including a 15 g/L agar row that is explicitly for TSA only and not Trypticase Soy Broth.

## Completeness

- The generated record is complete relative to `data/normalized_yaml/bacterial/acanthamoeba_medium.yaml`.
- It is not complete or internally coherent relative to DSMZ because alternative formulas and the storage buffer need separate recipe or subrecipe representation.
- No distilled water rows are retained for any of the three DSMZ formula contexts.
- The pH value is `6.5`, which applies only to the PYG alternative; the TSY alternative's pH 7.3 is present only in a preparation-step sentence.

## Findings

- BLOCKER: independent DSMZ formulas have been flattened into a single additive ingredient list. TSY, PYG, and the SPG storage buffer should not be summed into one final medium.
- BLOCKER: duplicate cleanup merged ingredient rows across distinct DSMZ sections, producing unsupported concentrations such as `12.0 G_PER_L` yeast extract and `0.8600000000000001 G_PER_L` KH2PO4.
- BLOCKER: agar is present as a final ingredient even though DSMZ calls for Trypticase Soy Broth, not Trypticase Soy Agar; the row is copied from a generic researched TSA constituent expansion and contradicts the source recipe.
- MAJOR: the TSB commercial-product expansion is grounded to a Wikipedia URL under `supplier_catalog.product_url`, not to a DSMZ instruction or a supplier product specification.
- MAJOR: the Sucrose-Phosphate-Glutamate storage buffer has been imported as though it were part of ACANTHAMOEBA MEDIUM.
- MINOR: pH and sterilization are attached to flattened steps, so only one structured `ph_value` can survive even though TSY and PYG have different pH targets.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/acanthamoeba_medium.yaml` from DSMZ Medium 1500 as separate TSY, PYG, and Sucrose-Phosphate-Glutamate buffer records or as structured alternative formulas if the schema supports them.
- Keep `Trypticase Soy Broth 30 g/L` as the sourced DSMZ ingredient unless a vendor specification is cited and the commercial expansion is explicitly modeled as an expansion of that one row.
- Remove agar from the liquid TSY recipe.
- Stop summing repeated ingredient names across the TSY, PYG, and storage-buffer sections.
- Preserve the distinct TSY pH 7.3 / 121 C treatment and PYG pH 6.5 / 110 C-or-filter treatment.
- Regenerate `data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml` after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch `DSMZ_Medium1500.pdf` and verify that each ingredient is assigned to exactly one of TSY, PYG, or Sucrose-Phosphate-Glutamate buffer.
- Re-run an exact ignored-file-inclusive search for `mediadive.medium:1500`, `DSMZ Medium 1500`, and `DSMZ_Medium1500.pdf` to confirm no stale flattened DSMZ 1500 record remains.

## Additional Notes

- The long maintenance and passage instructions imported from DSMZ are narrative culture-handling guidance, not all media-preparation steps. They should likely be retained as notes or protocol text instead of 12 generic `preparation_steps`.
