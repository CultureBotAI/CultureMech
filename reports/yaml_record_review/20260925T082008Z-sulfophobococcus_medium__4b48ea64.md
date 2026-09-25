# YAML Record Review: Sulfophobococcus Medium

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfophobococcus_medium__4b48ea64.yaml` (`CultureMech:002612`)
- Started UTC: `2026-09-25T08:20:08Z`
- Finished UTC: `2026-09-25T08:20:08Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfophobococcus_medium__4b48ea64.yaml` |
| Normalized source | `data/normalized_yaml/archaea/sulfophobococcus_medium.yaml` |
| CultureMech ID | `CultureMech:002612` |
| Media term | `mediadive.medium:J252` |
| Original source | JCM Medium J252, SULFOPHOBOCOCCUS MEDIUM |
| Merge fingerprint | `4b48ea64d9669915642158d3263495491dda5696c54ff875140a9cfb79c22df7` |
| Merged from | `sulfophobococcus_medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected `CultureMech:002612` identifier, `mediadive.medium:J252` source term, JCM 252 identity, and pH 7.6 value. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:002612`, `mediadive.medium:J252`, `sulfophobococcus_medium.yaml`, and the merge fingerprint found this normalized source and generated merge as the only direct recipe records, with the expected normalized indexes also referencing the same ID and source term.

Most simple salts are plausibly grounded against the MediaDive payload. The generated record incorrectly adds supplier-catalog decomposition rows for LB Medium, causing unsupported `Tryptone`, 5 g/L `Yeast extract`, and 10 g/L `Sodium chloride` ingredients. The required 1 g/L bovine serum albumin row from JCM and MediaDive is missing from `ingredients`, although the preparation text still describes it.

## Evidence

The live JCM 252 page and MediaDive J252 list 1 g yeast extract, 1 g bovine serum albumin, 50 mg FeSO4 x 7 H2O, 32 mg Na2-EDTA, 66 mg CaCl2 x 2 H2O, 31 mg MgSO4 x 7 H2O, 31 mg KCl, 2.1 mg ZnCl2, 2.3 mg MnSO4 x n H2O, 1.8 mg Na2B4O7 x 10 H2O, 1.5 g glycine, 230 mg Na2CO3, 0.5 g Na2S x 9 H2O, 1 mg resazurin, and 1 L distilled water.

The JCM and MediaDive preparation text says to mix components except yeast extract, bovine serum albumin, and Na2S x 9 H2O, boil briefly, flush with N2, adjust pH to 7.6 at 80-90C, dispense under N2, seal, autoclave, separately autoclave yeast extract and neutralized Na2S x 9 H2O under N2, filter-sterilize bovine serum albumin under N2, and add those three solutions aseptically and anaerobically before inoculation.

The generated YAML preserves the pH, simple J252 salt rows, glycine, sodium carbonate, sodium sulfide, resazurin, and preparation text. It omits the explicit distilled-water row, drops the bovine-serum-albumin ingredient, and includes unsupported LB Miller product rows that are not in the source recipe.

## Completeness

The generated record is incomplete because a required 1 g/L bovine serum albumin ingredient is absent. Its formulation is also over-complete because tryptone, the extra 5 g/L yeast extract, and sodium chloride are artifacts of unrelated LB Medium constituent research rather than constituents of JCM 252.

`target_organisms` is absent. The MediaDive and JCM recipe metadata reviewed here do not assert growth observations, so no growth target was inferred.

## Findings

- Bovine serum albumin is required at 1 g/L by JCM 252 and MediaDive J252 but is missing from `ingredients`.
- `Tryptone` at 10 g/L is unsupported by the JCM and MediaDive source recipe.
- The FoodOn-grounded 5 g/L `Yeast extract` row is unsupported and duplicates the real 1 g/L JCM yeast-extract row.
- `Sodium chloride` at 10 g/L is unsupported by the JCM and MediaDive source recipe.
- The imported LB Medium commercial-product notes and supplier-catalog metadata do not belong to this JCM 252 record.
- The 1 L distilled-water row is omitted from the flat generated record.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/sulfophobococcus_medium.yaml`, or the commercial-product constituent enrichment step that touched it, then regenerate `data/merge_yaml/merged/sulfophobococcus_medium__4b48ea64.yaml`.
- Add the 1 g/L bovine serum albumin ingredient and retain its filter-sterilized 10% stock handling in the preparation text.
- Remove the unsupported LB Medium notes and the derived tryptone, extra yeast-extract, and sodium-chloride rows.
- If source solvent rows are preserved for JCM media in a future generator pass, keep J252 with 1 L distilled water.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `CultureMech:002612`, `mediadive.medium:J252`, `4b48ea64d9669915642158d3263495491dda5696c54ff875140a9cfb79c22df7`, and `sulfophobococcus_medium.yaml`.
- Recompare the regenerated J252 ingredient list against JCM and MediaDive to make sure no LB Miller constituent rows remain.

## Additional Notes

Empty optional fields that are unrelated to source identity, the source-backed formulation, and source-backed growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the normalized source or the upstream product-constituent enrichment that added LB Medium rows.
