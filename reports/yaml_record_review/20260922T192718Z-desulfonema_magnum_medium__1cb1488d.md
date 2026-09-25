# YAML Record Review: desulfonema_magnum_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfonema_magnum_medium__1cb1488d.yaml
- Started UTC: 2026-09-22T19:23:50Z
- Finished UTC: 2026-09-22T19:27:18Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/desulfonema_magnum_medium__1cb1488d.yaml` |
| Generated or maintained | Generated merge output |
| Maintained owners | `data/normalized_yaml/bacterial/desulfonema_magnum_medium.yaml`, `data/normalized_yaml/bacterial/KOMODO_202_DESULFONEMA_MAGNUM_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:004297` |
| Label | `desulfonema_magnum_medium` |
| Original label | `DESULFONEMA MAGNUM MEDIUM` |
| Source identity | KOMODO 202 / DSMZ 202 |
| Merge lineage | `merge_recipes.py` merged `KOMODO_202_DESULFONEMA_MAGNUM_MEDIUM.yaml` and `desulfonema_magnum_medium.yaml` into fingerprint `1cb1488ded850934fc4fb71e0c3f9aa3d58f3df9bb35043b6b214740860dd538` |

I read the full generated record. A gitignore-independent search for the Desulfonema Magnum name and source identifiers found two other same-label generated records: TOGO M915 / JCM 876 in `desulfonema_magnum_medium__426b775d.yaml` and JCM 876 in `DESULFONEMA_MAGNUM_MEDIUM.yaml`. They were treated as sibling source variants, not as DSMZ 202 duplicates.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfonema_magnum_medium__1cb1488d.yaml` | Passed; no issues found |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/desulfonema_magnum_medium__1cb1488d.yaml --out /private/tmp/desulfonema_magnum_medium__1cb1488d.strict.tsv --workers 1 --quiet` | Passed; 0 errors |
| Reference validator, `linkml-reference-validator validate data data/merge_yaml/merged/desulfonema_magnum_medium__1cb1488d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator, `linkml-term-validator validate-data data/merge_yaml/merged/desulfonema_magnum_medium__1cb1488d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only the known `eutils` / `pkg_resources` deprecation warning was emitted |
| Embedded `curation_history` | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` entries |

