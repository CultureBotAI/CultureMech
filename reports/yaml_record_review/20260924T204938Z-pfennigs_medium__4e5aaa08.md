# YAML Record Review: PFENNIG'S MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/pfennigs_medium__4e5aaa08.yaml
- Started UTC: 2026-09-24T20:49:38Z
- Finished UTC: 2026-09-24T20:49:38Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pfennigs_medium__4e5aaa08.yaml`, the direct JCM-derived record for JCM medium 681 / PFENNIG'S MEDIUM.

The merged record has one source recipe, `pfennigs_medium`, with source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=681` and medium term `mediadive.medium:J681`.

## Validation

- LinkML open validation: passed; no issues found.
- Strict schema validation: passed; `/private/tmp/pfennigs_medium__4e5aaa08.strict.tsv` has one header row and zero error rows.
- Reference validation: passed; 1 file validated, 0 checks configured.
- Term validation: passed.
- Embedded curation history validation: Not checked; the available `just validate-history` target validates standalone `history/` records rather than `MediaRecipe.curation_history` blocks inside merged YAML.

## Identity and Grounding

The record is grounded to the correct direct JCM page for medium 681. The core salts, vitamin B12, acetate, thiosulfate, and pH correspond to PFENNIG'S MEDIUM.

However, this record is also a duplicate half of the same JCM recipe imported through TOGO M700 at `data/merge_yaml/merged/pfennigs_medium.yaml`. The two records failed to merge because this direct JCM import expanded the cross-referenced SL-10 trace element stock from JCM medium 433 into final ingredients, while the TOGO import retained the stock as an empty cross-reference.

The SL-10 stock ingredients have chemically plausible CHEBI groundings for stock rows, but they are grounded in the wrong scope. They appear as final PFENNIG'S MEDIUM ingredients with gram-per-liter concentrations rather than as members of a nested SL-10 stock solution that is added at 0.5 ml/L.

## Evidence

- Fetched JCM medium 681 and confirmed the direct source only calls for 0.5 ml Trace element solution SL-10 from JCM medium 433; it does not list HCl, FeCl2, ZnCl2, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, or Na2MoO4 as final PFENNIG'S MEDIUM rows.
- Fetched JCM medium 433 and confirmed those trace-metal rows belong to "Trace element solution SL-10" as a separate stock recipe.
- Compared the direct JCM merged record with the TOGO M700 sibling for the same JCM GRMD=681 source URL.
- Confirmed validation succeeds, so the defect is source fidelity and component hierarchy rather than YAML structure.

## Completeness

The direct import captures pH 7.2, converts 0.02 mg vitamin B12 to `2e-05 G_PER_L`, and grounds acetate and thiosulfate. It also keeps a preparation step that the post-autoclave block is added after autoclaving.

The record is incomplete because it omits the explicit 0.5 ml/L SL-10 stock addition and the 1 L distilled-water row from JCM 681. The nested SL-10 details from JCM 433 are not modeled as a solution; they are flattened into the final ingredient list, and the SL-10-only preparation text about dissolving FeCl2 in HCl is attached to the PFENNIG'S MEDIUM recipe.

## Findings

- Nine SL-10 stock components from JCM medium 433 are incorrectly present as final PFENNIG'S MEDIUM ingredients: HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O.
- The source's actual "Trace element solution SL-10" aliquot is missing. JCM 681 calls for 0.5 ml of the stock per liter after autoclaving.
- The target omits the 1 L distilled-water row from JCM 681.
- The SL-10 stock-only FeCl2/HCl dissolution instruction is attached as step 3 even though that instruction comes from JCM 433, not the PFENNIG'S MEDIUM page.
- The same source recipe remains split from the TOGO M700 version, so downstream consumers will see two different PFENNIG'S MEDIUM recipes for one JCM source.

## Recommended Edits

- Remove the JCM 433 trace-metal stock ingredients from the final PFENNIG'S MEDIUM ingredient list.
- Add `Trace element solution SL-10` as a 0.5 `ML_PER_L` stock addition and preserve its JCM medium 433 cross-reference.
- Preserve JCM 681's 1 L distilled-water row as solvent or final-volume context.
- Keep the after-autoclaving step for the SL-10 stock, Na2S x 9 H2O, NaHCO3, vitamin B12, acetate, and thiosulfate, but move the FeCl2/HCl stock-preparation instruction under the SL-10 stock or omit it from the final recipe.
- Re-run merge after repairing the direct JCM and TOGO M700 normalizations so this record merges with `pfennigs_medium.yaml`.

## Follow-up Checks

- Re-run LinkML open validation, strict validation, reference validation, and term validation on the regenerated merged record.
- Search with ignored files included for `GRMD=681`, `mediadive.medium:J681`, and `TOGO:M700` to confirm the direct and TOGO sources reconcile to one intended merged recipe.
- Inspect the regenerated ingredient list and confirm it contains the base salts, Na2S, NaHCO3, vitamin B12, acetate, thiosulfate, and a 0.5 ml/L SL-10 stock addition, not the SL-10 stock's HCl and trace-metal components as final ingredients.

## Additional Notes

Empty optional fields were not treated as defects. The sibling TOGO record was used only to confirm that the source identity is a merge duplicate of JCM medium 681.
