# YAML Record Review: acidianus_brierleyi_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/ACIDIANUS_BRIERLEYI_MEDIUM.yaml`
- Started UTC: 2026-09-21T08:50:37Z
- Finished UTC: 2026-09-21T08:53:28Z
- Verdict: needs curation

## Target

Generated merge record `ACIDIANUS_BRIERLEYI_MEDIUM.yaml` represents JCM Medium J176 / `mediadive.medium:J176` for ACIDIANUS BRIERLEYI MEDIUM. It is a singleton merge from `data/normalized_yaml/archaea/JCM_J176_ACIDIANUS_BRIERLEYI_MEDIUM.yaml`.

## Validation

- PASS: open LinkML schema validation with `linkml-validate`.
- PASS: strict schema layer validation with `scripts/validate_strict.py`.
- PASS: linkml-reference-validator on this generated record.
- PASS: linkml-term-validator on this generated record.
- Not checked: embedded `MediaRecipe.curation_history` entries; no focused generated-record history validator is documented, and `just validate-history` targets standalone `history/` files.

## Identity and Grounding

The generated target has the correct primary identity for JCM Medium J176: its `media_term` is `mediadive.medium:J176`, its notes point at `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=176`, and the fetched JCM page identifies medium 176 as `ACIDIANUS BRIERLEYI MEDIUM`.

The same recipe also exists in TOGO as M169. TOGO M169 reports `original_media_id: JCM_M176`, the same JCM `GRMD=176` URL, pH 2.0, and the same seven non-water components: 3 g `(NH4)2SO4`, 0.5 g `KH2PO4`, 0.5 g `MgSO4 x 7H2O`, 0.1 g `KCl`, 0.01 g `Ca(NO3)2`, 0.2 g yeast extract, and 10 g sulfur powder. CultureMech currently emits that TOGO source as the separate generated record `data/merge_yaml/merged/acidianus_brierleyi_medium__f8a53e2d.yaml`.

DSMZ Medium 150 and KOMODO Medium 150 have the same recipe name but are distinct formulations: they use `K2HPO4 x 3 H2O` and `Ca(NO3)2 x 4 H2O` at DSMZ source concentrations rather than JCM 176's `KH2PO4` and anhydrous `Ca(NO3)2`. They should not be merged into the JCM 176 target by name alone.

## Evidence

- Primary JCM source `GRMD=176`: source page fetched from JCM during review. It lists `(NH4)2SO4`, `KH2PO4`, `MgSO4 x 7H2O`, `KCl`, `Ca(NO3)2`, `Yeast extract (BD-Difco)`, `Sulfur (powder)`, and `Distilled water`; it instructs pH adjustment to 2.0 with 10 N H2SO4, separate autoclaving of yeast extract, and steaming sulfur for 3 h on each of three successive days.
- TOGO source M169: TOGO API record fetched during review. It names the original source `JCM_M176`, points at the same `GRMD=176` URL, carries pH 2.0, lists the same g-scale recipe with distilled water, and stores the H2SO4 instruction as a 10 N acid component plus a text comment.
- Local normalized source search: an ignored-inclusive exact ID search found only `JCM_J176_ACIDIANUS_BRIERLEYI_MEDIUM.yaml` for `mediadive.medium:J176` and only `TOGO_M169_Acidianus_Brierleyi_Medium.yaml` for exact `TOGO:M169`; the generated counterparts are `ACIDIANUS_BRIERLEYI_MEDIUM.yaml` and `acidianus_brierleyi_medium__f8a53e2d.yaml`.

## Completeness

The target preserves every non-water JCM mass amount and the key pH/separate-sterilization instructions. It omits the source's `Distilled water 1.0 L` row, generalizes `Yeast extract (BD-Difco)` to `Yeast extract`, and generalizes `Sulfur (powder)` to `Sulfur`, but those omissions do not change the intended non-water mass recipe.

The generated set is incomplete as a de-duplicated view because TOGO M169 remains split from the direct JCM import. The TOGO normalized source also lacks a structured `preparation_steps` entry even though TOGO's upstream `comments` field contains the JCM pH/autoclave/sulfur instructions.

## Findings

- MAJOR: The JCM 176 recipe is split across two generated records. `ACIDIANUS_BRIERLEYI_MEDIUM.yaml` is the direct JCM / `mediadive.medium:J176` singleton, while `acidianus_brierleyi_medium__f8a53e2d.yaml` is TOGO M169 for the same JCM M176 source. The two differ by parser representation, not by source identity or formulation: TOGO turns `Distilled water 1 L` into `1 G_PER_L`, stores H2SO4 as a variable ingredient, and drops the JCM comments from `preparation_steps`, so it fingerprints separately.
- MINOR: Sulfur powder is grounded as `CHEBI:26833` / `sulfur atom` in the JCM import. TOGO's `Sulfur (powder)` parse demonstrates a better ingredient string for the primary source row, and `CHEBI:33403` / `elemental sulfur` is a closer material grounding for solid sulfur powder.

## Recommended Edits

- Normalize `data/normalized_yaml/archaea/TOGO_M169_Acidianus_Brierleyi_Medium.yaml` to the same recipe model as JCM J176 before merge generation: do not retain 1 L water as `1 G_PER_L`, move the variable `H2SO4` row into a pH-adjustment preparation step or add the same variable component consistently to the JCM source, and preserve TOGO's comment as a `preparation_steps` item.
- Regenerate `data/merge_yaml/merged` after the TOGO normalized source is corrected and confirm that `JCM_J176_ACIDIANUS_BRIERLEYI_MEDIUM` and `TOGO_M169_Acidianus_Brierleyi_Medium` merge into one JCM 176 generated record.
- Preserve DSMZ Medium 150 / KOMODO Medium 150 as a different acidianus-brierleyi formulation; their phosphate and calcium salts do not match JCM 176.
- Consider regrounding JCM `Sulfur (powder)` from `CHEBI:26833` to `CHEBI:33403` and retaining the `Sulfur (powder)` label, because the source row is elemental solid sulfur rather than a free sulfur atom.

## Follow-up Checks

- Run strict, schema, reference, and term validation on the corrected TOGO normalized record.
- Regenerate merged YAML and verify that no `acidianus_brierleyi_medium__*.yaml` split record remains for exact `TOGO:M169`.
- Re-run an ignored-inclusive exact search for `GRMD=176`, `mediadive.medium:J176`, and exact `TOGO:M169` to confirm all JCM 176 source IDs resolve to the merged target.

## Additional Notes

The ignored-inclusive name search also found `data/merge_yaml/merged/acidianus_brierleyi_medium__37d28f59.yaml` for DSMZ Medium 150 and a KOMODO 150 source currently merged into `data/merge_yaml/merged/thiobacillus_caldus_medium.yaml`; both derive from DSMZ Medium 150 rather than JCM 176.
