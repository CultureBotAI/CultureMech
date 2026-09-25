# YAML Record Review: marinitoga_hydrogenitolerans_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/marinitoga_hydrogenitolerans_medium__039279e9.yaml`
- Started UTC: 2026-09-24T00:15:32Z
- Finished UTC: 2026-09-24T00:16:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:007830` |
| Name | `marinitoga_hydrogenitolerans_medium` |
| Original name | `Marinitoga Hydrogenitolerans Medium` |
| Category | `bacterial` |
| Generated status | Generated merge output from 2026-08-06 |
| Merge fingerprint | `039279e9b57a22dfcc4186fe95296e497901b9d507daebf7c6c4b2a9aa042007` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M1297_Marinitoga_Hydrogenitolerans_Medium.yaml` |

The reviewed file is a generated `data/merge_yaml/merged/` record. Any future scientific fix belongs in the normalized owner or in merge logic, followed by regeneration of the merged YAML and rendered products; the generated merge itself should not be curated in place.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marinitoga_hydrogenitolerans_medium__039279e9.yaml` | Passed with `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marinitoga_hydrogenitolerans_medium__039279e9.yaml --out /private/tmp/marinitoga_hydrogenitolerans_medium__039279e9.strict.tsv --workers 1 --quiet` | Passed. The strict TSV had only its header line, so there were 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marinitoga_hydrogenitolerans_medium__039279e9.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file scanned, 0 references checked. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marinitoga_hydrogenitolerans_medium__039279e9.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the standard `eutils` / `pkg_resources` warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/*.yaml`, not embedded `MediaRecipe.curation_history` blocks. |

