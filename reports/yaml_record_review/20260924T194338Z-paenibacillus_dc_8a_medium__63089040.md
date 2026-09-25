# YAML Record Review: paenibacillus_dc_8a_medium__63089040

- Repository: CultureMech
- Record: data/merge_yaml/merged/paenibacillus_dc_8a_medium__63089040.yaml
- Started UTC: 2026-09-24T19:43:38Z
- Finished UTC: 2026-09-24T19:43:38Z
- Verdict: needs curation

## Target

Reviewed generated MediaRecipe `CultureMech:002461`, `paenibacillus_dc_8a_medium`, generated from the direct MediaDive DC-8A / Paenibacillus DC-8A pair.

## Validation

- Open LinkML validation: Passed; exited 0 with `No issues found`.
- Strict validation: Passed; scanned 1 file with 0 ERROR rows. `/private/tmp/paenibacillus_dc_8a_medium__63089040.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The generated record is grounded as JCM Medium J1299 / PAENIBACILLUS DC-8A MEDIUM, but its `merged_from` list also includes DSMZ Medium 1809 / DC-8A Medium. An ignored-inclusive exact search for `mediadive.medium:J1299`, `mediadive.medium:1809`, `GRMD=1299`, `Paenibacillus DC-8A`, `DC-8A Medium`, `dc_8a_medium`, and `paenibacillus_dc_8a_medium` across `data/merge_yaml` and `data/normalized_yaml` found the direct JCM J1299 child, the DSMZ 1809 parent, and the TOGO M1396 JCM duplicate.

## Evidence

MediaDive J1299 and DSMZ 1809 share the same pH 9.0 DC-8A base: K2HPO4 2.9 g/L, Urea 4.2 g/L, Yeast extract 2 g/L, CaCl2 x 2 H2O 0.01 g/L, Na2CO3 1 g/L, L-Cysteine HCl x H2O 0.5 g/L, Resazurin 0.5 mg/L, 0.2 ml Mineral solution, 900 ml Distilled water, and a post-autoclave xylose stock addition. The nested 1 L Mineral solution contains MgCl2 x 6 H2O 25 g, CaCl2 x 2 H2O 37.5 g, FeSO4 x 7 H2O 0.312 g, and 1000 ml Distilled water.

The curated normalized pair correctly marks JCM J1299 as a `CONCENTRATION_VARIANT` of DSMZ 1809 because the JCM child uses a 10% (w/v), 100 ml Xylose solution whereas the DSMZ parent uses the lower 10 g/L xylose value.

## Completeness

The generated record is not a faithful recipe for either source. It is labeled as JCM J1299, but it merged the DSMZ 1809 parent and JCM J1299 child and emitted the lower 10 `G_PER_L` Xylose value from the parent. It also omits Distilled water, the 0.2 ml Mineral solution addition, and the post-autoclave 100 ml 10% Xylose stock addition, and it flattens mineral-stock rows into final top-level ingredients.

## Findings

1. A concentration variant was merged into its parent and assigned the wrong xylose concentration.

   The normalized sources deliberately keep DSMZ 1809 and JCM J1299 as a `CONCENTRATION_VARIANT` pair whose curated axis is xylose. Generation merged both into one record with `media_term: mediadive.medium:J1299` but `Xylose` 10 `G_PER_L`, the parent value, instead of the JCM 100 ml 10% xylose addition.

2. Mineral solution was flattened and calcium chloride was summed across scopes.

   Both MediaDive sources use only 0.2 ml Mineral solution in the 900 ml base. The generated record emits MgCl2 x 6 H2O 25 `G_PER_L`, FeSO4 x 7 H2O 0.312 `G_PER_L`, and a CaCl2 x 2 H2O row summed from 0.01 and 37.5 as 37.51 `G_PER_L`, which combines the base salt with a concentrated mineral stock component.

3. Required volume and stock-addition rows are missing.

   The source recipes include 900 ml Distilled water, 0.2 ml Mineral solution, and a post-autoclave xylose stock. None of those rows survive as scoped solution additions in the generated record.

4. The TOGO M1396 source duplicate is split away.

   TOGO M1396 imports JCM Medium 1299, but the generated TOGO record is still emitted separately as `paenibacillus_dc_8a_medium.yaml`.

## Recommended Edits

- Keep DSMZ 1809 and JCM J1299 as separate generated records linked by `CONCENTRATION_VARIANT`; do not merge them by their shared non-xylose base signature.
- Preserve `Mineral solution` as a 0.2 ml nested stock in both parent and child recipes.
- Preserve the JCM J1299 100 ml 10% (w/v) Xylose stock addition instead of overwriting it with the DSMZ 1809 10 `G_PER_L` parent value.
- Link TOGO M1396 as a source duplicate of direct JCM J1299.

## Follow-up Checks

- Re-run an ignored-inclusive exact search for `mediadive.medium:J1299`, `TOGO:M1396`, and `mediadive.medium:1809` after regeneration and confirm JCM J1299 plus TOGO M1396 emit as one child record while DSMZ 1809 emits as a separate parent record.
- Confirm regenerated calcium chloride has distinct base and mineral-stock scopes rather than one summed 37.51 `G_PER_L` top-level ingredient.
- Re-run open, strict, reference, and term validation on the regenerated YAML.

## Additional Notes

None found.
