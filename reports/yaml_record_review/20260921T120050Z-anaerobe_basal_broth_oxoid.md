# YAML Record Review: anaerobe_basal_broth_oxoid

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/anaerobe_basal_broth_oxoid.yaml`
- Started UTC: 2026-09-21T12:00:50Z
- Finished UTC: 2026-09-21T12:01:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:009243` |
| Name | `anaerobe_basal_broth_oxoid` |
| Original name | Anaerobe Basal Broth (Oxoid) |
| Source identity | `TOGO:M2690` |
| Category | `bacterial` |
| Physical state | `LIQUID` |
| Generated or maintained | Generated merge from `data/normalized_yaml/bacterial/anaerobe_basal_broth_oxoid.yaml` |
| Merge fingerprint | `635dff46b4fed1e9f29d8da09bb4c885fd7e35bf353f5e0461e8e9db1d8cace5` |

This is a singleton generated merge. Its normalized owner currently has the same scientific content and lacks only the generated `MERGED_RECIPES`, `merge_fingerprint`, and `merged_from` block.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anaerobe_basal_broth_oxoid.yaml` | Passed, `No issues found` |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/anaerobe_basal_broth_oxoid.yaml --out /private/tmp/anaerobe_basal_broth_oxoid.strict.tsv --workers 1 --quiet` | Passed, 0 files with errors and 0 total error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/anaerobe_basal_broth_oxoid.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks for this file |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/anaerobe_basal_broth_oxoid.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` / `pkg_resources` deprecation warning |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, and no focused validator is documented for one generated record's embedded `MediaRecipe.curation_history` block |

## Identity and Grounding

The record identity is coherent. The YAML ID `CultureMech:009243`, name `anaerobe_basal_broth_oxoid`, and `media_term` `TOGO:M2690` all point to TOGO's Anaerobe Basal Broth (Oxoid) record.

An ignored-inclusive exact search for `CultureMech:009243`, `TOGO:M2690`, `635dff46b4fed1e9f29d8da09bb4c885fd7e35bf353f5e0461e8e9db1d8cace5`, and `anaerobe_basal_broth_oxoid` across `data/`, `scripts/`, `reports/`, `history/`, `.claude/`, `CLAUDE.md`, and `justfile` found the normalized owner, generated merge, ID/catalog/index rows, review manifests, and archived validation rows. `find reports/yaml_record_review -maxdepth 1 -type f -name '*anaerobe_basal_broth_oxoid.md' -print` found no existing report for this target before this review.

Most grounded ingredient IDs match the TOGO component labels closely: sodium chloride, D-glucose for Dextrose, sodium hydrogencarbonate for Sodium bicarbonate, starch, sodium pyruvate, sodium succinate, hemin for Haemin, ferric pyrophosphate, sodium thioglycolate, DL-Dithiothreitol, L-cysteine hydrochloride, and water all preserve the intended supplied material. There are still grounding gaps:

- `Arginine` is grounded to `CHEBI:32696` / argininium(1+) and still has a legacy `mediaingredientmech_term` entry. The packaged MIM label index maps exact `Arginine` to `CHEBI:29016` / Arginine, so the current ion-specific grounding should be curator-reviewed.
- `Vitamin K` has no `term`. TOGO's component name is Vitamin K and its GMO label is Vitamin K1; the packaged MIM label index contains exact rows for both `Vitamin K` and `Vitamin K1`, so this should not remain ungrounded.
- `Yeast extract` and `Peptone` have no broad undefined-component grounding in this record, although their ungrounded state is less chemically dangerous than forcing a small-molecule CHEBI term.

## Evidence

The fetched TOGO M2690 API record supports the source accession, medium label, all 16 component labels, and all non-water gram quantities in the YAML.

| Component | TOGO amount | YAML amount | Judgment |
|---|---:|---:|---|
| Distilled water | 1 L | `1 G_PER_L` | Wrong unit |
| Yeast extract | 7 g | `7 G_PER_L` | Supported as 7 g per liter |
| Sodium chloride | 5 g | `5 G_PER_L` | Supported as 5 g per liter |
| Dextrose | 1 g | `1 G_PER_L` | Supported as 1 g per liter |
| Sodium bicarbonate | 0.4 g | `0.4 G_PER_L` | Supported as 0.4 g per liter |
| Starch | 1 g | `1 G_PER_L` | Supported as 1 g per liter |
| Sodium pyruvate | 1 g | `1 G_PER_L` | Supported as 1 g per liter |
| Sodium succinate | 0.5 g | `0.5 G_PER_L` | Supported as 0.5 g per liter |
| Arginine | 1 g | `1 G_PER_L` | Quantity supported; CHEBI grounding needs review |
| Haemin | 0.005 g | `0.005 G_PER_L` | Supported as 0.005 g per liter |
| Vitamin K | 0.0005 g | `0.0005 G_PER_L` | Quantity supported; term missing |
| Ferric pyrophosphate | 0.5 g | `0.5 G_PER_L` | Supported as 0.5 g per liter |
| Sodium thioglycollate | 0.5 g | `0.5 G_PER_L` | Supported as 0.5 g per liter |
| Dithiothreitol | 1 g | `1 G_PER_L` | Supported as 1 g per liter |
| L-Cysteine HCl | 0.5 g | `0.5 G_PER_L` | Supported as 0.5 g per liter |
| Peptone | 16 g | `16 G_PER_L` | Supported as 16 g per liter |

TOGO also reports pH `6.8 +/- 0.2` at 25 C for M2690. The generated YAML has no `ph_value` or other place that preserves this source condition.

## Completeness

The ingredient list is structurally complete relative to the inspected TOGO record. The main consequential omissions are pH, structured source references, and three unresolved or weak ingredient groundings: Vitamin K, Yeast extract, and Peptone.

Empty `solutions`, `preparation_steps`, `sterilization`, `target_organisms`, and `growth_metrics` are not defects for this record on the inspected evidence. The TOGO source gives a formulation and pH, but does not provide stock recipes, preparation steps, sterilization conditions, or tested organism-growth claims.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Distilled water is represented with a mass unit. | TOGO M2690 lists `Distilled water` as 1 L, while the YAML stores `value: '1'` and `unit: G_PER_L`. This is the final-volume solvent, not one gram per liter water. | `data/normalized_yaml/bacterial/anaerobe_basal_broth_oxoid.yaml` |
| Major | The source pH is missing. | TOGO M2690 has pH `6.8 +/- 0.2` at 25 C. The YAML has no `ph_value`, preparation note, or discussion flag preserving that condition. | `data/normalized_yaml/bacterial/anaerobe_basal_broth_oxoid.yaml` |
| Major | `Arginine` is over-narrowed to the protonated argininium cation and still carries a legacy MIM field. | TOGO names the component `Arginine`; the YAML maps it to `CHEBI:32696` / argininium(1+) and leaves `mediaingredientmech_term: MediaIngredientMech:000341`. The packaged MIM index maps exact `Arginine` to `CHEBI:29016` / Arginine. | `data/normalized_yaml/bacterial/anaerobe_basal_broth_oxoid.yaml` |
| Minor | `Vitamin K` remains ungrounded even though the imported TOGO label narrows it to Vitamin K1. | The YAML has no `term` or MIM CHEBI term for Vitamin K. The TOGO item has component name `Vitamin K` and GMO label `Vitamin K1`; the packaged MIM index has exact rows for `Vitamin K` and `Vitamin K1`. | `data/normalized_yaml/bacterial/anaerobe_basal_broth_oxoid.yaml` |
| Minor | The record has only a free-text source URL in `notes`. | `references` is absent, so the link-reference validator reports 0 checks despite the TOGO source URL being the only support for every amount and the pH. | `data/normalized_yaml/bacterial/anaerobe_basal_broth_oxoid.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/anaerobe_basal_broth_oxoid.yaml`, change Distilled water from `1 G_PER_L` to a volume representation such as `1 L` or `1000 ML_PER_L`, matching the repository convention for final-volume water.
2. Add `ph_value: 6.8` and preserve the `+/- 0.2` tolerance and 25 C measurement condition in notes or a structured condition slot if the schema has one.
3. Replace the Arginine grounding with a source-faithful term, remove the leftover `mediaingredientmech_term`, and add a current `mediaingredientmech_chebi_term` only after verifying the exact ID-label pair against the packaged MIM index.
4. Decide whether TOGO M2690's Vitamin K item should be grounded as broad `Vitamin K` or as the imported `Vitamin K1` label, then add the matching CHEBI term from the packaged MIM label index.
5. Add a `references` entry for the inspected TOGO M2690 API or source URL so reference validation exercises at least the source URL carried in `notes`.
6. Regenerate `data/merge_yaml/merged/anaerobe_basal_broth_oxoid.yaml` from the corrected normalized owner.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation on the normalized owner and regenerated merge.
- Run `just verify-merges` or the narrowest merge-freshness equivalent to prove the generated merge incorporates the normalized corrections.
- Re-check `data/import_tracking/reports/ungrounded_ingredients.tsv` or its current generator to confirm `CultureMech:009243` no longer reports unresolved Vitamin K after curation.
- Manually re-open TOGO M2690 and confirm the pH tolerance and any 25 C qualifier remain preserved after YAML serialization.

## Additional Notes

- The link reference validator passed with 0 checks, so it did not exercise TOGO M2690.
- The failed exploratory search of the removed `data/raw_yaml` path was not used for this review. The owner/source search that established this singleton's current owner used `rg --no-ignore --hidden` and `find` against existing paths.
- The imported TOGO properties classify Dithiothreitol as an inorganic compound even though it is an organic redox reagent. This review did not classify that imported role text as a YAML defect because the same source property is what the TOGO importer preserved.
