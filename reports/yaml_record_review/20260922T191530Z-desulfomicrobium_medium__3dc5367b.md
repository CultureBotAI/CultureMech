# YAML Record Review: desulfomicrobium_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfomicrobium_medium__3dc5367b.yaml
- Started UTC: 2026-09-22T19:12:35Z
- Finished UTC: 2026-09-22T19:15:30Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/desulfomicrobium_medium__3dc5367b.yaml` |
| Generated or maintained | Generated merge output |
| Maintained owner | `data/normalized_yaml/bacterial/desulfomicrobium_medium.yaml` |
| Related normalized record | `data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:002963` |
| Label | `desulfomicrobium_medium` |
| Original label | `DESULFOMICROBIUM MEDIUM` |
| Source identity | JCM / MediaDive medium J616 |
| Merge lineage | `merge_recipes.py` merged one source record, `desulfomicrobium_medium.yaml`, into fingerprint `3dc5367b7e4fd67b3965a04e76c241af29e2bf6ee0622c43e795b4301c98b89b` |

I read the full generated record. A gitignore-independent search for its name and source found `data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml`, the TOGO M625 import of the same original JCM M616 recipe, plus a separate KOMODO Desulfomicrobium WHB medium that names a different upstream medium and was not treated as an identity duplicate.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfomicrobium_medium__3dc5367b.yaml` | Passed; no issues found |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/desulfomicrobium_medium__3dc5367b.yaml --out /private/tmp/desulfomicrobium_medium__3dc5367b.strict.tsv --workers 1 --quiet` | Passed; 0 errors |
| Reference validator, `linkml-reference-validator validate data data/merge_yaml/merged/desulfomicrobium_medium__3dc5367b.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator, `linkml-term-validator validate-data data/merge_yaml/merged/desulfomicrobium_medium__3dc5367b.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; command exited 0 |
| Embedded `curation_history` | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` entries |

