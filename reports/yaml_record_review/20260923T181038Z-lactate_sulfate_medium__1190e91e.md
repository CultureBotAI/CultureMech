# YAML Record Review: lactate_sulfate_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lactate_sulfate_medium__1190e91e.yaml
- Started UTC: 2026-09-23T18:09:51Z
- Finished UTC: 2026-09-23T18:10:38Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/lactate_sulfate_medium__1190e91e.yaml`, generated `MediaRecipe` record `CultureMech:003053` for MediaDive/JCM medium J707.

- Maintained owner: `data/normalized_yaml/bacterial/lactate_sulfate_medium.yaml`.
- Merge provenance: `merged_from: lactate_sulfate_medium`; generated merge fingerprint `1190e91e524948b98db351d163586d1e74c45248448c2c5b635dc507a2581734`.
- Source claim: JCM Medium J707 / `mediadive.medium:J707`, original JCM GRMD 707.
- Current generated identity: `medium_type: COMPLEX`, `composition_type: UNDEFINED`, `physical_state: LIQUID`, pH 7.2.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lactate_sulfate_medium__1190e91e.yaml`; the command exited 0 with no output. |
| Strict schema | Passed with `python scripts/validate_strict.py data/merge_yaml/merged/lactate_sulfate_medium__1190e91e.yaml --out /private/tmp/lactate_sulfate_medium__1190e91e.strict.tsv --workers 1 --quiet`. |
| Reference integrity | Passed with `linkml-reference-validator validate data data/merge_yaml/merged/lactate_sulfate_medium__1190e91e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; there were 0 checks. |
| Term integrity | Passed with `linkml-term-validator validate-data data/merge_yaml/merged/lactate_sulfate_medium__1190e91e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

JCM GRMD 707 and MediaDive J707 both identify the recipe as `LACTATE SULFATE MEDIUM`; pH 7.2, physical state liquid, and the JCM source identity are grounded. An exact ignored-file-inclusive search of `data/normalized_yaml` and `data/merge_yaml` for `CultureMech:003053`, `mediadive.medium:J707`, `JCM Medium J707`, the JCM 707 URL, and `LACTATE SULFATE` found this MediaDive owner and generated merge plus a separate TOGO M729 owner and generated `LACTATE_SULFATE_MEDIUM.yaml` that also point to JCM 707.

The record's `target_organisms` entry is not grounded. JCM 707 and MediaDive J707 describe only the formulation; neither page says that `LACTATE SULFATE` is an organism or an isolate.

## Evidence

The main JCM 707 formulation lists yeast extract, Na2SO4, L-sodium lactate, MgSO4 x 7 H2O, NH4Cl, K2HPO4, CaCl2 x 2 H2O, trace vitamins, 0.01 percent Coenzyme M solution, Vitamin B12 solution, trace element solution, HEPES, resazurin, and 1 L distilled water. The pH 7.2 adjustment and N2 autoclaving steps in the YAML are supported by JCM's text.

The source then adds 10 ml each of sterile 7 percent NaHCO3 and 2.5 percent L-cysteine HCl x H2O solutions after autoclaving. It also uses volume additions for trace vitamins, Vitamin B12 solution, and trace element solution. The generated record instead flattens every stock component as a top-level final ingredient at stock concentration; for example, Vitamin B12 appears both in the trace vitamin stock and the separate Vitamin B12 solution and has been merged to `0.050100000000000006 G_PER_L`.

MediaDive expands the JCM referenced stocks, including the trace vitamin and trace element recipes. That supports the identities of the stock components but not their representation as undiluted final-medium `G_PER_L` rows.

## Completeness

The record is incomplete in these consequential places:

- It does not preserve trace-vitamin, Vitamin B12, and trace-element solution boundaries.
- Coenzyme M, NaHCO3, and L-cysteine solution additions are modeled as `G_PER_L` using the added millilitre amounts rather than the source solution strengths.
- The unsupported `target_organisms` backfill names the medium instead of an organism.
- The TOGO M729 import of the same JCM 707 medium remains a separate maintained owner rather than a source duplicate.
- Structured `sources` or `source_data` are absent; JCM and MediaDive provenance are only in `media_term` and `notes`.

Empty real target organism slots would be acceptable here because the inspected JCM/MediaDive recipe does not assert a tested organism.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Referenced stock components are flattened at stock strength. | JCM J707 adds 2 ml trace vitamins, 0.1 ml Vitamin B12 solution, and 12.5 ml trace element solution; the YAML stores all nested stock ingredients as final medium ingredients and merges both Vitamin B12 rows. | `data/normalized_yaml/bacterial/lactate_sulfate_medium.yaml` or the MediaDive importer |
| Major | Solution volume additions are encoded as gram-per-litre concentrations. | JCM lists 0.2 ml of 0.01 percent Coenzyme M, 10 ml of 7 percent NaHCO3, and 10 ml of 2.5 percent L-cysteine solution; the record stores `0.2`, `10`, and `10` as `G_PER_L`. | `data/normalized_yaml/bacterial/lactate_sulfate_medium.yaml` or the MediaDive importer |
| Major | The target organism is a medium-name artifact. | The only `target_organisms` value is `LACTATE SULFATE`, which matches the medium name, while JCM 707 and MediaDive J707 do not name a target organism. | `data/normalized_yaml/bacterial/lactate_sulfate_medium.yaml` |
| Major | JCM 707 is duplicated across import paths. | The exact ignored-inclusive YAML search found this MediaDive/JCM owner and a separate TOGO M729 owner for the same JCM GRMD 707 source. | Merge or cross-import duplicate resolution |
| Minor | JCM provenance is only free text. | The JCM 707 URL is stored in `notes`; no structured `sources` slot captures JCM GRMD 707 or the MediaDive REST source. | `data/normalized_yaml/bacterial/lactate_sulfate_medium.yaml` |

## Recommended Edits

1. Represent trace vitamins, Vitamin B12 solution, and trace element solution as stock solutions, or recalculate every nested component to source-supported final-medium concentrations.
2. Replace the Coenzyme M, NaHCO3, and L-cysteine numeric `G_PER_L` rows with a representation of the actual source volume additions and stock strengths.
3. Remove `target_organisms: LACTATE SULFATE` and `organism_culture_type: isolate`.
4. Mark the MediaDive J707 and TOGO M729 records as source duplicates of one JCM 707 medium once their formula structures are normalized enough to compare.
5. Add structured JCM/MediaDive source metadata and regenerate the merged YAML.

## Follow-up Checks

- Rerun the open-schema, strict, reference, and term validators against the regenerated merged record.
- Recompare the main recipe, trace vitamin stock, Vitamin B12 stock, trace element stock, pH step, and post-autoclave additions against JCM GRMD 707.
- Search with `rg --no-ignore --hidden` for `LACTATE SULFATE` after curation to confirm it remains only as a medium label, not an organism.
- Confirm only one maintained JCM 707 recipe remains after source-duplicate resolution, with TOGO M729 and MediaDive J707 preserved as source accessions.

## Additional Notes

`data/normalized_yaml/bacterial/TOGO_M729_Lactate_Sulfate_Medium.yaml` is much less complete than the MediaDive owner because its referenced JCM stocks were migrated to empty `solutions` entries. Use the MediaDive/JCM expansion as the stronger maintained basis when reconciling the duplicate imports.
