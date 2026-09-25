# YAML Record Review: desulfonema_magnum_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfonema_magnum_medium__426b775d.yaml
- Started UTC: 2026-09-22T19:35:31Z
- Finished UTC: 2026-09-22T19:37:15Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/desulfonema_magnum_medium__426b775d.yaml` |
| Generated or maintained | Generated merge output |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M915_Desulfonema_Magnum_Medium.yaml` |
| Same-upstream sibling owner | `data/normalized_yaml/bacterial/JCM_J876_DESULFONEMA_MAGNUM_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:010335` |
| Label | `desulfonema_magnum_medium` |
| Original label | `Desulfonema Magnum Medium` |
| Source identity | TOGO Medium M915, derived from JCM M876 |
| Merge lineage | `merge_recipes.py` merged `TOGO_M915_Desulfonema_Magnum_Medium.yaml` into fingerprint `426b775dc45496c6ee76a727c9a26b3b38a667b65f2a1964e1ae0794df4cd460` |

I read the full generated record and its maintained normalized owner. TOGO's structured API identifies M915 as `Desulfonema Magnum Medium`, gives `JCM_M876` as `original_media_id`, and preserves the JCM `GRMD=876` source URL. A gitignore-independent exact search for the M915/J876 source identifiers across `data`, `src`, `scripts`, and the ignored review-report directory found the TOGO owner above, the same-upstream MediaDive owner `JCM_J876_DESULFONEMA_MAGNUM_MEDIUM.yaml`, and the sibling generated output `data/merge_yaml/merged/DESULFONEMA_MAGNUM_MEDIUM.yaml`.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfonema_magnum_medium__426b775d.yaml` | Passed; no issues found |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/desulfonema_magnum_medium__426b775d.yaml --out /private/tmp/desulfonema_magnum_medium__426b775d.strict.tsv --workers 1 --quiet` | Passed; 0 errors |
| Reference validator, `linkml-reference-validator validate data data/merge_yaml/merged/desulfonema_magnum_medium__426b775d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator, `linkml-term-validator validate-data data/merge_yaml/merged/desulfonema_magnum_medium__426b775d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only the known `eutils` / `pkg_resources` deprecation warning was emitted |
| Embedded `curation_history` | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` entries |

The documented `just` wrappers were not used for this focused record check because the local project `uv` environment currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools`. The equivalent validators above were run offline with Python 3.11 and the cached `linkml`, `pyyaml`, `linkml-reference-validator`, and `linkml-term-validator` packages.

## Identity and Grounding

The top-level identity is coherent for the TOGO mirror of JCM M876: the generated `media_term` is `TOGO:M915`, its label is `Desulfonema Magnum Medium`, and the import note points back to JCM M876. Direct JCM retrieval of `GRMD=876` returned a `Nothing found` page during this review, but both the TOGO M915 API payload and the MediaDive J876 REST payload independently preserve the same JCM URL for the same medium name.

The individual CHEBI groundings for water, magnesium sulfate heptahydrate, sodium chloride, calcium chloride dihydrate, potassium dihydrogen phosphate, ammonium chloride, resazurin, magnesium chloride hexahydrate, potassium chloride, carbon dioxide, and dinitrogen match the imported component labels. The grounding layer is not the main problem; the import flattened source semantics into misleading concentration units, empty stock-solution stubs, and generic variable ingredients.

## Evidence

TOGO M915 supports the first salt list as a 1 L basal solution containing 6.8 g MgSO4 x 7H2O, 25 g NaCl, 1.4 g CaCl2 x 2H2O, 0.14 g KH2PO4, 0.25 g NH4Cl, 0.5 mg resazurin, 5.6 g MgCl2 x 6H2O, and 0.72 g KCl. The generated record preserves the gram-valued salts but encodes the 1 L water row as `1 G_PER_L` and the 0.5 mg resazurin row as `0.5 G_PER_L`.

TOGO supports eight post-autoclave stock additions as milliliter additions, not as g/L concentrations: 1 ml FeCl2 solution from M180, 1 ml trace element solution from M180, 1 ml selenite-tungstate solution from M431, 20 ml 0.5% Na2CO3 solution, 10 ml 3% Na2S x 9H2O solution, 10 ml 4.8% KAl(SO4)2 x 12H2O solution, 10 ml 6% sodium benzoate solution, and 10 ml trace vitamins from M190. In the generated record these are eight `solutions:` entries with `name: Unknown solution`, empty `composition: []`, and the milliliter numbers copied to `G_PER_L`.

TOGO also supports procedural and condition claims that are absent or misplaced in the generated YAML. Its comments boil and cool the basal medium under an N2-CO2 4:1 gas mixture, check pH around 6.0, distribute and seal culture vessels under the same gas mixture before autoclaving, add autoclaved or filter-sterilized solutions stored under N2 in order, require overnight equilibration until a white precipitate forms, and treat 10-20 mg/L filter-sterilized sodium dithionate under N2 as an optional pre-inoculation stimulant. The generated record has no `preparation_steps`; instead, it promotes carbon dioxide gas, nitrogen gas, sodium dithionate, and a second N2 row to variable top-level ingredients.

MediaDive J876 corroborates the same high-level JCM identity and exposes a structured version of the formula, preparation text, and nested FeCl2, trace element, and selenite-tungstate stock solution recipes. That same upstream source is currently represented as a separate normalized `JCM_J876_DESULFONEMA_MAGNUM_MEDIUM.yaml` record and a separate generated `DESULFONEMA_MAGNUM_MEDIUM.yaml` record instead of merging with TOGO M915.