The documented `just` wrappers were not used for this focused record check because the local project `uv` environment currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools`. The equivalent validators above were run offline with Python 3.11 and the cached `linkml`, `pyyaml`, `linkml-reference-validator`, and `linkml-term-validator` packages.

## Identity and Grounding

The target is the intended JCM medium 616 import. The `mediadive.medium:J616` media term, the JCM page for `GRMD=616`, and the MediaDive REST payload all identify the upstream recipe as `DESULFOMICROBIUM MEDIUM`.

The generated target is not the only canonical Desulfomicrobium Medium in the merged directory. TOGO M625 carries `Original source: JCM - JCM_M616` and the same JCM URL, so `DESULFOMICROBIUM_MEDIUM.yaml` is a duplicate import of the same source recipe, not a separate WHB variant.

Several hydrated trace-metal salts are grounded only coarsely or not at all in the generated file. The most material grounding problem, though, is formulation topology rather than a single CHEBI term: JCM and MediaDive represent trace elements, bicarbonate, sulfide, and vitamins as stock additions, while the generated record serializes stock-strength rows as direct final-medium ingredients.

## Evidence

The JCM HTML page, MediaDive J616 REST payload, and TOGO M625 API payload agree on the medium identity, pH 7.0-7.2 preparation range, basal salts, 1 ml Trace element solution SL12B addition, 30 ml 8% NaHCO3 solution addition, 1 ml 5% Na2S x 9 H2O solution addition, 1 ml Vitamin solution addition, and separate SL12B and vitamin stock recipes.

The generated record supports the presence of the basal solutes, trace metals, bicarbonate, sulfide, and vitamins, but not their modeled scope:

- Trace element solution SL12B is a 1 ml stock addition, not direct top-level Na2-EDTA, FeSO4 x 7 H2O, CoCl2 x 6 H2O, MnCl4 x 4 H2O, ZnCl2, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, H3BO3, and CuCl2 x 2 H2O rows.
- 8% NaHCO3 and 5% Na2S x 9 H2O are milliliter additions from sterile stocks, not `30 G_PER_L` and `1 G_PER_L` direct ingredient rows.
- Vitamin solution is a 1 ml stock addition, not direct top-level vitamin rows at the per-liter stock concentrations.
- Distilled water is present in the basal medium, SL12B stock, and vitamin stock but is missing from the generated J616 record.

## Completeness

The generated target is stale relative to its maintained normalized owner. `data/normalized_yaml/bacterial/desulfomicrobium_medium.yaml` has a 2026-08-13 `apply_cocktail_nesting.py` event that moved five stock-strength components into two solutions, while the generated merge was last produced on 2026-08-06 and still has no `solutions:` block. A gitignore-independent search confirmed top-level `solutions:` is absent from the generated target and present in the maintained normalized owner.

That newer normalized repair is still incomplete. It moved FeSO4 x 7 H2O and four vitamins only; the rest of SL12B, p-Aminobenzoic acid, the 30 ml 8% bicarbonate addition, the 1 ml 5% sulfide addition, and the stock-solution waters still need source-scoped representation.

The empty `target_organisms` and `references` slots are not defects for this generated source recipe. The JCM, MediaDive, and TOGO pages inspected here provide formulation data, not strain-level growth evidence.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | JCM stock additions were flattened into direct final-medium ingredients. | JCM / MediaDive J616 has 1 ml SL12B, 30 ml 8% NaHCO3, 1 ml 5% Na2S x 9 H2O, and 1 ml Vitamin solution additions. The generated record has the corresponding trace metals and vitamins as top-level rows and has no `solutions:` block. | `data/normalized_yaml/bacterial/desulfomicrobium_medium.yaml`; reusable repair belongs in MediaDive import and cocktail-nesting rules. |
| Major | Two milliliter sterile-stock additions became gram-per-liter ingredient concentrations. | The source calls for 30 ml of 8% NaHCO3 and 1 ml of 5% Na2S x 9 H2O after cooling. The target encodes `NaHCO3` as `30 G_PER_L` and `Na2S x 9 H2O` as `1 G_PER_L`, losing both percentage strengths and addition volumes. | `data/normalized_yaml/bacterial/desulfomicrobium_medium.yaml` and MediaDive solution-row import logic. |
| Major | Distilled-water rows are missing from every J616 solution scope. | JCM and MediaDive list water in the basal medium, in Trace element solution SL12B, and in Vitamin solution. The generated target has no water entry. | `data/normalized_yaml/bacterial/desulfomicrobium_medium.yaml` and the related MediaDive solution import. |
| Major | The same upstream JCM M616 recipe is exposed as two generated media. | The target is MediaDive `J616`; `DESULFOMICROBIUM_MEDIUM.yaml` is TOGO `M625` and preserves `Original source: JCM - JCM_M616`. | Both JCM and TOGO normalized records plus merge source crosswalk logic. |
| Minor | The reviewed generated file predates a partial normalized fix. | The normalized owner now has a partial `solutions:` block from 2026-08-13, but the generated file was merged on 2026-08-06 and still exposes all rows flat. | Regenerate `data/merge_yaml/merged/desulfomicrobium_medium__3dc5367b.yaml` after completing the normalized repair. |

## Recommended Edits

1. Complete the solution repair in `data/normalized_yaml/bacterial/desulfomicrobium_medium.yaml`: preserve SL12B, 8% NaHCO3, 5% Na2S x 9 H2O, and Vitamin solution as separate additions with their JCM volumes.
2. Move every SL12B constituent, every vitamin constituent, and the relevant distilled-water rows into the correct nested solution scopes.
3. Correct the bicarbonate and sulfide additions so `30 ml` of `8% NaHCO3` and `1 ml` of `5% Na2S x 9 H2O` are not modeled as `G_PER_L` masses.
4. Merge or cross-link `data/normalized_yaml/bacterial/desulfomicrobium_medium.yaml` with `data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml` so generated output has one canonical JCM M616 Desulfomicrobium record.
5. Regenerate the merged record from the maintained normalized input rather than editing `data/merge_yaml/merged/desulfomicrobium_medium__3dc5367b.yaml` directly.

## Follow-up Checks

1. Rerun open schema, strict schema, term, and reference validation on the edited normalized J616 record, the TOGO M625 sibling, and the regenerated merged output.
2. Rerun the merge step and confirm `data/merge_yaml/merged/desulfomicrobium_medium__3dc5367b.yaml` no longer has top-level SL12B or vitamin-stock components.
3. Compare the regenerated record against the JCM `GRMD=616` page and MediaDive REST J616 for the four stock-addition volumes, pH range, solution water rows, and post-autoclave preparation order.
4. Recheck the generated merge directory and confirm there is no second canonical record for original JCM M616.

## Additional Notes

- `find` and `rg --no-ignore --hidden` were used for absence-sensitive searches, so ignored review reports and generated files were included where relevant.
- No report for `desulfomicrobium_medium__3dc5367b` existed under `reports/yaml_record_review/` before this one; that ignored directory was checked with `find`.
