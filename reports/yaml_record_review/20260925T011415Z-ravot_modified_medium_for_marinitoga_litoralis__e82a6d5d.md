# YAML Record Review: RAVOT MODIFIED MEDIUM FOR MARINITOGA LITORALIS

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ravot_modified_medium_for_marinitoga_litoralis__e82a6d5d.yaml`
- Started UTC: 2026-09-25T01:10:44Z
- Finished UTC: 2026-09-25T01:14:15Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:003068` |
| Name | `ravot_modified_medium_for_marinitoga_litoralis` |
| Original name | `RAVOT MODIFIED MEDIUM FOR MARINITOGA LITORALIS` |
| Category | `bacterial` |
| Source term | `mediadive.medium:J724`, label `RAVOT MODIFIED MEDIUM FOR MARINITOGA LITORALIS` |
| Source URL in notes | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=724` |
| Merge fingerprint | `e82a6d5dfcb6c95e277e911cd9ce0ac3b0bde309576c9f2ff5e520123c48dbdd` |
| Generated from | `data/normalized_yaml/bacterial/ravot_modified_medium_for_marinitoga_litoralis.yaml` |

This is a generated merge artifact under `data/merge_yaml/merged/`. Its formula is currently inherited unchanged from the maintained normalized J724 owner at `data/normalized_yaml/bacterial/ravot_modified_medium_for_marinitoga_litoralis.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ravot_modified_medium_for_marinitoga_litoralis__e82a6d5d.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ravot_modified_medium_for_marinitoga_litoralis__e82a6d5d.yaml --out /private/tmp/ravot_modified_medium_for_marinitoga_litoralis__e82a6d5d.strict.tsv --workers 1 --quiet` | Passed; exit 0 and `/private/tmp/ravot_modified_medium_for_marinitoga_litoralis__e82a6d5d.strict.tsv` has one header row and 0 error rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ravot_modified_medium_for_marinitoga_litoralis__e82a6d5d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 total checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ravot_modified_medium_for_marinitoga_litoralis__e82a6d5d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning before `Validation passed`. |
| Embedded `curation_history` | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not the embedded `MediaRecipe.curation_history` array in this merged YAML. |

## Identity and Grounding

The local identity is coherent: the generated record, its maintained normalized owner, and the live JCM page all identify JCM medium 724, `RAVOT MODIFIED MEDIUM FOR MARINITOGA LITORALIS`, at `GRMD=724`.

A gitignore-independent exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports` for `mediadive.medium:J724`, `GRMD=724`, `CultureMech:003068`, and `ravot_modified_medium_for_marinitoga_litoralis` found a second normalized/generated recipe, `data/normalized_yaml/bacterial/TOGO_M747_Ravot_Modified_Medium_For_Marinitoga_Litoralis.yaml` and `data/merge_yaml/merged/RAVOT_MODIFIED_MEDIUM_FOR_MARINITOGA_LITORALIS.yaml`. TOGO M747 names `original_media_id` `JCM_M724` and `src_url` `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=724`, so it is source-equivalent to this J724 record but remains a separate normalized owner and generated merge output.

Most simple salt and buffer ingredient identifiers match the inspected source formula, including NaCl, MgCl2 x 6 H2O, KCl, NH4Cl, KH2PO4, CaCl2 x 2 H2O, PIPES, K2HPO4, and Na2S x 9 H2O. Two groundings are chemically too broad or wrong:

- `Sodium acetate x 3 H2O` is hydrated in the JCM source and the TOGO JSON, but is grounded to `CHEBI:32954` / `sodium acetate`, not an exact trihydrate.
- `Sulfur` is supplied as sulfur powder in the JCM source and the TOGO JSON, but is grounded to `CHEBI:26833` / `sulfur atom`, not elemental sulfur or sulfur powder.

## Evidence

The JCM source page for `GRMD=724` supports the recipe identity, pH 6.0, liquid physical state, N2 atmosphere, and the main one-liter component table. The JCM table states 26.0 g NaCl, 0.5 g MgCl2 x 6 H2O, 0.5 g KCl, 0.3 g NH4Cl, 0.1 g KH2PO4, 0.1 g CaCl2 x 2 H2O, 0.83 g sodium acetate x 3 H2O, 2.0 g yeast extract, 2.0 g Trypticase peptone, 2.0 g maltose, 3.3 g PIPES, 5.0 g sulfur powder, 1.0 mg resazurin, and 1.0 L distilled water.

The live JCM page and TOGO M747 JSON both keep three later rows as post-autoclave solution additions:

| JCM addition | Source amount | Current generated row |
|---|---:|---|
| 7% KH2PO4 solution | 4.3 ml | Merged into `KH2PO4` as `4.3` `G_PER_L` plus the base `0.0981354` `G_PER_L` |
| 7% K2HPO4 solution | 4.3 ml | `K2HPO4`, `4.3` `G_PER_L` |
| 3% Na2S x 9 H2O solution | 10.0 ml | `Na2S x 9 H2O`, `10` `G_PER_L` |

The maintained MediaDive solution import at `data/normalized_yaml/bacterial/mediadive_4648_Main_sol_J724.yaml` has the same boundary loss upstream: it carries the three added solution volumes as `PERCENT_V_V` component rows, omits the 7% and 3% stock strengths, and records `Original volume: 1019 mL` after scaling the base JCM component masses. The generated J724 medium then flattens those solution rows further into unsupported bulk `G_PER_L` ingredients.

The generated preparation text retains the two major source procedure paragraphs: mix everything except sulfur, adjust to pH 6.0, autoclave under N2, add anaerobic phosphate stocks after cooling, steam sulfur for 3 hr on 3 successive days, distribute under N2 into sulfur-containing vessels, seal with butyl rubber stoppers, and add the anaerobic Na2S x 9 H2O solution. It does not represent the stock solutions as first-class recipes or additions.