## Completeness

The record is materially incomplete for stock-solution and preparation detail. It carries cross-reference prose for M180, M431, and M190 but no resolved solution records for those additions; it carries concentration strings for the carbonate, sulfide, alum, and benzoate stock solutions but no `composition` entries; it drops all three source comments that define the anaerobic gas handling, pH context, sterilization order, overnight equilibration, optional dithionate addition, and inoculum guidance.

The empty `target_organisms` and `references` slots are not defects for this imported source recipe because TOGO M915 and MediaDive J876 are source formulations, not primary growth evidence.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Source units were mistranscribed as concentrations. | TOGO lists 1 L water and 0.5 mg resazurin in the basal solution, plus 1, 10, or 20 ml stock-solution additions after autoclaving. The generated target encodes water as `1 G_PER_L`, resazurin as `0.5 G_PER_L`, and all stock-addition volumes as `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M915_Desulfonema_Magnum_Medium.yaml` and TOGO import unit mapping. |
| Major | Every stock solution is unresolved or empty. | The target's eight `solutions:` entries all have `name: Unknown solution` and `composition: []`, including the three JCM medium cross-references and the four stock solutions whose percent strengths are embedded only in `preferred_term`. | Same TOGO normalized owner, plus solution migration or importer logic that handles referenced media and percent solution labels. |
| Major | Anaerobic preparation semantics were lost. | TOGO gives N2-CO2 gas handling, pH around 6.0, sealed autoclaving, post-autoclave solution additions, overnight equilibration, optional 10-20 mg/L dithionate before inoculation, and storage under N2. The generated target has no preparation steps and instead has variable ingredient rows for gas and sodium dithionate. | Same TOGO normalized owner. |
| Major | The same JCM M876/J876 recipe is split into two generated records. | The TOGO normalized file cites `JCM_M876`; MediaDive J876 exposes `source: JCM` and the same `GRMD=876` link in `data/normalized_yaml/bacterial/JCM_J876_DESULFONEMA_MAGNUM_MEDIUM.yaml`; the merge products remain separate as `desulfonema_magnum_medium__426b775d.yaml` and `DESULFONEMA_MAGNUM_MEDIUM.yaml`. | TOGO and MediaDive normalized source records plus merge-deduplication rules. |
| Minor | The imported classification says this is undefined/complex despite a defined formulation. | TOGO and MediaDive list a recipe made from salts, gases, resazurin, sodium dithionate, and chemically defined stock solutions; MediaDive marks the same medium `complex_medium: no`. The TOGO record has `composition_type: UNDEFINED` and compatibility `medium_type: COMPLEX`. | `data/normalized_yaml/bacterial/TOGO_M915_Desulfonema_Magnum_Medium.yaml`. |

## Recommended Edits

1. Rework `data/normalized_yaml/bacterial/TOGO_M915_Desulfonema_Magnum_Medium.yaml` or the TOGO importer so source `L`, `mg`, and `ml` quantities are not blindly written as `G_PER_L`; preserve the 0.5 mg resazurin amount and stock-addition volumes with explicit volume semantics or a checked final-concentration conversion.
2. Resolve the M180, M431, and M190 cross-references to modeled solution records, and model the 0.5% carbonate, 3% sulfide, 4.8% alum, and 6% benzoate stocks as real solutions rather than empty `Unknown solution` stubs.
3. Import the TOGO comment paragraphs into preparation and condition fields so gas handling, pH around 6.0, sterilization, post-autoclave addition order, N2 storage, overnight equilibration, optional dithionate addition, and inoculum fraction are retained.
4. Collapse TOGO M915 and MediaDive J876 into one same-upstream JCM recipe, or add a merge rule that recognizes `JCM_M876` and `mediadive.medium:J876` as the same source before regenerating `data/merge_yaml/merged/`.
5. Reclassify the TOGO-derived record as `composition_type: DEFINED` with `medium_type: DEFINED` if all referenced stocks are resolved to chemically defined recipes.

## Follow-up Checks

1. Rerun open schema, strict schema, term, and reference validation on the edited TOGO and MediaDive normalized records and on the regenerated merged output.
2. Compare the regenerated TOGO-derived record against the TOGO M915 API, checking the 0.5 mg resazurin row, every milliliter stock addition, pH around 6.0, N2-CO2 atmosphere, N2 stock-storage context, optional sodium dithionate concentration, and all retained comments.
3. Compare the regenerated JCM/MediaDive path against MediaDive J876 and its solution IDs 4863, 3846, 3847, and 4172 to make sure the FeCl2, trace element, and selenite-tungstate stocks remain scoped to the right solution.
4. Re-run merge freshness or the equivalent merge-deduplication check and confirm there is no longer a separate TOGO M915 generated record for the same JCM M876 source.

## Additional Notes

- `find` and `rg --no-ignore --hidden` were used for absence-sensitive searches, so ignored review reports and generated files were included where relevant.
- No report for `desulfonema_magnum_medium__426b775d` existed under `reports/yaml_record_review/` before this one; that ignored directory was checked with `find`.
- JCM's `GRMD=876` URL returned a `Nothing found` HTML page during this review, so JCM's direct page text was not independently available.