The documented `just` wrappers were not used for this focused record check because the local project `uv` environment currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools`. The equivalent validators above were run offline with Python 3.11 and the cached `linkml`, `pyyaml`, `linkml-reference-validator`, and `linkml-term-validator` packages.

## Identity and Grounding

The record denotes DSMZ Medium 202 as mirrored through KOMODO and MediaDive. The target `media_term`, merge metadata, and `parent_media` point to `mediadive.medium:202`; the MediaDive REST payload and DSMZ PDF both identify medium 202 as `DESULFONEMA MAGNUM MEDIUM`.

The generated record's source provenance is misleading. Its `notes` field is inherited from KOMODO and says `Aerobic: Yes`, but the DSMZ 202 recipe requires anoxic Hungate tubes, 80% N2 / 20% CO2 for Solution A and Solution E, 100% N2 for Solutions B, D, and F, and 100% N2 plus filtration for Solution C.

The individual CHEBI groundings are mostly coherent for exact salts, but the source scopes are not. Solution A through F, SL-10, selenite-tungstate, and Wolin vitamins are flattened into one top-level `ingredients` list.

## Evidence

DSMZ and MediaDive support the high-level identity, pH 7.0, and the Solution A through F topology. DSMZ 202 first combines 952 ml Solution A, 10 ml Solution B, 1 ml Solution C, 10 ml Solution D, 20 ml Solution E, and 10 ml Solution F; then Solution A contains 1 ml SL-10, 1 ml selenite-tungstate, and 0.5 ml 0.1% sodium resazurin, while Solution C consists of 1 ml Wolin's vitamin solution.

The generated record does not preserve any of those solution boundaries:

- Solution A salts are top-level ingredients at Solution A stock g/L values.
- Solution B benzoate, Solution D alum, Solution E carbonate, and Solution F sulfide are top-level ingredients at 60, 48, 50, and 30 g/L stock concentrations.
- SL-10 constituents, selenite-tungstate constituents, and Wolin vitamin constituents are top-level ingredients at their stock concentrations.
- Distilled water rows for Solution A, B, D, E, F, SL-10, selenite-tungstate, and Wolin vitamins are all absent.

DSMZ also supports two preparation notes: the anaerobic/autoclave/filter-sterilize sequence for Solutions A through F and the optional sodium dithionite plus 5-10% inoculum note. The generated record has no `preparation_steps`.

## Completeness

This generated record is missing every required stock and solution boundary, including the main A-to-F assembly and the three nested stock solutions. A gitignore-independent search of the target file found no top-level `solutions:` key even though MediaDive 202 exposes nine solution records for this medium.

The empty `target_organisms` and `references` slots are not defects for this source recipe because DSMZ and KOMODO provide formulation provenance, not growth-study evidence.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The DSMZ 202 nested solution topology was completely flattened. | MediaDive 202 has Solution A through F, SL-10, selenite-tungstate, and Wolin's vitamin solution. The generated record has only top-level ingredients and no `solutions:` block. | `data/normalized_yaml/bacterial/desulfonema_magnum_medium.yaml`, `data/normalized_yaml/bacterial/KOMODO_202_DESULFONEMA_MAGNUM_MEDIUM.yaml`, and MediaDive/DSMZ solution import logic. |
| Major | Multiple stock concentrations are encoded as if they were final medium concentrations. | DSMZ 202 adds 10 ml Solution B, 10 ml Solution D, 20 ml Solution E, 10 ml Solution F, 1 ml SL-10, 1 ml selenite-tungstate, and 1 ml Wolin vitamins; the generated row values are the stock g/L values for those solutions. | Same normalized DSMZ/KOMODO owners plus the cocktail-nesting repair path. |
| Major | Preparation steps were dropped. | DSMZ 202 specifies the gas sparging, anoxic Hungate tube dispensing, separate autoclaving, Solution C filtration, final addition sequence, overnight equilibration, optional sodium dithionite, and inoculum fraction. The generated target has no `preparation_steps`. | MediaDive preparation-step import for `data/normalized_yaml/bacterial/desulfonema_magnum_medium.yaml`, then the KOMODO source duplicate and generated merge. |
| Major | The record preserves a wrong aerobicity claim from KOMODO. | The generated `notes` say `Aerobic: Yes`; the DSMZ formulation is explicitly anaerobic and uses N2/CO2 or N2 in every solution preparation path. | `data/normalized_yaml/bacterial/KOMODO_202_DESULFONEMA_MAGNUM_MEDIUM.yaml`; merge provenance should retain source conflict instead of promoting the KOMODO note. |
| Minor | Distilled water rows are absent. | DSMZ 202 lists water in Solution A, B, D, E, F, SL-10, selenite-tungstate, and Wolin vitamins. The generated target has no water row. | The same DSMZ/KOMODO normalized owners. |

## Recommended Edits

1. Restore DSMZ 202 as a solution-structured recipe under `data/normalized_yaml/bacterial/desulfonema_magnum_medium.yaml`, with Solution A through F and the SL-10, selenite-tungstate, and Wolin vitamin stocks in their own scopes.
2. Propagate the corrected DSMZ topology into `data/normalized_yaml/bacterial/KOMODO_202_DESULFONEMA_MAGNUM_MEDIUM.yaml` or link the KOMODO record as a source duplicate without preserving the false `Aerobic: Yes` assertion.
3. Reattach the DSMZ preparation steps to the appropriate main and stock solution scopes.
4. Preserve the distilled-water rows for the component solutions so the stock recipes are complete.
5. Regenerate `data/merge_yaml/merged/desulfonema_magnum_medium__1cb1488d.yaml` from the maintained normalized inputs.

## Follow-up Checks

1. Rerun open schema, strict schema, term, and reference validation on both edited normalized records and on the regenerated merged output.
2. Compare the regenerated record against DSMZ / MediaDive 202, checking every A-to-F addition volume, nested SL-10/selenite-tungstate/Wolin component, and preparation step.
3. Recheck the generated YAML for a `solutions:` block and absence of top-level benzoate, alum, carbonate, sulfide, SL-10, selenite-tungstate, and vitamin stock rows.
4. Confirm the KOMODO source note no longer asserts aerobic growth or, at minimum, carries that field as a contradicted upstream value.

## Additional Notes

- `find` and `rg --no-ignore --hidden` were used for absence-sensitive searches, so ignored review reports and generated files were included where relevant.
- No report for `desulfonema_magnum_medium__1cb1488d` existed under `reports/yaml_record_review/` before this one; that ignored directory was checked with `find`.