## Completeness

The consequential missing representation is the stock-solution boundary. A user following the current merged YAML would add 4.3 g/L K2HPO4 and 10 g/L Na2S x 9 H2O as direct solids, and would add an extra 4.3 g/L KH2PO4 via the duplicate merge note, instead of adding small milliliter volumes of 7% and 3% stocks.

The sibling TOGO M747 import points at the same JCM page and preserves the stock rows as `solutions`, but those solution entries have empty `composition` arrays and put the final addition volumes in `G_PER_L`; they are not usable definitions of 7% KH2PO4, 7% K2HPO4, or 3% Na2S x 9 H2O stocks. The two source-equivalent records therefore need to be reconciled after the stock solution representation is corrected.

The record has no `target_organisms`, strain-specific growth metrics, or literature references. I did not flag those empty optional fields because the inspected JCM and TOGO source records are recipes, not growth studies.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Three stock-solution additions are encoded as unsupported direct `G_PER_L` ingredients. | JCM and TOGO both say the two 7% phosphate rows are 4.3 ml additions and the 3% Na2S x 9 H2O row is a 10.0 ml addition; the generated target instead has `KH2PO4` `4.3981354` `G_PER_L`, `K2HPO4` `4.3` `G_PER_L`, and `Na2S x 9 H2O` `10` `G_PER_L`. | `data/normalized_yaml/bacterial/ravot_modified_medium_for_marinitoga_litoralis.yaml`; likely also the MediaDive flattening path reflected in `data/normalized_yaml/bacterial/mediadive_4648_Main_sol_J724.yaml` |
| Major | The record is split from a source-equivalent TOGO import. | An exact gitignore-independent search found TOGO M747 at `data/normalized_yaml/bacterial/TOGO_M747_Ravot_Modified_Medium_For_Marinitoga_Litoralis.yaml`; its live API response points to the same original JCM 724 source page as this J724 record. | `data/normalized_yaml/bacterial/ravot_modified_medium_for_marinitoga_litoralis.yaml`; `data/normalized_yaml/bacterial/TOGO_M747_Ravot_Modified_Medium_For_Marinitoga_Litoralis.yaml`; merge/import equivalence rules |
| Major | `Sulfur` is grounded to `CHEBI:26833` / `sulfur atom`, which is not the supplied elemental sulfur powder. | The JCM source names `Sulfur (powder)`, and TOGO M747 labels the same source item as sulfur powder. | `data/normalized_yaml/bacterial/ravot_modified_medium_for_marinitoga_litoralis.yaml` |
| Major | `Sodium acetate x 3 H2O` is grounded to an anhydrous sodium acetate term. | The JCM source names the trihydrate; the target's `term` drops that hydration state by using `CHEBI:32954` / `sodium acetate`. | `data/normalized_yaml/bacterial/ravot_modified_medium_for_marinitoga_litoralis.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/ravot_modified_medium_for_marinitoga_litoralis.yaml`, remove the spurious direct 4.3 and 10 `G_PER_L` rows created from stock additions. Represent 7% KH2PO4 solution, 7% K2HPO4 solution, and 3% Na2S x 9 H2O solution as stock additions with their source addition volumes, or with reviewed final amounts that explicitly use both the percent stock strengths and final volume convention.
2. Fix the MediaDive J724 import/flattening path that materialized the solution volumes as `PERCENT_V_V` component rows in `data/normalized_yaml/bacterial/mediadive_4648_Main_sol_J724.yaml`, so regenerating JCM J724 cannot reintroduce those rows as solids.
3. Reconcile `data/normalized_yaml/bacterial/TOGO_M747_Ravot_Modified_Medium_For_Marinitoga_Litoralis.yaml` with the J724 owner after both imports preserve the JCM stock-solution boundary.
4. Re-ground `Sulfur` from `CHEBI:26833` to an exact elemental sulfur or sulfur-powder term, verified by OAK or another local ontology resolver.
5. Re-ground `Sodium acetate x 3 H2O` to an exact sodium acetate trihydrate term if one is available; otherwise leave the hydrated source string ungrounded and document that no exact term was selected.
6. Regenerate the merged outputs after the maintained normalized records or import rules are fixed.

## Follow-up Checks

- Re-run the focused open-schema, strict, reference, and term validators on the repaired normalized J724 record and regenerated `data/merge_yaml/merged/ravot_modified_medium_for_marinitoga_litoralis__e82a6d5d.yaml`.
- Re-run the same validators on `data/normalized_yaml/bacterial/TOGO_M747_Ravot_Modified_Medium_For_Marinitoga_Litoralis.yaml` and its generated `RAVOT_MODIFIED_MEDIUM_FOR_MARINITOGA_LITORALIS.yaml` output after the source-equivalent duplicate is harmonized.
- Run the merge freshness/equivalence check after regeneration to verify that the two JCM 724 imports no longer publish incompatible generated recipes.
- Manually compare the regenerated ingredient rows against live JCM `GRMD=724` or the TOGO M747 JSON and verify that the 7% and 3% rows are no longer direct bulk gram-per-liter ingredients.

## Additional Notes

- Fetching `https://mediadive.dsmz.de/rest/medium/724` returned a MediaDive `DataNotFound` response. I therefore used the live JCM `GRMD=724` page named in this record and the live TOGO M747 API payload as direct source text for this review.
- A gitignore-independent exact search over `data/raw`, `data/normalized_yaml`, and `data/merge_yaml` for local paths containing `Ravot` found related R101, G60, and R8 Ravot variants plus the JCM 724/JCM M724 owners discussed above; it found no additional local Marinitoga litoralis owner in that bounded path search.
