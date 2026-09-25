# YAML Record Review: artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.yaml
- Started UTC: 2026-09-21T15:10:35Z
- Finished UTC: 2026-09-21T15:12:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.yaml` |
| Stable ID | `CultureMech:001173` |
| Name | `artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium` |
| Original name | `Artificial sea water - Tryptone soy broth Medium (ASW TSB Medium)` |
| Category | `bacterial` |
| Merge state | Single-source merge from `artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium` with fingerprint `185e8b50e29fc146b297e646590bf47441b4d2c7e7bb6c945d611782a4cb5efe` |

The target is a generated MediaDive/DSMZ merge. Correct the normalized owner and any importer or migration rule that flattened nested stock solutions, then regenerate this merged record.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.yaml --out /private/tmp/artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, and no focused validator for embedded `MediaRecipe.curation_history` arrays is exposed. |

The documented `just validate-*` wrappers remain blocked for this environment by project dependency resolution under Python 3.13, so this review used the equivalent no-project Python 3.11 validators already cached under `/private/tmp/uv-cache-culturemech-review`.

## Identity and Grounding

- **Medium identity is correct.** The DSMZ PDF for Medium 1691 is `Artificial sea water - Tryptone soy broth Medium (ASW TSB Medium)`, matching the local `mediadive.medium:1691` identity and `CultureMech:001173`.
- **The basal agar medium identity is supported.** DSMZ lists 17 g trypticase peptone, 3 g peptone from soy meal, 2.5 g D-glucose, 20 g Bacto Agar, pH 7.3, and ASW/Biomaris as the basal medium.
- **The source hierarchy is not preserved.** DSMZ has nested subrecipes for Artificial Sea Water 2x concentrate, Trace Element Solution SL-10, and Vitamin Solution; the CultureMech record flattens every ASW salt, trace element, and vitamin into direct final-medium ingredients.
- **One trace ingredient is grounded to the wrong hydrate state.** The source row is `NiCl2 x 6 H2O`, but the CultureMech term is `CHEBI:34887` with label `nickel dichloride`, not a hexahydrate-specific nickel chloride term.

## Evidence

- The inspected DSMZ Medium 1691 PDF separates the recipe into basal medium, Artificial Sea Water Solution 2x, Trace Element Solution SL-10, and Vitamin solution sections.
- DSMZ adds 1.0 ml Trace Element Solution SL-10 and 1.0 ml Vitamin Solution to 1000 ml of medium after autoclaving and cooling to 55 C. The current record has no `solutions` entries for either stock and instead stores their source stock-strength ingredients directly.
- The DSMZ trace stock dissolves `FeCl2 x 4 H2O` in 10.00 ml HCl, dilutes, adds the other salts, and brings the stock to 1000.0 ml. That stock-preparation paragraph is currently a top-level `DISSOLVE` step, so the scope is ambiguous and detached from a Trace Element Solution record.

## Completeness

- The basal medium is incomplete because it has direct ASW salts but no explicit `Artificial Sea Water` or `Biomaris` component.
- The two post-autoclave 1.0 ml stock additions are missing as solution additions.
- No `target_organisms`, `growth_metrics`, or incubation conditions are present. That is acceptable because the inspected DSMZ page supplies the medium formulation rather than a strain-specific growth assay.
- A gitignore-independent `find` search under `reports/yaml_record_review` found no pre-existing `*artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.md` report before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Nested ASW, trace-element, and vitamin stock recipes were flattened into direct final-medium ingredients. | DSMZ Medium 1691 defines a basal medium and three subrecipes; the final medium receives ASW or Biomaris as a component, then 1.0 ml each of Trace Element Solution SL-10 and Vitamin Solution. The CultureMech ingredients list instead contains the ASW salts, trace salts, HCl, and all vitamins as final-medium ingredient rows at stock-source amounts. | `data/normalized_yaml/bacterial/artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.yaml`; likely also the MediaDive import or solution migration path. |
| Major | `NiCl2 x 6 H2O` is grounded to an anhydrous nickel chloride term. | The source hydrate label is `NiCl2 x 6 H2O`; the record's term label is `nickel dichloride`, which erases the six-water hydrate state that the source explicitly supplies. | `data/normalized_yaml/bacterial/artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.yaml`. |

No blockers found: the YAML validates and the DSMZ/MediaDive identity is correct.

## Recommended Edits

1. Rebuild `data/normalized_yaml/bacterial/artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.yaml` so direct ingredients contain the basal TSB/agar rows plus a properly represented ASW/Biomaris component, with the trace-element and vitamin stocks moved under `solutions` at 1.0 ml per liter.
2. Move the FeCl2/HCl dilution paragraph onto the Trace Element Solution SL-10 stock instead of leaving it as a top-level final-medium preparation step.
3. Reground `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride term or leave it explicitly unresolved if a verified CHEBI identifier is unavailable.
4. Regenerate the merge layer.

## Follow-up Checks

- Re-run `just validate-schema data/normalized_yaml/bacterial/artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.yaml` and `just validate-strict data/normalized_yaml/bacterial/artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.yaml` after the normalized edit.
- Re-run `just validate-references data/normalized_yaml/bacterial/artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.yaml` after stock-solution references are added.
- Compare the regenerated merge against DSMZ Medium 1691 and verify that the 1 ml trace/vitamin additions, ASW subrecipe boundary, pH 7.3 adjustment, and 55 C post-autoclave addition are all represented at the correct scope.

## Additional Notes

- `find data/normalized_yaml -iname '*artificial*sea*water*tryptone*soy*broth*medium*' -print` found the single normalized owner at `data/normalized_yaml/bacterial/artificial_sea_water_tryptone_soy_broth_medium_asw_tsb_medium.yaml`.
- An exact gitignore-independent search for `CultureMech:001173` and `mediadive.medium:1691` in the normalized owner and generated record found the same stable ID and MediaDive grounding in both files.
