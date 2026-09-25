# YAML Record Review: COLUMBIA-GLUCOSE-CYSTEINE-AGAR

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_glucose_cysteine_agar.yaml`
- Started UTC: 2026-09-22T11:15:40Z
- Finished UTC: 2026-09-22T11:17:42Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:001536`
- Normalized source: `data/normalized_yaml/bacterial/columbia_glucose_cysteine_agar.yaml`
- Source identity: DSMZ Medium 429c, `COLUMBIA-GLUCOSE-CYSTEINE-AGAR`
- Current generated merge: one source recipe, `columbia_glucose_cysteine_agar`

## Validation

- Open schema validation: pass.
- Strict validation: pass.
- Reference validation: pass with 0 checks.
- Term validation: pass.
- Embedded `curation_history`: not checked by the standalone history validator.

## Identity and Grounding

- DSMZ Medium 429c specifies autoclaved Columbia agar base with 4% horse or sheep blood, followed after cooling by 1% glucose and 0.1% cysteine.
- DSMZ 429c only mentions liquid media 220 or 215 as freeze-dried ampoule rehydration media.
- The generated record treats the DSMZ 220 tryptone-soya agar formula and an unsupported DSMZ 215 BHI expansion as peer ingredients of DSMZ 429c.
- A gitignore-independent search over `data` found KOMODO 429c source records merged into the broad `columbia_blood_agar__e1a4386f.yaml` record instead of this DSMZ 429c record.

## Evidence

- DSMZ source checked: `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium429c.pdf`.
- Local normalized owner checked: `data/normalized_yaml/bacterial/columbia_glucose_cysteine_agar.yaml`.
- Local generated KOMODO merge checked: `data/merge_yaml/merged/columbia_blood_agar__e1a4386f.yaml`.

## Completeness

- The bacterial category, complex undefined type, and solid agar state are appropriate.
- Glucose at `10 G_PER_L` and cysteine at `1 G_PER_L` match DSMZ's 1% and 0.1% additions if interpreted as weight-per-volume stock additions to 1 L final medium.
- The record needs Columbia agar base, 4% blood, glucose, and cysteine only.

## Findings

1. `Casein peptone`, `Soy peptone`, `NaCl`, and `Agar` come from the DSMZ 220 rehydration medium, not from DSMZ 429c.
2. `Calf brains`, `Beef heart`, `Proteose peptone`, `Dextrose`, `Sodium chloride`, and `Disodium phosphate` are an unsupported expansion of BHI for the DSMZ 215 rehydration option.
3. `Columbia agar base` is recorded as `1000 G_PER_L`, converting an opaque base solution volume into an impossible kilogram-per-liter dry mass.
4. `Horse blood` is recorded as `40 G_PER_L`; the DSMZ instruction supports 4% horse or sheep blood.
5. KOMODO 429c source records are currently merged under broad Columbia blood agar output, so DSMZ 429c is missing its KOMODO source duplicate and sheep-blood variant context.

## Recommended Edits

1. Repair `data/normalized_yaml/bacterial/columbia_glucose_cysteine_agar.yaml` by retaining only Columbia agar base, blood at 4%, glucose at 1%, and cysteine at 0.1%.
2. Remove the DSMZ 220 and DSMZ 215 rehydration-media ingredients and all BHI expansion metadata.
3. Record blood as a percentage supplement and preserve DSMZ's horse-or-sheep alternative without converting it to `40 G_PER_L`.
4. Rebuild the 429c source graph so KOMODO 429c is a source duplicate of DSMZ 429c, while the KOMODO sheep-blood replacement is modeled as a variant rather than as Columbia blood agar.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the repaired generated record.
- Confirm the regenerated DSMZ 429c record no longer contains `Casein peptone`, `Soy peptone`, `Calf brains`, `Beef heart`, or BHI supplier metadata.
- Confirm that broad `columbia_blood_agar__e1a4386f.yaml` no longer absorbs the KOMODO 429c records.

## Additional Notes

- No schema-level defects were found.
- DSMZ 429c has no source-catalogue duplicate in the generated output; its one-source merge is stale relative to the KOMODO source records already present elsewhere in the repository.
