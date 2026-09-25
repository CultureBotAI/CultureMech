# YAML Record Review: COLUMBIA BLOOD AGAR WITH CHARCOAL

- Repository: CultureMech
- Record: `data/merge_yaml/merged/COLUMBIA_BLOOD_AGAR_WITH_CHARCOAL.yaml`
- Started UTC: `2026-09-22T11:04:04Z`
- Finished UTC: `2026-09-22T11:06:35Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:001534` for DSMZ / MediaDive Medium `429a`, `COLUMBIA BLOOD AGAR WITH CHARCOAL`, generated from `data/normalized_yaml/bacterial/columbia_blood_agar_with_charcoal.yaml` on merge fingerprint `0c9917adf6af5e7bda99a7dcfad95b514aef9183ccd2f5a620740327039befe6`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/COLUMBIA_BLOOD_AGAR_WITH_CHARCOAL.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The source identity is DSMZ Medium 429a, a charcoal variant of Columbia blood agar.

The formula is source-inflated in the maintained input. DSMZ 429a says to add 2 g/L activated charcoal to Columbia agar base before autoclaving and to add 4% horse blood after cooling. The local direct record also imports peptone, meat extract, agar, casein peptone, soy peptone, NaCl, and a Brain Heart Infusion product expansion that are not DSMZ 429a ingredients.

## Evidence

The inspected DSMZ 429a PDF supports `Columbia agar base`, `Activated charcoal`, and `Horse blood`. It also supports the preparation note about adding charcoal before autoclaving, adding horse blood after cooling to 50 C, swirling agar while suspending, wetting dry plate surfaces before inoculation, incubating Neisseria strains in a humid microaerobic atmosphere, and rehydrating freeze-dried ampoules in liquid media 220, 215, or 1.

The rehydration-media references are not composition includes. The local record imported or expanded Medium 1 Nutrient Broth, Medium 215 BHI, and Medium 220 Caso/Tryptone Soya Agar components into the charcoal agar formula. The pH 7.0, Bacillus MnSO4, and pH 7.3 / Tryptone Soya Agar preparation steps likewise belong to referenced downstream media, not to DSMZ 429a.

The local `40 G_PER_L` horse-blood row is a lossy conversion of the source's 4% horse-blood supplement. The `1000 G_PER_L` Columbia agar base row also models one liter of prepared agar base as a mass concentration.

## Completeness

The correct parent formula should contain only Columbia agar base, activated charcoal at 2 g/L, and horse blood at 4% final concentration. Empty target-organism and growth-evidence fields are acceptable for this source-only branch.

The related KOMODO 429a input is also malformed: it omits the activated-charcoal component and was later pulled into the broad KOMODO 429 parent merge instead of remaining a distinct charcoal variant. That is owned by `data/normalized_yaml/bacterial/KOMODO_429a_COLUMBIA_BLOOD_AGAR_WITH_CHARCOAL.yaml` and the merge regeneration, not by this direct DSMZ input.

## Findings

- Major: `data/normalized_yaml/bacterial/columbia_blood_agar_with_charcoal.yaml` contains referenced Medium 1, 215, and 220 ingredients that DSMZ 429a names only as freeze-dried-ampoule rehydration media.
- Major: the Brain Heart Infusion commercial-product expansion is unsupported because BHI appears only through referenced Medium 215.
- Major: 4% horse blood is represented as `40 G_PER_L`.
- Major: one liter of Columbia agar base is represented as `1000 G_PER_L`.
- Major: pH and Bacillus sporulation steps from unrelated referenced media are present on DSMZ 429a.

## Recommended Edits

- In `data/normalized_yaml/bacterial/columbia_blood_agar_with_charcoal.yaml`, keep the DSMZ 429a formula to Columbia agar base, 2 g/L activated charcoal, and 4% horse blood.
- Remove Peptone, Meat extract, Agar, Casein peptone, Soy peptone, NaCl, calf brain, beef heart, Proteose peptone, dextrose, sodium chloride, and disodium phosphate from the direct 429a recipe.
- Preserve the rehydration-media numbers only as preparation context or notes; do not import media 220, 215, or 1 into the 429a composition.
- Model the Columbia agar base as a prepared base volume or opaque product, and model horse blood as a 4% liquid supplement.
- Regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm the regenerated 429a formula has activated charcoal at 2 g/L and horse blood at 4% without rehydration-media ingredient rows.
- Confirm no Brain Heart Infusion expansion remains.
- Confirm the pH 7.0, Bacillus sporulation, and pH 7.3 / Tryptone Soya Agar preparation steps are gone from DSMZ 429a.

## Additional Notes

Empty optional fields are not defects.
