# YAML Record Review: HALF STRENGTH BACTO MARINE BROTH with 50% Seawater

- Repository: CultureMech
- Record: data/merge_yaml/merged/half_strength_bacto_marine_broth_with_50_seawater.yaml
- Started UTC: 2026-09-23T08:53:29Z
- Finished UTC: 2026-09-23T08:54:52Z
- Verdict: needs curation

## Target

- Reviewed generated YAML for `HALF STRENGTH BACTO MARINE BROTH with 50% Seawater`.
- Stable ID: `CultureMech:015362`.
- Primary source in generated record: DSMZ/MediaDive `mediadive.medium:514g`.
- Merge fingerprint: `0afc0a1f985a9b7ccbbb677c2b0e5cce0a2d1eee7589d96114d6dd94ad9ec402`.

## Validation

- LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`: pass.
- Strict validation with `scripts/validate_strict.py`: pass, 0 error rows in `/private/tmp/half_strength_bacto_marine_broth_with_50_seawater.strict.tsv`.
- LinkML reference validation: pass, 0 checked references.
- LinkML term validation with `conf/oak_config.yaml`: pass.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The generated record is rooted in DSMZ/MediaDive medium `514g`.
- An exact `rg --no-ignore --hidden` search for `mediadive.medium:514g` and `DSMZ_Medium514g.pdf` found only the expected normalized DSMZ 514g source, generated output, and index entries under `data/merge_yaml` and `data/normalized_yaml`; no same-source duplicate was found in those trees.
- The generated output also merges 156 additional sources, mostly KOMODO DSMZ 514 variants, into the DSMZ 514g recipe.

## Evidence

- The DSMZ 514g PDF lists half-strength Bacto Marine Broth with 500 ml seawater or Biomaris and 500 ml distilled water, pH 7.6 plus or minus 0.2 at 25 C, and optional solidification with 15 g/L agar.
- The MediaDive REST record for `514g` carries the same half-strength component values, 500 ml `Sea water`, 500 ml distilled water, pH 7.6, and optional agar.
- The generated record preserves the half-strength salt and nutrient masses, the pH, and the agar note, but imports 500 ml seawater as `Sea water` 500 `G_PER_L`.
- The merged `bacto_marine_broth_difco_2216` KOMODO source is labeled as KOMODO 514 / DSMZ 514, but its normalized composition has the same half-strength 514g values; current DSMZ/MediaDive 514 is full-strength Bacto Marine Broth with 5 g/L Bacto peptone, 1 g/L yeast extract, 19.45 g/L NaCl, 5.9 g/L MgCl2, and other salts at twice the 514g amounts.

## Completeness

- DSMZ 514g has no target organisms, and none are expected in this generated source.
- `Bacto peptone`, `Yeast extract`, and `Sea water` are ungrounded complex ingredients.
- The generated output has the pH and both DSMZ 514g preparation notes, but uses `SOLID_AGAR` physical state even though agar is optional in the source.
- Merge metadata is present but overbroad: 157 source records are collapsed onto one canonical record with many unrelated strain-specific names.

## Findings

- Major: DSMZ 514g is overmerged with 156 other sources, including DSMZ 514 / KOMODO 514 records that should carry the full-strength Bacto Marine Broth formula rather than the half-strength 514g formula.
- Major: The 500 ml seawater source row is imported as `500 G_PER_L`.
- Minor: The optional 15 g/L agar addition drives `physical_state: SOLID_AGAR`, so the liquid half-strength broth and optional solid medium are not represented separately.
- Minor: Complex ingredients and seawater remain ungrounded.

## Recommended Edits

- Split DSMZ/MediaDive 514g from DSMZ/MediaDive 514 and KOMODO 514 descendants unless a source explicitly says half-strength with 50 percent seawater.
- Correct the KOMODO DSMZ 514 enrichment path so Bacto Marine Broth (Difco 2216) keeps the current DSMZ 514 full-strength formula.
- Represent 500 ml seawater as a 50 percent seawater basis or another volume-aware addition, not as 500 g/L.
- Decide whether DSMZ 514g should stay `SOLID_AGAR` with optional agar or be modeled as a liquid parent with a 15 g/L solidification variant.

## Follow-up Checks

- After repair, verify that `bacto_marine_broth_difco_2216` no longer appears in this record's `merged_from` list and that the DSMZ 514g canonical record still has 2.5 g/L Bacto peptone, 0.5 g/L yeast extract, 9.725 g/L NaCl, and a 50 percent seawater basis.

## Additional Notes

- None found.
