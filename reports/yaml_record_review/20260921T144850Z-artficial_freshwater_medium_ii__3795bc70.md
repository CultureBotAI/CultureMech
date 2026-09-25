# YAML Record Review: ARTFICIAL FRESHWATER MEDIUM II

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/artficial_freshwater_medium_ii__3795bc70.yaml`
- Started UTC: 2026-09-21T14:48:50Z
- Finished UTC: 2026-09-21T14:49:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:002298` |
| Label | `artficial_freshwater_medium_ii` |
| Source identity | MediaDive `J1125`, JCM Medium 1125 |
| Generated status | Generated merge under `data/merge_yaml/merged/`; do not edit in place |
| Maintained owner | `data/normalized_yaml/bacterial/artficial_freshwater_medium_ii.yaml` |
| Merge provenance | Single-source merge from `artficial_freshwater_medium_ii.yaml` on fingerprint `3795bc7007afbe600569117f6e6d8fcfdc2dcb039f6b17e817a6626eccca4fbb` |

This review covers exactly `data/merge_yaml/merged/artficial_freshwater_medium_ii__3795bc70.yaml`. `find reports/yaml_record_review -name '*artficial_freshwater_medium_ii__3795bc70.md' -print` searched the ignored `reports/yaml_record_review/` tree and found no prior report named for this target.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/artficial_freshwater_medium_ii__3795bc70.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/artficial_freshwater_medium_ii__3795bc70.yaml --out /private/tmp/artficial_freshwater_medium_ii__3795bc70.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/artficial_freshwater_medium_ii__3795bc70.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/artficial_freshwater_medium_ii__3795bc70.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The only emitted message was the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | `just validate-history` | Not checked: the repository exposes this validator for standalone `history/*.yaml` records, not for embedded `MediaRecipe.curation_history` blocks in one merged recipe. |

The project `just` wrappers were not rerun in this pass because this checkout currently resolves through Python 3.13 and attempts to build `llvmlite==0.46.0`, which fails before any target-specific YAML validation. The no-project commands above exercise the narrow validators against this one generated record.

## Identity and Grounding

The generated record correctly denotes MediaDive `J1125` / JCM Medium 1125. MediaDive REST reports `id: J1125`, `name: ARTFICIAL FRESHWATER MEDIUM II`, `source: JCM`, and the same JCM 1125 URL that the CultureMech record stores in `notes`. JCM Medium 1125 has the same title, so the record identity and misspelled upstream label match.

Several chemical groundings are sound: the normalized MediaDive `g_l` values for KH2PO4, NH4Cl, KCl, Na2SO4, and Resazurin were carried over as grams per liter, and those compounds are linked to matching CHEBI entries. Hydrate-sensitive grounding is not complete: the record maps `NiCl2 x 6 H2O` to `CHEBI:34887` with label `nickel dichloride`, which drops the hexahydrate form printed by JCM Medium 187 and represented in the MediaDive trace-element stock.

## Evidence

MediaDive J1125 and JCM 1125 both preserve three recipe layers:

| Layer | Supported source rows |
|---|---|
| Main JCM 1125 base | KH2PO4, NH4Cl, KCl, Na2SO4, FeCl2 solution, Trace element solution, Selenite-tungstate solution, Resazurin, and 960 ml distilled water |
| JCM 1125 additions | 30 ml 8% NaHCO3; 2.5 ml 1 M MgCl2 x 6H2O; 1 ml 1 M CaCl2 x 2H2O; 1 ml each of vitamin, thiamine, and vitamin B12 stocks; 1 ml 10% yeast extract; 10 ml 1 M glycerin; 5 ml 5% Na2S x 9H2O before use |
| Referenced stocks | MediaDive solution records `3846`, `3847`, and `4172`, corresponding to JCM 187 FeCl2, JCM 187 trace-element, and JCM 431 selenite-tungstate stocks |

The generated CultureMech record loses those layer boundaries. The FeCl2, trace-element, and selenite-tungstate stock components are flattened into direct final-medium ingredients, so their source stock `g_l` values are presented as if they were final J1125 medium concentrations. The three vitamin-family references are left as empty `Unknown solution` stubs, and the source does not provide the JCM 403 stock compositions inline, so JCM 403 must be inspected to fill them.

JCM 1125 supports the two main preparation paragraphs in the generated record, but not with the generated actions: dispensing into bottles is not an autoclave action. JCM 1125 also prints the sodium-lactate instruction as a strain-specific comment for JCM 31104, not as a fourth `MIX` step in the glycerin-containing base recipe.

## Completeness

The direct `Distilled water` row from the MediaDive/JCM main solution is absent from the generated record even though JCM lists 960.0 ml and MediaDive keeps it as a `Distilled water` row in `Main sol. J1125`.

Optional `target_organisms` are absent; that is acceptable because neither the MediaDive J1125 import nor the JCM recipe records a curated growth-evidence assertion. Optional growth metrics and incubation conditions are likewise not defects for this source-only medium record.

The generated record has no formal `references` list. Its only source recovery data are in the free-text `notes` field, even though MediaDive J1125, JCM 1125, JCM 187, JCM 403, and JCM 431 are all necessary to recover the full formulation.

## Findings

