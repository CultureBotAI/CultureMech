# YAML Record Review: Low-Strength Artificial Seawater Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/low_strength_artificial_seawater_medium__5cd782ae.yaml`
- Started UTC: `2026-09-23T20:24:25Z`
- Finished UTC: `2026-09-23T20:26:02Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:003047`
- `name`: `low_strength_artificial_seawater_medium`
- `original_name`: `LOW-STRENGTH ARTIFICIAL SEAWATER MEDIUM`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `mediadive.medium:J701`
- `merge_fingerprint`: `5cd782aea3560cf4ee6b6aa8a87499a074c2a1ae8717a162394cc25eb47bc837`
- `merged_from`: `artificial_seawater_medium`, `low_strength_artificial_seawater_medium`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/low_strength_artificial_seawater_medium__5cd782ae.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:003047`, `mediadive.medium:J701`, `mediadive.medium:J972`, `low_strength_artificial_seawater_medium`, `artificial_seawater_medium`, and the merge fingerprint found the maintained J701 owner, the maintained J972 owner, this generated J701 record, a TOGO M723 same-name low-strength sibling, and additional artificial-seawater owners.
- The generated J701 record merged the JCM 701 low-strength recipe with `artificial_seawater_medium`, which resolves to JCM 972 / MediaDive J972 in `data/normalized_yaml/bacterial/artificial_seawater_medium.yaml`.
- MediaDive REST resolves JCM J701 as `LOW-STRENGTH ARTIFICIAL SEAWATER MEDIUM` with JCM GRMD 701 as its source link.
- MediaDive REST resolves JCM J972 as `ARTIFICIAL SEAWATER MEDIUM`; its recipe uses Medium 701 with 3.0 g/L final yeast extract and 2.5 g/L final peptone, then adjusts pH to 7.5.
- The generated J701 target retains the J701 name and organic nutrient amounts, but marks J972 as a `SOURCE_DUPLICATE` parent and synonym even though J972 intentionally changes the J701 organic concentrations.

## Evidence

- MediaDive J701 lists 24 g NaCl, 0.7 g KCl, 7 g `MgCl2 x 6 H2O`, 0.1 g yeast extract, 0.5 g peptone, and 1000 ml distilled water in a 1000 ml main solution.
- TOGO M723 independently lists the same low-strength formula and identifies the source as JCM 701.
- MediaDive J972 lists no separate ingredient rows; instead, its Main solution J972 says to use Medium 701 with 3.0 g/L final yeast extract and 2.5 g/L final peptone, then adjust pH to 7.5.
- TOGO M1022 reports the expanded J972 formula as 24 g NaCl, 7 g `MgCl2 x 6 H2O`, 0.7 g KCl, 3 g yeast extract, 2.5 g peptone, and 1 L distilled water at pH 7.5.
- The maintained J972 owner currently contains the copied J701 ingredient amounts, but its preparation step still states the source-level 3.0 g/L yeast extract and 2.5 g/L peptone modifications.

## Completeness

- The reviewed J701 record has the five non-water ingredient rows expected for JCM 701.
- The reviewed J701 record omits the MediaDive 1000 ml distilled-water row.
- J701 and J972 are materially different formulations because J972 increases yeast extract from 0.1 g/L to 3.0 g/L, increases peptone from 0.5 g/L to 2.5 g/L, and adds an explicit pH 7.5 adjustment.
- The generated record has no `references` entry carrying either the JCM source URL or the MediaDive REST URL.
- A generated TOGO M723 sibling already represents the same JCM 701 low-strength source under `CultureMech:010131`.

## Findings

1. The generated J701 record treats the full-strength J972 formula as a source duplicate.
   - Evidence: `parent_media`, `variant_relationship`, and `variant_modifications` mark `data/normalized_yaml/bacterial/artificial_seawater_medium.yaml` as a `SOURCE_DUPLICATE`, and `synonyms` lists `mediadive.medium:J972` as an alias; MediaDive J972 raises Medium 701 to 3.0 g/L yeast extract and 2.5 g/L peptone before pH adjustment.
   - Impact: the generated corpus collapses a low-strength medium and a full-strength derivative that should remain distinct concentration variants.

2. The J972 owner has an internally inconsistent copied composition.
   - Evidence: `data/normalized_yaml/bacterial/artificial_seawater_medium.yaml` stores the J701 organic amounts, 0.1 g/L yeast extract and 0.5 g/L peptone, under notes saying they were copied from JCM Medium 701, while its preparation step says to use 3.0 g/L final yeast extract and 2.5 g/L final peptone.
   - Impact: merge fingerprinting sees J701 and J972 as the same five-row ingredient signature and emits a false duplicate.

3. The source solvent row is absent.
   - Evidence: MediaDive J701 includes 1000 ml distilled water in Main sol. J701, while the generated record has only NaCl, KCl, `MgCl2 x 6 H2O`, yeast extract, and peptone.
   - Impact: the record lacks the make-up volume that defines the source concentrations.

4. A second active generated record represents the same low-strength JCM 701 recipe.
   - Evidence: TOGO M723 resolves to JCM 701 and has the same 24 g/L NaCl, 0.7 g/L KCl, 7 g/L `MgCl2 x 6 H2O`, 0.1 g/L yeast extract, and 0.5 g/L peptone signature.
   - Impact: the generated corpus carries two active CultureMech IDs for the same JCM 701 medium.

## Recommended Edits

1. Fix `data/normalized_yaml/bacterial/artificial_seawater_medium.yaml` so JCM J972 materializes the source modifications as 3.0 g/L yeast extract and 2.5 g/L peptone, then rebuild merged output.
2. Classify J701 and J972 as concentration variants rather than `SOURCE_DUPLICATE` records.
3. Reconcile the J701 MediaDive owner with the TOGO M723 owner so JCM 701 has one generated CultureMech ID.
4. Add the J701 1000 ml distilled-water source row or document why normalized final-volume water rows are intentionally suppressed for this source.
5. Add structured source references for JCM GRMD 701 and MediaDive J701.

## Follow-up Checks

- Re-fetch MediaDive J701, MediaDive J972, TOGO M723, and TOGO M1022, then confirm regenerated J701 and J972 records retain separate yeast extract, peptone, and pH values.
- Re-run open schema, strict schema, reference, and term validation on the rebuilt record.
- Run an ignored-inclusive exact search for `low_strength_artificial_seawater_medium`, `J701`, `JCM_M701`, `TOGO:M723`, and `mediadive.medium:J701` to verify JCM 701 is no longer emitted under two active generated records.

## Additional Notes

- Exact duplicate checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.