The regular `just` recipes were not used because this checkout currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools` before reaching record validation.

## Identity and Grounding

- The generated record identity is internally coherent: `CultureMech:007830`, `TOGO:M1297`, the `Marinitoga Hydrogenitolerans Medium` label, and the TOGO/JCM provenance all describe JCM Medium 1210 as exposed through TOGO Medium M1297.
- The `media_term` grounding to `TOGO:M1297` matches the target TOGO record. The inspected TOGO M1297 API payload and MediaDive `J1210` payload preserve the same medium identity from JCM Medium 1210.
- The exact maintained owner is `data/normalized_yaml/bacterial/TOGO_M1297_Marinitoga_Hydrogenitolerans_Medium.yaml`. That owner now has a 2026-09-11 `repair_togo_m1297_score15.py` curation event that corrects the formulation and provenance, so the reviewed generated file is stale rather than the sole source needing direct curation.
- An exact gitignore-independent scan for the sibling IDs found `CultureMech:002379` / `mediadive.medium:J1210` in `data/normalized_yaml/bacterial/JCM_J1210_MARINITOGA_HYDROGENITOLERANS_MEDIUM.yaml` and `data/merge_yaml/merged/MARINITOGA_HYDROGENITOLERANS_MEDIUM.yaml`. That is a separate MediaDive/JCM source copy of the same JCM medium, not the maintained owner of this TOGO-sourced target.
- Existing ingredient ontology links on water, resazurin, and dinitrogen are chemically reasonable. The generated target still maps MES to `CHEBI:39010`; the repaired normalized owner maps the same ingredient to `CHEBI:39005`, which is the closer identity for 2-(N-morpholino)ethanesulfonic acid.

## Evidence

- Source identity: supported. The generated notes and curation history trace the record to TOGO M1297 and JCM Medium 1210, and the inspected TOGO/JCM/MediaDive records all identify this source as `Marinitoga Hydrogenitolerans Medium`.
- Base ingredients: partly supported but stale. Sea salts at 30 g/L, MES at 4 g/L, tryptone at 1 g/L, and yeast extract at 1 g/L match the source formulation. The generated target gives resazurin as 0.5 g/L and distilled water as 1 g/L; the JCM formulation instead lists 0.5 mg/L resazurin and 1 L distilled water, as already encoded in the normalized owner.
- Stock-solution additions: unsupported as generated. The generated `solutions` entries preserve the 1.0 M glucose, 5% Na2S x 9H2O, and 5% L-cysteine HCl H2O stock labels, but they are empty solutions with `G_PER_L` addition amounts of 14, 10, and 10. JCM Medium 1210 adds these three stock solutions at 14 ml/L, 10 ml/L, and 10 ml/L after autoclaving; the 1.0 M and 5% values describe nested stock composition, not root final-medium grams per liter.
- Preparation and conditions: materially incomplete as generated. The generated target omits pH 6.0, bubbling with N2, distribution under N2, sealing with butyl rubber stoppers, autoclaving at 121 degrees C for 15 min, cooling, and anaerobic aseptic addition of autoclaved stock solutions. Those steps are already represented in the repaired normalized owner.
- References: incomplete as generated. The generated target has provenance in prose notes and curation history, but no `references` block carrying the TOGO, JCM, or MediaDive URLs that now exist in the normalized owner.
- Applications: weak but acceptable. `Microbial cultivation` is consistent with a named JCM growth medium; no source-specific organism or growth-performance claim is asserted in this generated target.

## Completeness

- A gitignore-independent exact field scan of only the reviewed generated YAML and `data/normalized_yaml/bacterial/TOGO_M1297_Marinitoga_Hydrogenitolerans_Medium.yaml` found `preparation_steps` and `references` only in the normalized owner, at lines 210 and 243. It found no `sources`, `source_data`, `target_organisms`, `growth_metrics`, `parent_media`, `variant_children`, or `variant_relationship` field in either exact file.
- The missing `preparation_steps`, `sterilization`, `ph_value`, and `references` fields in the generated target are not optional harmless blanks here: the authoritative JCM recipe includes preparation details needed to make this anaerobic medium correctly, and the normalized owner already carries them.
- Empty `target_organisms` and `growth_metrics` are acceptable for this review. The inspected recipe source establishes the medium formulation, not a narrow organism-specific growth metric.
- The separate MediaDive/JCM copy, `data/normalized_yaml/bacterial/JCM_J1210_MARINITOGA_HYDROGENITOLERANS_MEDIUM.yaml`, is still an older flattened import. Do not use it to overwrite the repaired TOGO M1297 owner until that sibling has been separately reviewed and curated.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The generated merge is stale and omits the 2026-09-11 repaired formulation. | The generated file still has no `ph_value`, no `preparation_steps`, no `sterilization`, no `references`, resazurin as `0.5 G_PER_L`, water as `1 G_PER_L`, and empty `solutions` entries with 14/10/10 `G_PER_L` additions. The normalized TOGO owner already corrected those values and stock compositions from TOGO M1297 / JCM Medium 1210. | Regenerate `data/merge_yaml/merged/marinitoga_hydrogenitolerans_medium__039279e9.yaml` from `data/normalized_yaml/bacterial/TOGO_M1297_Marinitoga_Hydrogenitolerans_Medium.yaml`; if regeneration does not carry those fields through, fix `scripts/merge_recipes.py` or the merge model path that drops them. |

No blocker findings: the YAML is valid and the record denotes the right TOGO/JCM source medium.

No minor findings found.

## Recommended Edits

1. Regenerate the merged recipe from `data/normalized_yaml/bacterial/TOGO_M1297_Marinitoga_Hydrogenitolerans_Medium.yaml` so the generated file picks up pH 6.0, 0.5 mg/L resazurin, 1 L distilled water, 14/10/10 ml/L stock additions, nested stock composition, preparation steps, sterilization, and references.
2. If a clean regeneration still drops any of those fields, fix the merge code path that builds records under `data/merge_yaml/merged/` from normalized source recipes.
3. Review `data/normalized_yaml/bacterial/JCM_J1210_MARINITOGA_HYDROGENITOLERANS_MEDIUM.yaml` before adding a duplicate-source relationship or merging the TOGO and MediaDive copies; that sibling currently represents the same JCM medium with the older flattened stock-solution units.

## Follow-up Checks

- Run `just verify-merges` after regeneration to prove the maintained normalized owner and the generated merged record are synchronized.
- Re-run open-schema, strict, term, and reference validation on `data/merge_yaml/merged/marinitoga_hydrogenitolerans_medium__039279e9.yaml`.
- Manually compare the regenerated target against TOGO M1297, JCM Medium 1210, and MediaDive J1210 to confirm the pH, N2 atmosphere, autoclave sequence, and three stock-solution additions remain source-faithful.
- After the JCM/MediaDive sibling is curated, check whether `CultureMech:007830` and `CultureMech:002379` should be represented as duplicate source copies or merged by the recipe-merging rules.

## Additional Notes

- This review intentionally did not patch `data/merge_yaml/merged/marinitoga_hydrogenitolerans_medium__039279e9.yaml`; it is generated output.
- The normalized TOGO owner has a better current representation than the MediaDive JCM `J1210` owner. Linking or merging those copies before the JCM owner is repaired could reintroduce the same root 14/10/10 `G_PER_L` stock-solution error.