| Severity | Finding | Evidence | Maintained owner for a fix |
|---|---|---|---|
| Major | Nested stock compositions were flattened into direct final-medium ingredients. | MediaDive J1125 models FeCl2, trace-element, and selenite-tungstate recipes as separate solution records, while lines 119-238 of the generated YAML place HCl, FeCl2 x 4H2O, trace metals, NaOH, selenite, and tungstate directly in `ingredients` with their stock `g_l` values. | Move these rows under named `solutions` in `data/normalized_yaml/bacterial/artficial_freshwater_medium_ii.yaml`; regenerate the merge output. |
| Major | Milliliter stock additions were converted into gram-per-liter ingredient or solution amounts. | MediaDive and JCM list NaHCO3, MgCl2 x 6H2O, CaCl2 x 2H2O, yeast extract, glycerin, and Na2S x 9H2O as ml additions of percent or molar stocks; the generated record stores the same numeric values as `G_PER_L`. The three vitamin-family additions under `solutions` also use `1 G_PER_L` rather than 1 ml/L. | Record these additions as stock solutions with `ML_PER_L` amounts in the normalized owner. |
| Major | The 960 ml distilled-water base row is missing. | MediaDive J1125 recipe order 9 and JCM 1125 both list Distilled water at 960 ml in the main solution. No `Distilled water` row appears in the generated ingredients or solutions. | Restore `Distilled water` as a main-solution ingredient in the normalized owner. |
| Major | The vitamin, thiamine, and vitamin B12 stocks are empty unknown solutions. | Lines 305-323 have `composition: []`, `unit: G_PER_L`, and `name: Unknown solution` for all three JCM 403 references. | Curate the JCM 403 subrecipes into the three solution blocks under the normalized owner. |
| Major | The sodium-lactate variant comment was turned into a glycerin-recipe preparation step. | Line 255 records the JCM 31104 sodium-lactate substitution as step 4 with `action: MIX`, even though it is a comment defining an alternate variant, not an instruction for the base glycerin recipe. | Convert this to a maintained variant relationship or a discussion note; the sodium-lactate formulation is already represented by the separate TOGO M1204 record. |
| Major | A hydrated nickel salt is grounded as anhydrous nickel dichloride. | `NiCl2 x 6 H2O` maps to `CHEBI:34887` / `nickel dichloride` at lines 189-198, but JCM 187 and MediaDive solution `3847` specify `NiCl2 x 6H2O`. | Resolve the hexahydrate against the packaged MIM label index, or leave it explicit and unmapped if no exact CHEBI term is available. |
| Minor | The post-dispensing instruction is misclassified as `AUTOCLAVE`. | Step 2 describes aseptic anaerobic distribution and bottle sealing, then pre-use reduction; it is not an autoclave step. | Split the paragraph into `ALIQUOT`, `MIX`, or narrower actions while preserving the source order. |

## Recommended Edits

1. Replace the flattened MediaDive J1125 import in `data/normalized_yaml/bacterial/artficial_freshwater_medium_ii.yaml` with the same nested stock structure already curated for the TOGO M1203 JCM 1125 owner, preserving MediaDive `J1125` identity.
2. Fill the three JCM 403 vitamin-family stocks from JCM Medium 403, each at 1 ml/L in the final medium.
3. Represent 30 ml/L 8% NaHCO3, 2.5 ml/L 1 M MgCl2 x 6H2O, 1 ml/L 1 M CaCl2 x 2H2O, 1 ml/L 10% yeast extract, 10 ml/L 1 M glycerin, and 5 ml/L 5% Na2S x 9H2O as solution additions, not direct `G_PER_L` rows.
4. Restore the 960 ml distilled-water row and formal `references` to MediaDive J1125, JCM 1125, JCM 187, JCM 403, and JCM 431.
5. Rework `preparation_steps` so they contain only source procedural instructions; model the JCM 31104 sodium-lactate substitution as a variant link or bounded discussion instead of a step.
6. Correct or remove the `NiCl2 x 6 H2O` CHEBI grounding if no exact hexahydrate term is available through the repository's MIM index.

## Follow-up Checks

- Run `just validate data/normalized_yaml/bacterial/artficial_freshwater_medium_ii.yaml` after editing the normalized owner.
- Run `just validate-references data/normalized_yaml/bacterial/artficial_freshwater_medium_ii.yaml` and confirm every added JCM or MediaDive reference resolves through the repository cache path.
- Rerun merge generation and verify `data/merge_yaml/merged/artficial_freshwater_medium_ii__3795bc70.yaml` preserves nested solutions, `ML_PER_L` stock additions, 960 ml water, and repaired preparation actions.
- Run the same open-schema, strict, reference, and term validators against the regenerated merged record.
- Manually compare the regenerated MediaDive J1125 record against JCM Media 1125, 187, 403, and 431; the FeCl2, trace, selenite-tungstate, vitamin, thiamine, and vitamin B12 stock boundaries are the highest-risk fields.

## Additional Notes

- This generated record is not stale relative to its normalized owner; the normalized owner already has the same flattened composition and empty vitamin-family solution stubs. Future fixes belong in `data/normalized_yaml/bacterial/artficial_freshwater_medium_ii.yaml` or in the MediaDive importer that created the flattened layout.
- The adjacent TOGO M1203/M1204 records now contain richer JCM 1125 curation, but they are separate source records and should not be treated as the authoritative owner of this MediaDive `J1125` record.
